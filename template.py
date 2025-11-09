from decimal import Decimal, ROUND_HALF_UP
import json
from typing import Any, Dict, List

from convert_to_words import convert_to_words

TWO_PLACES = Decimal("0.01")


def _to_decimal(value: Any) -> Decimal:
    """Convert value to Decimal with two decimal places."""
    return Decimal(str(value)).quantize(TWO_PLACES, rounding=ROUND_HALF_UP)


def format_polish_number(number: Any, with_currency: bool = True) -> str:
    """Format a number using Polish thousands separator and comma decimals."""
    amount = _to_decimal(number)
    formatted = f"{amount:.2f}"
    integer_part, decimal_part = formatted.split(".")

    groups: List[str] = []
    while integer_part:
        groups.insert(0, integer_part[-3:])
        integer_part = integer_part[:-3]
    integer_with_spaces = " ".join(groups)

    result = f"{integer_with_spaces},{decimal_part}"
    if with_currency:
        result += " PLN"
    return result


def prepare_invoice_context(data: Dict[str, Any]) -> Dict[str, Any]:
    """Build the context dictionary used to render the invoice template."""
    try:
        invoice_number = data["invoice_number"]
        issue_date = data["issue_date"]
        sale_date = data["sale_date"]
        seller_name = data["seller_name"]
        seller_nip = data["seller_nip"]
        seller_street_address = data["seller_street_address"]
        seller_postal_code = data["seller_postal_code"]
        seller_city = data["seller_city"]
        buyer_name = data["buyer_name"]
        buyer_nip = data["buyer_nip"]
        buyer_street_address = data["buyer_street_address"]
        buyer_postal_code = data["buyer_postal_code"]
        buyer_city = data["buyer_city"]
        items_data = data["items"]
    except KeyError as exc:  # pragma: no cover - simple validation
        raise ValueError(f"Missing required field: {exc.args[0]}") from exc

    items: List[Dict[str, str]] = []
    total_net = Decimal("0")
    total_vat = Decimal("0")

    for index, item_data in enumerate(items_data, start=1):
        try:
            quantity_decimal = Decimal(str(item_data["quantity"]))
            net_unit_price_decimal = _to_decimal(item_data["net_unit_price"])
            vat_rate_decimal = Decimal(str(item_data["vat_rate"]))
        except KeyError as exc:
            raise ValueError(f"Missing required item field: {exc.args[0]}") from exc

        net_total = (quantity_decimal * net_unit_price_decimal).quantize(
            TWO_PLACES, rounding=ROUND_HALF_UP
        )
        vat_amount = (net_total * vat_rate_decimal / Decimal("100")).quantize(
            TWO_PLACES, rounding=ROUND_HALF_UP
        )
        gross_total = (net_total + vat_amount).quantize(
            TWO_PLACES, rounding=ROUND_HALF_UP
        )

        total_net += net_total
        total_vat += vat_amount

        items.append(
            {
                "lp": item_data.get("lp", str(index)),
                "description": item_data.get("description", ""),
                "unit": item_data.get("unit", ""),
                "quantity": str(item_data.get("quantity", "")),
                "net_unit_price": format_polish_number(
                    net_unit_price_decimal, with_currency=False
                ),
                "net_total": format_polish_number(net_total, with_currency=False),
                "vat_rate": str(item_data.get("vat_rate", "")),
                "vat_amount": format_polish_number(vat_amount, with_currency=False),
                "gross_total": format_polish_number(gross_total, with_currency=False),
            }
        )

    total_gross = (total_net + total_vat).quantize(TWO_PLACES, rounding=ROUND_HALF_UP)

    payment_method = data.get("payment_method", "")
    payment_due_date = data.get("payment_due_date", "")
    bank_account = data.get("bank_account", "")
    authorized_issuer = data.get("authorized_issuer", "")

    amount_due_in_words = convert_to_words(f"{total_gross:.2f}")

    return {
        "invoice_number": invoice_number,
        "issue_date": issue_date,
        "sale_date": sale_date,
        "seller_name": seller_name,
        "seller_nip": seller_nip,
        "seller_street_address": seller_street_address,
        "seller_postal_code": seller_postal_code,
        "seller_city": seller_city,
        "buyer_name": buyer_name,
        "buyer_nip": buyer_nip,
        "buyer_street_address": buyer_street_address,
        "buyer_postal_code": buyer_postal_code,
        "buyer_city": buyer_city,
        "items": items,
        "total_net_amount": format_polish_number(total_net),
        "total_vat_amount": format_polish_number(total_vat),
        "total_gross_amount": format_polish_number(total_gross),
        "payment_method": payment_method,
        "payment_due_date": payment_due_date,
        "bank_account": bank_account,
        "amount_due_in_words": amount_due_in_words,
        "authorized_issuer": authorized_issuer,
    }


def load_invoice_context_from_file(path: str = "invoice_data.json") -> Dict[str, Any]:
    """Load invoice data from JSON file and prepare rendering context."""
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return prepare_invoice_context(data)


if __name__ == "__main__":  # pragma: no cover - manual testing helper
    context = load_invoice_context_from_file()
    print(json.dumps(context, indent=2, ensure_ascii=False))
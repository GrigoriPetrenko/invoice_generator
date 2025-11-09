import os
from typing import Dict

from template import load_invoice_context_from_file

TEMPLATE_PATH = os.path.join("templates", "invoice.html")
CSS_PATH = os.path.join("templates", "invoice.css")
OUTPUT_DIR = "output"


def _read_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def generate_items_rows(items):
    rows = ""
    for item in items:
        rows += f"""
                <tr>
                    <td>{item['lp']}</td>
                    <td>{item['description']}</td>
                    <td>{item['unit']}</td>
                    <td>{item['quantity']}</td>
                    <td>{item['net_unit_price']}</td>
                    <td>{item['net_total']}</td>
                    <td>{item['vat_rate']}%</td>
                    <td>{item['vat_amount']}</td>
                    <td>{item['gross_total']}</td>
                </tr>"""
    return rows


def render_invoice_html(context: Dict[str, str]) -> str:
    html_content = _read_file(TEMPLATE_PATH)
    css_content = _read_file(CSS_PATH)

    css_style_tag = f"<style>\n{css_content}\n</style>"
    html_content = html_content.replace(
        '<link rel="stylesheet" href="invoice.css">', css_style_tag
    )

    items_table_rows = generate_items_rows(context["items"])

    replacements = {
        "{{INVOICE_NUMBER}}": context["invoice_number"],
        "{{ISSUE_DATE}}": context["issue_date"],
        "{{SALE_DATE}}": context["sale_date"],
        "{{SELLER_NAME}}": context["seller_name"],
        "{{SELLER_NIP}}": context["seller_nip"],
        "{{SELLER_STREET_ADDRESS}}": context["seller_street_address"],
        "{{SELLER_POSTAL_CODE}}": context["seller_postal_code"],
        "{{SELLER_CITY}}": context["seller_city"],
        "{{BUYER_NAME}}": context["buyer_name"],
        "{{BUYER_NIP}}": context["buyer_nip"],
        "{{BUYER_STREET_ADDRESS}}": context["buyer_street_address"],
        "{{BUYER_POSTAL_CODE}}": context["buyer_postal_code"],
        "{{BUYER_CITY}}": context["buyer_city"],
        "{{ITEMS_TABLE_ROWS}}": items_table_rows,
        "{{TOTAL_NET_AMOUNT}}": context["total_net_amount"],
        "{{TOTAL_VAT_AMOUNT}}": context["total_vat_amount"],
        "{{TOTAL_GROSS_AMOUNT}}": context["total_gross_amount"],
        "{{PAYMENT_METHOD}}": context["payment_method"],
        "{{PAYMENT_DUE_DATE}}": context["payment_due_date"],
        "{{BANK_ACCOUNT}}": context["bank_account"],
        "{{AMOUNT_DUE_IN_WORDS}}": context["amount_due_in_words"],
        "{{AUTHORIZED_ISSUER}}": context["authorized_issuer"],
    }

    for placeholder, value in replacements.items():
        html_content = html_content.replace(placeholder, value)

    return html_content


def generate_invoice(context: Dict[str, str], output_dir: str = OUTPUT_DIR) -> str:
    os.makedirs(output_dir, exist_ok=True)
    html_content = render_invoice_html(context)

    safe_invoice_number = context["invoice_number"].replace("/", "-")
    filename = f"invoice_{safe_invoice_number}.html"
    output_path = os.path.join(output_dir, filename)

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(html_content)

    return output_path


def main():
    context = load_invoice_context_from_file()
    output_path = generate_invoice(context)
    print(f"Invoice saved as: {output_path}")


if __name__ == "__main__":  # pragma: no cover - CLI usage
    main()
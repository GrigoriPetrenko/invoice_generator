# Polish VAT Invoice Generator

A small Python tool that turns invoice data stored in a JSON file into a ready-to-print HTML invoice.

## How to Run

1. Install Python 3.10+
2. Open a terminal in the project folder and create a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```
3. Install the only required library:
   ```bash
   pip install flask
   ```
4. Choose how you want to generate the invoice:
   - **Command line** (uses `invoice_data.json`):
     ```bash
     python invoice_generator.py
     ```
     The HTML file will be saved in `output/`.
   - **Browser page** (upload a JSON file):
     ```bash
     python web_app.py
     ```
     Open `http://127.0.0.1:5000` in your browser, select the JSON file, click “Generuj fakturę”, and the invoice HTML opens in a new tab.

## JSON Template Example

Create or edit `invoice_data.json` following this structure:

```json
{
  "invoice_number": "FV/2024/001",
  "issue_date": "2024-01-15",
  "sale_date": "2024-01-15",
  "seller_name": "Your Company Sp. z o.o.",
  "seller_nip": "1234567890",
  "seller_street_address": "ul. Example 123",
  "seller_postal_code": "00-000",
  "seller_city": "Warszawa",
  "buyer_name": "Client Company Ltd.",
  "buyer_nip": "0987654321",
  "buyer_street_address": "ul. Client 456",
  "buyer_postal_code": "01-234",
  "buyer_city": "Kraków",
  "items": [
    {
      "lp": "1",
      "description": "Software Development Services",
      "unit": "godz",
      "quantity": "10",
      "net_unit_price": "100.00",
      "vat_rate": "23"
    }
  ],
  "payment_method": "Przelew bankowy",
  "payment_due_date": "2024-02-15",
  "bank_account": "12 3456 7890 1234 5678 9012 3456",
  "authorized_issuer": "Jan Kowalski"
}
```

Adjust the values to match your invoice. Each item in the `items` list becomes a row on the invoice.
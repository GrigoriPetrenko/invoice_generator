# Polish VAT Invoice Generator

A Python-based invoice generator that creates professional Polish VAT invoices in HTML format. The system automatically calculates totals, converts amounts to Polish words, and generates ready-to-print invoices.

## Features

- ✅ **Polish VAT Invoice Format** - Compliant with Polish invoice requirements
- ✅ **JSON Data Input** - Easy invoice data management via JSON file
- ✅ **Automatic Calculations** - Net, VAT, and gross totals calculated automatically
- ✅ **Polish Number to Words** - Converts invoice amounts to Polish words (e.g., "tysiąc osiemset czterdzieści pięć złotych")
- ✅ **Multiple Items Support** - Handle invoices with multiple line items
- ✅ **HTML Generation** - Produces standalone HTML files with embedded CSS
- ✅ **Organized Structure** - Clean project structure with templates and output folders

## Project Structure

```
facture_generator/
├── templates/              # Template files
│   ├── invoice.html       # HTML invoice template with placeholders
│   └── invoice.css        # Stylesheet for invoice layout
├── output/                 # Generated invoices (git-ignored)
│   └── invoice_*.html     # Generated invoice files
├── template.py            # Data loader - reads JSON and calculates totals
├── invoice_generator.py   # Main generator - creates HTML from template
├── convert_to_words.py    # Polish number-to-words converter
├── invoice_data.json      # Invoice data (edit this to create invoices)
└── README.md              # This file
```

## How It Works

### Step 1: Data Loading (`template.py`)
1. Reads invoice data from `invoice_data.json`
2. Extracts all invoice fields (seller, buyer, items, payment info)
3. Calculates totals for each item:
   - Net total = quantity × net unit price
   - VAT amount = net total × (VAT rate / 100)
   - Gross total = net total + VAT amount
4. Calculates overall totals (sum of all items)
5. Converts total amount to Polish words using `convert_to_words()`

### Step 2: HTML Generation (`invoice_generator.py`)
1. Imports all calculated data from `template.py`
2. Reads the HTML template from `templates/invoice.html`
3. Reads CSS from `templates/invoice.css`
4. Generates table rows for each item dynamically
5. Replaces all placeholders (e.g., `{{INVOICE_NUMBER}}`) with actual data
6. Embeds CSS directly into HTML (makes invoices self-contained)
7. Saves the final invoice to `output/` folder with filename based on invoice number

### Step 3: Template System
- **Placeholders**: HTML template uses `{{PLACEHOLDER_NAME}}` syntax
- **Replacement**: All placeholders are replaced with actual values from JSON
- **Items Table**: Generated dynamically from items array in JSON

## How to Use

### 1. Edit Invoice Data

Edit `invoice_data.json` with your invoice information:

```json
{
  "invoice_number": "FV/2024/001",
  "issue_date": "2024-01-15",
  "sale_date": "2024-01-15",
  "seller_name": "Your Company Name",
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
  "authorized_issuer": "John Doe"
}
```

### 2. Generate Invoice

Run the generator:

```bash
python invoice_generator.py
```

### 3. Find Your Invoice

The generated invoice will be saved in the `output/` folder:
```
output/invoice_FV-2024-001.html
```

Open the HTML file in any web browser to view or print.

## Adding Multiple Items

To add multiple items to an invoice, simply add more objects to the `items` array in `invoice_data.json`:

```json
"items": [
  {
    "lp": "1",
    "description": "Software Development Services",
    "unit": "godz",
    "quantity": "10",
    "net_unit_price": "100.00",
    "vat_rate": "23"
  },
  {
    "lp": "2",
    "description": "Consulting Services",
    "unit": "godz",
    "quantity": "5",
    "net_unit_price": "150.00",
    "vat_rate": "23"
  }
]
```

## VAT Rates

Supported VAT rates:
- **23%** - Standard rate
- **8%** - Reduced rate
- **5%** - Reduced rate

Simply specify the rate as a number in `invoice_data.json` (e.g., `"vat_rate": "23"`).

## Dependencies

This project uses only Python standard library - **no external dependencies required!**

- `json` - For reading invoice data
- `os` - For file operations

## Polish Number Conversion

The `convert_to_words.py` module converts numbers to Polish words:

- Handles amounts up to 9999
- Converts decimal parts (grosze) to words
- Proper Polish grammar (złoty/złote/złotych, grosz/grosze/groszy)
- Supports both comma and period as decimal separators

Example:
- `1845.60` → `"tysiąc osiemset czterdzieści pięć złotych sześćdziesiąt groszy"`
- `"1121,50"` → `"tysiąc sto dwadzieścia jeden złotych pięćdziesiąt groszy"`

## Customization

### Changing Template Style

Edit `templates/invoice.css` to customize the invoice appearance:
- Colors
- Fonts
- Spacing
- Layout

### Modifying Template Structure

Edit `templates/invoice.html` to change:
- Invoice layout
- Field order
- Additional sections

**Note**: Make sure to preserve placeholder names (e.g., `{{INVOICE_NUMBER}}`).

## Output

Generated invoices are:
- **Self-contained** - CSS is embedded, no external files needed
- **Print-ready** - Optimized for printing
- **Named by invoice number** - Easy to organize and find

## Git Ignore

The `output/` folder is automatically ignored by git (see `.gitignore`). This means:
- Generated invoices won't be committed to version control
- Each user can generate their own invoices locally
- Template files remain tracked in git

## Example Workflow

1. **Create new invoice**:
   ```bash
   # Edit invoice_data.json with new invoice data
   # Change invoice_number, dates, items, etc.
   ```

2. **Generate invoice**:
   ```bash
   python invoice_generator.py
   ```

3. **View/Print**:
   - Open `output/invoice_FV-2024-001.html` in browser
   - Print or save as PDF

## Troubleshooting

### Import Error
If you get import errors, make sure all files are in the correct locations:
- `template.py` in root directory
- `convert_to_words.py` in root directory
- `templates/` folder with `invoice.html` and `invoice.css`

### Calculation Errors
- Check that quantity and net_unit_price are valid numbers in JSON
- Ensure VAT rate is a valid number (23, 8, or 5)

### File Not Found
- Make sure you're running `invoice_generator.py` from the project root directory
- Verify `templates/` folder exists with both HTML and CSS files

## License

This project is open source and available for personal and commercial use.

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve the invoice generator!
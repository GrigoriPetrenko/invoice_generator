# Invoice Generator - Implementation Plan

## Project Overview
Build a Polish VAT invoice generator that creates professional invoices in HTML format with the ability to convert to PDF.

## Current Status
- ✅ HTML invoice template created (`invoice.html`)
- ✅ CSS separated into `invoice.css`
- ✅ HTML placeholders created for dynamic data
- ✅ Variables and calculations implemented in `template.py`
- ✅ Polish number formatting function created
- ✅ VAT menu system implemented
- ✅ Automatic calculations for totals
- 🔄 Working on HTML generator (`invoice_generator.py`)

---

## Implementation Steps

### Phase 1: Python Data Structure Setup
**Objective**: Create a Python module to manage invoice data

**Status**: ✅ Simplified approach - implemented directly in `template.py`

**What was done**:
- ✅ All invoice variables defined as simple Python variables
- ✅ Data structure with dictionaries for items
- ✅ Helper functions: `get_vat_rate()`, `format_polish_number()`
- ✅ Automatic calculations (net_total, VAT, gross_total)
- ✅ Polish currency formatting

**Note**: Instead of classes, we're using a simpler approach with direct variable assignments and calculations.

---

### Phase 2: HTML Template Generator
**Objective**: Generate HTML from Python data

**Tasks**:
1. Create `invoice_generator.py` 🔄 **CURRENT STEP**
   - Function to load invoice data
   - Use simple string replacement for placeholders
   - Generate items table rows dynamically
   - Output generated HTML file

2. Support multiple items
   - Dynamic table generation for items list (todo: support multiple items)
   - Proper calculations and totals ✅ DONE

3. Add helper functions
   - Number to words conversion (Polish) - TODO
   - Date formatting ✅ DONE in template.py
   - Currency formatting ✅ DONE with Polish number format

---

### Phase 3: Interactive Input System
**Objective**: Allow user to input invoice data via console

**Status**: ✅ Already implemented in `template.py`!

**Tasks**:
1. ✅ Data collection via `input()`
   - Interactive prompts for all invoice fields
   - VAT menu with choice validation
   - All fields collected

2. ⏳ Still todo:
   - Save data to JSON or Python file
   - Menu system for invoice management

---

### Phase 4: PDF Generation
**Objective**: Convert HTML invoice to PDF

**Tasks**:
1. Install required libraries
   - `weasyprint` or `pdfkit` for HTML to PDF conversion

2. Create `pdf_converter.py`
   - Function to convert HTML to PDF
   - Handle page breaks correctly
   - Maintain formatting

---

### Phase 5: CLI Application
**Objective**: Create user-friendly command-line interface

**Tasks**:
1. Create `main.py`
   - Command-line interface
   - Options: create, generate, convert
   - Help documentation

2. Add features:
   - Input invoice data interactively
   - Generate HTML from template
   - Convert to PDF
   - Save invoice data

---

### Phase 6: Advanced Features (Optional)
**Objective**: Enhance functionality

**Tasks**:
1. Invoice numbering system
   - Auto-increment invoice numbers
   - Save sequence in config

2. Template customization
   - Allow multiple template styles
   - Logo insertion

3. Invoice storage
   - JSON database for invoices
   - Search and retrieve past invoices

4. Email integration
   - Send invoice via email
   - Attach PDF

---

## File Structure

```
facture_generator/
├── invoice.html              # ✅ HTML template with placeholders
├── invoice.css               # ✅ Separated CSS styles
├── template.py               # ✅ Data collection & calculations
├── implementation_plan.md    # ✅ Project documentation
├── invoice_generator.py      # 🔄 HTML generation engine (next)
├── main.py                   # ⏳ CLI application
├── data/                     # ⏳ Data storage directory
│   └── invoices.json        # Saved invoices
├── output/                   # ⏳ Generated files directory
│   ├── html/                # Generated HTML invoices
│   └── pdf/                 # Generated PDF invoices
└── README.md                 # ⏳ Project documentation
```

---

## Dependencies

### Required Python Libraries:
- `jinja2` - Template engine for HTML generation
- `weasyprint` or `pdfkit` - HTML to PDF conversion

### Installation:
```bash
pip install jinja2 weasyprint
# or
pip install jinja2 pdfkit
```

---

## Next Steps
1. Review and approve this plan
2. Start with Phase 1: Create data structure
3. Test each phase before moving to next
4. Iterate based on feedback

---

## Notes
- Focus on Polish VAT invoice compliance
- Keep code modular and maintainable
- Add error handling at each step
- Document all functions


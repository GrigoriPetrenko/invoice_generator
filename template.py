import json
from convert_to_words import convert_to_words

# Load invoice data from JSON file
with open('invoice_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Invoice Header - now from file!
invoice_number = data['invoice_number']
issue_date = data['issue_date']
sale_date = data['sale_date']

# Seller Information - from file!
seller_name = data['seller_name']
seller_nip = data['seller_nip']
seller_street_address = data['seller_street_address']
seller_postal_code = data['seller_postal_code']
seller_city = data['seller_city']

# Buyer Information - from file!
buyer_name = data['buyer_name']
buyer_nip = data['buyer_nip']
buyer_street_address = data['buyer_street_address']
buyer_postal_code = data['buyer_postal_code']
buyer_city = data['buyer_city']

# Get items from file
items_data = data['items']
items = []

# Convert example: Convert 18228.60 to '18 228,60'
def format_polish_number(number):
    formatted = f"{number:.2f}"
    integer_part, decimal_part = formatted.split(".")

    if len(integer_part) > 3:
        integer_part = integer_part[:-3] + " " + integer_part[-3:]
    return integer_part + "," + decimal_part + " PLN"

for item_data in items_data:
    quantity = float(item_data['quantity'])
    net_unit_price = float(item_data['net_unit_price'])
    vat_rate = float(item_data['vat_rate'])
    
    # Calculate
    net_total = quantity * net_unit_price
    vat_amount = net_total * (vat_rate / 100)
    gross_total = net_total + vat_amount

    # Calculate totals
    total_net = sum(float(item['net_total'].replace(' ', '').replace(',', '.')) for item in items)
    total_vat = sum(float(item['vat_amount'].replace(' ', '').replace(',', '.')) for item in items)
    total_gross = sum(float(item['gross_total'].replace(' ', '').replace(',', '.')) for item in items)



    # Add to items list
    items.append({
        "lp": item_data['lp'],
        "description": item_data['description'],
        "unit": item_data['unit'],
        "quantity": item_data['quantity'],
        "net_unit_price": item_data['net_unit_price'],
        "net_total": format_polish_number(net_total)[:-4],
        "vat_rate": item_data['vat_rate'],
        "vat_amount": format_polish_number(vat_amount)[:-4],
        "gross_total": format_polish_number(gross_total)[:-4]
    })

        # Or simpler - recalculate from items_data
    total_net = sum(float(item['quantity']) * float(item['net_unit_price']) for item in items_data)
    total_vat = sum(total_net * (float(item['vat_rate']) / 100) for item in items_data)
    total_gross = total_net + total_vat

    total_net_amount = format_polish_number(total_net)
    total_vat_amount = format_polish_number(total_vat)
    total_gross_amount = format_polish_number(total_gross)

    payment_method = data['payment_method']
    payment_due_date = data['payment_due_date']
    bank_account = data['bank_account']
    amount_due_in_words = convert_to_words(total_gross)
import json

# Load invoice data from JSON file
with open('invoice_data.json', 'r', encoding='utf-8') as file:
    invoice_data = json.load(file)

#Invoice Header
invoice_number = input("Provide document number: ")
issue_date = input("Provide creation date: ")
sale_date = input("Provide sele date: ")
#Seller Information
seller_name = input("Provide seler name: ")
seller_nip = input("Provide seler NIP: ")
seller_street_address = input("Provide seler address: ")
seller_postal_code = input("Provide seler post code: ")
seller_city = input("Provide seler city: ")
#Buyer Information
buyer_name = input("Provide buyer name: ")
buyer_nip = input("Provide buyer NIP: ")
buyer_street_address = input("Provide buyer address: ")
buyer_postal_code = input("Provide buyer post code: ")
buyer_city = input("Provide buyer city: ")
#Define the function to get vat rate
def get_vat_rate():
    print("\nChoose VAT rate:")
    print("1. 23%")
    print("2. 8%")
    print("3. 5%")
    vat_rate = input("Enter the number of the VAT rate: ")
    
    if vat_rate == "1":
        return "23"
    elif vat_rate == "2":
        return "8"
    elif vat_rate == "3":
        return "5"
    else:
        return "23"
# Collect bill input values
quantity_str = input("Quantity: ")
net_unit_price_str = input("Net unit price: ")
vat_rate_str = get_vat_rate()

# Convert bill to numbers
quantity = float(quantity_str)
net_unit_price = float(net_unit_price_str)
vat_rate = float(vat_rate_str)

#Calculate bill inputs
net_total = quantity * net_unit_price
vat_amount = net_total * (vat_rate / 100)
gross_total = net_total + vat_amount

# Conver example Convert 18228.60 to '18 228,60
def format_polish_number(number):
    formatted = f"{number:.2f}"
    integer_part, decimal_part = formatted.split(".")

    if len(integer_part) > 3:
        integer_part = integer_part[:-3] + " " + integer_part[-3:]
    return integer_part + "," + decimal_part + " PLN"

#Total Amount
total_net_amount = format_polish_number(net_total)
total_vat_amount = format_polish_number(vat_amount)
total_gross_amount = format_polish_number(gross_total)
#Services Items
items = [
    {
            "lp": input("Item number: "),
            "description": input("Item description: "),
            "unit": "szt./godz",
            "quantity": quantity_str,
            "net_unit_price": net_unit_price_str,
            "net_total": format_polish_number(net_total)[:-4],
            "vat_rate": vat_rate_str,
            "vat_amount": format_polish_number(vat_amount)[:-4],
            "gross_total": format_polish_number(gross_total)[:-4]
    },
]

#Payment Information
payment_method = input("Input payment method: ")
payment_due_date = input("Input due date: ")
bank_account = input("Input bank account: ")
amount_due_in_words = input("Provide amount due in words: ")
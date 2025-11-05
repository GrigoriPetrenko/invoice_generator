# Step 1: Import the variables from template.py
from template import invoice_number, issue_date, sale_date, seller_name, seller_nip, seller_street_address, seller_postal_code, seller_city, buyer_name, buyer_nip, buyer_street_address, buyer_postal_code, buyer_city, items, total_net_amount, total_vat_amount, total_gross_amount, payment_method, payment_due_date, bank_account, amount_due_in_words

# Step 2: Read the HTML template
with open('invoice.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Step 3: Generate items table rows
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

items_table_rows = generate_items_rows(items)

# Step 4: Replace the placeholder with actual data
html_content = html_content.replace('{{INVOICE_NUMBER}}', invoice_number)
html_content = html_content.replace('{{ISSUE_DATE}}', issue_date)
html_content = html_content.replace('{{SALE_DATE}}', sale_date)
html_content = html_content.replace('{{SELLER_NAME}}', seller_name)
html_content = html_content.replace('{{SELLER_NIP}}', seller_nip)
html_content = html_content.replace('{{SELLER_STREET_ADDRESS}}', seller_street_address)
html_content = html_content.replace('{{SELLER_POSTAL_CODE}}', seller_postal_code)
html_content = html_content.replace('{{SELLER_CITY}}', seller_city)
html_content = html_content.replace('{{BUYER_NAME}}', buyer_name)
html_content = html_content.replace('{{BUYER_NIP}}', buyer_nip)
html_content = html_content.replace('{{BUYER_STREET_ADDRESS}}', buyer_street_address)
html_content = html_content.replace('{{BUYER_POSTAL_CODE}}', buyer_postal_code)
html_content = html_content.replace('{{BUYER_CITY}}', buyer_city)
html_content = html_content.replace('{{ITEMS_TABLE_ROWS}}', items_table_rows)
html_content = html_content.replace('{{TOTAL_NET_AMOUNT}}', total_net_amount)
html_content = html_content.replace('{{TOTAL_VAT_AMOUNT}}', total_vat_amount)
html_content = html_content.replace('{{TOTAL_GROSS_AMOUNT}}', total_gross_amount)
html_content = html_content.replace('{{PAYMENT_METHOD}}', payment_method)
html_content = html_content.replace('{{PAYMENT_DUE_DATE}}', payment_due_date)
html_content = html_content.replace('{{BANK_ACCOUNT}}', bank_account)
html_content = html_content.replace('{{AMOUNT_DUE_IN_WORDS}}', amount_due_in_words)

# Step 4: Save the result
with open('generated_invoice.html', 'w', encoding='utf-8') as file:
    file.write(html_content)
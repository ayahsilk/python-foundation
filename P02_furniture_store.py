long_couch_description="Long couch. Tufted polyester blend on wood. 32inches high x 40 inches deep. Brown or blue."
long_couch_price=254.00
mystical_magical_loveseat="fancy loveseat. faux leather on birch. 29.50 inches high x 54.75 inches wide x 30 inches deep. black."
mystical_magical_loveseat_price=180.50
lamba_lamp_description="beautiful lamp. glass and iron. 36 inches tall. brown with cream shade."
lamba_lamp_price=52.15
#we store the tax rate as a float(8.8%)
sales_tax=0.088
#every customer starts with 0 dollars and no items.
customer_one_total=0
customer_one_itemization=""
#the customer decides to buy the loveseat
customer_one_total+=long_couch_price
customer_one_itemization+=long_couch_description+"\n"
#the customer also decides to buy the lamp
customer_one_total+=lamba_lamp_price
customer_one_itemization+=lamba_lamp_description+"\n"
#calculate the tax aed on the subtotal
customer_one_tax=customer_one_total*sales_tax
customer_one_total+=customer_one_tax
#we use f-strings for professional currency formatting
print("\n"+"*"*30)
print("   OFFICIAL RECEIPT")
print("*"*30)
print("\nCUSTOMER ITEMS:")
print(customer_one_itemization)
print("-"*30)
print(f"SUBTOTAL + TAX:${customer_one_total:.2f}")
print("*"*30)
print(" THANK YOU FOR SHOPPING!")
print("*"*30)
#---Step 1:define the math---
def calculate_total(price, tax_rate):
    tax_amount=price*tax_rate
    total=price+tax_amount
    print(f"the final price with tax is: ${total:.2f}")
    #---STEP 2:USE THE TOOL---
    #Now we can calculate any price instantly!
    calculate_total(100.00,0.08)
    calculate_total(250.50,0.05)
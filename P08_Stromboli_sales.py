toppings=["pepperoni","cheese","sausage","olives","anchovies","mushrooms"]
prices=[2,6,1,3,2,7,2]
num_stromboli=len(toppings)
print(f"we sell{num_stromboli}different kinds of stromboli")
stromboli=list(zip(prices, toppings))
print("\nUnsorted stromboli(price, topping):")
print(stromboli)
stromboli.sort()#sorts from cheapest to most expensive
print("\nSorted Menu:")
print(stromboli)
priciest_stromboli=stromboli[-1]#gets the last item
three_cheapest=stromboli[:3] #slices from index 0 to 2
print(f"\ncheapest option:{cheapest_stromboli}")
print(f"priciest option:{priciest_stromboli}")
print(f"budget options:{three_cheapest}")

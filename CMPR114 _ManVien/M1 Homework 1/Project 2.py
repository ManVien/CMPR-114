price_item1 = float(input("Enter the price of item 1: $"))
price_item2 = float(input("Enter the price of item 2: $"))
price_item3 = float(input("Enter the price of item 3: $"))
price_item4 = float(input("Enter the price of item 4: $"))
price_item5 = float(input("Enter the price of item 5: $"))

subtotal = price_item1 + price_item2 + price_item3 + price_item4 + price_item5
sales_tax = subtotal * 0.07
total = subtotal + sales_tax

print("The subtotal of the sale: $", subtotal)
print("The amount of sales tax: $", f'{sales_tax:.2f}')
print("The total: $", f'{total:.2f}')


charge = float(input('Enter the charge for the food '))
tip = charge * 0.18
sales_tax = charge * 0.07
total_amount = charge + tip + sales_tax
print(f'The amount of tip is {tip:.2f}')
print(f'The amount of sales tax is {sales_tax:.2f}')
print(f'The total amount of a meal purchased at a restaurant is {total_amount: .2f}')


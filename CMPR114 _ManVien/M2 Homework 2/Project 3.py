# Software Sales

# This program displays the amount of the discount (if any)
# and the total amount of the purchase after the discount.

# A package that retails for $99
RETAIL_PRICE = 99

# Prompt the user to enter the number of packages purchased
quantity = int(input('Enter the number of packages purchased: '))

# quantity between 0 and 9, no discount
if quantity >= 0 and quantity <= 9:
    print('There is no discount for the number of packages purchased that is less than 10.')
    print('The total amount of the purchase is $', RETAIL_PRICE * quantity)
# quantity between 10 and 19, discount 10%
elif quantity >= 10 and quantity <= 19:
    discount = 0.1
    print(f'The amount of the discount is $ {RETAIL_PRICE * quantity * discount: .2f}')
    print(f'The total amount of the purchase after the discount is $ {RETAIL_PRICE * quantity * (1 - discount):.2f}')
# quantity between 20 and 49, discount 20%
elif quantity >= 20 and quantity <= 49:
    discount = 0.2
    print(f'The amount of the discount is $ {RETAIL_PRICE * quantity * discount: .2f}')
    print(f'The total amount of the purchase after the discount is $ {RETAIL_PRICE * quantity * (1 - discount):.2f}')
# quantity between 50 and 99, discount 30%
elif quantity >= 50 and quantity <= 99:
    discount = 0.3
    print(f'The amount of the discount is $ {RETAIL_PRICE * quantity  * discount: .2f}')
    print(f'The total amount of the purchase after the discount is $ {RETAIL_PRICE * quantity * (1 - discount):.2f}')
# quantity 100 or more, discount 40%
elif quantity >= 100: 
    discount = 0.4
    print(f'The amount of the discount is $ {RETAIL_PRICE * quantity  * discount: .2f}')
    print(f'The total amount of the purchase after the discount is $ {RETAIL_PRICE * quantity * (1 - discount):.2f}')
# quantity less than 0, error message is displayed
else:
    print('Invalid entry. The number of package purchased must not be less than 0. Please try again.')


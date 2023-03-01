# This program asks the user to enter a number which is multiplied by 10,
# and the while loop should iterate as long as result is less than 100.

# Get a number.
number = float(input('Enter a number: '))

# The number is multiplied by 10 
product = number * 10

# Continue processing as long as product
# is less than 100.
while product < 100:
    print(f'The value of product: {product:.2f}')
    product *= 10



# Shipping Charges

# This program determines the shipping charges based on the weight and rate.

# Get the weight of a package
weight = float(input('Enter the weight of a package: '))

# Determine the rate of that weight and its shipping charge
# 2 pound or less
if weight > 0 and weight <= 2:
    charge = weight * 1.50
    print(f'The shipping charge is ${charge: .2f}')
# over 2 pounds but not more than 6 pounds
elif weight > 2 and weight <= 6:
    charge = weight * 3.00
    print(f'The shipping charge is ${charge: .2f}')
# over 6 pounds but not more than 10 pounds
elif weight > 6 and weight <= 10:
    charge = weight * 4.00
    print(f'The shipping charge is ${charge: .2f}')
# over 10 pounds
elif weight > 10:
    charge = weight * 4.75
    print(f'The shipping charge is ${charge: .2f}')
else: 
    # error message if the user enters a number that is less than or equal to 0.
    print('The weight of a package must be bigger than 0, try again.')




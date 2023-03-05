# Sum of Numbers
# This program asks the user to enter a series of positive numbers
# and display their sum.

print('This program calculates the sum of a series of positive numbers. Enter a negative number to end.')
# Get the first number
number = float(input('\nEnter a positive number which is greater than 0: '))

# Assign the value of the first number to total
total = number

# Use a loop to enter a series of positive numbers
while number > 0:
    number = float(input('\nEnter another positive number or enter a negative number to end: '))
    # add the number to total if it is positive
    if number > 0:
        total += number

# Display the results
if total > 0:
    print(f'\nThe sum of a series of positive numbers is {total}.')

print()

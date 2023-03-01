# This program calculates the sum and the average 
# of a series of numbers entered by the user.

MAX = 5 # The maximum number

# Initialize an accumulator variable.
total = 0.0

# Explain what we are doing.
print('This program calculates the sum and the average of')
print(f'{MAX} numbers you will enter.\n')

# Get the numbers and accumulate them.
for counter in range(MAX):
    number = int(input('Enter a number: '))
    total = total + number

# Display the total of the numbers.
    print(f'The total is {total}.')

# Calculate the average of the 5 numbers.
average = total / MAX

# Display the average.
print(f'\nThe average of the 5 numbers is {average:.2f}')



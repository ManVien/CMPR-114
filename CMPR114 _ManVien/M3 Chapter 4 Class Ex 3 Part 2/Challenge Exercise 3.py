# Bug Collector
# This program asks for number of bugs collected for each day
# by using a loop and display the total number of bugs collected
# during the five days.

MAX = 5 # during the five days

# Initialize an accumulator variable.
total = 0

# Explain what we are doing.
print('This program calculates the total number of bugs collected')
print(f'during the {MAX} days.\n')

# Get the number of bugs collected for each day
for day in range(MAX):
    number = int(input(f'Enter the number of bugs collected for day {day + 1}: '))

    # Add the number of bugs to the accumulator
    total += number

# Display the total number of bugs collected during five days.
print(f'\nThe total number of bugs collected is {total}.')


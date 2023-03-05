# Average Rainfall
# This program displays the number of months, the total inches of
# rainfall, and the average rainfall per month for entire period 
# by using a nested loop.

# Constant variable
MONTHS_PER_YEAR = 12

# Initialize an accumulator variable
total_inches = 0.0

# Get the number of years
year = int(input('Enter the number of years: '))

# Determine if the value of year is smaller than 0
# display error message and ask user to enter the
# number of years again. 
while year <= 0:
    year = int(input('Invalid Entry. Please enter the number of years: '))

# outer loop iterates once for each year
for number in range(year):
    print(f'\nThe following data is for year {number + 1} rainfall.')
    # inner loop iterates twelve times, once for each month
    for month in range(MONTHS_PER_YEAR):
        inches = float(input(f'Enter the inches of rainfall for month {month + 1}: '))
        # add the inches of rainfall to the accumulator
        total_inches += inches

# calculate the number of months
total_months = year * MONTHS_PER_YEAR

# calculate the average rainfall over a period of years
average = total_inches / total_months 

# display the results
print(f'\nThe number of months is {total_months}.')
print(f'The total inches of rainfall is {total_inches:.2f}.')
print(f'The average rainfall per month for the entire period is {average:.2f}.')
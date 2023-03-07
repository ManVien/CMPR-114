# This program asks user to enter 4 scores
# and calculates the sum and average of scores

# The maximum number of scores
MAX = 4 

# Initialize an accumulator variable.
total = 0

# Explain what we are doing.
print('This program calculates the sum of ' f'{MAX} scores you will enter.')

# Get the scores and accumulate them.
for counter in range(MAX):
    number = int(input('Enter a score: '))
    total = total + number

# Calculate the average.
average = total / MAX

# Display the sum and average of the scores.
print(f'The sum is {total}.')
print(f'The average is {average}.')





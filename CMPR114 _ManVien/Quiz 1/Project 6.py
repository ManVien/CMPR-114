# This program asks the user to enter 4 scores and
# output the letter grade associated with the average grade.

# The maximum number of scores
MAX = 4

# Initialize an accumulator variable.
total = 0.0

# Prompt the user to enter a score.
for counter in range(MAX):
    score = float(input('Enter a score: '))
    total = total + score

# Calculate the average
average = total / MAX

# Display error message when average is greater than 100.
if average > 100:
    print('\nThe average is greater than 100.\n')

# Set the total to 0 to start the new calculation for average
total = 0.0

# Use a while loop - inform the user to re-enter the scores.
while average > 100:
    for index in range(MAX):
        score = float(input('Please re-enter a score: '))
        total = total + score
    average = total / MAX

# Determine whether the letter grade is.
if average >= 90 and average <= 100:
    print(f'The average grade is {average:.1f}.')
    print('The letter grade is A.')
elif average >= 80 and average <= 89:
    print(f'The average grade is {average:.1f}.')
    print('The letter grade is B.')
elif average >= 70 and average <= 79:
    print(f'The average grade is {average:.1f}.')
    print('The letter grade is C.')
elif average >= 60 and average <= 69:
    print(f'The average grade is {average:.1f}.')
    print('The letter grade is D.')
elif average < 60:
    print(f'The average grade is {average:.1f}.')
    print('The letter grade is F.')

# insert a new line
print() 




# Calories Burned
# This program uses a loop to display the number of calories 
# burned after 10, 15, 20, 25, and 30 minutes.

# named constant 
CALORIES_BURNED_PER_MINUTE = 4.2

# the starting value is 10 
# the sequence's ending limit is 31
# the step value is 5
for time in range(10,31,5):
    calories_burned = time * CALORIES_BURNED_PER_MINUTE
    # display the number of calories burned 
    print(f'The number of calories burned after {time} minutes is {calories_burned:.2f}')
    print() # display a blank line



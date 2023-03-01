# This program asks user to enter 4 sets of temps under 102.5
# and get the sum and average of the 4 temps when user enter 
# a temp over 102.5

# Create a variable to control the loop.
count = 1

# Initialize an accumulator variable.
total = 0.0

# Get the temps and accumulate them.
while count < 5:
    temps = float(input(f'Enter the temperature {count} under 102.5: '))

    total += temps

    count += 1
  
# Calculate the average 
average = total / (count - 1)

# Display the results
print(f'The sum of the four temperatures is {total:.2f}')
print(f'The average of the four temperatures is {average:.2f}')
    



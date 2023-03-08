# This program calculates the sum of a tuple 
# using while loop 

test_tup = (15, 20, 123, 47, 26, 81)

# Create a variable to control the loop.
counter = 0

# Initialize an accumulator variable
total = 0

while counter < len(test_tup):
    total = total + test_tup[counter]
    counter += 1

print('The sum of this tuple is', total)

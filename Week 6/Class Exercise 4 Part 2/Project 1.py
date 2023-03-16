# This program displays a random number
# in the range of 1 through 10.
import random

def main():
    # Get a random number.
    number = random.randint(1,10)

    # Display the number.
    print('Display a random number in the range of 1 through 10.')
    print(f'The number is {number}.')

# Call the main function.
main()

print('\nUse for loop to print the random numbers')
for num in range (20):
    print(random.randint(1,10))

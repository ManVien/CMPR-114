# Number Analysis Program
# This program asks user to enter a series of 20 numbers
# and display the lowest number, the highest number,
# the total of the numbers, and the average of the numbers.

def main():

    # Get the numbers from the user.
    numbers = get_numbers()

    # Get the lowest number.
    lowest = min(numbers)

    # Get the highest number.
    highest = max(numbers)

    # Get the total of the numbers.
    total = get_total(numbers)
    
    # Calculate the average. 
    average = total / len(numbers)

    # Display the results
    print(f'\nThe lowest number in the list is {lowest}')
    print(f'The highest number in the list is {highest}')
    print(f'The total of the numbers in the list is {total}')
    print(f'The average of the numbers in the list {average:.2f}')
    print()

# The get_numbers function gets a series of numbers
# from the user and stores them in a list.
# A reference to the list is returned.
def get_numbers():
    # Create an empty list.
    series = []

    # A series of 20 numbers.
    MAX = 20

    # Get the numbers from the user and add them to 
    # the list.
    for counter in range(MAX):
        number = float(input(f'Enter value of number {counter + 1}: '))
        series.insert(counter, number)

    # Return the list.
    return series

# The get_total function accepts a list as an 
# argument and returns the total of the values in
# the list.
def get_total(num):
    # Create a variable to use as an accumulator.
    total = 0.0

    # Calculate the total of the list elements.
    for value in num:
        total += value

    # Return the total.
    return total

# Call the main function.
if __name__ == '__main__':
    main()
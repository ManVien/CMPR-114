# Create a 1-D list with the numbers 20-30 and get the sum and average of the numbers.

def main():
    numbers = [20,21,22,23,24,25,26,27,28,29,30]
    
    sum = 0
    average = 0

    for value in numbers:
        sum += value 

    average = sum / len(numbers)
    print('The list is: ', numbers)
    print('The sum is', sum)
    print('The average is', average)
    
main()
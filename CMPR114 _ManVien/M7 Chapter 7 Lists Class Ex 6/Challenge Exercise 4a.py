def total():

    numbers = [1,2,3,4,5,6,7,8,9,10]

    sum = 0

    for value in numbers:
        sum += value #total the numbers in the list

    average = sum / len(numbers) #the lens functions returns the number of items in the list
    print('the total is ', sum, ' the average is ', average)

    # Open a file for writing.
    outfile = open('numberList.txt','w')

    # Write the list to the file.
    outfile.write(str(numbers))

    # Close the file
    outfile.close()

    print()

    print(numbers)

    print('\nrecorded the numbers list to a text file.\n')

total()


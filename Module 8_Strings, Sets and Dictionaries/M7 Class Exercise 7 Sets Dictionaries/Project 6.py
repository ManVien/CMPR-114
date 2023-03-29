# This program will add to the list and delete from the list,
# and demonstrate how to total and average number of items in a list.
def main():

    names = ['Howard','Jamie','Jill']
    #element    0       1       2

    print('The list before the insert or remove.')

    print(names)

    NameRemove = input('Enter the name to remove: ')

    names.insert(0,'Joe') # insert the new name at element 0, moving or shifting element 0 to 1
    names.remove(NameRemove) # removes the name from the list
    print('The list after the insert.')

    print(names)

main()

def total():

    numbers = [1,2,3,4,5,6,7,8,9,10]

    sum = 0

    for value in numbers:
        sum += value # total the numbers in the list

    average = sum / len(numbers) # the len functions returns the number of items in the list
    print('\nThe total is ', sum, '. The average is ', average)

total()
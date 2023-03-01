# Project #2
# creating lists, with input values and outputting the list to a text file

def main1():
    prodNums = ['V475','F987','Q143','R688'] #list of values

    search = input ('enter a product number: ')

    if search in prodNums: #determines if the product # is in the list
        print(search,' was found in the list ')

    else:
        print(search,' was not found in the list ')

main1()

def main2():
    nameList = []

    again = 'y'

    while again == 'y':
        name = input('\nenter a name: ')

        nameList.append(name) # appends the names in a list format

        print('do you want to add another name? ')
        again = input('y = yes, hit any other key for NO: ')
        print()

        print('here are the names you entered ')

        for name in nameList: #loop through each name
            print(name)

        outfile = open('names.txt','w')

        outfile.write(str(nameList))

        outfile.close()

        print('recorded the names in the list ')

main2()

# this program will add to the list and delete from the list
def main():

    names = ['Howard','Jamie','Jill']
    #element    0       1       2

    print('\nthe list before the insert or remove ')

    print(names)

    NameRemove = input('\nenter the name to remove ')

    names.insert(0,'Joe') #insert the new name at element 0, 
                          # moving or shifting element 0 to 1
    names.remove(NameRemove) #remove the name from the list
    print('\nthe list after the insert ')

    print(names)

main()

def total():

    numbers = [1,2,3,4,5,6,7,8,9,10]

    sum = 0

    for value in numbers:
        sum += value #total the numbers in the list

    average = sum / len(numbers) #the lens functions returns the number of items in the list
    print('\nthe total is ', sum, ' the average is ', average)

total()

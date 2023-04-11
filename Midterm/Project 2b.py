# This program will write to the coffee text file. 
# Ask user to enter their favorite coffee brand, 
# with the prod number 99-8888, and price $9.88.  
# Verify by reading the file content.

def write():
    try:
        brand = input('Enter the favorite coffee brand: ')
        prod_num = input('Enter the prod number: ')
        price = float(input('Enter the price: '))

        outFile = open('coffee.txt','a') # the a letter means to append

        outFile.write('\n' + brand + ',' + prod_num + ',' + str(price))

        outFile.close()

        print('data recorded\n')

    except Exception as err: # built-in Exception error processing
            print(err)

write()

def read():
    try:
        infile = open('coffee.txt','r')

        fileContents = infile.read()

        infile.close()

        print(fileContents)

    except Exception as err: # built-in Exception error processing
        print(err)

read()

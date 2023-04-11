# This program asks user to enter expenses in rent, gas, food, clothing, and car payment
# and write this to text file. Then read and print the content of the file.

def write():
    try: 
        rent = float(input('Enter the rent expense: $'))
        gas = float(input('Enter the gas expense: $'))
        food = float(input('Enter the food expense: $'))
        clothing = float(input('Enter the clothing expense: $'))
        car_payment = float(input('Enter the car payment: $'))

        outFile = open('expenses.txt','a') # the a letter means to append

        outFile.write('Rent: $' + str(rent))
        outFile.write('\nGas: $' + str(gas))
        outFile.write('\nFood: $' + str(food))
        outFile.write('\nClothing: $' + str(clothing))
        outFile.write('\nCar payment: $' + str(car_payment))

        outFile.close()

        print('data recorded\n')
    except Exception as err:
        print(err)

write()

def read():
    try:
        infile = open('expenses.txt','r')

        fileContents = infile.read()

        infile.close()

        print(fileContents)
    except Exception as err:
        print(err)

read()

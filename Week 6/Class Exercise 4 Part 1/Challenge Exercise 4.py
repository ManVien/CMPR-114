# This program asks user to enter three numbers, 
# uses global variables, and displays the sum and 
# average of three numbers. 

def add():
    global total
    global average
    num1 = float(input('Enter number 1: '))
    num2 = float(input('Enter number 2: '))
    num3 = float(input('Enter number 3: '))
    total = num1 + num2 + num3
    average = total / 3
    return total, average
    
add()
print('The sum of three numbers is', total)
print(f'The average of three numbers is {average:.2f}')


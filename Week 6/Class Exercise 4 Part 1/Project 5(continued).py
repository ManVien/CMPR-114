# This program will add 3 + 4 using a function named add
# with a global variable. 

def add(num1, num2):
    global total
    total = num1 + num2
    return total
    
add(3,4)
print(total)

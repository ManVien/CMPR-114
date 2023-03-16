# This program will add three numbers using a function 
# named add with a global variable. 

def add(num1, num2, num3):
    global total
    total = num1 + num2 + num3
    return total
    
add(3,4,5)
print(total)

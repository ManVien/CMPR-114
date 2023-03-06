personAge = int(input('enter your age: '))

if personAge < 0:
    print('invalid')
elif personAge <= 1:
    print('infant')
elif personAge > 1 and personAge < 13:
    print('child')
elif personAge >= 13 and personAge < 20:
    print('teen')
elif personAge >= 20:
    print('adult')


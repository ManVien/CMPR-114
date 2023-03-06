#get the inputs
#is used to return a floating-point number from a number or a string representation of a numeric value
rate = float(input('enter the pay rate:   '))
hours = int(input('enter the # of hours worked:   '))

if hours <= 40:
    sal = hours * rate
    print('the salary is $' + str(sal))
else:
       #1: 40 * rate   #2: take the first 40 hours from #1 to give you overtime hours * rate * 1.5, time and half
    sal = (40 * rate) + (hours - 40) * rate * 1.5
    print('the salary is $' + str(sal))



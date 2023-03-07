# This program asks user to enter the sales,
# and display the commission.

# Prompt the user to enter the sales.
sales = float(input('Enter the sales: '))

# Determine whether the sales is in. 
if sales >= 50000 and sales <= 60000:
    print('Commission is 10%.')
elif sales >= 70000 and sales <= 80000:
    print('Commission is 20%.')
elif sales >= 90000 and sales <= 100000:
    print('Commission is 30%.')

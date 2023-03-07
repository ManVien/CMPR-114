# This program asks user to enter the sales,
# multiply the salary with commission, and
# add the results to the salary.

# Prompt the user to enter the sales.
sales = float(input('Enter the sales: '))

# Determine whether the sales is in. 
if sales >= 50000 and sales < 70000:
    salary = 70000
    commission = 0.1
    # Calculate the new salary after adding the commission.
    new_salary = salary + salary * commission
    print(f'The new salary is ${new_salary:,.2f}')
elif sales >= 70000 and sales <= 80000:
    salary = 80000
    commission = 0.2
    # Calculate the new salary after adding the commission.
    new_salary = salary + salary * commission
    print(f'The new salary is ${new_salary:,.2f}')
elif sales >= 90000 and sales <= 100000:
    salary = 90000
    commission = 0.3
    # Calculate the new salary after adding the commission.
    new_salary = salary + salary * commission
    print(f'The new salary is ${new_salary:,.2f}')


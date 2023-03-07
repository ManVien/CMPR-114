# This program asks the user to enter the gross salary and 
# add 10% to the gross salary.

# Prompt the user to enter the salary.
salary = float(input('Enter the gross salary: '))

# Calculate the new salary.
new_salary = salary + salary * 0.1

# Display the result.
print(f'The new salary after adding 10% is ${new_salary:,.2f}.')
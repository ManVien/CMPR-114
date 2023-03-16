# This program asks the user to enter the hours worked and hourly pay
# and displays the output by using a function with passing arguments.

hours_worked = float(input('Enter the hours worked: '))
hourly_pay = float(input('Enter the hourly pay: '))

# The show_hours_and_pay function accepts 
# the hours worked and hourly pay as arguments.
def show_hours_and_pay(hours, pay):
    print(f'The hours worked: {hours}.\nThe hourly pay: ${pay:,.2f}.')

# Call the function.
show_hours_and_pay(hours_worked, hourly_pay)

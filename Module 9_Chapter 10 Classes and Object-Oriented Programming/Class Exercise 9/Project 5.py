# import the other class file name
import class3

# start the main function
def main():
    start_bal = float(input('Enter the starting balance: '))
    
    # call the external class3.name of the class, in our case its
    # called BankAccount from the class3
    savings = class3.BankAccount(start_bal)

    pay = float(input('How much were you paid this week? '))
    print('will deposit that amount into your account')

    # the deposit function is passing one argument called amount
    # so we have to fulfill that argument with pay
    savings.deposit(pay)
                                        # retrieved the balance from the external class
    print('your account balance is $', format(savings.get_balance(), ',.2f'))

    cash = float(input('How much would you like to withdrawal? '))
    print('will withdrawal that amount into your account')

    # calls the withdraw function from the external class
    # and fulfills the one argument that is passed with cash
    savings.withdraw(cash)
                                        # retrieved the balance from the external class
    print('your account balance is $', format(savings.get_balance(), ',.2f'))

main()
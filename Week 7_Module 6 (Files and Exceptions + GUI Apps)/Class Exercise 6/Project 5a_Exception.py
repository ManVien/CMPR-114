# Project 5a: using the try and catch statement with the while loop

def main():

    while True:

        try: # try the batch of code below, if there are no errors than disregard the except
            hours = int(input('hours worked '))
            pay = float(input('hourly pay '))
            gross = hours * pay
            print('gross pay $', format(gross, ',.2f'))
            break

            print('recorded')

        except ValueError: # if there are errors on the try statement, run the below print
            print('ERROR: hours worked and pay must be valid numbers, try again.')

        except Exception as err: # built-in Exception error processing
            print(err)

main()


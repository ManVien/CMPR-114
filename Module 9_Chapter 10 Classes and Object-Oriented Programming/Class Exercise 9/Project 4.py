# import the other class file name
import class7

# start the main function
def main():

    name = input("Enter the name: ")
    address = input("Enter the address: ")
    phone = input("Enter the phone: ")

    # calling class7 or the first file, then the name of the class, then the name of the function which
    # equals to the input variables
    v1 = class7.Customer.set_name = name
    v2 = class7.Customer.set_address = address
    v3 = class7.Customer.set_phone = phone

    print("Hello " + v1 + " your address is " + v2 + " and your # is " + v3)

main()

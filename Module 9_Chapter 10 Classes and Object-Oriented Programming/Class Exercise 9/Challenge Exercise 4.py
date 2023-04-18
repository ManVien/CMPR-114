# Continue project 4, add the city, and zip code with the person’s age.

# import the other class file name
import class7

# start the main function
def main():

    name = input("Enter the name: ")
    address = input("Enter the address: ")
    phone = input("Enter the phone: ")
    city = input("Enter the city: ")
    zipcode = input("Enter the zip code: ")
    age = int(input("Enter the age: "))

    # calling class7 or the first file, then the name of the class, then the name of the function which
    # equals to the input variables
    v1 = class7.Customer.set_name = name
    v2 = class7.Customer.set_address = address
    v3 = class7.Customer.set_phone = phone
    v4 = class7.Customer.set_city = city
    v5 = class7.Customer.set_zipcode = zipcode
    v6 = class7.Customer.set_age = age

    print("Hello " + v1 + ". Your address is " + v2 + ". Your # is " + v3)
    print("Your city is " + v4 + ". Your zip code is " + v5 + ". Your age is " + str(v6))
main()

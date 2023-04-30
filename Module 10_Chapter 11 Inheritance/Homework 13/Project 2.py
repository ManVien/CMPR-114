# Person and Customer Classes
# This program demonstrates an instance of the Customer class.

import person

def main():
    
    customer = person.Customer('Man Vien', '111 St', '(111)222-3333', 123, True)

    # display the data
    print('Customer Name:', customer.get_name())
    print('Customer Address:', customer.get_address())
    print('Customer Telephone:', customer.get_telephone_number())
    print('Customer Number:', customer.get_customer_number())
    customer.get_on_mailing_list()

    print()

main()
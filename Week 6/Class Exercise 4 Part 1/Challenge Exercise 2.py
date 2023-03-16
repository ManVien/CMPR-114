# This program with a function allows user to enter the
# last, first names, address, city, state, with zip code.
    
def personal_information():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    address = input('Enter your address: ')
    city = input('Enter your city: ')
    state = input('Enter your state: ')
    zip_code = input('Enter your zip code: ')

    print('\nYour first name: ', first_name)
    print('Your last name: ', last_name)
    print('Your city: ', city)
    print('Your address: ', address)
    print('Your state: ', state)
    print('Your zip code: ', zip_code)
    print()
    
personal_information()


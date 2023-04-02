# Pickled Vegetables
# This program keeps vegetable names and prices in a dictionary as key-value pairs.
# The program should display a menu that lets the user see a list of all vegetables and their
# prices, add a new vegetable and price, change the price of an existing vegetable, and delete
# an existing vegetable and price. The program should pickle the dictionary and save it to a
# file called vegetables.dat when the user exits the program. Each time the program starts,
# it should retrieve the dictionary from the file and unpickle it.

import pickle

# Global constants for menu choices
VIEW = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# main function
def main():
    vegetables = read()

    # Initialize a variable for the user's choice.
    choice = 0

    while choice != QUIT:
        # Get the user's menu choice.
        choice = get_menu_choice()

        # Process the choice.
        if choice == VIEW:
            view(vegetables)
        elif choice == ADD:
            add(vegetables)
        elif choice == CHANGE:
            change(vegetables)
        elif choice == DELETE:
            delete(vegetables)

    save(vegetables)

# The get_menu_choice function displays the menu
# and gets a validated choice from the user.
def get_menu_choice():
    print()
    print('Vegetables and Prices')
    print('---------------------------')
    print('1. View a list of all vegetables and prices')
    print('2. Add a new vegetable and price')
    print('3. Change the price of a vegetable')
    print('4. Delete a vegetable and price')
    print('5. Quit the program')
    print()

    # Get the user's choice.
    choice = int(input('Enter your choice: '))

    # Validate the choice.
    while choice < VIEW or choice > QUIT:
        choice = int(input('Enter a valid choice: '))

    # return the user's choice.
    return choice

# The view function view a list of all vegetables and prices 
# in the vegetables dictionary.
def view(vegetables):
    print("\nVegetables: ")
    for veg, price in vegetables.items():
        print('Name:', veg)
        print('Price:', price)

# The add function adds a new vegetable and price 
# into the vegetables dictionary.
def add(vegetables):
    # Get a name and price.
    new_veg = input("Enter the new vegetable' name: ")
    new_price = input('Enter the new price: ')

    # If the name does not exist, add it.
    if new_veg not in vegetables:
        vegetables[new_veg] = new_price
    else:
        print('That entry already exists.')

# The change function changes the price of a vegetable.
def change(vegetables):
    # Get a name to look up.
    changed_veg = input("Enter the vegetable's name: ")

    if changed_veg in vegetables:
        # Get a new price.
        changed_price = float(input('Enter the new price: '))

        # Update the entry.
        vegetables[changed_veg] = changed_price
    else:
        print('That name is not found.')

# The delete function deletes a vegetable and price
# from the vegetables dictionary.
def delete(vegetables):
    # Get a name to look up.
    deleted_veg = input("Enter the vegetable's name: ")
 
    # If the name is found, delete the entry.
    if deleted_veg in vegetables:
        del vegetables[deleted_veg]
    else:
        print('That name is not found.')
        
def read():
    end_of_file = False # to indicate end of file

    # Open a file for binary reading.
    input_file = open('vegetables.dat','rb')
    
    # Read to the end of the file.
    while not end_of_file:
        try:
            # Unpickle the next object.
            vegetables = pickle.load(input_file)
            return vegetables
        except EOFError:
            # Set the flag to indicate the end 
            # of the file has been reached.
            end_of_file = True

    # Close the file.
    input_file.close()

def save(vegetables):
    try:
        # Open a file for binary writing.
        output_file = open('vegetables.dat','wb')
   
        # Get data about a person and save it.
        pickle.dump(vegetables, output_file)

        # Close the file.
        output_file.close()
    except Exception as err:  # built-in Exception error processing
        print(err)

# Call the main function.
if __name__ == '__main__':
    main()
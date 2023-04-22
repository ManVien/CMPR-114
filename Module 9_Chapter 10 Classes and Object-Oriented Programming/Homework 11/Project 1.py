# This program creates an object of the class that prompts the user to enter the name,
# type, and age of a pet. This data should be stored as the object’s attributes. 
# Use the object’s accessor methods to retrieve the pet’s name, type, and age
# and display this data on the screen.

import Pet

def main():
    # Get the pet data.
    name = input("Enter the pet's name: ")
    animal_type = input("Enter the pet's type: ")
    age = int(input("Enter the pet's age: "))

    # Create an instance of the Pet class.
    pet1 = Pet.Pet(name, animal_type, age)

    # Display the data that was entered.
    print('\nHere is the data that you entered:')
    print(f'Pet\'s name: {pet1.get_name()}')
    print(f'Pet\'s type: {pet1.get_animal_type()}')
    print(f'Pet\'s age: {pet1.get_age()}')

main()
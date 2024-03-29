# Kilometer Converter
# This program asks the user to enter a distance in kilometers
# and converts that distance to miles.

def main():
    # Get a distance in kilometers.
    kilometers = float(input('Enter a distance in kilometers: '))
    miles = get_conversion(kilometers)
    show_conversion(miles)

def get_conversion(kilometers):
    # Convert distance to miles.
    miles = kilometers * 0.6214
    return miles

def show_conversion(miles):
    # Display the distance in miles.
    print(f'The distance in miles is {miles:.2f}.')

# Call the main function.
main()

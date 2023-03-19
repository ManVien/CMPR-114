# Property Tax
# This program asks the user to enter the actual value
# of a piece of property and displays the assessment value
# and property tax.

# Constant variables
ASSESSMENT_RATE = 0.6   # 60 percent of the property's actual value
TAX_RATE = (0.72/100)   # 72 cents for each $100 of the assessment value

def main():
    # Get the actual value of a piece of property.
    actual_value = float(input('Enter the actual value of a piece of property: $'))
    # Call the show_assessment_and_property_tax function
    show_assessment_and_property_tax(actual_value, ASSESSMENT_RATE, TAX_RATE)

# The show_assessment_and_property_tax function accepts three arguments 
# and displays the assessment value and property tax.
def show_assessment_and_property_tax(actual_value, ASSESSMENT_RATE, TAX_RATE):
    assessment_value = actual_value * ASSESSMENT_RATE
    property_tax = assessment_value * TAX_RATE

    print(f'The assessment value is ${assessment_value:,.2f}.\n'
          f'The property tax is ${property_tax:,.2f}.\n')

# Call the main function.
main()

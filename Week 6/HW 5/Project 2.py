# Stadium Seating
# This program asks the user to enter the numbers of tickets for
# each class of seats were sold and displays the amount of income
# generated from ticket sales.

# Global constant variables 
CLASS_A_PRICE = 20
CLASS_B_PRICE = 15
CLASS_C_PRICE = 10

def main():
    # Create a list of seating categories.
    seating_categories = ['A','B','C']
    # Create an empty list.
    number_of_tickets = []

    index = 0
    for i in seating_categories:
        # Get the number of tickets for each class of seats were sold. 
        ticket = int(input(f'Enter the number of class {i} tickets: '))
        # insert the number of tickets for each class.
        number_of_tickets.insert(index, ticket)      
        index += 1

    # Call the calculate_sales function.
    income_a, income_b, income_c, total_income = calculate_sales(number_of_tickets, 
                                                                CLASS_A_PRICE, CLASS_B_PRICE, CLASS_C_PRICE)
    # Call the show_income function.
    show_income(income_a, income_b, income_c, total_income)

# The calculate_sales function accepts the arguments and
# return the sales of ticket class A, B, and C and total sales. 
def calculate_sales(number_of_tickets,
                    CLASS_A_PRICE, CLASS_B_PRICE, CLASS_C_PRICE):

    sales_a = number_of_tickets[0] * CLASS_A_PRICE
    sales_b = number_of_tickets[1] * CLASS_B_PRICE
    sales_c = number_of_tickets[2] * CLASS_C_PRICE
    total_sales = sales_a + sales_b + sales_c
    return sales_a, sales_b, sales_c, total_sales

# The show_income function accepts four arguments and
# displays the amount of income generated from ticket sales.
def show_income(sales_a, sales_b, sales_c, total_income):
     print(f'\nThe amount of income generated from class A ticket sales is ${sales_a:,.2f}.')
     print(f'The amount of income generated from class B ticket sales is ${sales_b:,.2f}.')
     print(f'The amount of income generated from class C ticket sales is ${sales_c:,.2f}.')
     print(f'The amount of income generated from total ticket sales is ${total_income:,.2f}.\n')

# Call the main function.
main()


# This program creates three RetailItem objects and stores the data in them.
 
import RetailItem

def main():

    # Create the instance of the RetailItem class.
    item1 = RetailItem.RetailItem('Jacker', 12, 59.95)
    item2 = RetailItem.RetailItem('Designer Jeans', 40, 34.95)
    item3 = RetailItem.RetailItem('Shirt', 20, 24.95)

    # Display the data that was entered.
    print('Description\t\tUnits in Inventory\tPrice')

    print(item1)

    print(item2.get_description() + "\t\t\t" + str(item2.get_units()) + "\t\t" +
          str(item2.get_price()))

    print(item3)

    print()

main()

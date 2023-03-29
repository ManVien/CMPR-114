# This program replaces an old item in a list with a new item.

def main():
    food = ['Pizza','Burgers','Chips']
    print('Here are the food items in the list')
    print(food)
    item = input('Which items in the list do you want to change? ')

    try: # the try statement will try the batch of code below.
        itemIndex = food.index(item) # gets the items index in the list

        newItem = input('Enter the new value: ') # enter the value to replace with

        food[itemIndex] = newItem # replace the old item with the new item

        print('Here is the revised list ')

        print(food)

    except ValueError: # if an error is found, it will print the error
        print('The item was not found in the list')

main()
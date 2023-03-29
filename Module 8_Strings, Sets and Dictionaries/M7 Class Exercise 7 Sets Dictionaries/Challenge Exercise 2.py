# Create a GUI with some listboxes items

# Import all the tkinter pack
from tkinter import *

# Create a Tk root window named top
top = Tk()

# Create listbox object
listbox = Listbox(top, height = 10,
                  width = 15, bg = 'grey',
                  activestyle = 'dotbox',
                  font = 'Helvita',
                  fg = 'yellow',
                  selectmode = MULTIPLE)

# Define the size of the window
top.geometry('300x250')

# Define the label for the list
label = Label(top, text = 'FOOD ITEMS')

# Insert elements by index with their names as parameters
listbox.insert(1, 'Sandwich')
listbox.insert(2, 'Burger')
listbox.insert(3, 'Pizza')
listbox.insert(4, 'French Fries')
listbox.insert(5, 'Hot Dogs')
listbox.insert(6, 'CheeseBurger')

# Function to print the selected value form in the listbox
def selected_item():
    for i in listbox.curselection():
        # Traverse the tuple return by curselection method 
        # and print corresponding value(s) in the listbox
        print(listbox.get(i))

# Create a button widget and 
# map the command parameter 
# to selected_item function
btn = Button(top, text = 'Print Selection', command = selected_item)

# Placing the button in the listbox
btn.pack(side = 'bottom')

# Pack the widgets
label.pack()
listbox.pack()

# Display until user exits themselves
top.mainloop()

# Sum of Numbers
# This program reads all of the numbers stored in the numbers.txt file
# and calculates their total.

import tkinter as tk # import the gui interface controls
from tkinter import messagebox # imports the messagebox display

win = tk.Tk() # create the window interface
win.geometry("300x70") # width x height in pixels
win.title("Sum of Numbers") # Label for the title

def write():
    try:
        outfile = open("number.txt","w")

        for value in range(100, 1100, 100):
            outfile.write(str(value) + "\n")

        outfile.close()
    except Exception as err:
        print(err)

write()

def calculate_total():
    try:
        infile = open("number.txt","r")

        tot = 0
        nums_list = []

        for line in infile:
            content = float(line)
            nums_list.append(content)
            tot += content

        messagebox.showinfo("Sum of Numbers", "Numbers in file:\n" + str(nums_list) + "\n" 
                            + f"Total: {tot}")

        infile.close()
    except Exception as err:
        print(err)

def quit():
    messagebox.showinfo("Exit","Thank you...")
    win.destroy() # closes the interface

btnTotal = tk.Button(win, text = "total", command = calculate_total) # Button widget

btnQuit = tk.Button(win, text = "quit", command = quit) # Button widget

btnTotal.pack(side = 'top')
btnQuit.pack(side = 'bottom')

win.mainloop() # ensures the interfaces stays on the screen on window



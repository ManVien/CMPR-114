# This program create a GUI interface that will write 3 numbers
# and sum + averages the total into a text file.

from email import message
import tkinter as tk # import the gui interface controls
from tkinter import messagebox # imports the messagebox display

win = tk.Tk() # create the window interface
win.geometry("400x150") # width x height in pixels
win.title("Numbers, Sum, and Average") # Label for the title

lblNumber1 = tk.Label(win, text = "enter the first number").grid(column = 0, row = 0) # Label widget
lblNumber2 = tk.Label(win, text = "enter the second number").grid(column = 0, row = 1) 
lblNumber3 = tk.Label(win, text = "enter the third number:").grid(column = 0, row = 2) 

num1 = tk.StringVar() # the StringVar manages the Entry widget
txtNumber1 = tk.Entry(win, width = 12, textvariable = num1).grid(column = 1, row = 0) # Text Entry widget
num2 = tk.StringVar()
txtNumber2 = tk.Entry(win, width = 12, textvariable = num2).grid(column = 1, row = 1) 
num3 = tk.StringVar()
txtNumber3 = tk.Entry(win, width = 12, textvariable = num3).grid(column = 1, row = 2)

def write():
    text_file = open("sum_and_average.txt","a")
    total1 = total()
    average1 = average()
    content = text_file.write("The three numbers are: " + str(num1.get()) + ", " 
                              + str(num2.get()) + " and " + str(num3.get()) + "\n"
                              + f"The total is {total1:.2f}" + "\n" 
                              + f"The average is {average1:.2f}" + "\n") 

    text_file.close()
    messagebox.showinfo("Numbers, Sum, and Average","Data Recorded")

def quit():
    messagebox.showinfo("Numbers, Sum, and Average","Thank you...")
    win.destroy() # closes the interface

def total():   
    total = float(num1.get()) + float(num2.get()) + float(num3.get())
    messagebox.showinfo("Numbers, Sum, and Average","Total : " + str(total)) 
    return total

def average():  
    average = (float(num1.get()) + float(num2.get()) + float(num3.get())) / 3.0
    messagebox.showinfo("Numbers, Sum, and Average","Average : " + str(average)) 
    return average

                                            # command calls the total function
btnTotal = tk.Button(win, text = "total", command = total).grid(column = 0, row = 6) # Button widget

                                            # command calls the average function
btnAverage = tk.Button(win, text = "average", command = average).grid(column = 1, row = 6) # Button widget

                                            # command calls the quit function
btnQuit = tk.Button(win, text = "quit", command = quit).grid(column = 2, row = 6) # Button widget

                                            # call the function write
btnWrite = tk.Button(win, text = "transfer", command = write).grid(column = 3, row = 6) # Button widget

win.mainloop() # ensures the interfaces stays on the screen on window



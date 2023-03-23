# Continuing with project 5b, add the address, city, state with zip code
# and transfer the information to a text file.

from email import message
import tkinter as tk # import the gui interface controls
from tkinter import messagebox # imports the messagebox display

win = tk.Tk() # create the window interface
win.geometry("300x200") # width x height in pixels
win.title("Customer Information") # Label for the title

lblLastname = tk.Label(win, text = "enter the lastname").grid(column = 0, row = 0) # Label widget
lblFirstname = tk.Label(win, text = "enter the firstname").grid(column = 0, row = 1) 
lblAddress = tk.Label(win, text = "enter the address").grid(column = 0, row = 2) 
lblCity = tk.Label(win, text = "enter the city").grid(column = 0, row = 3) 
lblState = tk.Label(win, text = "enter the state").grid(column = 0, row = 4) 
lblZipcode = tk.Label(win, text = "enter the zipcode").grid(column = 0, row = 5) 

def write():
    text_file = open("Customers.txt","a")
    content = text_file.write("\nConfirmation: " + str(LN.get()) + ", " + str(FN.get()) + "\n"
                              + str(AR.get()) + "\n" + str(CT.get()) + ", " + str(ST.get()) + " " 
                              + str(ZC.get()))
    text_file.close()
    messagebox.showinfo("information","Data Recorded")

def quit():
    messagebox.showinfo("information","Thank you...")
    win.destroy() # closes the interface

def submit():   # function name
    messagebox.showinfo("information","entered :" + LN.get() + "," + FN.get() + "\n"
                        + AR.get() + "\n" + CT.get() + ", " + ST.get() + " " + ZC.get()) # display info

LN = tk.StringVar() # the StringVar manages the Entry widget
txtLastname = tk.Entry(win, width = 12, textvariable = LN).grid(column = 1, row = 0) # Text Entry widget
FN = tk.StringVar()
txtFirstname = tk.Entry(win, width = 12, textvariable = FN).grid(column = 1, row = 1) 
AR = tk.StringVar() # the StringVar manages the Entry widget
txtAddress = tk.Entry(win, width = 12, textvariable = AR).grid(column = 1, row = 2) 
CT = tk.StringVar() # the StringVar manages the Entry widget
txtCity = tk.Entry(win, width = 12, textvariable = CT).grid(column = 1, row = 3) 
ST = tk.StringVar() # the StringVar manages the Entry widget
txtState = tk.Entry(win, width = 12, textvariable = ST).grid(column = 1, row = 4) 
ZC = tk.StringVar() # the StringVar manages the Entry widget
txtZipcode = tk.Entry(win, width = 12, textvariable = ZC).grid(column = 1, row = 5) 


                                            # command calls the click function
btnSubmit = tk.Button(win, text = "submit", command = submit).grid(column = 0, row = 10) # Button widget

                                            # command calls the quit function
btnQuit = tk.Button(win, text = "quit", command = quit).grid(column = 1, row = 10) # Button widget

                                            # call the function write
btnWrite = tk.Button(win, text = "transfer", command = write).grid(column = 2, row = 10) # Button widget

win.mainloop() # ensures the interfaces stays on the screen on window
submit()


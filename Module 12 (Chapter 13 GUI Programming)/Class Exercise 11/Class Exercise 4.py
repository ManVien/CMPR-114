# Create three BUTTONS and when pressed, it will display a POSITIVE QUOTE.

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tkinter.Tk()

        self.main_window.geometry("200x100")

        # Create three Button widget, each with a different
        # positive quote as its text and a corresponding
        # command that displays that quote when the button
        # is clicked.
        self.my_button1 = tkinter.Button(self.main_window, 
                                        text='Positive Quote 1', 
                                        command=self.display_quote1)

        self.my_button2 = tkinter.Button(self.main_window, 
                                        text='Positive Quote 2', 
                                        command=self.display_quote2)

        self.my_button3 = tkinter.Button(self.main_window, 
                                        text='Positive Quote 3', 
                                        command=self.display_quote3)

        # Pack the Button.
        self.my_button1.pack()
        self.my_button2.pack()
        self.my_button3.pack()

        # Enter the tkinter main loop.
        tkinter.mainloop()

    def display_quote1(self):
        # Display an info dialog box.
        tkinter.messagebox.showinfo('Positive Quote 1', 
                                    'You can do it!')

    def display_quote2(self):
        # Display an info dialog box.
        tkinter.messagebox.showinfo('Positive Quote 2', 
                                    'Believe in yourself!')

    def display_quote3(self):
        # Display an info dialog box.
        tkinter.messagebox.showinfo('Positive Quote 3', 
                                    'The best view comes after the hardest climb.')
        
# Create an instance of the MyGUI class.
if __name__ == '__main__':
    my_gui = MyGUI()
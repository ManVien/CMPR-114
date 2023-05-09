# Create three labels with values of last name, 
# first name, and age.

import tkinter

class MyGUI:
    def __init__(self):

    # Create the main window widget.
        self.main_window = tkinter.Tk()

    # Modify the title bar width 
        self.main_window.geometry("300x100")

    # Create three labels with values of last name, 
    # first name, and age
        self.last_name_label = tkinter.Label(self.main_window, text = 'Vien')
        self.first_name_label = tkinter.Label(self.main_window, text = 'Man')
        self.age_label = tkinter.Label(self.main_window, text = '26')
    
    # Call the labels widget's pack method.
        self.last_name_label.pack()
        self.first_name_label.pack()
        self.age_label.pack()

    # Enter the tkinter main loop.
        tkinter.mainloop()

# Create an instance of the MyGUI class.
if __name__ == '__main__':
    my_gui = MyGUI()

# Using the geometry method, increase the width so the title is visible
import tkinter

class MyGUI:
    def __init__(self):

    # Create the main window widget.
        self.main_window = tkinter.Tk()

    # Modify the title bar width 
        self.main_window.geometry("300x100")

    # Display a title.
        self.main_window.title('My First GUI')

    # Enter the tkinter main loop.
        tkinter.mainloop()

# Create an instance of the MyGUI class.
if __name__ == '__main__':
    my_gui = MyGUI()

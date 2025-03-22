from tkinter import *

class GUI01:
    # Constructor
    def __init__(self):
        # Create a window
        self.window = Tk()
        self.window.geometry("300x50")
        self.window.title("GUI Example")

        # Create a button and register a handler
        self.btn = Button(self.window, text="Click Me", command=self.clicked)
        self.btn.grid(column=0, row=0)

        # Create a label
        self.lbl = Label(self.window, text="Hello")
        self.lbl.grid(column=1, row=0)

    # Handler for the button
    def clicked(self):
        self.lbl.configure(text="Button was clicked!")

    # method to run the window
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    gui = GUI01()
    gui.run()

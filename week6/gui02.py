from tkinter import *
from tkinter import messagebox as msg

class GUI02:
    # constructor
    def __init__(self):
        self.create_window()
        self.create_widgets()
    
    def create_window(self):
        self.window = Tk()
        self.window.geometry("300x100")
        self.window.title("GUI 02")

    def create_widgets(self):
        self.lbl_name = Label(self.window, text='Name:')
        self.lbl_name.grid(column=0, row=0, sticky=E)

        self.txt_name = Entry(self.window, width=20)
        self.txt_name.grid(column=1, row=0, sticky=W)

        self.btn_hello = Button(self.window, text='Hello', command=self.btn_hello_clicked)
        self.btn_hello.grid(column=1, row=1, sticky=W)

        self.lbl_hello = Label(self.window, text='')
        self.lbl_hello.grid(column=1, row=2, sticky=W)

        self.txt_hello = Entry(self.window, width=20)
        self.txt_hello.grid(column=1, row=3, sticky=W)
    
    def btn_hello_clicked(self):
        # Get the name from the text box
        name = self.txt_name.get()
        # Display a message box
        msg.showinfo('Hello', f'Hello {name}!')
        # Update the label
        self.lbl_hello.configure(text=f'Hello {name}!')
        # Update the text box
        self.txt_hello.delete(0, END)       # Clear the text box
        self.txt_hello.insert(0, f'Hello {name}!') # Insert the new text
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    gui = GUI02()
    gui.run()
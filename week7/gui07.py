from tkinter import *
from tkinter import messagebox as msg

class GUI05:
    def __init__(self):
        self.create_window()
        self.create_widgets()
    
    def create_window(self):
        self.window = Tk()
        self.window.geometry("250x240")
        self.window.title("GUI 05")
    
    def create_widgets(self):
        self.lbl_chooseitems = Label(self.window, text='Choose Items:')
        self.lbl_chooseitems.grid(column=0, row=0, sticky=W, columnspan=2)

        self.book_value = IntVar()
        self.chk_books = Checkbutton(self.window, text='Books ($10)', variable=self.book_value)
        self.chk_books.grid(column=1, row=1, sticky=W)

        self.notebook_value = IntVar()
        self.chk_notebooks = Checkbutton(self.window, text='Notebooks ($5)', variable=self.notebook_value)
        self.chk_notebooks.grid(column=1, row=2, sticky=W)

        self.bag_value = IntVar()
        self.chk_bag = Checkbutton(self.window, text='Bag ($15)', variable=self.bag_value)
        self.chk_bag.grid(column=1, row=3, sticky=W)

        self.btn_confirm = Button(self.window, text='Confirm', command=self.btn_confirm_clicked)
        self.btn_confirm.grid(column=1, row=4, sticky=W)

        self.lbl_total = Label(self.window, text='Total:')
        self.lbl_total.grid(column=0, row=5, sticky=E)

        self.lbl_totalamount = Label(self.window, text='$0')
        self.lbl_totalamount.grid(column=1, row=5, sticky=W)
    
    def btn_confirm_clicked(self):
        total = 0
        if self.book_value.get() == 1: # checkbutton for book is checked
            total += 10
        if self.notebook_value.get() == 1: # checkbutton for notebook is checked
            total += 5
        if self.bag_value.get() == 1: # checkbutton for bag is checked
            total += 15
        # update the total amount
        self.lbl_totalamount.config(text=f'${total}')

    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    window = GUI05()
    window.run()
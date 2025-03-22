from tkinter import *
from tkinter import messagebox as msg

class GUI03:
    # constructor
    def __init__(self):
        self.create_window()
        self.create_widgets()
    
    def create_window(self):
        self.window = Tk()
        self.window.geometry('300x300')
        self.window.title('GUI 03')
    
    def create_widgets(self):
        self.lbl_product = Label(self.window, text='Product:')
        self.lbl_product.grid(column=0, row=0, sticky=E)

        self.txt_product = Entry(self.window, width=20)
        self.txt_product.grid(column=1, row=0, sticky=W)

        self.lbl_price = Label(self.window, text='Price:')
        self.lbl_price.grid(column=0, row=1, sticky=E)

        self.txt_price = Entry(self.window, width=20)
        self.txt_price.grid(column=1, row=1, sticky=W)

        self.lbl_quantity = Label(self.window, text='Quantity:')
        self.lbl_quantity.grid(column=0, row=2, sticky=E)

        self.txt_quantity = Entry(self.window, width=20)
        self.txt_quantity.grid(column=1, row=2, sticky=W)

        self.btn_buy = Button(self.window, text='Buy', command=self.btn_buy_clicked)
        self.btn_buy.grid(column=1, row=3, sticky=W)

        self.lbl_receipt = Label(self.window, text='Receipt:')
        self.lbl_receipt.grid(column=0, row=4, sticky=E)

        self.txt_receipt = Entry(self.window, width=20)
        self.txt_receipt.grid(column=1, row=4, sticky=W)

    def btn_buy_clicked(self):
        product = self.txt_product.get() # Get the product name
        price = float(self.txt_price.get()) # Get the price
        quantity = int(self.txt_quantity.get()) # Get the quantity
        total = price * quantity # Calculate the total
        
        receipt = f'{quantity} {product}, ${total}'
        self.txt_receipt.delete(0, END) # Clear the text box
        self.txt_receipt.insert(0, receipt) # Insert the new text
    
    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    gui = GUI03()
    gui.run()

from tkinter import *
from tkinter import messagebox as msg

class GUI08:
    def __init__(self):
        self.create_window()
        self.create_widgets()
    
    def create_window(self):
        self.window = Tk()
        self.window.geometry("250x240")
        self.window.title("GUI 08")

    def create_widgets(self):
        self.lbl_pizza_delivery = Label(self.window, text='Pizza Delivery')
        self.lbl_pizza_delivery.grid(column=0, row=0, sticky='WE', columnspan=2)

        self.lbl_pizza = Label(self.window, text='Pizza:')
        self.lbl_pizza.grid(column=0, row=1, sticky=E)

        self.pizza_value = IntVar()
        self.rd_mozzarella = Radiobutton(self.window, text='Mozzarella ($10)', variable=self.pizza_value, value=10, command=self.calculate_total)
        self.rd_mozzarella.grid(column=1, row=1, sticky=W)

        self.rd_seafood = Radiobutton(self.window, text='Seafood ($15)', variable=self.pizza_value, value=15, command=self.calculate_total)
        self.rd_seafood.grid(column=1, row=2, sticky=W)

        self.rd_sausage = Radiobutton(self.window, text='Sausage ($12)', variable=self.pizza_value, value=12, command=self.calculate_total)
        self.rd_sausage.grid(column=1, row=3, sticky=W)

        self.lbl_drink = Label(self.window, text='Drink:')
        self.lbl_drink.grid(column=0, row=4, sticky=E)

        self.drink_value = IntVar()
        self.rd_coke = Radiobutton(self.window, text='Coke ($2)', variable=self.drink_value, value=2, command=self.calculate_total)
        self.rd_coke.grid(column=1, row=4, sticky=W)

        self.rd_juice = Radiobutton(self.window, text='Juice ($3)', variable=self.drink_value, value=3, command=self.calculate_total)
        self.rd_juice.grid(column=1, row=5, sticky=W)

        self.rd_water = Radiobutton(self.window, text='Water (Free)', variable=self.drink_value, value=0, command=self.calculate_total)
        self.rd_water.grid(column=1, row=6, sticky=W)

        self.lbl_total = Label(self.window, text='Total:')
        self.lbl_total.grid(column=0, row=7, sticky=E)

        self.lbl_totalamount = Label(self.window, text='$0')
        self.lbl_totalamount.grid(column=1, row=7, sticky=W)

    def calculate_total(self):
        total = 0
        total += self.pizza_value.get()
        total += self.drink_value.get()
        self.lbl_totalamount.config(text=f'${total}')

    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    window = GUI08()
    window.run()
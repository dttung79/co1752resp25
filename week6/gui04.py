from tkinter import *
from tkinter import messagebox as msg

class GUI04:
    def __init__(self):
        self.create_window()
        self.create_widgets()
    
    def create_window(self):
        self.window = Tk()
        self.window.geometry("300x400")
        self.window.title("GUI 04")

    def create_widgets(self):
        self.lbl_comp1682 = Label(self.window, text='COMP1682')
        self.lbl_comp1682.grid(column=0, row=0, sticky=E)

        self.txt_comp1682 = Entry(self.window, width=20)
        self.txt_comp1682.grid(column=1, row=0, sticky=W)

        self.lbl_comp1701 = Label(self.window, text='COMP1701')
        self.lbl_comp1701.grid(column=0, row=1, sticky=E)

        self.txt_comp1701 = Entry(self.window, width=20)
        self.txt_comp1701.grid(column=1, row=1, sticky=W)

        self.lbl_comp1711 = Label(self.window, text='COMP1711')
        self.lbl_comp1711.grid(column=0, row=2, sticky=E)

        self.txt_comp1711 = Entry(self.window, width=20)
        self.txt_comp1711.grid(column=1, row=2, sticky=W)

        self.btn_calculate = Button(self.window, text='Calculate', command=self.btn_calculate_clicked)
        self.btn_calculate.grid(column=1, row=3, sticky=W)

        self.lbl_average = Label(self.window, text='Average:')
        self.lbl_average.grid(column=0, row=4, sticky=E)

        self.txt_average = Entry(self.window, width=20)
        self.txt_average.grid(column=1, row=4, sticky=W)

        self.lbl_rank = Label(self.window, text='Rank:')
        self.lbl_rank.grid(column=0, row=5, sticky=E)

        self.txt_rank = Entry(self.window, width=20)
        self.txt_rank.grid(column=1, row=5, sticky=W)

    def btn_calculate_clicked(self):
        comp1682 = float(self.txt_comp1682.get())
        comp1701 = float(self.txt_comp1701.get())
        comp1711 = float(self.txt_comp1711.get())
        
        average = (comp1682 + comp1701 + comp1711) / 3
        if average < 40 or comp1682 < 40 or comp1701 < 40 or comp1711 < 40:
            rank = 'Unqualified'
        elif average < 65:
            rank = 'Qualified'
        elif average < 80:
            rank = 'Merit'
        else:
            rank = 'Distinction'
        
        self.txt_average.delete(0, END)
        self.txt_average.insert(0, f'{average:.2f}')
        self.txt_rank.delete(0, END)
        self.txt_rank.insert(0, rank)

    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    gui = GUI04()
    gui.run()
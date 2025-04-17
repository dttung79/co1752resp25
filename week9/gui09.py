from tkinter import *
from tkinter import messagebox as msg
from base_gui import BaseGUI
from book import Book
from tkinter import filedialog

class BookManager(BaseGUI):
    def __init__(self, dimensions="500x240", title="Book Manager"):
        super().__init__(dimensions, title)
        self.books = []
        #self.load_books()

    def load_books(self):
        file_name = filedialog.askopenfilename(title="Select a file", filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))

        with open(file_name, 'r') as file:
            # skip the header line
            next(file)
            for line in file:
                title, author, price = line.strip().split(',')
                book = Book(title, author, float(price))
                self.books.append(book)

        self.lst_books.delete(0, END)  # clear the listbox
        for book in self.books:
            self.lst_books.insert(END, book.title)

    def create_widgets(self):
        self.lbl_title = Label(self.window, text='Title:')
        self.lbl_title.grid(row=0, column=0, sticky=W)

        self.txt_title = Entry(self.window)
        self.txt_title.grid(row=0, column=1, sticky=W, columnspan=3)
        self.txt_title.focus()

        self.lbl_author = Label(self.window, text='Author:')
        self.lbl_author.grid(row=1, column=0, sticky=W)

        self.txt_author = Entry(self.window)
        self.txt_author.grid(row=1, column=1, sticky=W, columnspan=3)

        self.lbl_price = Label(self.window, text='Price:')
        self.lbl_price.grid(row=2, column=0, sticky=W)

        self.txt_price = Entry(self.window)
        self.txt_price.grid(row=2, column=1, sticky=W, columnspan=3)

        self.btn_add = Button(self.window, text='Add', command=self.add_book)
        self.btn_add.grid(row=3, column=1, sticky=W)

        self.btn_edit = Button(self.window, text='Edit', command=self.edit_book)
        self.btn_edit.grid(row=3, column=2, sticky=W)

        self.btn_delete = Button(self.window, text='Delete', command=self.delete_book)
        self.btn_delete.grid(row=3, column=3, sticky=W)

        self.lst_books = Listbox(self.window, width=25, selectmode=SINGLE, exportselection=FALSE)
        self.lst_books.grid(row=0, column=4, rowspan=4, columnspan=2, sticky=W)
        self.lst_books.bind('<<ListboxSelect>>', self.book_selected)

        self.btn_load = Button(self.window, text='Load Books', command=self.load_books)
        self.btn_load.grid(row=4, column=4, sticky=W)

        self.btn_save = Button(self.window, text='Save Books', command=self.save_books)
        self.btn_save.grid(row=4, column=5, sticky=E)

    def save_books(self):
        file_name = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
        with open(file_name, 'w') as file:
            file.write("Title,Author,Price\n") # write header
            for b in self.books:
                file.write(f"{b.title},{b.author},{b.price}\n")
        msg.showinfo("Books Saved", "Books saved successfully.")

    def delete_book(self):
        try:
            selected_index = self.lst_books.curselection()[0]
            msg.showerror("No Selection", "Please select a book to delete.")

            self.lst_books.delete(selected_index)
            self.books.pop(selected_index)
            msg.showinfo("Book Deleted", "Book deleted successfully.")
        except IndexError:
            msg.showerror("No Selection", "Please select a book to delete.")

    def book_selected(self, event):
        # get current selection from the listbox
        selected_index = self.lst_books.curselection()[0]
        # get the selected book from the list
        book = self.books[selected_index]
        self.txt_title.delete(0, END)
        self.txt_title.insert(0, book.title)
        self.txt_author.delete(0, END)
        self.txt_author.insert(0, book.author)
        self.txt_price.delete(0, END)
        self.txt_price.insert(0, str(book.price))
    
    def edit_book(self):
        # get the selected book from the list
        selected_index = self.lst_books.curselection()[0]
        book = self.books[selected_index]
        
        if self.txt_title.get() == "" or self.txt_author.get() == "" or self.txt_price.get() == "":
            msg.showerror("Invalid Input", "Please fill in all fields.")
            return
        
        # update the book's details
        book.title = self.txt_title.get()
        book.author = self.txt_author.get()
        try:
            book.price = float(self.txt_price.get())
        except ValueError:
            msg.showerror("Invalid Input", "Please enter a valid price.")
            return
        # update the listbox
        self.lst_books.delete(selected_index)
        self.lst_books.insert(selected_index, book.title)

        msg.showinfo("Book Updated", f"Book '{book.title}' updated successfully.")

    def add_book(self):
        try:
            title = self.txt_title.get() # get the title from the entry
            author = self.txt_author.get() # get the author from the entry
            price = float(self.txt_price.get()) # get the price from the entry
            a_book = Book(title, author, price) # create a book object
            self.books.append(a_book) # add the book to the list
            self.lst_books.insert(END, title) # add the title to the listbox
            msg.showinfo("Book Added", f"Book '{title}' added successfully.")
        except ValueError:
            msg.showerror("Invalid Input", "Please enter a valid price.")

if __name__ == '__main__':
    window = BookManager()
    window.run()
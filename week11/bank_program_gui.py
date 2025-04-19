from tkinter import filedialog
from base_gui import BaseGUI
from account import Account
from normal_account import NormalAccount
from debit_account import DebitAccount
from bank_manager import BankManager
from tkinter import *
from tkinter import messagebox as msb

class BankProgramGUI(BaseGUI):
    def __init__(self, dimensions="600x400", title="Bank Program"):
        super().__init__(dimensions=dimensions, title=title)
        self.bank_manager = BankManager("TPBank")   # create an object of BankManager
    
    def create_widgets(self):
        # listbox to display accounts
        self.lst_accounts = Listbox(self.window, width=30)
        self.lst_accounts.grid(row=0, column=0, rowspan=5, columnspan=2, padx=10, pady=10)
        # bind listbox selection to view account details
        self.lst_accounts.bind('<<ListboxSelect>>', self.view_account)
        # buttons load and save
        self.btn_load = Button(self.window, text="Load", command=self.load_accounts)
        self.btn_load.grid(row=5, column=0, padx=10, pady=10)
        self.btn_save = Button(self.window, text="Save")
        self.btn_save.grid(row=5, column=1, padx=10, pady=10)
        # display account details
        self.lbl_id = Label(self.window, text="ID:")
        self.lbl_id.grid(row=0, column=2, padx=10, pady=10)
        self.txt_id = Entry(self.window)
        self.txt_id.grid(row=0, column=3, columnspan=3, padx=10, pady=10)

        self.lbl_type = Label(self.window, text="Type:")
        self.lbl_type.grid(row=1, column=2, padx=10, pady=10, sticky="E")

        self.type_var = IntVar()
        self.rd_debit = Radiobutton(self.window, text="Debit", variable=self.type_var, value=0)
        self.rd_debit.grid(row=1, column=3, columnspan=3, padx=10, pady=10, sticky="W")
        self.rd_normal = Radiobutton(self.window, text="Normal", variable=self.type_var, value=1)
        self.rd_normal.grid(row=2, column=3, columnspan=3, padx=10, pady=10, sticky="W")

        self.lbl_balance = Label(self.window, text="Balance:")
        self.lbl_balance.grid(row=3, column=2, padx=10, pady=10, sticky="E")
        self.txt_balance = Entry(self.window)
        self.txt_balance.grid(row=3, column=3, columnspan=3, padx=10, pady=10)
        self.lbl_limit = Label(self.window, text="Limit:")
        self.lbl_limit.grid(row=4, column=2, padx=10, pady=10, sticky="E")
        self.txt_limit = Entry(self.window)
        self.txt_limit.grid(row=4, column=3, columnspan=3, padx=10, pady=10)

        self.btn_add = Button(self.window, text="Add")
        self.btn_add.grid(row=5, column=3, padx=10, pady=10)
        self.btn_edit = Button(self.window, text="Edit")
        self.btn_edit.grid(row=5, column=4, padx=10, pady=10)
        self.btn_del = Button(self.window, text="Del")
        self.btn_del.grid(row=5, column=5, padx=10, pady=10)

        actions = ['Deposit', 'Withdraw']
        self.var_action = StringVar()
        self.var_action.set(actions[0])
        self.cmb_action = OptionMenu(self.window, self.var_action, *actions)
        self.cmb_action.grid(row=6, column=0, padx=10, pady=10)

        self.lbl_amount = Label(self.window, text="Amount:")
        self.lbl_amount.grid(row=6, column=2, padx=10, pady=10, sticky="E")
        self.txt_amount = Entry(self.window)
        self.txt_amount.grid(row=6, column=3, columnspan=3, padx=10, pady=10)
        self.txt_amount.bind('<Return>', self.do_action)
    
    def do_action(self, event):
        # get selected account ID
        selected_index = self.lst_accounts.curselection()[0]
        # get account with the selected ID
        account = self.bank_manager.find_by_id(selected_index + 1)
        if self.var_action.get() == 'Deposit':
            # get amount from text box
            amount = float(self.txt_amount.get())
            # deposit amount to account
            account.deposit(amount)
            # update the account balance
            self.txt_balance.delete(0, END)
            self.txt_balance.insert(0, account.balance)
            msb.showinfo("Success", f"Deposited ${amount} to account ID {account.id}. New balance: ${account.balance}")
        elif self.var_action.get() == 'Withdraw':
            amount = float(self.txt_amount.get())
            # withdraw amount from account
            account.withdraw(amount)

            self.txt_balance.delete(0, END)
            self.txt_balance.insert(0, account.balance)
            msb.showinfo("Success", f"Withdrew ${amount} from account ID {account.id}. New balance: ${account.balance}")
    def load_accounts(self):
        file_name = filedialog.askopenfilename(title="Select a file", filetypes=[("CSV files", "*.csv")])
        with open(file_name, 'r') as f:
            lines = f.readlines()
            # skip the header
            lines = lines[1:]
            for line in lines:
                data = line.strip().split(',')
                account_type = data[1]
                balance = float(data[2])
                limit = float(data[3])
                self.bank_manager.add_account(balance, account_type, limit)
                self.lst_accounts.insert(END, f"ID: {self.bank_manager._accounts[-1].id}")

    def view_account(self, event):
        # get the selected account ID
        selected_index = self.lst_accounts.curselection()[0]
        # get account with the selected ID
        account = self.bank_manager.find_by_id(selected_index + 1)
        if account != None:
            # set the account details in the text boxes
            self.txt_id.delete(0, END)
            self.txt_id.insert(0, account.id)
            self.txt_balance.delete(0, END)
            self.txt_balance.insert(0, account.balance)
            if isinstance(account, DebitAccount):
                self.type_var.set(0)
                self.txt_limit.delete(0, END)
                self.txt_limit.insert(0, account._limit)
            else:
                self.type_var.set(1)
                self.txt_limit.delete(0, END)
                self.txt_limit.insert(0, 0)
        else:
            msb.showerror("Error", "Account not found")
if __name__ == "__main__":
    gui = BankProgramGUI()
    gui.run()
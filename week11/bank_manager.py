from normal_account import NormalAccount
from debit_account import DebitAccount

class BankManager:
    def __init__(self, name):
        self._name = name
        self._accounts = self._load_accounts()

    @property
    def name(self):
        return self._name
    
    def _load_accounts(self):
        # Load accounts from a file or database
        # For simplicity, we'll just create some dummy accounts here
        return [
            NormalAccount(1000),
            DebitAccount(2000, 500),
            NormalAccount(3000)
        ]
    
    def add_account(self, balance, account_type='normal', limit=0):
        if account_type == 'normal':
            account = NormalAccount(balance)
        elif account_type == 'debit':
            account = DebitAccount(balance, limit)
        else:
            raise ValueError("Invalid account type")
        
        self._accounts.append(account)
        print(f"Added new {account_type} account successfully.")
        print(account)

    def __find_by_id(self, acc_id):
        for account in self._accounts:
            if account.id == acc_id:
                return account
        return None
    
    def remove_account(self, acc_id):
        acc = self.__find_by_id(acc_id)
        if acc == None:
            print(f"Account with ID {acc_id} not found.")
            return
        self._accounts.remove(acc)
        print(f"Account with ID {acc_id} removed successfully.")
    
    def view_account(self, acc_id):
        acc = self.__find_by_id(acc_id)
        if acc == None:
            print(f"Account with ID {acc_id} not found.")
            return
        print(acc)
    
    def deposit(self, acc_id, amount):
        acc = self.__find_by_id(acc_id)
        if acc == None:
            print(f"Account with ID {acc_id} not found.")
            return
        acc.deposit(amount)

    def withdraw(self, acc_id, amount):
        acc = self.__find_by_id(acc_id)
        if acc == None:
            print(f"Account with ID {acc_id} not found.")
            return
        acc.withdraw(amount)
    
    def view_all(self):
        print("All accounts in bank:")
        for acc in self._accounts:
            print(acc)
        print("Total accounts:", len(self._accounts))
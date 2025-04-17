from abc import ABC, abstractmethod

class Account(ABC):
    auto_id = 0 # class variable to automatically increment account ID
    def __init__(self, balance: float):
        self._balance = balance      # instance variable
        Account.auto_id += 1         # increment account ID for each new instance    
        self._id = Account.auto_id   # set the account ID for this instance

    @property
    def id(self):
        return self._id
    
    @property
    def balance(self):
        return self._balance
    
    @abstractmethod
    def deposit(self, amount: float):
        pass

    @abstractmethod
    def withdraw(self, amount: float):
        pass

    def __str__(self):
        return f'Account ID: {self._id}, Balance: ${self._balance}'
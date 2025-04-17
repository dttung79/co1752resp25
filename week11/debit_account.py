from account import Account

class DebitAccount(Account):
    def __init__(self, balance: float, limit: float = 0):
        self._limit = limit
        super().__init__(balance)
    
    # override the deposit method
    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
        print(f"Deposited ${amount}. New balance: ${self._balance}")
    
    # override the withdraw method
    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance + self._limit:
            raise ValueError("Withdrawal exceeds balance and limit")
        self._balance -= amount
        print(f"Withdrew ${amount}. New balance: ${self._balance}")

    # override the __str__ method to add limit information
    def __str__(self):
        return super().__str__() + f", Limit: ${self._limit}"

if __name__ == "__main__":
    debit_01 = DebitAccount(1000, 500)
    print(debit_01)
    debit_01.withdraw(1200) # can withdraw 1200 because of the limit
    try:
        debit_01.withdraw(500) # cannot be withdrawn because it exceeds the limit
    except ValueError as e:
        print(e)
    print(debit_01)
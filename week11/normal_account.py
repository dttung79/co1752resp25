from account import Account

class NormalAccount(Account):
    def __init__(self, balance: float):
        super().__init__(balance)   # Call the constructor of the parent class

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
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        print(f"Withdrew ${amount}. New balance: ${self._balance}")

if __name__ == "__main__":
    # Example usage
    account_01 = NormalAccount(1000)
    print(account_01)
    account_01.deposit(500)
    account_01.withdraw(200)
    print(account_01)

    account_02 = NormalAccount(2000)
    print(account_02)

    acount_03 = NormalAccount(3000)
    print(acount_03)



from bank_manager import BankManager

def main():
    running = True
    bank = BankManager("TPBank")
    while running:
        print_menu(bank)
        choice = int(input("Enter your choice: "))
        if choice == 1: add_account(bank)
        elif choice == 2: remove_account(bank)
        elif choice == 3: view_account(bank)
        elif choice == 4: deposit(bank)
        elif choice == 5: withdraw(bank)
        elif choice == 6: view_all(bank)
        elif choice == 7: running = False
        else: print("Invalid choice. Please try again.")

def print_menu(bank):
    print(f"\nWelcome to {bank.name} Bank")
    print("Please choose an option:")
    print("1. Add Account")
    print("2. Remove Account")
    print("3. View Account")
    print("4. Deposit")
    print("5. Withdraw")
    print("6. View All Accounts")
    print("7. Exit")

def add_account(bank):
    balance = float(input("Enter initial balance: "))
    account_type = input("Enter account type (normal/debit): ").lower()
    limit = 0
    if account_type == 'debit':
        limit = float(input("Enter debit limit: "))
    bank.add_account(balance, account_type, limit)

def remove_account(bank):
    acc_id = int(input("Enter account ID to remove: "))
    bank.remove_account(acc_id)

def view_account(bank):
    acc_id = int(input("Enter account ID to view: "))
    bank.view_account(acc_id)

def deposit(bank):
    try:
        acc_id = int(input("Enter account ID to deposit to: "))
        amount = float(input("Enter deposit amount: "))
        bank.deposit(acc_id, amount)
    except ValueError as e:
        print(f"Error: {e}")

def withdraw(bank):
    try:
        acc_id = int(input("Enter account ID to withdraw from: "))
        amount = float(input("Enter withdrawal amount: "))
        bank.withdraw(acc_id, amount)
    except ValueError as e:
        print(f"Error: {e}")

def view_all(bank):
    bank.view_all()

if __name__ == "__main__":
    main()
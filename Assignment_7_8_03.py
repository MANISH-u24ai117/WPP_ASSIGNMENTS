class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, balance=0):
        self.accounts[account_number] = balance

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number] += amount
            print(f"Deposited {amount} to account {account_number}.")
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number] >= amount:
                self.accounts[account_number] -= amount
                print(f"Withdrew {amount} from account {account_number}.")
            else:
                print("Insufficient funds.")
        else:
            print("Account not found.")

    def display_balance(self, account_number):
        if account_number in self.accounts:
            print(f"Balance of account {account_number}: {self.accounts[account_number]}")
        else:
            print("Account not found.")

# User Input
bank = Bank()
account_number = input("Enter account number: ")
balance = float(input("Enter initial balance: "))
bank.create_account(account_number, balance)

deposit_amount = float(input("Enter amount to deposit: "))
bank.deposit(account_number, deposit_amount)

withdraw_amount = float(input("Enter amount to withdraw: "))
bank.withdraw(account_number, withdraw_amount)

bank.display_balance(account_number)

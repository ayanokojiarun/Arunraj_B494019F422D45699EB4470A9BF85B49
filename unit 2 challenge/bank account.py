class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ${amount}.\n New balance: ${self.__account_balance}")
        else:
            print("Invalid deposit amount.\n Amount must be greater than zero.\n")

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew ${amount}.\n New balance: ${self.__account_balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.\n")

    def display_balance(self):
        print(f"Account Balance for {self.__account_holder_name}: ${self.__account_balance}")

# Creating an instance of the BankAccount class
account1 = BankAccount("12345", "John Doe", 1000)

# Testing deposit and withdrawal functionality
account1.display_balance()
account1.deposit(500)
account1.withdraw(200)
account1.withdraw(1500)

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
        else: 
            print("Amount must be a positive integer!")

    def withdraw(self, amount):
        if amount > 0 and amount < self.__balance:
            self.__balance -= amount
        else:
            print("You don't have enough balance!")

    def display_account_info(self):
        print(f"Account number: ({self.__account_number}) Balance: P{self.__balance}")

    def __display_balance(self):
        print(f"{self.__balance}")

    def get_account_number(self):
        return self.__account_number
    
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, balance):
        if isinstance(balance, (int, float)) and balance >= 0:
            self.__balance = balance
            print(f"Balance updated to {self.__balance:.2f}.")
        else:
            print("Invalid balance. Balance must be a non-negative number.")
        

account = BankAccount("123456789", 500.00)
account.deposit(150.00)
account.withdraw(100.00)
account.set_balance(-50.00)
account.display_account_info()

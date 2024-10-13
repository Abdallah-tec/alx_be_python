class BankAccount():
    def __init__(self,account_Balance):
        self.account_Balance = account_Balance

    def deposit(self,amount):
        self.amount = amount
        self.account_Balance = self.account_Balance + amount
    
    def withdraw(self,amount):
        self.amount = amount
        if amount <= self.account_Balance :
            self.account_Balance = self.account_Balance - amount
            return True
        else:
            return False
    def display_balance(self):
        print(f"Current Balance: $['{self.account_Balance}']")



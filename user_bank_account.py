class BankAccount:

    all_instances = []

    def __init__(self, int_rate= 0.01, balance=0):
        self.int_rate= int_rate
        self.balance = balance
        BankAccount.all_instances.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            print(f"Insufficient funds")
        return self
    
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
            
    def yield_interest(self, amount):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        else:
            print(f"Error")
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_withdraw(self, amount):
        BankAccount(self.account.withdraw)        
        return self
    
    def make_deposit(self, amount):
        BankAccount(self.account.deposit)
        return self
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Checking Balance: {self.account.balance}")

Jake = User("Jake", "Jake@gmail.com")
Emily = User("Emily", "EmilyEmily@meh.com")

Jake.make_deposit(1000).make_withdraw(10).display()
Emily.make_deposit(10000).make_withdraw(260).display()
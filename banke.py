class BankAccount:
    owner =""
    balance =0.0
    def __init__(self,owner,balance):
        self.owner= owner
        self.balance = balance 

    def deposit(self,amount):
        self.balance+= amount
        print(self .owner, "deposited pkr", amount, " New balance:", self.balance,"pkr")

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            print(self.owner, "withdrew pkr", amount, " New balance:", self.balance,"pkr")
        else:
            print("Insufficient funds for", self.owner)

account1 = BankAccount("Alice", 1000.0)
account1.deposit(500.0)
account1.withdraw(200.0)  
print()
account2 = BankAccount("Bob", 2000.0)
account2.deposit(100000.0)    
account2.withdraw(9500.0)     

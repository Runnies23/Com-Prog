# class BankAccount:
#     def __init__(self, accountID:str, balance:float=0.00):
#         self.accountID = accountID
#         self.balance = balance

#     def __str__(self):
#         return f"ID: {self.accountID}, Balance: {self.balance:.2f}"
    
#     def set_account_ID(self, newID):
#         self.accountID = newID

#     def set_balance(self,new_balance):
#         self.balance = new_balance

#     def get_account_ID(self):
#         return self.accountID
    
#     def get_balance(self):
#         return self.balance
    
#     def deposit(self, amount):
#         self.balance += amount

#     def withdrawal(self, amount):
#         self.balance -= amount

class BankAccount:
    def __init__(self, accountID: str="1001", balance: float=0.00):
        self.accountID = accountID
        self.balance = balance

    def __str__(self) -> str:
        return f"ID: {self.accountID}, Balance: {self.balance:.2f}"

    def set_accout_ID(self, newID: str):
        self.accountID = newID

    def set_balance(self, new_balance: float):
        self.balance = new_balance

    def get_account_ID(self) -> str:
        return self.accountID
    
    def get_balance(self) -> int:
        return self.balance
    
    def deposit(self, amount: float):
        self.balance += amount

    def withdrawal(self, amount: float):
        self.balance -= amount
        
account = BankAccount("1001", 500)

while True:
    choice = int(input("Deposit (1), Withdrawal (2), Update (3), or Exit (0): "))
    if choice == 0:
        break
    elif choice == 1:
        amount = float(input("Enter your deposit amount: "))
        account.deposit(amount)
        print(account)
    elif choice == 2:
        amount = float(input("Enter your withdrawal amount: "))
        account.withdrawal(amount)
        print(account)
    else:
        amount = float(input("Enter your update amount: "))
        account.set_balance(amount)
        print(account)



# account = BankAccount("1001",500)

# print(account.get_account_ID())
# print(account.get_balance())
# account.set_balance(5000)
# print(account.get_balance())

# amount = float(input("Enter your deposit amount: "))
# account.deposit(amount)
# print(amount)

# amount = float(input("Enter your withdrawal amount: "))
# account.withdrawal(amount)
# print(account)

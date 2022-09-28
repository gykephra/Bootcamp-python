from datetime import datetime, date
from operator import ne
class BankAccount:
    def __init__(self, account_number, account_name, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []
        if balance > 0:
            self.deposit(balance, account_name, "Alice Ilboudo", "BCB Centre")
    
    def view_balance(self, person, user, venue, amount=0):
        self.transactions.append({'transaction_type': 'View Balance', 'transaction_time': datetime.now(), 'transaction_amount': amount, 'transaction_by': person, 'transaction_operator': user, 'transaction_venue': venue})
        print(f"Balance for account {self.account_number}: {self.balance}")
    
    def deposit(self, amount, person, user, venue):
        if amount <= 0:
            print("Invalid amount")
        elif amount < 100:
            print("Minimum deposit is 100")
        else:
            self.balance += amount
            self.transactions.append({'transaction_type': 'Deposit', 'transaction_time': datetime.now(), 'transaction_amount': amount, 'transaction_by': person, 'transaction_operator': user, 'transaction_venue': venue})
            print("Deposit Succcessful")
    
    def withdraw(self, amount, person, user, venue):
        if amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance -= amount
            self.transactions.append({'transaction_type':'withdrawal', 'transaction_time': datetime.now(), 'transaction_amount': amount, 'transaction_by': person, 'transaction_operator': user, 'transaction_venue': venue})
            print("Withdraw Approved")
            return amount
    
    def view_transactions(self):
        print("Transactions:")
        print("-------------\n\n\n")
        for transaction in self.transactions:
            print(transaction)
            print("\n---")

newCount = BankAccount("BA0001","YAO Ephra", 75000000)
newCount.view_balance("YAO Ephra","Alex Kam","IB_Bank")
newCount.deposit(1000000,"")
newCount.view_balance("")
newCount.withdraw()
newCount.view_balance()
newCount.view_transactions()

transactions = newCount.transactions
print(f" Le nombre de transactions est :{len(transactions)}")
print(transactions)

from django.db import models

# Create your models here.
class bankAcct:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = 0
    def make_deposit(self, amount):
        self.balance += amount
        return self
    def make_withdrawal(self, amount):
        if (self.balance - amount) > 0:
    	    self.balance -= amount
        else:
    	    print("INSUFFICIENT FUNDS")
    	return self
    def display_acct_info(self):
        print(self.balance)
        print(self.int_rate)
        return self
    def yield_interest(self):
        self.balance *= self.int_rate
        return self

class RetirementAccount(bankAcct):
    def __init__(self, int_rate, is_roth, balance=0):
        self.int_rate = int_rate
        self.balance = balance
    	self.is_roth = is_roth  
class RetirementAccount(bankAcct):
    def withdraw(self, amount, is_early):
    	if is_early:
    	    amount = amount * 1.10
    	if (self.balance - amount) > 0:
    	    self.balance -= amount
        else:
    	    print("INSUFFICIENT FUNDS")
    	return self

class User:
    def __init__(self, name, email, balance):
        self.name = name
        self.email = email
        self.balance = 0
        self.acct = bankAcct(int_rate=.2, balance=balance)
    def make_deposit(self, amount):
        self.acct.balance += amount
        return self
    def make_withdrawal(self, amount):
        self.acct.balance -=amount
        return self
    def display_user_balance(self):
        print(self.acct.balance)
        print(self.name)
        return self
    def transfer_money(self, other_user, amount):
        self.acct.balance = amount
        other_user.acct.balance += amount
        return self

# Create a BankAccount class

# Every bank account should have balance and interest_rate attributes (instance variables)

# Since we want these fields to be set for every account, you'll need to add an __init__ method to your class

# At this point you should test out creating an instance of your class to make sure it works

# Define a __str__() instance method so you can print bank account objects and see a nice, meaningful string. Make sure this method returns a string, rather than printing it!

# Your class should have an instance method called deposit that accepts one amount argument and adds that amount to the total balance

# Test out your method by calling it on an instance of your class

# There should be a withdraw instance method that accepts one amount argument and subtracts it from the total balance

# Don't forget to test it out!

# Finally, there should be a gain_interest instance method that increases the total balance according to the interest rate.

class BankAccount:
    def __init__(self, name, balance, interest_rate):
        self.name = name
        self.balance = balance
        self.interest_rate = interest_rate
    
    def __str__(self):
        return 'this bank account belongs to {}, the current balance is ${} and the interest rate is {}%'.format(self.name, self.balance, self.interest_rate*100)
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount

    def gain_interest(self):
        self.balance *= (1+self.interest_rate)

account1 = BankAccount('Adam', 10000, 0.02)

print(account1)
account1.deposit(10000)
print(account1)
account1.withdraw(100)
print(account1)
account1.gain_interest()
print(account1)
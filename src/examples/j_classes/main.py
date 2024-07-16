import account

a = account.Account(250) #created a variable/object of the Account class type
balance = a.get_balance()
print(balance)


amount = int(input("enter withdraw amount: "))

a.withdraw(amount)
balance = a.get_balance()

print(balance)


amount = int(input("enter deposit amount: "))

a.deposit(amount)
balance = a.get_balance()

print(balance)

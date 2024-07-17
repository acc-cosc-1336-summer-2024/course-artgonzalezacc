import account
import atm

a = account.Account(0) #created a variable/object of the Account class type
balance = a.get_balance()
print(balance)

atm = atm.ATM(a)
atm.make_deposit()

atm.display_balance()

atm.make_withdraw()
atm.display_balance()



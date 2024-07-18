from src.examples.j_classes.atm import ATM
from src.examples.j_classes.customer import Customer

customer1 = Customer(100, 50)

a = customer1.get_account(0)
balance = a.get_balance()
print(balance)

atm = ATM(a)
atm.make_deposit()

atm.display_balance()

atm.make_withdraw()
atm.display_balance()



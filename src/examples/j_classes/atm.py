

class ATM:
    __account = 0

    def __init__(self, account):
        self.__account = account

    def display_balance(self):
        print(self.__account.get_balance())

    def make_deposit(self):
        amount = 0

        amount = int(input("Enter deposit amount: "))
        self.__account.deposit(amount)

    def make_withdraw(self):
        amount = 0

        amount = int(input("Enter withdraw amount"))
        self.__account.withdraw(amount)
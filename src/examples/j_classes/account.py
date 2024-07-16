class Account:
    __balance = 0 ##__ means private

    #constructor-class variable/attributes initializer
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self): ##no underscore means public
        return self.__balance
    
    def deposit(self, amount):
        if(amount > 0):
            self.__balance += amount

    def withdraw(self, amount):
        if(amount > 0 and amount <= self.__balance):
            self.__balance -=




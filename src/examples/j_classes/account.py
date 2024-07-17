import random

class Account:
    __balance = 0 ##__ means private

    #constructor-class variable/attributes initializer
    def __init__(self, balance):
        
        if(balance <= 0):
            self.__get_balance_from_db()
        else:
            self.__balance = balance

    def get_balance(self): ##no underscore means public
        return self.__balance
    
    def deposit(self, amount):
        if(amount > 0):
            self.__balance += amount

    def withdraw(self, amount):
        if(amount > 0 and amount <= self.__balance):
            self.__balance -= amount

    def __get_balance_from_db(self): #private-can only be called from within this class
        self.__balance = random.randint(1, 10000)

    




class Account:
    __balance = 0 ##__ means private

    def get_balance(self): ##no underscore means public
        return self.__balance

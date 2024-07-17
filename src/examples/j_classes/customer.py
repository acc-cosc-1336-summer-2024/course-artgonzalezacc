from src.examples.j_classes.account import Account

class Customer:
    __list_accounts  = []

    def __init__(self, checking_balance, savings_balance):
        checking_account = Account(checking_balance) 
        savings_account = Account(savings_balance)

        self.__list_accounts.append(checking_account)
        self.__list_accounts.append(savings_account)

    def get_account(self, index):
        return self.__list_accounts[index]
    
    
        
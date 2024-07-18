from src.examples.j_classes.account import Account

class Customer:

    def __init__(self, checking_balance, savings_balance):
        self.__list_accounts  = []    
        checking_account = Account(checking_balance) 
        savings_account = Account(savings_balance)

        self.__list_accounts.append(checking_account)
        self.__list_accounts.append(savings_account)
        print(self.__list_accounts[0].get_balance(), self.__list_accounts[1].get_balance())

    def get_account(self, index):
        return self.__list_accounts[index]
    
    
        
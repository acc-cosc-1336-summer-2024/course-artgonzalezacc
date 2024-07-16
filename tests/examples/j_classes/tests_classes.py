import unittest

from src.examples.j_classes.account import Account

class Test_Config(unittest.TestCase):

    def test_account_begin_balance(self):
        account = Account(500)

        self.assertEqual(500, account.get_balance())

    def test_account_deposit(self):
        account = Account(500)

        self.assertEqual(500, account.get_balance())

        account.deposit(100)

        self.assertEqual(600, account.get_balance())

    def test_account_withdraw(self):
        account = Account(500)

        self.assertEqual(500, account.get_balance())
        
        account.withdraw(100)

        self.assertEqual(400, account.get_balance())
    

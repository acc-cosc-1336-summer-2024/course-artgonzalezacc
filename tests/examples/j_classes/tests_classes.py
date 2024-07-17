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

    def test_account_deposit_less_than_0(self):
        account = Account(500)

        self.assertEqual(500, account.get_balance())

        account.deposit(-50)

        self.assertEqual(500, account.get_balance())

    def test_account_withdraw_less_than_0(self):
        account = Account(500)

        self.assertEqual(500, account.get_balance())

        account.withdraw(-50)

        self.assertEqual(500, account.get_balance())

    def test_account_withdraw_more_than_balance(self):
        account = Account(500)
        self.assertEqual(500, account.get_balance())

        account.withdraw(501)

        self.assertEqual(500, account.get_balance())

    def test_account_deposit_followed_by_withdraw(self):
        account = Account(500)
        self.assertEqual(500, account.get_balance())

        account.deposit(100)
        self.assertEqual(600, account.get_balance())

        account.withdraw(50)
        self.assertEqual(550, account.get_balance())

    def test_account_withdraw_followed_by_deposit(self):

        account = Account(500)
        self.assertEqual(500, account.get_balance())

        account.withdraw(100)
        self.assertEqual(400, account.get_balance())

        account.deposit(50)
        self.assertEqual(450, account.get_balance())

    def test_get_balance_from_db(self):
        account = Account(0)

        self.assertEqual(True, account.get_balance() >= 1)
        self.assertEqual(True, account.get_balance() <= 10000)

    

from src.examples.j_classes.atm import ATM
from random import randint

def display_menu():
    print('1-Display Balance')
    print('2-Deposit')
    print('3-Withdraw')
    print('4-Exit')

def run_menu(customers):

    while(True):
        num = input('Press Enter: ')
        print(len(customers))
        customer_index = randint(0, len(customers))
        print(customer_index)
        customer = customers[customer_index-1] # reference one customer

        account_index = int(input("Enter 1 for checking 2 for savings: "))
        account = customer.get_account(account_index - 1)

        atm = ATM(account)

        choice = -1

        while choice != 4:
            display_menu()
            choice = int(input('Enter menu option: '))
            handle_menu_option(choice, atm)

def handle_menu_option(choice, atm):
    if(choice == 1):
        atm.display_balance()
    elif(choice == 2):
        atm.make_deposit()
    elif(choice == 3):
        atm.make_withdraw()
    elif(choice == 4):
        print('Exiting...')
    else:
        print('Invalid option...')


def test_config():
    return True

def display_numbers(num):

    indx = 0

    while(indx < num):#boolean expression 
        print(indx, indx <num, indx + 1) 
        indx = indx + 1#statement that makes boolean expression false

#sum_of_squares(3) 1*1 + 2*2 + 3*3 = 14
def sum_of_squares(num):
    sum = 0
    i = 0

    while(i <= num):#boolean expression
        sum = sum + i * i
        i += 1 #statement that makes the boolean expression false
    
    return sum

def display_number_for(num):

    for val in range(0, num) :
        print(val+1)

def sum_of_squares_for(num):

    sum = 0

    for val in range(0, num):
        sum = sum + (val+1) * (val+1)
    
    return sum

def while_nested_loop(num):
    i = 0

    while(i < num):
        print(i, 'Waiting for inner loop')
        
        j = 0
        while(j < num):
            print(j, '\t inner loop')
            j += 1
        
        i += 1

def while_multiplication_table(row, col):

    r = 0

    while(r < row):
        c = 0

        while(c < col):
            product = (r + 1) * (c + 1)
            print(str(product).rjust(3, " "), end=" ")
            c += 1

        r += 1

        print(" ")

def for_nested_loop(num):

    for i in range(0, num):
        print('Waiting for inner loop')

        for j in range(0, num):
            print('\t inner loop')

def for_multiplication_table(row, col):

    for r in range(0, row):

        for c in range(0, col):
            product = (r + 1 ) * (c + 1)
            print(str(product).rjust(3, " "), end=" ")

        print(" ")

def display_menu():
    print('1-Option 1')
    print('2-Option 2')
    print('3-Exit')

def run_menu():

    option = '1'

    while(option != '3'):
        display_menu()
        option = input("Enter your menu option: ")
        handle_menu_option(option)

def handle_menu_option(option):
    
    if(option == '1'):
        option_1()
    elif(option == '2'):
        option_2()
    elif(option == '3'):
        print('Exiting...')
    else:
        print('Invalid input')


def option_1():
    print('user selected option 1')

def option_2():
    print('user selected option 2')

def validate_input_w_while():
    value = 0

    while(value <= 0):
        value = int(input("Enter a value: "))

    print(value)





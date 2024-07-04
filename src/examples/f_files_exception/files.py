#
def open_file(file_name):
    file = open(file_name, 'r')

    #nothing

    file.close()

def write_to_file(file_name):
    file = open(file_name, 'w')

    file.write('John Locke\n')
    file.write('David Hume\n')
    file.write('Edmund Burke\n')

    file.close()

def read_from_file(file_name):
    file = open(file_name, 'r')

    files_lines = file.read()

    print(files_lines)

    file.close()

def read_from_file_one_line_at_a_time(file_name):
    file = open(file_name, 'r')

    line1 = file.readline().rstrip('\n')
    line2 = file.readline().rstrip('\n')
    line3 = file.readline().rstrip('\n')

    print(line1)
    print(line2)
    print(line3)

    file.close()

def append_to_file(file_name):
    file = open(file_name, 'a')

    file.write('Carl Marx\n')

    file.close()

def write_sales_data(file_name):
    file = open(file_name, 'w')

    num1 = input("Enter sales data: ")
    num2 = input("Enter sales data: ")
    num3 = input("Enter sales data: ")

    file.write(num1 + '\n')
    file.write(num2 + '\n')
    file.write(num3 + '\n')
    
    file.close()

def read_sales_data(file_name):
    file = open(file_name, 'r')

    num1 = int(file.readline())
    num2 = int(file.readline())
    num3 = int(file.readline())

    total = num1 + num2 + num3

    print(f'The numbers are: {num1} {num2} {num3}')
    print(f'Their total is: {total}')
    
    file.close()

def read_sales_data_w_while_loop(file_name):
    file = open(file_name, 'r')

    line = file.readline()

    total = 0

    while line != '':
        amount = int(line)
        total += amount
        print(amount)

        line = file.readline()
        
    print()
    print(total)

    file.close()

def read_sales_data_w_for_loop(file_name):
    file = open(file_name, 'r')

    total = 0

    for line in file:
        amount = int(line)
        total += amount
        print(amount)

    print()
    print(total)

    file.close()

def write_employee_records(file_name):
    file = open(file_name, 'w')

    choice = '1'

    while choice == '1':
        id = input('Enter id:')
        name = input('Enter name: ')
        dept = input('Enter dept: ')

        file.write(id + '\t')
        file.write(name + '\t')
        file.write(dept + '\n')

        choice = input('Enter 1 to continue')


    file.close()

def read_employee_records(file_name):
    file = open(file_name, 'r')

    for line in file:
        record = line.split('\t') #creates a list in this format ['1', 'joe', 'dept']
        id = record[0]
        name = record[1]
        dept = record[2].rstrip('\n')

        print(id, name, dept)

    file.close()

def write_prog_lang_list(file_name):
    file = open(file_name, 'w')

    prog_langs = [['C#', '2001', 'lang'], ['Python', '1996', 'lang'], ['Java', '1991', 'lang']]

    for lang in prog_langs:
        file.write(lang[0] + '\t')# C#
        file.write(lang[1] + '\t')# 2001
        file.write(lang[2] + '\n')#lang

    file.close()

def read_prog_langs_records(file_name):
    file = open(file_name, 'r')

    list_langs = []

    for line in file:
        record = line.split('\t')
        lang = record[0]
        year = record[1]
        cat = record[2].rstrip('\n')

        employee = [lang, year, cat]

        list_langs.append(employee)

    for employee in list_langs:
        print(employee[0], employee[1], employee[2])

    file.close()

    


        

        
        




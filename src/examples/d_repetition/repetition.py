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


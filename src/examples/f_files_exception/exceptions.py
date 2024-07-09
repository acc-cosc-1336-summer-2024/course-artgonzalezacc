def test_config():
    return True

def divide_two_numbers(num1, num2):
    
    result = 0

    if(num2 != 0):
        result = num1 / num2
    else:
        return "Division by 0 not allowed"

    return result

def multiply_two_numbers():
    
     num1 = input("Enter num1: ")
     
     while not num1.isdigit():
        num1 = input("Please enter digits.. Enter num1: ")

     num2 = input("Enter num2: ")
     
     while not num2.isdigit():
        num2 = input("Please enter digits...Enter num2: ")

     result = int(num1) * int(num2)
     print(result)

def open_file_for_reading(file_name):

    try:
        file = open(file_name, 'r')

        contents = file.read()

        print(contents)

        file.close()
    except IOError:
        print('Cannot read the file, not found at location ....')

def open_sales_file_for_reading(file_name):
    
    try:
    
        file = open(file_name, 'r')

        total = 0
        
        for line in file:
            amount = int(line)
            total += amount
        
        print(total)

        file.close()
    except IOError:
        print('Error reading the file')
        #save the error contents to an error log
    except ValueError:
        print("File contains invalid data")#for the end-user
        #save the error contents to an error log


 
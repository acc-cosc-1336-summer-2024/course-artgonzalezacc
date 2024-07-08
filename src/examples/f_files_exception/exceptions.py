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
 
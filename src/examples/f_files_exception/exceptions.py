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
    
    num1 = int(input("Enter num1: "))
    num2 = float(input("Enter num2: "))

    result = num1 * num2
    print(result)

#
#print(var1) can't use outside of the function

def local_variables(num1, num2):
    var1 = 5
    var2 = "Python"
    num1 = 0
    num2 = 100

    print(num1, num2, var1, var2)


#print(var1) can't use outside of the function

def local_variables_value_return(num1, num2):
    num3 = num1 + num2

    return num3
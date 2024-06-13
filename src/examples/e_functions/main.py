#main program
import void_functions

num1 = 100 #global variable
num2 = 200 #global variable

def main():
    global num1 #tell python to use num1 global variable
    num1 = 2 #local variables - belong to main 
    
    num2 = 3  #local variables - belong to main 
    void_functions.local_variables(5, 8) #function arguments --. feed in to the function parameters
    print('After local_variables executes')
    print(num1, num2)

    print('value return function....')
    result = void_functions.local_variables_value_return(10, 15)
    print(result)

main()

#display global variable
print(num1, num2)
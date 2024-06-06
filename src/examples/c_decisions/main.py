import decisions

value1 = input("Enter a number: ") #read form keyboard , Python brings in values as a string variable
#check if is a number

result = decisions.is_number_not_in_range(int(value1), 1, 10) #convert value to an integer number with the int function

print(result)


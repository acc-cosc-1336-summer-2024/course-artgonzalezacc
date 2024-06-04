import devprocess

value1 = input("Enter a number: ") #python treats numbers as characters from input
value2 = input("Enter a number: ")

result = devprocess.add_numbers(int(value1), int(value2)) #convert the value to an integer using the int function

print(result)

value1 = input("Enter a number: ") #python treats numbers as characters from input
value2 = input("Enter a number: ")

result = devprocess.subtract_numbers(float(value1), float(value2))
print(result)



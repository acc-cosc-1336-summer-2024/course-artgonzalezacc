import decisions

value1 = input("Enter a number: ") #read form keyboard , Python brings in values as a string variable

generation = decisions.get_generation(int(value1))

print(generation)


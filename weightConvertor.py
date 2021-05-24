# Weight converter program

# Define variable
weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')

# create if or else statements
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")
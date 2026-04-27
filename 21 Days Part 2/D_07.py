binary = input("Enter a binary number: ")

try:
    decimal = int(binary, 2)
    print("Decimal value:", decimal)
except ValueError:
    print("Invalid binary number!")

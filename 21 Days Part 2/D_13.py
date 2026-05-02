num = int(input("Enter a number: "))
divisor = int(input("Enter the number to check divisibility by: "))

if divisor == 0:
    print("Cannot divide by zero!")
elif num % divisor == 0:
    print(f"{num} is divisible by {divisor}")
else:
    print(f"{num} is NOT divisible by {divisor}")

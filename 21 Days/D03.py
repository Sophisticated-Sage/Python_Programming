#Armstrong no
number = int(input("Enter a number: "))
digits = str(number)
n = len(digits)
sum_of_powers = sum(int(digit) ** n for digit in digits)

if sum_of_powers == number:
    print(f"{number} is an Armstrong number")
else:
    print(f"{number} is not an Armstrong number")

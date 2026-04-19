print("Q 1. Write a program to check whether a given number is positive, negative or zero.\n")

num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

print("\nQ 2. Take a user's age as input and decide: age<13 = 'Child', age >= 13 and <= 19 = 'Teenager', else = 'Adult'.\n")

age = int(input("Enter your age: "))
if age < 13:
    print("Child")
elif age <= 19:
    print("Teenager")
else:
    print("Adult")

print("\nQ 3. Write a program to check whether a given year is a leap year or not.\n")

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")

print("\nQ 4. Accept a number from the user and check whether it is even or odd.\n")

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
    
print("\nQ 5. Given three numbers, find out which one is the largest.\n")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    print(f"The largest number is {a}")
elif b >= a and b >= c:
    print(f"The largest number is {b}")
else:
    print(f"The largest number is {c}")

print("\nQ 6. A shop gives discounts: if bill>500 then 20%, if bill>200 then 10%, else no discount. Write a program to calculate the final price.\n")

bill = float(input("Enter the bill amount: "))
if bill > 500:
    discount = bill * 0.20
elif bill > 200:
    discount = bill * 0.10
else:
    discount = 0
final_price = bill - discount
print(f"Final price after discount: {final_price}")

print("\nQ 7. Write a program to check if a character entered by the user is a vowel or consonant.\n")

char = input("Enter a character: ").lower()
if len(char) == 1 and char.isalpha():
    if char in 'aeiou':
        print("The character is a vowel.")
    else:
        print("The character is a consonant.")
else:
    print("Invalid input. Please enter a single alphabet character.")

print("\nQ 8. A grading system: marks>=90, grade='A'; marks>=75, grade='B'; marks>=50, grade='C'; else 'fail'.\n")

marks = float(input("Enter your marks: "))
if marks >= 90:
    grade = 'A'
elif marks >= 75:
    grade = 'B'
elif marks >= 50:
    grade = 'C'
else:
    grade = 'Failed'
print(f"Your grade is: {grade}")
    
print("\nQ 9. Write a program to check whether a number is divisible by 3, 5, or both.\n")

num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("The number is divisible by both 3 and 5.")
elif num % 3 == 0:
    print("The number is divisible by 3.")
elif num % 5 == 0:
    print("The number is divisible by 5.")
else:
    print("The number is not divisible by 3 or 5.")
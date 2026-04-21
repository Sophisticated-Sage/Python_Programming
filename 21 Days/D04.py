#Palindrome no
number = int(input("Enter a number: "))
original = number
reversed_num = 0

while number > 0:
    digit = number % 10
    reversed_num = reversed_num * 10 + digit
    number //= 10

if reversed_num == original:
    print(f"{original} is a palindrome number")
else:
    print(f"{original} is not a palindrome number")

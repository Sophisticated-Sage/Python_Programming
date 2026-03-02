#1
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact = fact * i
print("Factorial =", fact)
print()

#2
num2 = int(input("Enter a number: "))
temp = num2
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp = temp // 10
if sum == num2:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
print()

#3
n = int(input("Enter number of terms: "))
a = 0
b = 1
for i2 in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
print()

#4
num3 = int(input("Enter a number: "))
if num3 > 1:
    for i3 in range(2, num3):
        if num3 % i3 == 0:
            print("Not Prime")
            break
    else:
        print("Prime Number")
else:
    print("Not Prime")
print()

#5
num4 = int(input("Enter a number: "))
temp2 = num4
reverse = 0
while temp2 > 0:
    digit = temp2 % 10
    reverse = reverse * 10 + digit
    temp2 = temp2 // 10
if reverse == num4:
    print("Palindrome")
else:
    print("Not Palindrome")
print()

#6
num5 = int(input("Enter a number: "))
sum1 = 0
while num5 > 0:
    digit = num5 % 10
    sum1 += digit
    num5 = num5 // 10
print("Sum of digits =", sum1)
print()

#7
count = 0
for i4 in range(1, 101):
    if i4 % 5 == 0 or i4 % 7 == 0:
        print(i4, end=" ")
        count += 1
print("\nTotal Count =", count)
print()

#8
text = input("Enter a string: ")
print("Uppercase:", text.upper())
print()

#9
for num6 in range(2, 101):
    for i5 in range(2, num6):
        if num6 % i5 == 0:
            break
    else:
        print(num6, end=" ")
print()

#10
num7 = int(input("Enter a number: "))
for i6 in range(1, 11):
    print(num7, "*", i6, "=", num7 * i6)
print()
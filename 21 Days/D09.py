print("Q 1. Print all numbers from 1 to 100 that are divisible by both 3 and 5.\n")

print("Numbers from 1 to 100 divisible by both 3 and 5:")
for i in range(1, 100+1): #or "for i in range(1, 101):" either of them works
    if i % 3 == 0 and i % 5 == 0:
        print(i)

print("\nQ 2. Given a list of numbers [2, 4, 6, 8, 10], print the square of each number using a for loop.\n")

print("Squares of list 'a' is:")
a = [2, 4, 6, 8, 10]
for i in a:
    print(i**2)

print("\nQ 3. Write a program to calculate the factorial of a given number using a for loop.\n")

f = int(input("Enter a number to find its factorial: "))
fact = 1
for i in range(1, f+1):
    fact *= i
print(f"The factorial of the given number is: {fact}")

print("\nQ 4. Given a string 'programming', count how many vowels it has using a for loop.\n")

s = "programming"
v = ['a', 'e', 'i', 'o', 'u']
sum = 0
for i in s:
    if i in v:
        sum += 1
print(f"There are {sum} vowel/s in the word {s}")
    
print("\nQ 5. Use a for loop to find the largest number in the list [12, 45, 7, 23, 89, 34].\n")

list1 = [12, 45, 7, 23, 89, 34]
l = list1[0]
for i in list1:
    if i > l:
        l = i
print(f"The largest number in the list is: {l}")

print("\nQ 6. Iterate through a list of fruits and stop the loop when 'cherry' is found (use break).\n")

fruits = ["apple", "banana", "cherry", "mango", "orange"]
for fruit in fruits:
    print(fruit)
    if fruit == "cherry":
        print(f"Found {fruit}, stopping loop.")
        break

print("\nQ 7. Iterate through numbers 1-10 and skip (continue) printing even numbers.\n")

for i in range(1, 10+1): #or "for i in range(1, 11):" either of them works
    if i % 2 == 0:
        continue
    print(i)

print("\nQ 8. Use a nested for loop to print the multiplication table for numbers 1 to 5.\n")

for i in range(1, 5+1): #or "for i in range(1, 6):" either of them works
    for j in range(1, 5+1): #or "for j in range(1, 6):" either of them works
        print(f"{i} x {j} = {i*j}", end="\t")
    print()
    
print("\nQ 9. Print numbers from 50 down to 1 using a while loop.\n")

print("Numbers from 50 to 1 in descending order:")
i = 50
while i >= 1:
    print(i, end='\n')
    i -= 1

print("\nQ 10. Keep asking the user for input until they type 'exit'.\n")

x = input("Enter something: ")
while x.lower() != 'exit':
    x = input("Enter something: ")

print("\nQ 11. Write a program to reverse a number (e.g. 12345 -> 54321) using a while loop.\n")

num = int(input("Enter a number to reverse: "))
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
print("Reversed number:", reversed_num)

print("\nQ 12. Print the fibonacci sequence up to n terms using a while loop.\n")

n = int(input("Enter the number of terms: "))
a, b = 0, 1
count = 0

while count < n:
    print(a, end=' ')
    a, b = b, a + b
    count += 1
print()
    
print("\nQ 13. Given a number, keep dividing it by 2 using a while loop until it becomes less than 1, and print each step.\n")

num = float(input("Enter a number: "))
while num >= 1:
    print(num)
    num /= 2

print("\nQ 14. Use a while loop with break to stop when the user enters a negetive number.\n")

while True:
    num = int(input("Enter a number (negative to stop): "))
    if num < 0:
        break

print("\nQ 15. Use a while loop with continue to skip printing numbers that are multiples of 5 (up to 50).\n")

i = 1
while i <= 50:
    if i % 5 == 0:
        i += 1
        continue
    print(i)
    i += 1

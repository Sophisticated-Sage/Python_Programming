#1
x = 9
y = 7
z = 0
print("x + y = ", x + y)
print("x - y = ", x - y)
print("x * y = ", x * y)
print("x / y = ", x / y)
print()

#2
r = int(input("Enter the radius: "))
pi = 3.14159
area = pi * (r ** 2)
print(f"The area of the circle with radius {r} is: {area}")
print()

#3, 4, 5
x1 = int(input("Enter the first number: ")) #use no 4 as input for x1
y1 = int(input("Enter the second number: ")) #use no 3 as input for y1

result = (x1 + y1) * (x1 + y1)

print(f"The result of (x + y) * (x + y) is: {result}") #expected output is 49
print()

#6
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))

c = (a**2 + b**2) ** 0.5

print("Hypotenuse =", c)
print()

#7
p = float(input("Enter principal: "))
r1 = float(input("Enter rate: "))
t = float(input("Enter time: "))

si = (p * r1 * t) / 100

print("Simple Interest =", si)
print()

#8
a1 = float(input("Enter side a: "))
b1 = float(input("Enter side b: "))
c1 = float(input("Enter side c: "))

s = (a1 + b1 + c1) / 2
area = (s * (s - a1) * (s - b1) * (s - c1)) ** 0.5

print("Area of triangle =", area)
print()

#9
seconds = int(input("Enter total seconds: "))

hours = seconds // 3600
remaining = seconds % 3600
minutes = remaining // 60
secs = remaining % 60

print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", secs)
print()

#10
a2 = int(input("Enter first number: "))
b2 = int(input("Enter second number: "))

a2 = a2 + b2
b2 = a2 - b2
a2 = a2 - b2

print("After swapping:")
print("a =", a2)
print("b =", b2)
print()

#11
n = int(input("Enter n: "))
sum = n * (n + 1) // 2
print("Sum =", sum)
print()

#12
print("A B  A&B  A|B  A^B")
for a3 in [0, 1]:
    for b3 in [0, 1]:
        print(a3, b3, " ", a3 & b3, "  ", a3 | b3, "  ", a3 ^ b3)
print()

#13
num = int(input("Enter number: "))
shift = int(input("Enter shift value: "))
print("Left Shift:", num << shift)
print("Right Shift:", num >> shift)
print()

#14
num = int(input("Enter number: "))
sequence = (10, 20, 56, 78, 89)
if num in sequence:
    print("Number is in sequence")
else:
    print("Number is NOT in sequence")
print()

#15
ch = input("Enter character: ")
text = input("Enter string: ")
if ch in text:
    print("Character is present")
else:
    print("Character is NOT present")
print()
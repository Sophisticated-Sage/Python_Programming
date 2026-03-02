#1
num = int(input("Enter number: "))
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both 3 and 5")
print()

#2
num1 = int(input("Enter number: "))
if num1 % 5 == 0:
    print("It is a multiple of 5")
else:
    print("It is NOT a multiple of 5")
print()

#3
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Greatest =", a)
elif b > a:
    print("Greatest =", b)
else:
    print("Numbers are equal")
print()

#4
a1 = int(input("Enter first number: "))
b1 = int(input("Enter second number: "))
c1 = int(input("Enter third number: "))

if a1 > b1 and a1 > c1:
    print("Greatest =", a1)
elif b1 > c1:
    print("Greatest =", b1)
else:
    print("Greatest =", c1)
print()

#5
a2 = float(input("Enter a: "))
b2 = float(input("Enter b: "))
c2 = float(input("Enter c: "))
D = b2*b2 - 4*a2*c2
if D > 0:
    root1 = (-b2 + D**0.5) / (2*a2)
    root2 = (-b2 - D**0.5) / (2*a2)
    print("Real and different roots")
    print("Roots:", root1, "and", root2)
elif D == 0:
    root = -b2 / (2*a2)
    print("Real and equal roots")
    print("Root:", root)
else:
    real = -b2 / (2*a2)
    imag = (-D)**0.5 / (2*a2)
    print("Imaginary roots")
    print("Roots:", real, "+ i", imag, "and", real, "- i", imag)
print()

#6
year = int(input("Enter year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
print()

#7
day = int(input("Enter day: "))
month = int(input("Enter month: "))
year1 = int(input("Enter year: "))
# Days in months
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# Check leap year
if (year1 % 400 == 0) or (year1 % 4 == 0 and year1 % 100 != 0):
    days[1] = 29
day += 1
if day > days[month - 1]:
    day = 1
    month += 1
    if month > 12:
        month = 1
        year1 += 1
print("Next Date:")
print("Day =", day, "Month =", month, "Year =", year1)
print()

#8
name = input("Enter Name: ")
roll = input("Enter Roll Number: ")
sapid = input("Enter SAPID: ")
sem = input("Enter Semester: ")
course = input("Enter Course: ")
print("Enter marks of five subjects:")
pds = int(input("PDS: "))
python = int(input("Python: "))
chem = int(input("Chemistry: "))
eng = int(input("English: "))
phy = int(input("Physics: "))
total = pds + python + chem + eng + phy
percentage = total / 5
cgpa = percentage / 10
# Grade Calculation
if 0 <= cgpa <= 3.4:
    grade = "F"
elif 3.5 <= cgpa <= 5.0:
    grade = "C+"
elif 5.1 <= cgpa <= 6.0:
    grade = "B"
elif 6.1 <= cgpa <= 7.0:
    grade = "B+"
elif 7.1 <= cgpa <= 8.0:
    grade = "A"
elif 8.1 <= cgpa <= 9.0:
    grade = "A+"
else:
    grade = "O (Outstanding)"
print("\n----- Grade Sheet -----")
print("Name:", name)
print("Roll Number:", roll)
print("SAPID:", sapid)
print("Sem:", sem)
print("Course:", course)
print("\nMarks:")
print("PDS:", pds)
print("Python:", python)
print("Chemistry:", chem)
print("English:", eng)
print("Physics:", phy)
print("\nPercentage:", percentage, "%")
print("CGPA:", round(cgpa, 2))
print("Grade:", grade)
print()
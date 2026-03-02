#2 A
print("Hello Everyone !!!")
#2 B
print("Hello\nWorld")
#2 C
print("Hello\n\tWorld")
#2 D
a = input("Enter your name: ")
b = input("Enter your DOB (MM/DD/YYYY): ")
print(f"{a}'s date of birth is {b}")

#3
x = "Hello"
print(x)

#4
a1 = int(input("Enter a number: "))
a2 = float(input("Enter another number: "))
a3 = input("Enter a string: ")
print(a1, a2, a3)

#5
fname = input("Enter your name: ")
lname = input("Enter your surname: ")
print(fname + " " + lname)

#6
fname1 = input("Enter your name: ")
lname1 = input("Enter your surname: ")
nname1 = input("Enter your nickname: ")
print(f"{fname1} ({nname1}) {lname1}")

#7
name2 = input("Enter your name: ")
s = int(input("Enter your SAP ID: "))

if len(str(s)) != 9:
    print("Invalid SAP ID")
else:
    pass

dob = input("Enter your DOB (MM/DD/YYYY): ")
address = input("Enter your address: ")
p = input("Enter your Progamme: ")
s2 = input("Enter your Semester: ")

if s2 <"1" or s2 > "3":
    print("Invalid Semester")

print(f"Name: {name2}\nSAP ID: {s}\nDate Of Birth: {dob}\nAddress: {address}\nProgramme: {p}\nSemester: {s2}")

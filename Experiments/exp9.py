#1
class Student:
    def get_data(self):
        self.name = input("Enter Name: ")
        self.sap_id = input("Enter SAP ID: ")
        self.phy = int(input("Physics Marks: "))
        self.chem = int(input("Chemistry Marks: "))
        self.maths = int(input("Maths Marks: "))
    def display(self):
        print("\nName:", self.name)
        print("SAP ID:", self.sap_id)
        print("Physics:", self.phy)
        print("Chemistry:", self.chem)
        print("Maths:", self.maths)

# Creating 3 objects
students = []
for i in range(3):
    print("\nEnter details for Student", i+1)
    s = Student()
    s.get_data()
    students.append(s)

# Display all students
print("\n--- Student Details ---")
for s in students:
    s.display()
print()

#2
class Student:
    def __init__(self, name, sap_id, phy, chem, maths):
        self.name = name
        self.sap_id = sap_id
        self.phy = phy
        self.chem = chem
        self.maths = maths
    def display(self):
        print("\nName:", self.name)
        print("SAP ID:", self.sap_id)
        print("Marks:", self.phy, self.chem, self.maths)
    def marks_percentage(self):
        total = self.phy + self.chem + self.maths
        return total / 3
    def result(self):
        if self.phy > 40 and self.chem > 40 and self.maths > 40:
            return "Pass"
        else:
            return "Fail"

# Input n students
n = int(input("Enter number of students: "))
students = []
for i in range(n):
    print("\nEnter details for Student", i+1)
    name = input("Name: ")
    sap = input("SAP ID: ")
    phy = int(input("Physics: "))
    chem = int(input("Chemistry: "))
    maths = int(input("Maths: "))
    s = Student(name, sap, phy, chem, maths)
    students.append(s)

# Display details
total_class = 0
for s in students:
    s.display()
    percent = s.marks_percentage()
    total_class += percent
    print("Percentage:", percent)
    print("Result:", s.result())

# Class Average
print("\nClass Average:", total_class / n)
print()

#3 A
class Parent:
    def show(self):
        print("This is Parent class")
class Child(Parent):
    def display(self):
        print("This is Child class")
obj = Child()
obj.show()
obj.display()
print()

#3 B
class A:
    def methodA(self):
        print("Class A")
class B(A):
    def methodB(self):
        print("Class B")
class C(B):
    def methodC(self):
        print("Class C")
obj = C()
obj.methodA()
obj.methodB()
obj.methodC()
print()

#3 C
class Father:
    def skills1(self):
        print("Gardening")
class Mother:
    def skills2(self):
        print("Cooking")
class Child(Father, Mother):
    pass
obj = Child()
obj.skills1()
obj.skills2()
print()

#4
class Parent:
    def show(self):
        print("Parent method")
class Child(Parent):
    def show(self):
        print("Child method (Overridden)")
obj = Child()
obj.show()
print()

#5
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def display(self):
        print("Point(", self.x, ",", self.y, ")")

# Example
P1 = Point(10, 20)
P2 = Point(12, 15)
P3 = P1 + P2
P3.display()
print()
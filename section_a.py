# Question 1
class Student:
    school_name = "UPES"

    def info(self, name, age):
        self.name = name
        self.age = age
        
student1 = Student()
student2 = Student()
student1.info("Aman", 20)
student2.info("Riya", 21)
print(f"Student 1: {student1.name}, Age: {student1.age}")
print(f"Student 2: {student2.name}, Age: {student2.age}")

# Question 2
class Employee:
    company_name = "ABC Ltd"

    def info(self, name, salary):
        self.name = name
        self.salary = salary
        
    def change_company(new_name):
        Employee.company_name = new_name

class EmployeeInfo(Employee):    
    def show_details(self, info):
        print(f"Name: {info.name}, Salary: {info.salary}")

choice = input("1. To create an employee\n2. To change company name\n3. To show details\n4. To quit (1/2/3/4): ")
while True:
    if choice == '1':
        n = input("Enter employee name: ")
        s = int(input("Enter employee salary: "))
        Employee().info(n, s)
    elif choice == '2':
        new_name = input("Enter new company name: ")
        Employee.change_company(new_name)
    elif choice == '3':
        EmployeeInfo().show_details()
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
    
# Question 3
class MathHelper:
    def is_even(n):
        if n % 2 == 0:
            return True
        else:
            return False
        
n = int(input("Enter a number: "))
print(f"Is the number even? {MathHelper.is_even(n)}")
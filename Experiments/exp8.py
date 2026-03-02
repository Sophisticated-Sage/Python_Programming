#1
# Open file
file = open("name.txt", "r")
names = file.read().splitlines()
file.close()

# a. Count number of names
print("Total names:", len(names))

# b. Count names starting with vowel
vowels = "AEIOUaeiou"
count_vowel = 0
for name in names:
    if name[0] in vowels:
        count_vowel += 1
print("Names starting with vowel:", count_vowel)

# c. Find longest name
longest = names[0]
for name in names:
    if len(name) > len(longest):
        longest = name
print("Longest name:", longest)
print()

#2
file = open("numbers.txt", "r")
nums = file.read().splitlines()
file.close()
numbers = []
for num in nums:
    numbers.append(int(num))

# a. Find max number
maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num
print("Maximum:", maximum)

# b. Find average
total = 0
for num in numbers:
    total += num
average = total / len(numbers)
print("Average:", average)

# c. Count numbers greater than 100
count = 0
for num in numbers:
    if num > 100:
        count += 1
print("Numbers greater than 100:", count)
print()

#3
file = open("city.txt", "r")
cities = file.readlines()
file.close()
total_area = 0

print("City Details:")
for line in cities:
    parts = line.split()
    city = parts[0]
    population = float(parts[1])
    area = float(parts[2])
    print(city, population, area)

    # b. Population > 10 Lakhs
    if population > 10:
        print("Population > 10 Lakhs:", city)
    total_area += area
print("Total Area of all cities:", total_area)
print()

#4
N = int(input("Enter number of test cases: "))
for i in range(N):
    try:
        a, b = input().split()
        result = int(a) // int(b)
        print(result)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)
print()

#5
try:
    filename = input("Enter file name: ")
    if not filename.endswith(".txt"):
        raise Exception("Invalid file type. Only .txt allowed.")
    file = open(filename, "r")
    content = file.read()
    if content == "":
        raise Exception("File is empty.")
    print("File Content:")
    print(content)
    file.close()
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("Error:", e)
print()
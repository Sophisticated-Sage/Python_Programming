#1
n = int(input("Enter number of values: "))
count0 = count1 = count2 = count3 = 0
for i in range(n):
    num = int(input("Enter value (0-3): "))
    if num == 0:
        count0 += 1
    elif num == 1:
        count1 += 1
    elif num == 2:
        count2 += 1
    elif num == 3:
        count3 += 1
print("0 occurred:", count0, "times")
print("1 occurred:", count1, "times")
print("2 occurred:", count2, "times")
print("3 occurred:", count3, "times")
print()

#2
n = int(input("Enter number of values: "))
values = []
for i in range(n):
    num = float(input("Enter value: "))
    values.append(num)
t = tuple(values)
average = sum(t) / len(t)
print("Tuple:", t)
print("Average:", average)
print()

#3
n = int(input("Enter N: "))
scores = list(map(int, input("Enter scores separated by space: ").split()))
max_score = max(scores)
while max_score in scores:
    scores.remove(max_score)
runner_up = max(scores)
print("Runner-up score:", runner_up)
print()

#4
n = int(input("Enter number of persons: "))
data = {}
for i in range(n):
    name = input("Enter name: ")
    city = input("Enter city: ")
    data[name] = city

# a. Display all names
print("Names:")
for name in data.keys():
    print(name)

# b. Display all cities
print("Cities:")
for city in data.values():
    print(city)

# c. Display name and city
print("Student Details:")
for name, city in data.items():
    print(name, "lives in", city)

# d. Count students in each city
city_count = {}
for city in data.values():
    if city in city_count:
        city_count[city] += 1
    else:
        city_count[city] = 1
print("Students in each city:")
for city, count in city_count.items():
    print(city, ":", count)
print()

#5
n = int(input("Enter number of movies: "))
movies = {}

for i in range(n):
    name = input("Movie name: ")
    year = int(input("Year: "))
    director = input("Director: ")
    cost = float(input("Production cost: "))
    collection = float(input("Collection: "))
    movies[name] = {
        "year": year,
        "director": director,
        "cost": cost,
        "collection": collection
    }

# a. Print all movie details
print("\nAll Movie Details:")
for name, details in movies.items():
    print(name, ":", details)

# b. Movies released before 2015
print("\nMovies released before 2015:")
for name, details in movies.items():
    if details["year"] < 2015:
        print(name)

# c. Movies that made profit
print("\nMovies that made profit:")
for name, details in movies.items():
    if details["collection"] > details["cost"]:
        print(name)

# d. Movies by particular director
search_director = input("\nEnter director name to search: ")
print("Movies directed by", search_director)
for name, details in movies.items():
    if details["director"] == search_director:
        print(name)
print()
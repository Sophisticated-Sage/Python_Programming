#1
def find_max_min(seq):
    maximum = seq[0]
    minimum = seq[0]

    for num in seq:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
    return maximum, minimum

numbers = [4, 9, 2, 15, 6]
max_val, min_val = find_max_min(numbers)
print("Maximum:", max_val)
print("Minimum:", min_val)
print()

#2
def sum_of_cubes(n):
    total = 0
    for i in range(1, n):
        total += i ** 3
    return total

print(sum_of_cubes(5))   # 1³ + 2³ + 3³ + 4³
print()

#3
def print_numbers(n):
    if n == 0:
        return
    print_numbers(n - 1)
    print(n)

print_numbers(5)
print()

#4
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def print_fibonacci(n, i=0):
    if i == n:
        return
    print(fibonacci(i), end=" ")
    print_fibonacci(n, i + 1)

print_fibonacci(7)
print()

#5
volume_cone = lambda r, h: (1/3) * 3.14 * r * r * h
print(volume_cone(3, 5))
print()

#6
volume_cone = lambda r, h: (1/3) * 3.14 * r * r * h
print(volume_cone(3, 5))
print()

#7 A
max_min = lambda lst: (max(lst), min(lst))
print(max_min([10, 6, 8, 90, 12, 56]))
print()

#7 B
def greet(name="Guest"):
    print("Hello", name)
greet("Rahul")
greet()
print()

#7 C
def total_sum(*numbers):
    total = 0
    for num in numbers:
        total += num
    print("Sum:", total)
total_sum(10, 20, 30)
print()
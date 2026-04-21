import math

def is_strong_number(n):
    """Check if a number is a strong number"""
    original = n
    sum_of_factorials = 0
    
    while n > 0:
        digit = n % 10
        sum_of_factorials += math.factorial(digit)
        n //= 10
    
    return original == sum_of_factorials

# Main program
num = int(input("Enter a number: "))

if is_strong_number(num):
    print(f"{num} is a strong number")
else:
    print(f"{num} is not a strong number")
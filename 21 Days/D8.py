limit = int(input("Enter the maximum range limit: "))
print(f"Think of an integer between 0 and {limit}")

count = limit + 1

num_lists = 0
temp = limit
while temp > 0:
    temp = temp // 2
    num_lists += 1

if num_lists == 0:
    num_lists = 1

lists = []
for bit in range(num_lists):
    lst = []
    for n in range(count):
        if (n >> bit) & 1:
            lst.append(n)
    lists.append(lst)

answers = []
for i, lst in enumerate(lists, start=1):
    print(f"\nList {i}: {lst}")
    ans = input(f"Is your number in this list {i}? (y/n): ")
    answers.append(1 if ans.lower() == 'y' else 0)

result = 0
for bit, val in enumerate(answers):
    if val == 1:
        result += (1 << bit)

print("\nYour number is:", result)

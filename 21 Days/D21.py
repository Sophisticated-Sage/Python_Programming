nums = list(map(int, input("Enter numbers separated by space: ").split()))

smallest = nums[0]

for num in nums:
    if num < smallest:
        smallest = num

print("Smallest number:", smallest)

nums = list(map(int, input("Enter numbers (space separated): ").split()))

n = len(nums) + 1  # one number missing
expected_sum = n * (n + 1) // 2
actual_sum = sum(nums)

missing = expected_sum - actual_sum

print("Missing number:", missing)

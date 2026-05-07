nums = list(map(int, input("Enter numbers: ").split()))

sorted_list = True

for i in range(len(nums) - 1):
    if nums[i] > nums[i + 1]:
        sorted_list = False
        break

if sorted_list:
    print("The list is sorted in ascending order.")
else:
    print("The list is NOT sorted.")

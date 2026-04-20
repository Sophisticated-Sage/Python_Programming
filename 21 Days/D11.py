print("\nQ 1. Convert the string s= ' PyThoN ProGRamMiNg ' into lowercase after removing spaces from both ends.\n")

s = ' PyThoN ProGRamMiNg '
result = s.strip().lower()
print(result)

print("\nQ 2. Replace all underscores in the string s='data_science_with_python' with spaces.\n")

s = 'data_science_with_python'
result = s.replace('_', ' ')
print(result)

print("\nQ 3. Convert the string s='introduction to python' so that each word starts with a capital letter.\n")

s = 'introduction to python'
result = s.title()
print(result)

print("\nQ 4. Check if the string s= 'MachineLearning' starts with 'Machine' and ends with 'Learning'.\n")

s = 'MachineLearning'
starts = s.startswith('Machine')
ends = s.endswith('Learning')
print(f"Starts with 'Machine': {starts}")
print(f"Ends with 'Learning': {ends}")
    
print("\nQ 5. Count how many times 'a' occurs in the string s= 'banana plantation area'.\n")

s = 'banana plantation area'
count = s.count('a')
print(f"Number of times 'a' occurs: {count}")

print("\nQ 6. Find the index of the first occurrence of 'on' in s= 'python is on fire'.\n")

s = 'python is on fire'
index = s.find('on')
print(f"Index of first occurrence of 'on': {index+1}")  # Adding 1 to convert 0-based index to 1-based index

print("\nQ 7. Split the string s= 'red,green,blue,yellow' into a list of colors.\n")

s = 'red,green,blue,yellow'
colors = s.split(',')
print(colors)

print("\nQ 8. Convert the string s= 'easy and powerful' to uppercase.\n")

s = 'easy and powerful'
result = s.upper()
print(result)
    
print("\nQ 9. Check if the string s= 'Python Programming' ends with 'ing'.\n")

s = 'Python Programming'
ends = s.endswith('ing')
print(f"Ends with 'ing': {ends}")

print("\nQ 10. Remove the spaces from the beginning and end of s= ' hello world '.\n")

s = ' hello world '
result = s.strip()
print(result)
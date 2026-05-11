username = input("Enter a username: ")

min_length = 4
max_length = 12

length = len(username)

if length < min_length:
    print("Username is too short.")
elif length > max_length:
    print("Username is too long.")
else:
    print("Username length is valid.")

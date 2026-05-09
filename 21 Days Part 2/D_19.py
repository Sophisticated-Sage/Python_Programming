email = input("Enter an email: ")

if "@" in email and "." in email:
    at_index = email.index("@")
    dot_index = email.rindex(".")

    if at_index < dot_index:
        print("Valid email format")
    else:
        print("Invalid email format")
else:
    print("Invalid email format")

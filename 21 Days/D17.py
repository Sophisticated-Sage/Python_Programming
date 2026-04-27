email = input("Enter your email: ")

if "@" in email:
    username, domain = email.split("@")
    
    if "." in domain:
        domain_name, extension = domain.split(".", 1)
        print("Username:", username)
        print("Domain:", domain_name)
        print("Extension:", extension)
    else:
        print("Invalid email format (missing extension)")
else:
    print("Invalid email format (missing @)")

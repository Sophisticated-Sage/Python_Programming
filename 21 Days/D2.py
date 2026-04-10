faculty_names = ["Dr V Maths", "Dr D Maths", "Dr H Maths", "Md K SS", "HH k Maths"]

for each in faculty_names:
    if each.startswith("Dr") and each.endswith("Maths"):
        pass
    else:
        print(each)
minutes = int(input("Enter total minutes: "))

hours = minutes // 60
remaining_minutes = minutes % 60

print(f"{minutes} minutes = {hours} hour(s) and {remaining_minutes} minute(s)")

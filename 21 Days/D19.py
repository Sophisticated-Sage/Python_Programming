from datetime import datetime

date_input = input("Enter a future date (YYYY-MM-DD): ")

try:
    future_date = datetime.strptime(date_input, "%Y-%m-%d")
    today = datetime.now()

    difference = future_date - today

    if difference.days >= 0:
        print(f"Days remaining: {difference.days}")
    else:
        print("That date has already passed!")
except ValueError:
    print("Invalid date format! Use YYYY-MM-DD")

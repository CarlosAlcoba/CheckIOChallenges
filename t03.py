user_date = int(input("Enter a date in the format DDMMYYYY: "))
day = user_date // 1000000
month = (user_date // 10000) % 100
year = user_date % 100000

print()
print(f"The reformatted date: {year}/{month:02}/{day:02}")

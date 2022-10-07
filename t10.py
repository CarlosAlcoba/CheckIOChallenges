size = int(input("Enter the initial size of the population: "))
births = int(input("Enter the average seconds between births: "))
deaths = int(input("Enter the average seconds between deaths: "))
immigrants = int(input("Enter the average seconds between immigrations: "))
years = int(input("Years: "))
SECONDS_YEAR = 31536000
new_size = ((SECONDS_YEAR / births) + (SECONDS_YEAR / immigrants) - (SECONDS_YEAR / deaths)) * 5 + size
print(new_size)
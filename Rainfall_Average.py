# Rainfall Calculator to get average based on how many years and months

years = int(input("How many years: "))

total_rainfall = 0.0
total_months = 0

for year in range(1, years + 1):
    print(f"\nYear {year}")
    for month in range(1, 13):
        rainfall = float(input(f"Enter how much rainfall for month {month} (in inches): "))
        total_rainfall += rainfall
        total_months += 1

average_rainfall = total_rainfall / total_months

print("\nRainfall Summary")
print(f"Total months: {total_months}")
print(f"Total rainfall: {total_rainfall:.2f} inches")
print(f"Average rainfall per month: {average_rainfall:.2f} inches")


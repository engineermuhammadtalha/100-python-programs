# display calendar of a given month and year
import calendar
print("Enter month and year to display calendar:")
month = int(input("Month (1-12): "))
year = int(input("Year (e.g., 2010): "))
print("\n", calendar.month(year, month))
# Example usage:

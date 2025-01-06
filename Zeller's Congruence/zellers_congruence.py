import math

# Input
year_value = eval(input("Enter year: (e.g. , 2008): "))
month_value = eval(input("Enter month: 1-12: "))
day_of_month_value = eval(input("Enter the day of the month: 1-31: "))

# Days
days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Calculation of zeller's congruence
if month_value < 3:
    year_value -= 1
    month_value += 12
k_zeller = year_value % 100
j_zeller = year_value // 100

h_zeller = (day_of_month_value +
            math.floor((26 * (month_value + 1)/10)) +
            k_zeller +
            math.floor(k_zeller/4) +
            math.floor(j_zeller/4) + 5 * j_zeller ) % 7

# Print
print(f"Day of the week is {days[h_zeller]}")
# Write a function to check if the year number is a leap year.
def is_leap_year(year):
    if year % 4 == 0:
        print("Leap year")
    else:
        print("Not a leap year")
        
is_leap_year(2020)
is_leap_year(2021)
is_leap_year(2022)
is_leap_year(2024) 
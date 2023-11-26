entered_yr = int(input("Enter the year: "))
is_leap_yr = False

if (entered_yr % 4 == 0 and entered_yr % 100 != 0) or (entered_yr % 400 == 0):
    is_leap_yr = True
else:
    is_leap_yr = False

print(f"{entered_yr} is a {is_leap_yr}")

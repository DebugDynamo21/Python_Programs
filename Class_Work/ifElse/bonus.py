# The current year and the year in which the employee joined
# the organization are entered through the keyboard. If the
# number of years for which the employee has served the
# organization is greater than 3 then a bonus of Rs. 2500/- is
# given to the employee. If the years of service are not
# greater than 3, then the program should do nothing.

current_year = int(input("Enter the current year: "))
joining_year = int(input("Enter the year of joining: "))

years_of_service = current_year - joining_year
bonus = 2500

if years_of_service > 3:
    print(f"The employee is eligible for a bonus of Rs. {bonus}/-")
else:
    print("The employee is not eligible for a bonus.")

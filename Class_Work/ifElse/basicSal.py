# The basic salary of an employee is input through the
# keyboard and if his basic salary is less than 1500 INR then
# HRA=10% of the basic salary and DA=90% of the basic
# salary. If his salary is either equal to or above 1500 INR,
# then HRA= 500 INR and DA=98% of basic salary. Write a
# Python program to find his gross salary.

basic_salary = float(input("Enter the basic salary of the employee: "))

if basic_salary < 1500:
    hra = 0.10 * basic_salary
    da = 0.90 * basic_salary
else:
    hra = 500
    da = 0.98 * basic_salary
    gross_salary = basic_salary + hra + da
    
print(f"The gross salary of the employee is: {gross_salary:.2f} INR")

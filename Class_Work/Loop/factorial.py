# Write a Python program to calculate the factorial of the given number.

n = int(input("Enter a number to calculate its factorial: "))
factorial = 1
for i in range (1, n + 1):
    factorial *= i
print(f"Factorial of {i} is: {factorial}")
# Write a Python program to print the table of the given number.

n = int(input ("Enter a number to print its table: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")
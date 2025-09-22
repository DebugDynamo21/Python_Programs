# Python program to check whether the given number is Armstrong number or not.

n = int(input("Enter a number: "))

a = n % 10
b = n // 10
b = b % 10
c = n // 100

if n == (a**3 + b**3 + c**3):
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")
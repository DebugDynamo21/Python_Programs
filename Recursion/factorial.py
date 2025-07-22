# Write a python program to find factorial of a number using recursion.abs

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Enter a number to find its factorial: "))
print(factorial(n))
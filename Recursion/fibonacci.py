# Write a program to find nth Fibonacci number using recursion.

def fibonacci(n):
    if n <= 0:  # Base case: if n is less than or equal to 0, return 0
        return 0
    elif n == 1:    # Base case: if n is 1, return 1
        return 1
    else:
        # Recursive case: return the sum of the two preceding Fibonacci numbers
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter value of n: "))
print(fibonacci(n))
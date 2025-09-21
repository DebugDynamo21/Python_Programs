# Write a Python program to check whether the given number is prime or not.

n = int(input("Enter a number: "))

is_prime = True
if n <= 1:  # 0 and 1 are not prime numbers
    is_prime = False
else:
    for i in range(2, n): # Check divisibility from 2 to n-1
        if n % i == 0:  # If divisible, it's not primes
            is_prime = False
            break
    if is_prime:    # If no divisors were found, it's prime
        print(n, "is a prime number")
    else:
        print(n, "is not a prime number")
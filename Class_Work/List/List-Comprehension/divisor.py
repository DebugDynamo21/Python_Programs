# Write a Python program to find out the divisors of the number using list comprehension.

n = int(input("Enter a number: "))
res = [i for i in range(1,n+1) if n % i == 0]
print(res)
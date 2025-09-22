# Python program to print all the odd numbers within the given range.

n = int(input("Enter n to print odd number from 1 to n: "))
for i in range (1, n+1):
    if i % 2 != 0:
        print(i, end=" ")
# Python program to print all the even numbers within the given range.

n = int(input("Enter n to print even number from 1 to n: "))
for i in range (0, n):
    if(i%2==0):
        print(i, end=" ")

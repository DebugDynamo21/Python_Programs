# Python program to calculate the sum of all odd numbers from 1 to a given number.

n = int(input("Enter n to print sum of odd numbers from 1 to n: "))
sum = 0

for i in range(1, n + 1):
    if i%2 != 0:
        sum+=i

print("The sum of odd numbers from 1 to n is: ",sum)
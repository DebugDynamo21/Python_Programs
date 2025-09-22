# Python program to calculate the sum of all numbers from 1 to a given number.

n = int(input("Enter n to print sum of number from 1 to n: "))
sum = 0

for i in range(1, n + 1):
    sum+=i

print("The sum of numbers from 1 to 20 is: ",sum)
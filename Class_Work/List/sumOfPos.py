# Write a Python program to find the sum of only the positive numbers in a given list.

l = []
n = int(input("Enter number of elements in list: "))

for i in range(n):
    a = int(input("Enter element: "))
    l.append(a)

sum = 0
for i in l:
    if i > 0:
        sum += i

print("The sum of positive elements is: ", sum)
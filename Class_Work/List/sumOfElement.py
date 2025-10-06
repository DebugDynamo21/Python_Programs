# Write a Python program to sum all the items in a list.

l = []
n = int(input("Enter number of elements in list: "))
s = 0

for i in range(n):
    a = int(input("Enter element: "))
    l.append(a)

print("The list is: ", l)

for i in range(n+1):
    s += i
print("The sum is: ", s)
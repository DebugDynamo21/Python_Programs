# Write a Python program to multiply all the items in a list.

l = []
n = int(input("Enter number of elements in list: "))

for i in range(n):
    a = int(input("Enter element: "))
    l.append(a)

print("The list is: ", l)

prod = 1
for i in l:
    prod *= i

print("The product of all elements if list: ", prod)
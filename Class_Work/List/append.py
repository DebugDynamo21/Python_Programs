# Write a Python program that accepts user input to populate the elements of a list.

l = []
n = int(input("Enter number of elements in list: "))

for i in range(n):
    a = int(input("Enter element: "))
    l.append(a)

print("List: ", l)
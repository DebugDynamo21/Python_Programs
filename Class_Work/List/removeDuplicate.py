# Write a Python program to remove duplicates from a list.

l = []
n = int(input("Enter number of elements in list: "))

for i in range(n):
    a = int(input("Enter element: "))
    l.append(a)

print("The list is: ", l)

dup = []
for i in l:
    if i not in dup:
        dup.append(i)

print("The list after removal of duplicates: ", dup)
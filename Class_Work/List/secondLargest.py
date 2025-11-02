# Write a python program to find the second largest element from the list.

n = int(input("Enter list size: "))
l = []

print(f"Enter ", n, " elements: ")
for i in range(n):
    a = int(input())
    l.append(a)

print("List is: ", l)

l.sort()
print("The sorted list", l)

secondLast = len(l) - 2
print("The second largest element: ", l[secondLast])
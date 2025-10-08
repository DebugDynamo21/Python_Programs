# Write a python program to check the list is empty or not.

l = []
n = int(input("Enter number of elements in list: "))
for i in range(n):
    a = int(input("Enter element: "))
    l.append(a)

print("The list is: ", l)

if not l:
    print("List is empty.")
else:
    print("List is not empty.")
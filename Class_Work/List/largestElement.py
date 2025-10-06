# Write a program to find the largest number from a list.abs

l = []
n = int(input("Enter number of elements in list: "))

for i in range(n):
    a = int(input("Enter element: "))
    l.append(a)

print("The list is: ", l)

max = l[0]
for i in l:
    if i > max:
        max = i

print("The biggest number in list is: ", max)
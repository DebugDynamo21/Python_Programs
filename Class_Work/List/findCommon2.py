# Write a python program to find common elements in two lists 
# and store these common elements in another list.

l1 = [2, 3, 5, 7, 11, 13, 17, 19, 23]
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l3 = []

print("List 1: ", l1)
print("List 2: ", l2)

for i in l1:
    if i in l2:
        l3.append(i)

print("List with common elements: ", l3)
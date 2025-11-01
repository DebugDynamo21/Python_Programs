# Write a python program to find the common elements between two lists.

l1 = [2, 4, 6, 8, 10, 12, 14, 16, 18]
l2 = [3, 6, 9, 12, 15, 18, 21, 24]

for i in l1:
    if i in l2:
        print(i)

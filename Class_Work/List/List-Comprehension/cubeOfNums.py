# Write a Python program to calculate the cube of only positive numbers from the given list.

l = [-1, 2, 3, -4, 5]

cube=[i**3 for i in l if i>0]
print(cube)
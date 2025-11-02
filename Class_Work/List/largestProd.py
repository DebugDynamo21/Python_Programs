# Write a python program to find the largest product of two distinct elements in a list.

L = [8, 2, 5, 1, 3]
L.sort()

print("List", L)

maxProd = L[-1] * L[-2]

print("Product of largest two distinct elements in a list: ", maxProd)
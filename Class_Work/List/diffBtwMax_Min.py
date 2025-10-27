# Create a list of numbers. Write a program to find the
# range (difference between the largest and smallest
# element) of the list.

l = [5, 13, 6, 19, 8, 15, 22, 11, 3, 6]

r1 = max(l) - min(l)

print("Largest element: ", max(l))
print("Smallest element: ", min(l))
print("The range (difference between largest and smallest) is: ", r1)

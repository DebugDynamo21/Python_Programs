# Write a Python program to calculate the cube of only even numbers from the given list.

cube=[i**3 for i in range(1, 10) if i % 2 == 0]

print(cube)
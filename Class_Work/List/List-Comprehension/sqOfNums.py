# Python program to calculate the square of list of numbers using list comprehension.

l = [1,2,3,4,5]
square = []

for i in l:
    square.append(i**2)
    
print('The list of squares', square)
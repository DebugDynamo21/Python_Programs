# Write a Python program to extract only first character from the given string using list comprehension.

l = ['Hello', 'Python', 'List', 'Comprehension']
res = [i[0] for i in l]

print("First character from each string: ", res)
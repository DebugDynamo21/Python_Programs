# Write a python program to check if a list is a palindrome.

l = [1, 2, 3, 2, 1]

print("List1: ", l)

if l == l[::-1]:
    print("List is palindrome")
else:
    print("Not palindrome")
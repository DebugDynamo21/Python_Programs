# Create a list of characters. Write a program to reverse the order of the elements in the list without using built-in
# functions. Use indexing method.

l = []
n = int(input('Enter the number of elements: '))

for i in range(n):
    a = int(input('Enter the element: '))
    l.append(a)
print('The List is: ',l)

rev = l[::-1]
print("Reversed list is: ", rev)
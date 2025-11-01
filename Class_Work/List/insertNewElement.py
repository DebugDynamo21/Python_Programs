# Create a list of numbers. Write a program to 
# insert a new element at a apecific position in the list.

list = [5, 10, 15, 20, 25, 30, 35, 40]

print("Original List: ", list)

idx = int(input("Enter index: "))
n = int(input("Enter element to insert: "))

list.insert(idx, n)

print("List after insertion: ", list)
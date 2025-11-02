# Write a Python program to find the sum of elements at
# even indices in a list.

mylist = [100,4,200,1,3,2,9,11,23,35,12,10,15,13,16,14,0]
print("List: ", mylist)

even = mylist[0::2]
print("Elements at even index: ", even)

total = sum(even)
print("Sum of elements at even index: ", total)
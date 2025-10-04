# Write a Python program to convert a list of string to list of integers.

l = ['1','2','3','4','5']
print("String list: ", l)

res = [int(i) for i in l]

print("Integer list: ", res)
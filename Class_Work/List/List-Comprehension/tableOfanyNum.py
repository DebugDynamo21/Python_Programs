# Print table of any number using list comprehension

n = int(input("Enter a number: "))
res = [n*i for i in range(1,11)]

print(res)
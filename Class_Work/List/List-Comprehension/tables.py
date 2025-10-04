# Print table of 1 to n using list comprehension

n = int(input("Enter number to print table(1-n): "))
for i in range(1, n+1):
    table = [i*j for j in range(1,11)]
    print(table)
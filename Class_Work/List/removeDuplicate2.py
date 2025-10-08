l = []
n = int(input("Enter number of elements in list: "))

for i in range(n):
    a = int(input("Enter element: "))
    l.append(a)

print("The list is: ", l)

s = set(l)
print("The list without duplicates: ", list(s))
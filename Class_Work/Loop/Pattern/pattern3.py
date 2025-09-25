# Python Program to print following Pattern.

# A B C D E
# A B C D E
# A B C D E
# A B C D E
# A B C D E

n = int(input("Enter number of rows: "))
for i in range(n):
    for j in range(65, 65+n):
        print(chr(j), end=" ")
    print()
# Python Program to print following Pattern.

#   A
#   A B
#   A B C
#   A B C D
#   A B C D E

n = int(input("Enter number of rows: "))
for i in range (n):
    for j in range (65, 65 + n):
        if j <= 65 + i:
            print(chr(j), end = " ")
    print()
    
# chr() function is used to convert ASCII value to character.
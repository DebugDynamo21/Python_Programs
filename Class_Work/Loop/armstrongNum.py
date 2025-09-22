# Python program to generate Armstrong number between 1 to 500.

for i in range(1, 500):
    a = i % 10
    b = i // 10
    b = b %  10
    c = i // 100
    if i == (a**3 + b**3 + c**3):
        print(i, end=" ")
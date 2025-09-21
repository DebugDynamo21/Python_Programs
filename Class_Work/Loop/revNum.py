# Write a Python program to calculate the reverse number of a 5 digits number.

n = int(input("Enter a five digit number: "))
rev = 0

while(n > 0):
    rem = n % 10
    rev = rev * 10 + rem
    n = n // 10

print("Reversed Number is: ", rev)
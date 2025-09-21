# Write a Python program to calculate the sum of digits of a 5 digits number.

n=int(input("Enter a five digit number: "))
s=0
while(n>0):
    rem = n % 10
    s += rem
    n = n // 10
print("Sum of digits is: ",s)
    
# Python program to count the total number of digits in number.

n = int(input("Enter a number to count its number of digits: "))
digit = 0
while(n>0):
    rem = n%10
    digit += 1
    n = n//10
print("Number of digits is: ", digit)
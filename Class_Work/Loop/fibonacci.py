# Python program to generate the Fibonacci series.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
n = int(input("Enter number of terms to print: "))

print("The fibonacci series is: ")
print(num1, num2, end=" ")

for i in range(n-2):
    c = num1 + num2
    print(c, end=" ")
    num1 = num2
    num2 = c
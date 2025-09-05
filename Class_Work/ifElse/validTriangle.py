# Write a program to check whether a triangle is valid or not,
# when the three angles of the triangle are entered through
# the keyboard. A triangle is valid if the sum of all three
# angles is equal to 180 degrees.

a1 = (input("Enter first angle: "))
a2 = (input("Enter first angle: "))
a3 = (input("Enter first angle: "))

if a1 + a2 + a3 == 180:
    print("Triangle is valid")
else:
    print("Triangle is invalid")
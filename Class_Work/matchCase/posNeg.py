# Write a python program to check whether the given number is
# negative, positive or zero.

n = int(input("Enter a number: "))
match n:
    case 0:
        print("The number is zero.")
    case n if n > 0:
        print("The number is positive.")
    case n if n < 0:
        print("The number is negative.")
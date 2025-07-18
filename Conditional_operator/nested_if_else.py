# Nested if else
# Check whether a number is positive or negative and even or odd

num = int(input("Enter a number: "))

if(num >= 0):
    print("Positive Number")
    if(num % 2 == 0):
        print("Even Number")
    else:
        print("Odd Number")
else:
    print("Negative Number")
# Write a program in python to check given number is a buzz
# number or not. (A number is said to be buzz if it ends with 7
# or divisible by 7.

num = int(input("Enter a number: "))
if num % 7 == 0 or num % 10 == 7:
    print(f"{num} is a buzz number")
else:
    print(f"{num} is not a buzz number")
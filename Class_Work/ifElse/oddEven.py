# Any integer is input through the keyboard. Write a program
# to find out whether it is an odd number or an even number.

num = int(input("Enter a number: "))
if(num % 2 == 0):
    print(num, "is even num")
else:
    print(num, "is odd num")
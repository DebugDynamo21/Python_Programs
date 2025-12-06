# 1. Input a 5 digit number from the user and find its reverse.

# n = int(input("Enter a five digit number: "))
# revNum = 0
# for i in range(5):
#     a = n % 10
#     revNum = revNum * 10  + a
#     n = n // 10
# print("Reversed number is: ",revNum)


# 2. WAP to print ASCII value of a character.

# a = input("Enter a character to get ascii value: ")
# print("ASCII value of {a} ", a, " is: ", ord(a))

# 3. WAP to find the difference of two numbers without using minus(-) operator.

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# diff = a + (~b + 1)     # ~ is used tot find 1's complement.

# print("The difference is: ", diff)


# 4. WAP to multiply two numbers without using multiply operator.

# a = int(input("Enter first number: "))
# # b = int(input("Enter second number: "))

# prod = a << 2
# print("The product is: ", prod)

# 5. WAP that accepts an integer(n) and compute the value of n + nn + nnn.

# n = int(input("Enter a number: "))
# sum = n + n * 11 + n * 111
# print(sum)


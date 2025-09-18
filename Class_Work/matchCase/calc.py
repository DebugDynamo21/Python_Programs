# Write a python program for calculator.

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
op = input("Enter an operator +, -, *, /: ")
match op:
    case "+":
        print(f"{x} + {y} = {x + y}")
    case "-":
        print(f"{x} - {y} = {x - y}")
    case "*":
        print(f"{x} * {y} = {x * y}")
    case "/":
        if y != 0:
            print(f"{x} / {y} = {x / y}")
        else:
            print("Error: Division by zero")
    case _:
        print("Invalid operator! Please enter correct operator.")
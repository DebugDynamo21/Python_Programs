# Write a python program to check whether the person is
# minor, senior or adult.

# Minor - If the person’s age is less than 18

# Senior - If the person’s age is greater than 65

# Adult – If the person is greater than or equal to 18 and
# less than 65.

age = int(input("Enter the age of the person: "))
match age:
    case age if age > 0 and age < 18:
        print("The person is a minor.")
    case age if age >= 18 and age < 65:
        print("The person is an adult.")
    case age if age >= 65:
        print("The person is a senior.")
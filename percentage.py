# Write a program to assign grades to student according to their marks.

marks = float(input("Enter your percentage: "))

if(marks >= 90):
    print("Grade A")
elif(marks >= 80 and marks < 90):
    print("Grade B")
elif(marks >= 70 and marks < 80):
    print("Grade C")
elif(marks >= 60 and marks < 70):
    print("Grade D")
else:
    print("Grade F")
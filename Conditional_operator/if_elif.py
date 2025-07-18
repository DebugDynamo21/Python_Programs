# Multiple conditions (if- elif-else)
# Write a python program to input marks of student and output corresponding grade.

marks = int(input("Enter your marks: "))

if(marks >= 90):
    print("Grade: A")
elif(marks >= 75):
    print("Grade: B")
elif (marks >= 60):
    print("Grade: C")
else:
    print("Grade: F (Fail)")

# Nested dictionary

student = {
    "name" : "Student 1",
    "score" : {
        "physics" : 93,
        "maths" : 93,
        "chemistry" : 92
    }
}
print(student)

# To print score dictionary only
print(student["score"])

# To print particular value of a key
print(student["score"]["physics"])
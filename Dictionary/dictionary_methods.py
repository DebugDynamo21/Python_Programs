# DICTIONARY METHODS

student = {
    "Name" : "Student 1",
    "Score" : {
        "phy" : 64.3,
        "chem" : 52.4,
        "maths" : 55.7
    }
}

# 1) dictionary_name.keys() - returns all keys
print(student.keys())

# This dictionary can be type casted to list 
print(list(student.keys()))

# 2) dictionary_name.value() - returns all values
print(student.values())
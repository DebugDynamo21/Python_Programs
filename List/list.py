# LIST:- Are similar to array in other languages.
#       It can be of any type string, integer, float 
#       or combination of all.

# We can modify any element of list but in case of string
# it is not possible to modify any element of a string

marks = [91.2, 82.9, 76.3, 91.5, 32.7]
print(marks)

# To know the type marks variable
print(type(marks))

# To access any particular element in a list
print(marks[0])

# To know the length of list
print(len(marks))

# LIST SLICING- similar to string slicing
# list_ namel starting_idx : ending_idx ] #ending idx is not included
# negative indexing is also possible in list

print(marks[1:4])   #prints the values on index 1 to 3
print(marks[:4])    #assumes starting index to be 0
print(marks[1:])    #assumes ending index to be len of list
# Update an array using append

import array as arr
a = arr.array('i', [10,20,30,40])
print("Array initially: ", a)

a.append(50)
print("Array after append: ", a)
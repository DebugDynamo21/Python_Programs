# Delete an element from an array using del()

import array as arr
a = arr.array('i', [10,20,30,40,50])
print("Array initially: ", a)

del(a[3])
print("Array after delete: ", a)
# Update an array using extend()

import array as arr
a = arr.array('i', [10,20,30,40,50])
print("Array initially: ", a)

a.extend([60,70,80,90,100])
print("Array after extend: ", a)
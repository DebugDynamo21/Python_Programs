# Update an array using indexing.

import array as arr
a = arr.array('i', [1,2,3,4,5,6,7])
print("Array in beginning: ", a)

a[2] = 20
print("Array after first change: ", a)

a[6] = 12
print("Array after second change: ",a)
#LIST METHODS
# syntax- list_name.method

list = [2, 1, 3, 6, 4]

# 1. list.append(element to append) - add that element in the last of the list
list.append(7)
print(list)

# 2. list.sort() - sorts list in ascending order
list.sort()
print(list)

# 3. list.sort(reverse = True) - sorts the list in descending order
list.sort(reverse = True)
print(list)

# 4. list.reverse() - reverse the list
list.reverse()
print(list)

# 5. list.insert(index, element to add) - inserts an element at a particular index
list.insert(3, 5)
print(list)

# 6. list.remove(element to remove) - remove the first occurence element in the list
num = [11, 17, 15, 18, 15]
num.remove(15)
print(num)

# 7. list.pop(index) - removes that index value
list.pop(3)
print(list)

# agr hm print(_) me list.append ya or koi method ko print krenge to 
# None return krega kyuki vo sirf list me modification krta h
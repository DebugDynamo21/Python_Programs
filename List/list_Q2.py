# WAP to check if a list contains a palindrome of elements.

list1 = [1, 2, 3, 4]

copy_list1 = list.copy(list1)
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("Not palindrome")

list2 = ["m", "a", "m"]

copy_list2 = list.copy(list2)
copy_list2.reverse()

if(copy_list2 == list2):
    print("palindrome")
else:
    print("Not palindrome")
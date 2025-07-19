# WAP to ask the user to enter names of their 3 favorite
# movies & store them in a list.

movies = []     #create an empty list
mov1 = input("Enter 1st movie: ")
mov2 = input("Enter 2nd movie: ")
mov3 = input("Enter 3rd movie: ")

#append the input movies name in the list
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)
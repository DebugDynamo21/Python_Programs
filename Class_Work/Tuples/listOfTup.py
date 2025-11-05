# Create a list of tuples with numbers and their cubes.abs

L = [1, 2, 3, 4, 5, 6]
res = []
for i in L:
    res.append((i, i**3))
print(res)
# This code will create file2.txt file and content of this file will be
# 'This is just an example'

file = open('file2.txt','w')
file.write('This is an example text file')

file = open('file2.txt', 'r')
data = file.read()
print(data)

file.close()
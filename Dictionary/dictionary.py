# Dictionay in python :(Similar to structure in C) :-

# Are used to store data values in (key:value) pairs. They are unordered, 
# mutable(changable) andon't allow duplicate keys

# syntax : dictionary_name = {
#           "key" : value
#          }

info = {
   "name" : "hardik",       # string type
   "age" : 20,              #integer type
   "subjects" : ["python", "C", "Java"],    #list type
   "marks" : 93.2,          #float type
   "is_adult" : True,       #boolean type
   "topics" : ("dictionary", "set")     #tuple type
}
print(info)

# Key can also be a integer, floating, boolean, etc. type

# To print particular dictionary value

print(info["name"])
print(info["age"])
print(info["marks"])

# To change the value of any key 
info["name"] = "Hardik Bhardwaj"
print(info)

# To add new key:value pair in our dictionary(info)
info["surname"] = "Sharma"
print(info)
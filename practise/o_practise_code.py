# Python Dictionary

# creating dictionary
# student = {
#     "Name" : "Monish",
#     "Age" : 21,
#     "City" : "Bengaluru"
# }
# print(student)



# empty dictionary
# data = {}
# print(type(data))

# data = dict()
# print(type(data))


# key value pairs
# student = {"Name": "Monish", "Age" : 21, "City" : "Bengaluru"}

# dictionary values
# data = {"int": 30, "float": 3.4, "string": "monish", "boolean": True,"list" : [1,2,3],"tuple": (1,2,3)}
# print(data)



# Accessing Values
# data = {"int": 30, "float": 3.4, "string": "monish", "boolean": True,"list" : [1,2,3],"tuple": (1,2,3)}
# print(data["int"])
# print(data["float"])
# print(data.get("string"))
# print(data.get("win"))




# Adding key value pairs
# student = {
#     "name": "Monish"
# }
# student["age"] = 22
# student["city"] = "Bengaluru"
# print(student)


# Updating existing values
# student["age"] = 21
# student["city"] = "Karnataka,Bengaluru"
# print(student)

# Updating/merging values
# student = {
#     "name" : "Monish",
#     "age" : 22
# }
# student.update({
#     "age" : 21,
#     "city" : "Bengalure"
# })

# print(student)




# Removing Elements
# 1.pop()
data = {"int": 30, "float": 3.4, "string": "monish", "boolean": True,"list" : [1,2,3],"tuple": (1,2,3)}
# int = data.pop("int")
# print(data)

# 2.popitem()
# item = data.popitem()
# print(data)
# print(item)

# 3. clear
# res = data.clear()
# print(data)


# 4. del
# del data["int"]
# print(data)


# Iterating Over Dictionaries
# data = {"int": 30, "float": 3.4, "string": "monish", "boolean": True,"list" : [1,2,3],"tuple": (1,2,3)}

# for key in data:
#     print(key)

# for values in data.values():
#     print(values)

# for key,value in data.items():
#     print(f"{key} : {value}")



# Membership testing
# print("30" in data)
# print("int" in data)


# Dictionary Methods
data = {"int": 30, "float": 3.4, "string": "monish", "boolean": True,"list" : [1,2,3],"tuple": (1,2,3)}


# # 1. keys()
# print(data.keys())

# # 2. values()
# print(data.values())

# # 3. items()
# print(data.items())

# 4. copy()
# a = {
#     "name": "Monish",
#     "city": "Bengaluru"
# }
# b = a.copy()
# print(a)
# print(b)

# 5. setdefault()
# data = {}
# data.setdefault("count",0)
# print(data)


# fromkeys()
# keys = ["a","b","c"]
# data = dict.fromkeys(keys,0)
# print(data)


# Nested Dictionaries
# students = {
#     "student1":{
#         "Name" : "Monish",
#         "age" :21
#     },
#     "student2":{
#         "Name" : "Virat",
#         "age" :37
#     }
# }
# print(students["student1"])
# print(students["student2"]["Name"])


# Dictionary containing Lists
# student = {
#     "Name": "Monish",
#     "Marks": [85,90,89]
# }
# print(student["Marks"][0])
# print(student.get("Marks")[1])


# Dictionary containing tuples
# coordinates = {
#     "point_1":(10,20),
#     "point_2":(30,40)
# }
# print(coordinates["point_1"])
# print(coordinates["point_1"][0])
# print(coordinates["point_2"])
# print(coordinates["point_2"][1])


# Dictionary Comprehension
# square = {x:x*x for x in range(1,5)}
# print(square)


# Dictionary Unpacking
# a = {"Name":"Monish"}
# b = {"Age":21}
# res = {**a,**b}
# print(res)
# print(type(res))

# Dictionary Operators
# | - dictionary merge
# a = {1:"a"}
# b = {2:"b"}
# res = a | b    # a |= b, This updates a with the mappings from b.
# print(res)


# Assignment = No copy
# d1 = {"a":1, "b":2}
# d2 = d1
# print(d1)
# print(d2)
# print(d1==d2)

# Shallow copy
# d1 = {"num":[10,20,30]}
# d2 = d1.copy()
# d2["num"].append(40)
# print(d1)
# print(d2)
# print(d1==d2)

# # deep copy
# import copy
# d1 = {
#     "num":[[10,20],[30,40]],
#     "num1":[[50,60],[70,80]]}
# d2 = copy.deepcopy(d1)
# d2["num"][1].append(50)

# print(d1)
# print("\n")
# print(d2)
# print("\n")
# print(d1==d2)
# print(d1 is d2)



# Dictionary with functions
# def get_name(student):
#     return student["name"],student["age"]
# student = {
# "name": "Monish",
# "age": 21
# }
# print(get_name(student))


numbers = [2, 3, 2, 5, 3, 2]

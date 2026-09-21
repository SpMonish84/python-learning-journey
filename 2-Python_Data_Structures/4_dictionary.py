# Python Dictionary
# dictionary is a data structure that stores information in key value pairs. while keys must be unique and immutable like strings or numbers, values can be of any data type,whether mutable or immutable.
# this makes dictionaries ideal for accessing data by a specific name rather than a numeric position like in list

data = {"name" : "monish","age" : 21}
print(data)

# creating a Dictionary
# created by writing key-value paris inside{},where each key is connected to a value using colon : a dictionary can also be created using dict()func.
a = {"x" : 1, "y" : 2}
print(a)

b = dict(name ="monish",age =21)
print(b)

# Accessing a dictionary item : 
# a value in a dictionary is accessed by using its key. this can be done either with square brackets or with get()func. both returns the value linked to the given key
d = {"name" : "monish","age" : 21}
print(d["name"])
print(d.get("age"))


# Adding and Updating Dictionary Items
# new items are added to a dictionary using the assignment operator (=),by giving a new key a value
# if an existing key is used with assignment operator, its value is updated with the new one 
d = {"name" : "monish"}
d["age"] = 21
d["name"] = "MONISH"
print(d)


# Removing Dictionary Items 
# can be removed using built-in deletion methods that work on keys
# 1. del : removes an item using its key
d = {"a" : 1, "b" : 2}
del d["a"]
print(d)

# 2. pop() : removes the item with the given key and returns its value
d = {"a" : 1, "b" :2}
val = d.pop("a")
print(val)
print(d)

# 3. popitem() : removes and returns the last inserted key value pair
d = {"a" : 1, "b" : 2}
print(d.popitem())

# 4. clear() : removes all items from the dictionary
d = {"a" : 1, "b" : 2}
d.clear()
print(d)


# update() method : is a built in dictionary function that updates the key value pairs of dictionary using elements form another dictionary or an iterable of key-value pairs.
# using this method can include new data or merge it with existing dictionary entries
d1 = {"Name" : "monish", "Age" : "21", "country" : "india"}
d2 = {"Name" : "Virat", "Age" : "37"}
d1.update(d2)
print(d1)

# copy() method : returns a shallow copy of the dictionary
d = {"name" : "Monish","age" : 21}
copy_dict = d.copy()
print(copy_dict)
print(d == copy_dict)
print(d is copy_dict)


# setdefault() method : returns the value of a key if the key is in the dictionary else inserts the key with a value to the dictionary
student = {"name" : "Monish", "age" : "21"}
print(student.setdefault("course","Python")) # dictionary.setdefault("key","value")
print(student)


# Iterating through a Dictionary
# a dictionary can be traversed using a for loop to access its keys,values or both key-value pairs by using the built in methods
# 1. Iterate keys : returns all keys from the dictionary
d = {"a" : 1, "b" : 2}
for key in d:
    print(key)


# 2. Iterate values: Returns all the values from the dictionary
d = {"a" : 1, "b" : 2}
for value in d.values():
    print(value)


# 3. Iterate key-value pairs: returns all the key value pairs as tuple
d = {"a" : 1, "b" : 2}
for key,value in d.items():
    print(key ,":",value)



# Nested Dictionaries : is a dictionary that contains another dictionary as one of its values.
d = {
    "student" : "monish",
    "age" : 20,
    "marks" : {
        "phy" : 90,
        "chem" : 92,
        "math" :97
    }
}
print(d["marks"]["chem"])


# Dictionary Comprehension
# is used to create a dictionary in a short and clear way. it allows keys and values to be generated from a loop in one line.helps in dictionaries
# directly without writing multiple statements

sq = {x : x**2 for x in range(1,6)}
print(sq)

# creating a dictionary from 2 lists
# this method creates dictionary by paring each item from one list with the matching item from another list using zip()
keys = ['a','b','c','d','e']
values = [1,2,3,4,5]
d = {k:v for (k,v) in zip(keys,values)}
print(d)

# using fromkeys() method
# the fromkeys() creates a dictionary by taking a group of keys and assigning the same value to all of them
d = dict.fromkeys(range(5), True)
print(d)


# Dictionary comprehension with conditional statements
# can include condtions in a dictionary comprehension to filter items or apply logic only to specific values.
d = {x: x**3 for x in range(10) if x ** 3 % 4 == 0}
print(d)


# Nested Dictionary Comprehension
# we can also create dictionaries within dictionaries using nested dictionary comprehension. useful when each key maps to another dictionary of related values
s = "VK"
res = {x: {y: x+y for y in s} for x in s}
print(res)



# Copy vs Deep Copy

# Shallow Copy : creates a new object that refrences the same underlying data for the original object. This means although the objects have different names.both objects point to the same memory location
# so if changes in either of the object then the changes will affect both objects
# 1. create new dictionary with same structure(key-value pairs) as the original, but values themselves are refrences to original object
# 2. any changes made to mutable objects within the copied dictionary will also affect the original dictionary
print("\n")
import copy

# original dictionary
original_dict = {"a" : 1, "b" : [1,2,3]}
print("Original Dictionary: ",original_dict)

#shallow copy
shallow_copy = copy.copy(original_dict)
print("Shallow Copy: ",shallow_copy)

# Modifying data in shallow copy
shallow_copy['b'][1] = 4

# printing dictionary after change
print("Original Dictionary after change: ",original_dict)

# printing the copy after change
print("Shallow copy after change: ",shallow_copy)


# Deep Copy : creates a completely new object. this object have different names but here both object will not point to the same memory location
# so if made any changes in either of objects then the changes will not affect both the objects
# 1. creates a completely independent copy of both the dictionary structure and all of its values, including nested mutable object
# 2. Changes made to the copied dictionary won't affect the original.
print("\n")
# Original dictionary
original_dict = {"a" : 1, "b" : [1,2,3]}
print("Original Dictionary: ",original_dict)

# Perform a deep copy
deep_copy = copy.deepcopy(original_dict)
print("Deep Copy", deep_copy)

# modifying the deep copy
deep_copy["b"][1] = 5

# print both dictionaries to see the changes
print("Original Dictionary: ", original_dict)
print("Deep Copy: ", deep_copy)


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
# Feature	                 |     Shallow Copy	                                                                            |     Deep Copy                                                                      |
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
# Definition	             |     Creates a new object, but references the same nested objects as the original.	        |    Creates a new object and recursively copies all nested objects from the original|
# Memory Usage	             |     Consumes less memory because nested objects are shared.	                                |    Consumes more memory because all objects are copied independently.              |
# Copied Objects	         |     Changes made to nested objects are reflected in both the original and the copied object.	|    Changes made to nested objects are not reflected in the other object.           |
# Performance	             |     Faster because it does not copy nested objects.	                                        |    Slower because it recursively copies all nested objects.                        |
# Dependency	             |     Dependent on the original structure; nested objects are shared.	                        |    Independent of the original structure; nested objects are fully separate.       |
# Effect of Modification	 |     Modifying a nested mutable object affects both copies.	                                |    Modifying a nested mutable object affects only the copied object.               |
# Python Method	             |     copy.copy() or slicing ([:]) for some collections.	                                    |    copy.deepcopy()                                                                 |
# Use Case	                 |     When nested objects do not need to be modified independently.	                        |    When complete independence from the original object is required.                |9
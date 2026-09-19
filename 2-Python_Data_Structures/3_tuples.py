# Tuples in Python
# 1. A tuple is an immutable ordered collection on elements
# 2. can hold elements of different datatypes
# 3. these are ordered and heterogeneous and immutable

# Creating a Tuple
# can be created by placing all the items inside a parentheses () and separated by commas, can have any number of items
tup = ()
print(tup)
print(type(tup))

# Creating a tuple with mixed datatypes
# can store elements of diff datatypes like int, float, str, lists, dictionaries within a single structure
tup = (5, 1.4, 2+3j, True, [1,2,3], {"key":"value"})
print(tup)

# Tuple basic Operations
# Accessing a Tuple : by using indexing and slicing, similar to lists of elements. indexing starts from 0 for first element and goes upto n-1 where n is number of elements in tuple.
# negative indexing starts from -1 for last element and goes backward
tup = ("Hello")
print(tup[0])
print(tup[1:4])
print(tup[:3])
print(tup[4:])
print(tup[::-1])

# Concatenation of Tuples : done using + operator. combines 2 or more tuples to create a new tuple
tup1 = (1,2,3)
tup2 = ("Hi","World",6)
tup3 = tup1+tup2
print(tup3)

# Slicing of Tuple : creating a new tuple from a subset of elements of original tuple, slicing syntax [start:sinset-block-start:step]
tup = tuple('HELLOWORLD')
print(tup[1:])
print(tup[1:5])
print(tup[::-1])

# Deleting a Tuple : tuples are immutable, so individual elements of tuple cannot be deleted. however we can delete an entire tuple using del statement
tup = (0,1,2,3,4,5)
del tup 
# print(tup)

# Tuple unpacking
tup = ("hi","world","hello")
a,b,c = tup
print(a)
print(b)
print(c)

# tuple unpacking with asterisk ( * ) : used to grab multiple items into a list. useful to extract few specific elements and collect the rest together
tup = (1,2,3,4,5)
a, *b, c = tup
print(a)
print(b)
print(c)

# Tuple Methods
# 1. index() method : returns index of first occurrence, syntax tup.index(element)
tup = (1,2,3,4,5,12,23,4,34,1,2,4)
print(tup.index(2))

# 2. count() method : counts total occurrences, syntax tup.count(element)
tup = (1,2,3,4,5,12,2,23,4,34,1,2,4)
print(tup.count(2))
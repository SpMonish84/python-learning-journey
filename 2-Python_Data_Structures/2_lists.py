# Lists in Python
# list is a built in data structure used to store an ordered collection of items. They are dynamic, resizeable
# and capable of storing multiple data types

# 1. mutable : lists elements can be changed updated added or removed after the list is created.
# 2. ordered : elements maintain the order in which they are inserted
# 3. index-based : elements can be accessed using their positon, starting from index 0

# a = [int(),float(),complex(),str(),bool(),binary(),Nonetype]

# Creating a list
# 1. using square[] brackets :
a = [1,2,3]
print(a)

b = ["apple","banana","orange"]
print(b)

# 2. using list() constructor :
a = list((1,2,3,"Hello",3.5))
print(a)

b = list("Python")
print(b)

# 3. creating list with repeated elements using * operator
a = [2]*4
b = [0]*6
print(a)
print(b)


# Internal representation of lists
# stores the reference to objects, not the values directly
# The list keeps memory address of objects like integers, string or boolean
# actual objects exist separately in memory
# modifying a mutable object inside a list changes the original object
# reassigning an immutable object creates a new object instead of changing the old one
a = [1,2,3,"Python"]
print(a[0])
print(a)


# Accessing elements : using indexing. Py uses zero-based indexing, meaning a[0] represents the first element.
# negative indexing is also supported where -1 access the last element
a = [10,20,30]
print(a[0])
print(a[-1])


# Adding elements 
# 1. append() - adds an element at end of the list
a = [1,2,3]
a. append(4)
print(a)

# 2. insert() - adds an element at a specific position
a = [1,2,5]
a.insert(2,3) # insert(index,element)
a.insert(3,4)
print(a)

# 3. extend() - adds multiple elements to the end of list
a = ["a","b","c"]
a.extend(["d","e"])
print(a)

# Updating elements - since lists are mutable elements can be updated by assigning new values to their index
a = [10,20,30,40,50]
a[1] = 2
print(a)

# Removing Elements 
# 1. remove(): removes the first occurance of an element
a = [1,2,3]
a.remove(2)
print(a)

# 2. pop() : removes the element at a specific index or the last element if no index is specified
a = ["a","b","c"]
a.pop(2) # pop(index)
print(a)

# 3. del statement : deletes an element at a specified index
a = [1,2,3,4,5]
del a[4]
print(a)

# 4. clear() : removes all the items in a list
a = [1,2,3,4]
a.clear()
print(a)


# Iterating over lists - can be iterated using loops, allowing operations to be performed on each element
a = ['apple','banana','mango']
for item in a:
    print(item)


# Nested lists - list containing another list as its element. it is commonly used to represent
# matrices or tabular data and can be accessed by chaining multiple indexes
a = [[1,2,3],[4,5,6]]
print(a[1][2])
print(a[0])


# List Comprehension 
# concise way to create new lists by applying an expression to each item in an existing iterable like list,tuple or range
# helps to write clean efficient code compared to tradional loops

# sqr of every num
a = [2,3,4,5]
res = [val ** 2 for val in a]
print(res)


# Conditional Statements in list comprehension
# list comprehension can use conditions to select or transform items based on specific rules.
# even num from list a
a = [1,2,3,4,5]
res = [val for val in a if val % 2 == 0]
print(res)

# greater than 10 from list b
b = [20,1,2,34,45,12,3,5]
res = [val for val in b if val >= 10]
print(res)

# creating list from a range : create a list numbers within specific range
a = [i for i in range(11)]
print(a)

# using nested loops : a list of all coordinate pairs in a 3X3 grid can be genetated by combining 2 loops inside a list comprehension
c =[(x,y) for x in range(3) for y in range(3)]
print(c)

# flattening a list of lists : a nested list(matrix) can be transformed into a single flat list by iterating through each sublist and its elements
mat = [[1,2,3],[4,5,6],[7,8,9]]
res = [val for row in mat for val in row]
print(res)


# Multi-dimensional Lists : list containing other lists, often used to represent structured data like matrices, tables or 2D arrays
#its useful for storing and accessing data in rows and cols commonly applied in data analysis, maths and image processing
m = [[1,2,3],[4,5,6],[7,8,9]]
print(m)

# Creating a multidimensional list : list is created by nesting lists within a single list. It allows data to be organized in rows and columns similar to a matrix or table
m = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [18,49,22,66]
]
print(m)

# creating a multidimensional Zero matrix
# a zero matrix is a 2D list with all the elements set to zero. its commonly used as an initial structure for mathematical operations, data storage or placeholders before inserting actual values.
m,n = 4,5
mat = []

for i in range(m):
    row = []
    for j in range(n):
        row.append(0)
    mat.append(row)
print(mat)

# accessing a multidimensional list
# using row by row loop
a = [[1,2,3,4,5],[6,7,8,9,10],[18,49,22,66]]

for row in a:
    print(row)


# using index based nested loop
a = [[1,2,3,4,5],[6,7,8,9,0],[3,2,4,5,1],[0,7,6,8,9]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end = " ")
    print()


# Methods on Multidimensional Lists
# 1. using append() : adds a new sublist (row) to the end of outer list. commonly used when dynamically building matrices or adding data rows
# a = [[1,2,3],[4,5,6]]
# a.append([7,8,9])
# print(a)

# 2. using extend() : extends a chosen sublist by adding multiple elements from another iterable. for appending more data to an existing row
a = [[1,2,3],[4,5,6]]
a[0].append([7,8,9])
print(a)

# 3. using reverse() : reverses the order of elements within a list.can be applied either to a specific sublist or the entire outer list
a = [[1,2,3],[4,5,6]]
a[1].reverse()
print(a)
a.reverse()
print(a)

# 4. using indexing to read/write element
# you can access or modify elements in a specific position using double indexing, syntax a[i][j]
a = [[1,2,3],[4,5,6]]
print(a[0][2])
a[0][0] = 0
print(a)

# 5. Using list comprehension for processing rows
# list comprehension provide a compact way to modify or filter elements in rows or columns ideal for data transformations like scaling or filtering
a = [[1,2,3],[4,5,6]]
b = [[x*2 for x in row]for row in a]
print(b)
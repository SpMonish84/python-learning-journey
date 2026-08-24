# Data types in Python - Data types in Python define the type of value stored in a variable
# Numeric types → int, float, complex
# Boolean type → bool
# Sequence types → list, tuple, range
# Text type → str
# Set types → set, frozenset
# Mapping type → dict 
# Binary types → bytes, bytearray, memoryview
# Special type → NoneType (only None exists here)


# Why Data Types Are Needed
# 1. Organization of data → Helps Python distinguish between integers, strings, lists, etc.
# 2. Efficient memory use → Different types use memory differently (e.g., int vs list).
# 3. Operations control → Determines what operations are valid (you can add numbers, but you can’t directly add a number to a string).
# 4. Error prevention → Ensures logical consistency (e.g., prevents dividing text by 5).
# 5. Flexibility → Allows Python to handle everything from math to text processing to complex objects.



print("\n")
print("Numeric datatype")
# Numeric Data Types
# a. Integer - int() - value is represented by int class. It contains positive or negative whole numbers (without fractions or decimals).
# b. Float - float() - value is represented by float class. It is a real number with a floating-point representation. It is specified by a decimal point.
# c. Complex - complex() - represented by a complex class. It stores numbers with real and imaginary parts.
a = 10
b = 12.0
c = 3 + 5j
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(c.real)
print(c.imag)
print(type(c))


print("\n")
print("Boolean datatype")
# Boolean - bool() - represents one of two values: True or False. It is mainly used in conditions and comparisons and is represented by the bool class.
is_admin = False
a = True
print(10>5)
print(type(a))


print("\n")
print("String datatype")
# String - are used to store text data. A string is represented using the str class and can be created using single, double or triple quotes.
name = "Monish"
city = "Banglore"
print(name)
print(city)
print(type(name))


print("\n")
print("List datatype")
# List - l = [] are ordered and mutable collections used to store multiple items in a single variable. Elements in a list can be of different data types and are accessed using indexing.
l = [1,2,3]
print(l)
b = ["hello", "world", "welcome", 4, 5]
print(b[3])
print(b[-3])
print(type(l))


print("\n")
print("Tuple datatype")
# Tuple - t = () are ordered and immutable collections used to store multiple items in a single variable. Once created, tuple elements cannot be modified and are accessed using indexing.
t1 = (1,)
print(t1)
print(type(t1))
t2 = ("hello", 'world', 'welcome', 1, 2)
print(t2[3])
print(t2[-3])


print("\n")
print("Set datatype")
# Set - s = {} are unordered and mutable collections used to store unique elements. Since sets are unordered, elements cannot be accessed using indexing. Elements are usually accessed by iterating through the set using a loop.
s1 = {"a","b","c","b","a"}
print(s1)
print(type(s1))
s2 = {"hello", "world", "welcome"}
for i in s2:
    print(i)



print("\n")
print("Dictionary datatype")
# Dictionary - d = {key:"value"} are used to store data in key:value pairs. Each key in a dictionary must be unique and values are accessed using their keys with square brackets [] or get() method.
d = {1: "hello",2: "world",3: "welcome",4: 5}
print(d[1])
print(d.get(3))
print(type(d))




print("\n")
print("Built-In datatype")
# range - generates numbers
r = range(5)
print(r)
print(list(r))
print(type(r))

# frozenset - immutable version of set
fs = frozenset({1,2,3})
print(fs)
print(type(fs))



print("\n")
print("Binary types datatype")
# bytes - stores binary data
data = b"Hello"
print(data)
print(type(data))
# bytearray - mutable bytes
data1 = bytearray(b"Hello")
print(data1)
print(type(data1))
# memoryview - accesses binary data without copying
data3 = memoryview(bytes(5))
print(data3)
print(type(data3))


print("\n")
print("Special datatype")
# None - represents absent value
name = None
print(name)
print(type(name))


# Literals - literals are different from variables because variables store references to values, while literals are the values themselves.
# Literals can be integers, floats, strings, booleans, etc.




# isinstance() - returns true if object is an instance of a class or sub class of it, else returns false
# it is safer than using type() because it also works with inheritance(sub classes count as instance of their parent class)

# syntax : isinstance(obj, TypeName)

# Ex: x = 10
# print(isinstance(x, int))      # True
# print(isinstance(x, float))    # False
# print(isinstance(x, (int, float)))  # True (checks multiple types)

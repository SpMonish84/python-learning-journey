# a = 10.0
# b = "Python"

# print(type(a))
# print(type(b))

# print(isinstance(a,float))
# print(isinstance(b,str))

# x = True
# print(isinstance(x,int))


# print(True + True) # 2
# print(False + False) # 0
# print(False + True) # 1
# print(True + False) # 1
# print(False + 2) # 2
# print(True + 5) # 6


# Scientific Notation
# num1 = 1.23E4
# num2 = 5.6e-3
# print(num1,num2)
# aEb or aeb --> ax10^b


# # complex
# Real part, Imaginary part
# .real
# .imag
# j --> imaginary component in python

# x = 3 + 4j
# print(x.real)
# print(x.imag)
# print(type(x))


# bool, truthy and falsy values
# False
# None
# 0
# 0.0
# 0j
# ""
# []
# ()
# {}
# set()
# range(0)



# Strings
# str = "Python"

# name = 'monish'
# print(name)
# print(type(name))
# name1 = "S P MONISH"
# print(name1)
# print(type(name1))
# name2 = '''Shadow'''
# name3 = """Python"""
# print(name2)
# print(type(name2))
# print(name3)
# print(type(name3))
# name4 = """virat,
# abd,
# gayle"""
# print(name4)
# print(type(name4))


# str = "Python"
# print(str[0]) # P
# print(str[5]) # n
# print(str[-1]) # n
# print(str[-3]) # h
# # str[0] = "J"
# new_str = "J"+ str[1:]
# print(new_str)

# # slicing 
# word = "Java"
# print(word[0:2])
# print(word[:4])
# print(word[1:])

# # string operators - concatenation +, repetition *
# print("Hi, " + "Welcome")
# print("Hello"*3)

# a = "Python"
# print("P" in a)
# print("Java" not in a)


# # Q1
# a data type in python defines the type of value that is stored in a variable, a datatype is used to determine
# the type of operations that should be performed on the values. In python everything is treated as objects and every
# object has its own datatype
# the data type provides the value that is stored in a variabple,for ex: if a = 10, in the variable a the integer value object 10 is stored
# Python needs data types because without datatypes the programmer will not be knowing what kind of data is stored and used to perform operations.
# to prevent the error based on value assigned to variable, easy memeory efficiency


# # Q2
# type() tells us which data type value is assigned to the variable
# synatx = print(type(x))

# isinstance() is used when we have to find all the dataypes are of same type in a sequence
# syntax = isinstance(object, datatype)


# # Q3 
# type(10) == int 
# tells that whether the object 10 belongs to integer datatype or not

# isinstance(10, int)
# if theres a unknown variable and we want to check what type of value is stored so we check with object and its datatype


# # Q4
# int
# float
# complex
# bool
# None
# str
# list
# tuple
# set
# dict
# range



# # Q5
# 10 = it is a integer datatype, and its a positive whole number
# 10.0 = its a floating datatype, and its a positive floating number
# 10+0j = its a complex datatype, with real and imaginary parts real = 10, imag = 0, imaginary component = j
# "10" = its a str datatype with positive integer value 



# # Q6
# # None is a type of Datatype in Python, when None is assigned to a variable, it represents that the variable has no value in stored in it
# and it is used when particular data to stored in variable in the future
# a = None, No the variable a indicates the type of value stored in None datatype, leaving it blank which can be replaced with other datatype values

# # Q7
# Mutable objects: in python mutable objects are those when modified a object, and the changes occur in the same object is called mutable
# ex: list, set, dict, bytearray

# Immutable objects : in python immutable objects are those when modified a object, it does not create changes in the same object but the changes made can
# be stored in a new variable
# ex: int, float, complex, str, tuple


# # Q8
# immutable
# immutable
# immutable
# immutable
# immutable
# immutable
# mutable
# immutable
# immutable
# mutable
# mutable


# Q9
# a = 10, type = int
# b = 10.0, type = float
# c = "100", type = str
# d = False, type = bool
# e = True, type = bool
# f = False, type = str
# g = True, type = str


# # Q10
# a = "25" --> here variable a is referencing to the object is string type value "25"
# b = int(a) we are explictly converting the str data type value to integer data type
# first before conversion a ---->"25"(str) <-------b, here b is aso referencing to the same object as a 
# after conversion a = "25" str datatype  and b = 10 int datatype
# Yes a and b refer to the same object 



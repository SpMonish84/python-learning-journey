# # Python Built-in Functions
# | Category                        | Functions                                                                                                                                           
# | --------------------------------|---------------------------------------------------------------------------
# | 1. Input & Output               | `print()`, `input()`, `open()`                                                                                                                      
# | 2. Type Conversion              | `int()`, `float()`, `str()`, `bool()`, `complex()`, `list()`, `tuple()`, 
# |                                 | `set()`, `frozenset()`, `dict()`, `bytes()`, `bytearray()`, `memoryview()`
# | 3. Math & Numeric               | `abs()`, `round()`, `pow()`, `divmod()`, `sum()`, `min()`, `max()`                                                                                  
# | 4. Number System                | `bin()`, `oct()`, `hex()`                                                                                                                           
# | 5. Iteration & Sequences        | `len()`, `range()`, `enumerate()`, `zip()`, `sorted()`, `reversed()`                                                                                
# | 6. Iterators                    | `iter()`, `next()`, `aiter()`, `anext()`                                                                                                            
# | 7. Logical                      | `all()`, `any()`                                                                                                                                    
# | 8. Character Conversion         | `ord()`, `chr()`, `ascii()`                                                                                                                         
# | 9. Object Inspection            | `type()`, `id()`, `isinstance()`, `issubclass()`, `callable()`, `hash()`                                                                            
# | 10. Attribute Handling          | `getattr()`, `setattr()`, `hasattr()`, `delattr()`, `dir()`                                                                                         
# | 11. Namespace Functions         | `globals()`, `locals()`, `vars()`                                                                                                                   
# | 12. Functional Programming      | `map()`, `filter()`                                                                                                                                 
# | 13. OOP Functions               | `super()`, `property()`, `classmethod()`, `staticmethod()`, `object()`                                                                              
# | 14. Code Execution              | `eval()`, `exec()`, `compile()`, `__import__()`                                                                                                     
# | 15. Representation & Formatting | `repr()`, `format()`, `slice()`                                                                                                                     
# | 16. Debugging & Utilities       | `help()`, `breakpoint()`                                                                                                                            


# Input and Output Func
# 1. print() - displays output on the screen
name = 'Monish'
print(name)

# 2. input() - takes user input from the user through keyboard
name1 = input("Enter your name : ")

# 3. open() - opens the files (r- read, w- write, a- append, x- create, rb- read binary,wb- write binary)
file = open("student.txt","r")

# Type Conversion Func
# 4. int() - converts a value into an integer(whole number)
int(value)

# 5. float() - converts a value into a floating point number
float(value)

# 6. str() - converts a value into string
str(value)

# 7. bool() - conerts a value into boolean
bool(value)

# 8. complex() - creates a complex number
complex(value)

# 9. list() - converts an iterable into a list(mutable)
list("Python")

# 10. tuple() - converts a iterable into a tuple(immutable)
tuple([1,2,3])

# 11. set() - converts data into a set and automatically removes duplicates
set([1,2,2,2,3,3,3,4,1,5,6,2,3,4,5,6,7])

# 12. frozenset() - creates a immutable version of set and its unordered
fs = frozenset([1,2,3])

# 13. dict() - creates a dictionary
dict(name = "Monish", age = 21)

# 14. bytes() - creates immutable binary set
bytes("Python","utf-8")

# 15. bytearray() - mutable version of bytes
bytearray(b"Hello")

# 16. memoryview() - creates a binary data without copying it
data = bytes([23,45,46])
mv = memoryview(data)

# Math & Numeric Built-in Func
# 17. abs() - returns the absolute value of a number Absolute value means:Distance from zero on the number line. Distance is always positive.
abs(10)

# 18. round() - rounds a number to the nearest specified decimal place
round(number,digits)
round(3.2)
cgpa = 8.45678
round(cgpa, 2)

# 19. pow() - raises a number to a power
pow(base, exponent)
pow(2, 3) # 2x2x2=8

pow(a, b, c) #(a^b) % c

# 20. divmod() - returns both quotient and remainder after division
divmod(17,5)
# performs both 17//5,17%5

# 21. sum() - adds all the elements in a iterable
numbers = [10,20,30]
sum(numbers)

# 22. min() - returns the smallest value
min(10,20,30,5)
min("apple", "banana") # in string min compares based on assci value

# 23. max() - returns the largest value
max(10,20,30,5)

# Number System Func
# 24. bin() - converts a decimal integer into its binary representation
bin(10) #0b1010

# 25. oct() - converts a decimal integer to octal reprsentation
oct(10) #0o12

# 26. hex() - converts a decimal integer into hexadecimal representation
hex(10) #0ha

# Iteration & Sequence Func
# 27. len() - returns the number of items in an object
name = "Python"
len(name)

# 28. range() - generates a sequence of numbers
range(start,stop,step)
range(5) # 0 1 2 3 4
range(2,7) # 2 3 4 5 6
range(2,11,2) # 2 4 6 8 10

# 29. enumerate() - adds syntax to every item during iteration
fruits = ["apple","banana","kiwi"]
f = enumerate(fruits)
print(list(f))

# 30. zip() - combines multiple iterables element by element
names = ["ram","john","jim"]
marks = [90,89,95]
l = zip(names,marks)
print(list(l))

# 31. sorted() - returns a sorted version of data
numbers = [5,3,8,1,2,0]
sorted(numbers)
# default ascending order
sorted(numbers,reverse = True)
# descending order

# 32. reversed() - returns elements in a reverse order
numbers = [1,2,3,0,5,4]
l = reversed(numbers)
print(list(l))

# Iterators
# 33. iter() - converts a iterable into a iterator
numbers = [10,20,30]
it = iter(numbers)
print(list(it))

# 34. next() - returns the next element from a iterator
numbers = [10,20,30]
it = iter(numbers)
print(next(it))

# 35. aiter() - creates a asynchronous iterator
# async for item in source:
#    aiter()


# 36. anext()- returns the next value from an asynchronous iterator
# await anext(asyn_iterator


# Logical Built-in Func
# 37. all() - on True returns every element in iterable, returns False is at least one element is false
all([True,True,True]) # True
all([True,True,False,True]) # False

# 38. any() - True if atleast one element is True, False if only all elements are False
any([True,False,True,True])
any([False,False])

# Character Conversion Func
# 39. ord() - returns Unicode point integer value of a character
ord('A') #char - ascii value

# 40. chr() - converts unicode integer into its corresponding character
chr(65)#ascii - char value

# 41. ascii() - returns a string representation of an object where no ascii characters are escaped 
ascii("Monish") # 'Monish' nothing happens
ascii("é") # '\\xe9' ->Letters with accents: é, ñ, ü, Non-Latin scripts: ह (Hindi), 中, (Chinese), ع (Arabic), Symbols: ©, ✓, € and emojies

# Object Inspection Func
# 42. type() - returns the type(class) of an object
x=10
type(x)

# 43. id() - returns the unique identity of an object,usually related to its memory location
x = 100
print(id(x))

# 44. isinstance() - checks whether an object belongs to a specific class / type, returns True/False
x = 10
isinstance(x,int) # True

# 45. issubclass() - checks whether one class is derived from another class
class Animal:
    pass
class Dog(Animal):
    pass
issubclass(Dog, Animal) # issubclass(child,parent)

# 46. callable() - checks whether an object can be called using parenthesis(),returns True/False
print("hello")
callable(print)
x = 100
callable(x)

# 47. has() - returns the hash value of an object
# A hash is an integer used for fastlookup in sets, dictionaries.
hash("python") # some number
hash(100) # 100


# Attribute Handling Func
# 48. getattr() - Get Attribute - returns the value of an attribute
class Student:
    name = "Monish"
    age = 21
print(getattr(Student, "name")) #getattr(object, attribute_name)

# 49. setattr() - Sets or create an attribute
class Student:
    pass
print(setattr(Student, "name","Monish")) #setattr(object, attribute_name, value)

# 50. hasattr() - checks whether an object contains a particular attribute, returns True/False
class Student:
    name = "Monish" 
hasattr(Student, "name") #hasattr(object, attribute_name)

# 51. delattr() -  deletes an attribute
class Student:
    name = "Monish"
delattr(Student, "name") #delattr(object, attribute_name)

# 52. dir() - returns a list of all attribute and methods available in an object
name = "Python"
print(dir(name))

# Namespace Func
# 53. globals() - returns a dictionary containing all global variables
name = "Monish"
age = 21
print(globals())

# 54. locals() - returns a dictionary containin local variables
def show():
    name = "Monish"
    age = 21
    print(locals())

# 55. vars() - returns the __dict__ attribute of an object(returns the attributes stored inside an object)
class Student():
    pass
s = Student()
s.name = "Monish"
s.age = 21
print(vars(s))

# Functional Programming Func
# 56. map() - applies a function to every element of an iterable
numbers = [1,2,3,4,5]
result = []
def double(x):
    return x*2
result = map(double, numbers) # map(function, iterable)
print(list(result))

# 57. filter() - keeps only elements that satisfy a condition
num = [0,1,2,3,4,5,6]
res = []
def is_even(x):
    return x % 2 == 0
res = filter(is_even,num) # filter(function, iterable)
print(list(res))

# OOP Func
# 58. object() - is the root of parent of all classes in python
class Student (object):
    pass
obj = object() # Creates a basic object.

# 59. super() - gives access to methods and attributes of the parent class 
class Animal:
    def speak(self):
        print("Animal Sound")
class Dog(Animal):
    def speak(self):
        super().speak()
        print("Bark")
d = Dog()
d.speak()

# 60. property() - creates managed attributes, allows getter,setter,deleter to behave like normal variables
class Student:
    def __init__(self):
        self._age = -10
    
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            print("Age can not be negative")
s = Student()
print(s.age)
s.age = 21
print(s.age)
s.age = -4

# 61. classmethod() - a method that belongs to the class itself rather than a object
class Student : 
    college = "ABC"
    @classmethod
    def show_college(cls):
        print(cls.college)
Student.show_college()

# 62. staticmethod() - a method placed inside a class but completely independent of self and cls
class Math:
    @staticmethod
    def add(a,b):
        return a + b
Math.add(10,20)


# Code Execution Func
# 63. eval() - evaluates and executes a single python expression and returns the result
eval("10 + 20")

# 64. exec() - executes python code dynamically
code = """
for i in range(5)
print(i)
"""
print(exec(code))

# 65. compile() - converts source code into a code object
code = compile("10+20","<string>","eval") # compile(source, filename, mode)
print(eval(code))

# 66. import() - imports modules dynamically
math_module = __import__("math")
math_module.sqrt(16)

# Representation & Formatting Func
# 67. repr() - returns the official string representation of an object,(goal is show the object in a way that is useful for developer and debugging)
name = "Python"
repr(name)

# 68. format() - formats values into a specific display style
format(10,"b") # format(value, format_spec)
# Common Format Specifiers - b, o, x, f, %, .2f, .3f

# 69. slice() - creates a slice object 
name  = "Python"
name[1:4]
s = slice(1,4) # slice(start, stop, step)
print(name[s])

# Debugging & Utility Functions
# 70. help() - displays documentation about func,modules,calsses,methods,keywords
help(object)

# 71. breakpoint() - pauses prog exec and starts a bebugger
x = 10
y ="20"
breakpoint()
z = x+y
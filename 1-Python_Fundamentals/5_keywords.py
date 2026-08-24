# Python Keywords
print("Python Keywords")
# False      None       True
# and        as         assert
# async      await      break
# class      continue   def
# del        elif       else
# except     finally    for
# from       global     if
# import     in         is
# lambda     nonlocal   not
# or         pass       raise
# return     try        while
# with       yield      match
# case

# import keyword
# print(keyword.kwlist)


# Boolean and special keywords
# True - Boolean true value
x = True
# False - Boolean false value
y = False
# None - represents no value
z = None
print(type(x))
print(type(y))
print(type(z))


# Conditional keywords
# if - executes code if condtion is true
age = 15
if age >= 18:
    print("Adult")
# elif - checks another condtion if previous is false
elif age == 18:
    print("exactly 18")
# else - runs when all the condtion is false
else:
    print("under age")


# Loop keywords
# for - used for iteration
for i in range(5):
    print(i, end =" ")
# while - repeats while condtion is true
o = 10
while(o<5):
    o += 2
# break - immediately exits the lop
print("\t")
for j in range(5,11):
    print(j, end =" ")
    break
# pass - skips the particular iteration
print("\t")
for k in range(5,11):
    print(j, end =" ")
    pass


# Logical keywords
# and - both condtions must be true
print("\n")
And = 3 > 0 and 3 < 10
print(And)
# or - at least one condtion must be true
Or = 3 < 0  or 10 > 100 
print(Or)
# not - reverses a boolean value 
Not = not True
Not1 =  not False
print(Not)
print(Not1)

# Function keywords
# def - creates a function
def greet():
    print("hello")
greet()
# return - returns a value from function
def add(a,b):
    return a+b
# lambda - creates anonymous function
# syntax - lambda arguments: expression
add = lambda x, y: x + y
print(add(5, 3))   # 8


# class keyword
# class - creates a class
class Student :
    pass

# module keywords 
# import - imports a module
import math
# from - imports a specific item
from math import sqrt
# as - creates alias
import math as m
print(type(math))


# Exception Handling keywords
# try - monitors risky code
try:
    x = 10/0
# except - Handles exception.
except ZeroDivisionError:
# finally - Always executes.
#->finally:
    print("Done")
# raise - creates exception manually
#->raise ValueError("Invalid")
# assesrt -  debugging check
assert x > 0



# Variable scope keywords
# global - uses global variable inside function
global g
# nonlocal - uses variable from enclosing funtion
#-> nonlocal x 


#Membership keywords
# in - checks existance
3 in [1,2,3]
# not in - checks absence
5 not in[1,2,3]


# Identity keywords
# is - checks object identity
x is None
# is not - checks different identities
x is not None


# Delete keyword
# del - deletes refrence/object
del x


# Generator keyword 
#yield - creates generators
def gen():
    yield 1


# Context manager
# with - automatically manages resources
with open("file.txt") as f:
    data = f.read()


# Async Programming
# async - defines asynchronous function
async def main ():
    pass
# await - waits for async task
#-> await fetch_data()


# Pattern matching keywords
# match - starts pattern matching
#-> match day:
# case - defines patterns branch
#-> case 1:
print("Monday")
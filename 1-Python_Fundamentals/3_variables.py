#Variables - Variables are used to store 
# data that can be referenced and manipulated 
# during program execution.
a = 10
name = "monish"
age = 21

print("My name is :", name)
print("My age is :", age)
print (a)


a_ = 18
_a = 20
print(a_)
print(_a)


myVar = "abc"
myvar = "xyz"
print(myVar)
print(myvar)

# Assigning values to variables
# 1. Basic Assignment: Variables are assigned values using the = operator.
x = 1
y = 1.2
z = "ijk"
print(x,y,z)

# 2. Dynamic Typing: Python is dynamically typed, so the same variable can store different data types during execution.
a = -1
a = 1
a = "mno"
print(a,a,a)

# 3. Assigning Same Value: same value can be assigned to multiple variables in a single line.
a = b = c = 100
print(a,b,c)

# 4. Assigning Different Values: Multiple variables can also be assigned different values in a single line.
a, b, c = 1, 6.5, "py"
print(a,b,c)

#Concept of Object Reference
x = 5
y = x
#print(x,y) #->5
x = "py"
print(x,y) #->py,5
y = "computer"
print(x,y) #->py,computer
#Python variables store references to objects, not the actual values themselves. 
# When a variable is reassigned, it starts referencing a new object while the 
# old unreferenced object becomes eligible for garbage collection.



# Deleting a variable using the del keyword - used to delete a variable from memory. 
# After deletion, the variable can no longer be accessed.
x = 10
del x
#print(x)


# Swapping two variables without using temp variable
a = 5
b = 10
a,b = b,a
print(a,b)
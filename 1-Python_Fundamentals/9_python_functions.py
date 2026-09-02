# Functions - Python functions are reusable blocks of code used to perform a specific task. 
# They help organize programs into smaller sections and execute the same logic whenever needed by calling the function.

# defining a function
# def key word is used to define a function
# def function_name(parameters):
#    # function body
#    return value
def func():
    print("hello, Welcome")



# calling a function - After creating a function, call it by using the name of the functions followed by parenthesis containing parameters of that particular function.
# func_name(arguments)
func()


# function arguments - are values passed to a function when it is called.
# They allow functions to receive input data and perform operations using those values
def even_odd(n):
    if(n % 2==0):
        return "Even"
    else:
        return "Odd"
# n = float(input("Enter the number : "))
# print(even_odd(n))


# types of function arguments
# 1. Default argument - predefined value when no value is passed during the function call
def myFun(x,y=0):
    print("x : ", x)
    print("y : ", y)
myFun(10)


# 2. Keyword Arguments - pass values using parameter names, so argument order does not matter
def student(fname,lname):
    print(fname,lname)

student(fname = "S P",lname = "Monish")
student(lname =" Monish",fname = "S P")

# 3. Positional Arguments - values are assigned to parameters based on their function call
def name_age(name,age):
    print("Hi my name is :",name)
    print("My age is : ",age)

name_age("Monish",21)
name_age(21,"Monish")


# 4. Arbitary arguments - allow functions to accept multiple values.
# *args - collects extra postional arguments as tuple
# **kwargs - collects extra positional arguments as dictionary
def myDet(*args,**kwargs):
    for arg in args:
        print(arg)

    for key, value in kwargs.items():
        print(f"{key} == {value}")
myDet('hi','hello',fname = 's',mname = 'p',lname = 'monish')


# Functions within Functions
def f1():
    s = "hello"
    def f2():
        return(s)
    f2()
f1()


# Return Statement
def sq_val(n):
    return(n*n)
print(sq_val(3))



# pass by refrence and pass by value
x = [10,20,30]
# refrence - py creates list of objects in memory and x stores a refrence(address) to that object

# pass by refrence - 
# is a parameter passing mechanism where a function receives a direct reference to the original variable, 
# allowing changes inside the function to affect the original variable.

# pass by value -
# is a parameter-passing mechanism where a copy of the variable's value is passed to a function. 
# Changes made inside the function affect only the copy and do not modify the original variable.

# Python uses Pass by Object Reference (Call by Sharing). Functions receive references to objects, and modifications to mutable objects are visible outside the function, while reassignment creates new references.

# Python does not use Pass by Value or Pass by Reference. Python uses Pass by Object Reference (Call by Sharing). 
# Function parameters receive references to the same objects. If the object is mutable and modified, changes are visible 
# outside the function. If the parameter is reassigned, only the local reference changes and the original variable remains unaffected.
# Q1:
# Python is a dynamically typed programming language, its known for its easy readable syntax.
# characteristics of python
# 1. easy Syntax
# 2. it is both compiled and interpreted language
# 3. used in ml,datascience, web dev, web scrapping etc

# Q2:
# yes both are technically comments in python,
# the first represnts a single line comment
# the second one represents a multiline comment,multiline can be used with both double triple quotes'''---''' and triple double qoutes"""---"""

# Q3:
# the data type returned by input is string because the default datatype while using input will be string, until unless we typecaste implicitly or explicitly it remains string for every vale

# Q4:
# a = "10" - is a string value
# b = 20 - is a int value
# print(a+b) the code runs till this line and throws a error because we cannot add string and int values

# Q5: 
# a = 10 - 10 is stored in a
# b = a - the value of a i.e, 10 is stored in b so when printed both the a and b it returs 10
# python does not create seperate objects, it refres to the same object 

# Q6:
# x = 10 - x stores the int value 10
# y = x - y stores the int values of x i.e 10

# x = 20, now x is assigned with a new int value with 20 and stored in it

# print(x) - returms the value 20, because of the concept of object refrence, and last assigned values to the variable will be printed
# print(y) - returns the value 10, because it doesnot create a new object, it stores the refrence of the object created

# Q7:
# no it deletes the variable immediately so when we print the variable it throws a 

# Q8:
# a = 10
# b = 20
# we can switch the varaibles just by switching the varaible like assigning the variable a with the variable b value and vice versa
# a,b = b,a

# -----------------------------------------------------

# Q1:

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print("Hello",name,", you are",age,"years old")

# # Q2:
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# add = num1 + num2
# diff = num1 - num2
# mult = num1 * num2
# print("Sum: ", add)
# print("Difference: ", diff)
# print("Product: ", mult)


# # Q3
# a = int(input("Enter a integer value: "))
# b = int(input("Enter a integer value: "))
# print("Before swapping:")
# print("a = ", a)
# print("a = ", b)

# a,b = b,a
# print("After swapping:")
# print("a = ", a)
# print("b = ", b)

# # # Q4
# num = input("Enter a number: ")
# print("The value: ", num)
# print("Its data type: ", type(num))
# # conversion from str to int
# num = int(num)
# print("The value: ", num)
# print("Its data type: ", type(num))


# # Q5
# a = 100  - the variable a is references the integer object 100
# b = a - the assignment evaluates the currently refrenced variable a, b beacomes another refrence to the integer object 100 same as a
# which means 
# a----->100<-----b
# print(a) - returns the refreneced object 100
# print(b) - returns the referenced object 100

# a = 200 - a is reassigned to the a new integer object 200
# now 
# a---->200
# b---->100
# # output
# a = 100
# b = 100
# a = 200
# b = 100


# # Q6
# name = input("Enter your Name: ")
# age = int(input("Enter your Age: "))
# city = input("Enter your City: ")
# print("")
# print("User Profile")
# print("Name:", name)
# print("Age:", age)
# print("City:", city)

# # Q7
# the exact output is type of a is class string and type os b is class int, because
# the user enter a integer value, but the default value of input is string so the type of a is string
# and b = int(a) tells that we are implcitly which means we mannualy converting it to integer type


# # Q8
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# total_sum = num1 + num2
# diff = num1 - num2
# mult = num1 * num2
# flo_div = num1 // num2
# rem = num1 % num2
# print("Addition:", total_sum)
# print("Subtraction:", diff)
# print("Multiplication:", mult)
# print("Floor division:", flo_div)
# print("Remainder:", rem)

# # Q9
# x = 50 - a refrences the integer object 50
# x --->50
# y = x  - the assignment causes y to become another refrence to the same object that a currently refrences
# x ---->50<----y
# z = y - the assignment causes z also to become another reference ot he same object that a and b curently references
# x --->50<--- y
#        |
#        |
#        z

# x = 100 - x is reassigned to new integer object 100
# y = 200 - y is also reassigned to new object 200

# the value of x = 100
# the value of y = 200
# the values of z = 50


# # Q10
# val1 = input("Enter a value: ")
# val2 = input("Enter a value: ")

# print(val1)
# print(type(val1))

# print(val2)
# print(type(val2))

# val1, val2 = val2, val1

# print(val1)
# print(type(val1))

# print(val2)
# print(type(val2))


# Q11
#step1
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
fav_num = input("Enter your favourite number: ")
#step2
print()
print("Values")
print("Name:", name)
print("Age:", age)
print("City:", city)
print("Favourite number:", fav_num)
print()
print("Data type")
print(type(name))
print(type(age))
print(type(city))
print(type(fav_num))

#step4
fav_numA = fav_num
#step3
fav_num = int(fav_num)

#step5
print(fav_num)
print(fav_numA)

print(type(fav_num))
print(type(fav_numA))


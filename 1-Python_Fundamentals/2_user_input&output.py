#User input from keyboard using the function input()
name = input("Enter your name : ")


#Printing the output using the function print()
print("Welcome", name)


#type() function is used to find the data type of the variable
print(type(name))


#Taking multiple inputs at once using split() function
"""Python split() method is used to break a string into a list of 
smaller strings based on a specified delimiter. 
it is commonly used for text parsing, string extraction and 
processing CSV or space-separated data."""

a,b = input("Enter two numbers:" ).split()
print(a,b)



#Type Casting in Python - Converting one data type to another data type.

#Implicit Type Conversion - Converting Automatically
#int
a = 10
print(type(a))

#float
b = 5.5
print(type(b))

#string
c = "monish"
print(type(c))


#Explicit Type Conversion - converting from user manually
#int to float
a = 5
n = float(a)
print(n)
print(type(n))

#int to str
a = 10
n = str(a)
print(n)
print(type(n))



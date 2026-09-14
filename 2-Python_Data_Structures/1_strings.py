# Python String
# Strings are sequence of characters written inside quotes. it can include letters, numbers, symbols and spaces. it does not have separate character type
# 1. single character is treated as a string of length one
# 2. strings are commonly used for text handling and manipulation

# creating a string
# string can be created using either single '' or double "" quotes.both behave the same
a = 'HI'
b = "Hello World"
print(a)
print(b)

# Multiline Strings
# triple quotes "' "' or """ """ for strings that span multiple lines. new lines are preserved
s = """ I am learning
Python tutorial on GFG"""
print(s)

s = ''' Hello world 
this is Python'''
print(s)

# Accessing a string
# strings are indexed sequences. +ve indices start at 0 from the left, -ve incices start from at -1 from the right 
s = "ABCDEF"
# +ve indices
print(s[0])
print(s[3])
# -ve indices
print(s[-1])
print(s[-4])

# string slicing : is a way to extract a portion of a string by specifying the start and end indexes.syntax [start:end]
s = 'ABCDEF'
print(s[1:4])
print(s[:3])
print(s[0:])
print(s[::-1])

# Looping through strings : strings are iterable which means we can access each character one by one using a loop
s = "ABCDEF"
for char in s:
    print(char,end = " ")
print("\n")


# String Immutability : strings are immutable, meaning their values cannot be changed after creation. any modification to a string
# creates a new string instead of altering the original one
s = "aBCDEF"
s = "A" + s[1:]
print(s)


# Deleting a string : individual characters of a string cannot be deleted beacuse strings are immutable, however an entire string variable can be removed using del keyword
s = "ABC"
del s
# print(s)

# Updating a String : strings cannot be changed directly after creation.so any modifications results in a new string being created using slicing methods like replace()
s = "ABCD EF"
s1 = "H" + s[1:]
s2 = s.replace("ABC","abc")
print(s1)
print(s2)

# Concatenating and repeating Strings
# 1. concatenation : strings can be combined by using + operator
s1 = "Hello"
s2 = "World"
s3 = s1 +" "+ s2
print(s3)

# 2. repetition : a string can be repeated multiple times using * operator
s = "Hello "
print(s * 3)

# Formatting Strings
# 1. Using f-strings : f-strings allows to directly insert variables and expressions inside a string using {} brackets.
name  = "Monish"
age = "21"
print(f"My name is {name} and my age is {age}")

# 2. Using format() : format method allows inersting values into placeholders {} inside a string
s = "My name is {} and I'm {} years old.".format("Monish",21)
print(s)

# String Membership Testing
# in keyword is used to check whether a substring exists inside a string. It returns True if the substring is found otherwise returns False
s = "hello world"
print("Hi" in s)
print("hello" in s)

# String comparison : Python supports several operators for string comparison, including  ==, !=, <, <=, >, >=.
# these operators allow for both equality and lexicographical (alphabetical order) comparisons which is useful when sorting or arranging strings

s1 = "apple"
s2 = "banana"

# 1. == for equality check : simple way to check if 2 strings are identical. if both strings are equal, returns True otherwise returns False
print(s1 == s2)

# 2. != for inequality check : helps to verify if 2 strings are different. if strings are different returns True otherwise returns False
print(s1 != s2)

# 3. Lexicograhical comparison checks if one string appears before or after another in alphabetical order.
print(s1 < s2)
print(s1 > s2)

# Converting integer to String
# 1. using str() func : converts a value into its string representation. it takes the integer as input and returns the equivalent string
n = 18
s = str(n)
print(s)
print(type(s))

# 2. using f-strings : allows values to be placed directly inside a sting using {}. automatically converts integer into a string
n = 49
s = f"{n}"
print(s)
print(type(s))

# 3. using format() func : function inserts values into placeholder {} inside a string.
n = 22
s = "{}".format(n)
print(s)
print(type(s))


# 4. using %s formatting : %s placeholder inserts values into a string and automatically converts them to string format
n = 66
s = "%s" %n
print(s)
print(type(s))



# Convertion of String to int in python
# 1. int() Func : simplest way to convert a integer is by using the int() func.
# this func converts the entire string into a base-10 integer
s = "46"
num = int(s)
print(num)
print(type(num))

# Converting string with different bases
# the int() func also supports other number bases such as binary(base-2) or hexadecimal(base-16)

# Binary string
s = "1010"
num = int(s,2)
print(num)

# Hexadecimal string
s = "A"
num = int(s,16)
print(num)


# Handling invalid input String
# try and except : if input string contains non-numeric characters, int() will raise a valueerror.to handle this we use try-except block
s ="abc"
try:
    num = int(s)
    print(num)
except ValueError:
    print("invalid input,can't convert to int")

# str.isdigit : to check if a string is entirely numeric before converting
s = "12345"
if s.isdigit():
    num = int(s)
    print(num)
else:
    print("the string is not numeric")
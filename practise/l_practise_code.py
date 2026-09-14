# Data Structures, Strings

# string literals
# x = 100 # int
# x = '100' # str

# single quotes
# x = 'Monish'
# msg = 'Hello Python'

# Double quotes
# name = "I'm Monish"
# name = 'Welcome Monish'
# print(name)

# Triple quotes
# msg = """Hello""" # used for multiline strings
# print(msg)
# msg = """Hello World,
# Python Program"""
# print(msg)

# Empty Strings
# text = ""
# print(len(text))

# strings are sequence 
# msg = "PYTHON" # P - 0, Y - 1, T - 2...
# print(msg[0])
# print(msg[4])
# Python indexing starts at 0

# Positive indexing
# msg = "PYTHON"
# print(msg[4])
# print(msg[0])

# Negative indexing starts from -1 from the last character of string
# msg = "PYTHON"
# print(msg[-1])
# print(msg[-3])

# Index error - if index doesn't exist
# text = "Python"
# print(text[10]) # error because index not exists

# len() with strings
# txt = "PYTHON"
# print(len(txt))

# text = "Hello World"
# print(len(text)) # space is also counted

# string slicing string[start:stop]
# msg = "PYTHON"
# print(msg[0:3])
# start is included and stop is excluded

# omitting start
# print(msg[:4]) # Start from the beginning and stop before index 4.
# omitting stop
# print(msg[2:]) # Start at index 2 and continue to the end.
# Ommiting both
# print(msg[:]) # This creates another string containing the same characters.

# step on slicing
# print(msg[::2]) # prints every second character

# negative step
# print(msg[::-1])

# string immutability
# python strings are immutable, Once a string object has been created, its characters cannot be changed individually.
# msg[0] = 'j' # raises type error
# Variables can be reassigned; string objects themselves are immutable.

# string concatenation
# first = "Python"
# second = "Programming"
# result = first +" "+ second
# print(result)

# string repetition
# msg = "Hi"*3
# msg = ("Hi"+" ")*3
# print(msg)

# Membership
# msg = "PYTHON"
# print("PY" in msg)
# print("M" in msg)
# print("x" not in msg)
# print("O" not in msg)

# Iterating over strings
# msg = "PYTHON"
# for char in msg:
#     print(char)

# comparing strings
# print("abc" == "abc")
# print("abc" == "ABC")

# Lexicographical comparison > <
# "apple" < "banana"
# is true because the first differing character is a vs b.
# Don't think of this as "alphabetical sorting" in every possible human-language sense. 
# Python compares characters according to their Unicode values.

# escape sequence
# \n	Newline
# \t	Tab
# \\	Backslash
# \'	Single quote
# \"	Double quote
# \r	Carriage return
# \b	Backspace
# \f	Form feed
# \a	Bell/alert
# \0	Null character

# raw strings - r"....", used for 
# Windows paths
# Regular expressions
# Strings containing many backslashes

# string formatting
# name = "Monish"
# age = 21
# print("Name: " +name) # concatenation
# print("Name:", name) # comma-separated
# print("My name is {} and I am {} years old.".format(name,age)) # .format()
# print(f"My name is {name} and my age is {age}") # f-string
# print(f"sum: {10+20}")

#-------------------------------------------------------------------------------------------
# Create a string containing your name and print it.
# name = "Monish"
# print(name)

# Create three strings using: Single quotes, Double quotes, Triple quotes and Print all three.
# txt = 'monish'
# msg = "S P MONISH"
# text = """Hello, I'm S P Monish,
# I'm 21 years old."""
# print(txt)
# print(msg)
# print(text)


# Create an empty string and determine its length.
# name = ""
# print(len(name))


# text = "Python", find the character at: index 0,2,4,5
# text = "Python"
# print(text[0])
# print(text[2])
# print(text[4])
# print(text[5])


# find the characters at: index -1,-2,-5,-10
# text = "Programming"
# print(text[-1])
# print(text[-2])
# print(text[-5])
# print(text[-10])


# print: P,n
# text = "Python"
# print(text[0])
# print(text[5])

# print the first character using positive indexing and the last character using negative indexing.
# text = "Computer"
# print(text[0])
# print(text[-1])

# print: First character, Last character, Second character, Second-last character, Middle character
# text = "Programming"
# print(text[0])
# print(text[-1])
# print(text[1])
# print(text[5])


# print only the character at index 7.
# text = "Python Programming"
# print(text[7])

# Write a program that takes a string from the user and prints its first and last characters.
# name = input("Enter your name: ")
# print("Name:", name, "first char:", name[0], "last char:", name[-1])

# Extract: Python, using slicing.
# text = "Python Programming"
# print(text[:6])

# # Extract: Programming, using slicing.
# print(text[7:])

# # Extract the first 6 characters.
# print(text[:7])

# # Extract the last 11 characters using slicing.
# print(text[:12])

# # Extract: thon
# print(text[2:6])

# # Extract: Progr
# print(text[7:12])

# Print the first half of:
# text = "ABCDEFGHIJ"
# print(text[:4])

# # Print the second half.
# print(text[6:])

# Print every second character.
# text = "ABCDEFGHIJ"
# print(text[1::2])

# Print every third character.
# print(text[2::3])

# # Print characters at even indexes.
# print(text[::2])

# # Print characters at odd indexes.
# print(text[1::2])

# # Reverse the string using slicing.
# print(text[::-1])


# print: nhy using slicing.
# text = "Python"
# print(text[::-2])

# use slicing to obtain: JHFDB
# text = "ABCDEFGHIJ"
# print(text[::-2])


# Create two strings:Hello Python, Join them with a space using concatenation.
# first = "Hello"
# second = "Python"
# print(first +" "+ second)


# Take the user's first name and last name and create their full name using concatenation.
# fname = input("Enter the first name: ")
# lname = input("Enter the last name: ")
# res = fname +" "+ lname
# print("Full Name:", res)

# Create:**********, using string repetition.
# sign = "*"*10
# print(sign)

# Create:====================, using string repetition.
# sign = "="*20
# print(sign)

# Take a character from the user and a number from the user. Repeat that character the specified number of times.
# name = input("Enter a character: ")
# sign = int(input("Enter the number to repeat: "))
# res = name*sign
# print(res)


# check whether "Python" exists in the string.
# text = "Python Programming"
# print("Python" in text)

# # Check whether "Java" exists in the same string.
# print("Java" in text)

# # Check whether the character "P" exists.
# print("P" in text)

# # Check whether "z" does not exist.
# print("z" not in text)

# Take a string and a character from the user. Determine whether the character exists in the string.
# name = input("Enter a string: ")
# char = input("Enter a character: ")
# if (char in name):
#     print(f"{char} is present in {name}")
# else:
#     print(f"{char} is not present in {name}")

# use a for loop to print each character on a separate line.
text = "Python"
# for char in text:
#     print(char)

# Print every character of a string on the same line separated by spaces.
# for char in text:
#     print(char, end = " ")

# Take a string from the user and count the number of characters using a loop.
# Don't use len() for this question.
# name = input("Enter a string: ")
# count = 0
# for char in name:
#     count += 1
# print(count)

# Take a string and count how many vowels it contains.Don't use string methods.
# name = input("Enter a string: ")
# l = ["a","e","i","o","u","A","E","I","O","U"]
# count = 0
# for i in name:
#     if i in l:
#         count += 1
# print(count)

# Take a string and count how many consonants it contains.
# name = input("Enter a string: ")
# l = ["a","e","i","o","u","A","E","I","O","U"]
# count = 0
# for i in name:
#     if i not in l:
#         count += 1

# print(count)


# Take a string and count how many digits it contains.
# name = input("Enter a string: ")
# count = 0
# for i in name:
#     if i.isnumeric():
#         count += 1
# print(count)


# Take a string and count how many spaces it contains.
# name = input("Enter a string: ")
# count = 0
# for i in name:
#     if " " in i:
#         count += 1
# print(count)


# # Try to change the first character of: to "J" using indexing.
# text = "Python"
# text[0] = "J" # raises an error

# text = "Python"
# name = "Jython"
# print(text, name)

# Compare:"Python"&"Python" using ==
# print("Python" == "Python")
# print("Python" == "python")
# print("apple" == "banana")
# print("apple"<"banana")

# Take two strings from the user and determine whether they are equal.
# name = input("Enter a string: ")
# name1 = input("Enter a string: ")
# if name == name1:
#     print(f"{name} and {name1} are equal")
# else:
#     print(f"{name} and {name1} are not equal")

# Print:Hello World using a single print() statement and \n
# print("Hello"+"\n"+"World")

# Print:
Name = "Monish"
Age = "21"
Course = "Computer Science"
# using 
print(Name+"\t"+Age+"\t"+Course)

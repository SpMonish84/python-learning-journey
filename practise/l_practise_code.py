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
# Name = "Monish"
# Age = "21"
# Course = "Computer Science"
# # using 
# print(Name+"\t"+Age+"\t"+Course)


# Take a string from the user and reverse it.
# str = input("Enter the string: ")
# print("Reversed string:", str[::-1])

# Take a string and determine whether it is a palindrome. madam → Palindrome, hello → Not Palindrome
# str = input("Enter the string: ")
# str1 = ""
# for ch in str:
#     str1 = ch + str1

# if str == str1:
#     print(f"{str} is palindrome")
# else:
#     print(f"{str} is not palindrome")


# Take a string and print:
# First character: ?
# Last character: ?

# str = input("Enter a string: ")
# first_char = str[0]
# last_char = str[-1]
# print(f"First Character: {first_char} \t Last Character: {last_char}")


# # Take a string and print all vowels present in it.
# str  = input("Enter a string: ")
# vow = []
# vowels = ["a","e","i","o","u","A","E","I","O","U"]
# for ch in str:
#     if ch in vowels:
#         vow.append(ch)
# print(" ".join(vow))

# text = "Programming"
# chr = input("Enter a char: ")
# rep = 0
# for ch in text:
#     if chr == ch:
#         rep += 1
# print(rep)


# Take a string and create a new string with all spaces removed.
# str = input("Enter a string: ")
# dup_str = ""
# for ch in str:
#     if ch != " ":
#         dup_str += ch
# print(dup_str)

# str = input("Enter a string: ")
# dup_str = ""
# for ch in str:
#     if ch != " ":
#         dup_str += ch
# print("Count of words:", len(dup_str))



# Take a sentence such as:
# Python is easy to learn
# and count the number of words.
# Don't use split().

# str = input("Enter a string: ")
# count = 1
# for ch in str:
#     if ch == " ":
#         count += 1
# print(count)



#Take a sentence and determine which word has the greatest number of characters.
# Don't use split().
# This one is challenging.


# Anagrams - If two words have the same letters in the same frequency, just arranged differently, they are anagrams.
# listen → silent
# earth → heart
# race → care
# angel → glean
# dusty → study
# evil → vile → live


#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------

# String Methods
# Case Conversion Methods
# 1. capitalize() - The first character is converted to uppercase.The remaining characters are converted to lowercase.
# text = "monish"
# msg = "pYTHON"
# print(text.capitalize())
# print(msg.capitalize())

# 2. casefold() - returns a string converted to a more aggressive lowercase form, designed primarily for caseless string comparisons. But casefold() is more aggressive for certain Unicode characters.
# text = "Straße"
# print(text.casefold())


# 3. lower() - returns a new string with uppercase letters converted to lowercase.
# text = "PYTHON"
# print(text.lower())

# 4. swapcase() - converts: Uppercase → lowercase & Lowercase → uppercase
# msg = "Python"
# msg2 = "pYTHON"
# text = "PYTHON"
# print(msg.swapcase())
# print(msg2.swapcase())
# print(text.swapcase())


# 5. title() - returns a string where the first character of each word is converted to uppercase and the remaining cased characters are converted to lowercase.
# msg = "python programming"
# msg2 = "PYTHON PROGRAMMING"
# print(msg.title())
# print(msg2.title())

# 6. upper() - returns a new string where applicable lowercase letters are converted to uppercase.
# msg = "python"
# msg1 = "PyThOn"
# print(msg.upper())
# print(msg1.upper())

# capitalize() vs title()
# capitalize → first character of entire string
# title      → first character of each word

# lower() vs casefold()
# lower      → normal lowercase conversion
# casefold   → stronger case normalization for caseless comparison

# upper() vs swapcase()
# upper      → everything applicable becomes uppercase
# swapcase   → uppercase ↔ lowercase

#--------------------------------------------------------------------------------------------------------------------

# # Create a string "python" and convert it to uppercase.
# string = "python"
# print(string.upper())

# Create "python programming" and capitalize it.
# str = "python programming"
# print(str.capitalize())

# Create "python programming language" and convert it to title case.
# str = "python programming language"
# print(str.title())

# Create "Python Programming" and swap its case.
# str = "Python Programming"
# print(str.swapcase())

# Take a string from the user and convert it to lowercase.
# str = input("Enter the string: ")
# print(str.lower())

# Take a string from the user and convert it to uppercase.
# str = input("Enter the string: ")
# print(str.upper())


# Take a user's name as input and display it with the first character capitalized and the remaining characters lowercase.
# str = input("Enter your name: ")
# print(str.capitalize())


# Take a sentence and convert it completely to uppercase.
# sen = input("Enter a sentence: ")
# print(sen.upper())


# Take a sentence and convert it completely to lowercase.
# sen = input("Enter a sentence: ")
# print(sen.lower())


# Take two strings from the user and determine whether they are equal without considering uppercase/lowercase differences.
# Use casefold().
# txt = input("Enter a string: ")
# txt1 = input("Enter a string: ")
# if ((txt.casefold()) == (txt1.casefold())):
#     print("equal")
# else:
#     print("not equal")

#-------------------------------------------------------------------------------------------------------------------------------

# Searching & Counting Methods
# 7. count() - Counts how many times a substring occurs in a string.
# txt = "banana"
# print(txt.count("a"))
# print(txt.count("a",0,4)) # (substring,start,end)

# 8. find() - Finds the first occurrence of a substring and returns its index. if not found returns -1
# txt = "banana"
# print(txt.find("a"))
# print(txt.find("a",2,)) # find("char",start,end)

# 9.index() - Also finds the first occurrence of a substring. raises value error if ele not found
# txt = "banana"
# print(txt.index("a"))
# print(txt.index("a",2)) # find("char",start,end)

# 10. rfind() - Finds the last occurrence of a substring. returns -1 if not found
# str = "banana"
# print(str.rfind("a"))
# print(str.rfind("n",0,3))

# 11. rindex() - Finds the last occurrence of a substring. raises a value error if not found
# str = "banana"
# print(str.rindex("n"))
# print(str.rindex("a",1,4))

#-----------------------------------------------------------------------------------------------------

# Create a string "banana" and count how many times "a" occurs.
# str = "banana"
# print(str.count("a"))

# For "programming", count how many times "m" occurs.
# str = "programming"
# print(str.count("m"))

# For "hello world", count how many times "l" occurs.
# str = "hello world"
# print(str.count("l"))

# Count how many times "python" occurs in:
# str = "python is easy and python is powerful"
# print(str.count("python"))

# Find the position of the first "a" in:
# str = "banana"
# print(str.find("a"))

# Find the position of the first "m" in:
# str = 'Programming'
# print(str.find("m"))

# Using "banana", find the position of "a" using:
# str = "banana"
# print(str.find("a"))
# print(str.index("a"))
# print(str.rfind("a"))
# print(str.rindex("a"))


# str = "hello hello hello"
# print(str.count("hello"))
# print(str.find("hello"))
# print(str.rfind("hello"))


# str = "Python Programming"
# print(str.find("P"))
# print(str.find("P",6))
# print(str.find("o"))
# print(str.find("o",6))

# str = "mississippi"
# print(str.count("s"))
# print(str.find("s"))
# print(str.rfind("s"))
# print(str.find("i"))
# # print(str.rfind("i"))

# str = "banana"
# res = str.find("z")
# print(res)

# str = "banana"
# print(str.index("z")) # value error


# Write a program that asks the user for:
# Enter a sentence:
# Enter a character:
# Then determine whether the character exists in the sentence using find().
# str = input("Enter a sentence: ")
# str1 = input("Enter a character: ")
# if str.find(str1) != -1:
#     print("True")
# else:
#     print("False")


# Ask the user for a sentence and a character.
# Display:
# number of times the character occurs
# first position
# last position
# Use count(), find(), and rfind().
# str = input("Enter a sentence: ")
# str1 = input("Enter a character: ")
# print(str.count(str1))
# print(str.find(str1))
# print(str.rfind(str1))

# Ask the user for a sentence and a word.
# Determine:
# whether the word exists
# its first position
# its last position
# how many times it occurs
# str = input("Enter a sentence: ")
# str1 = input("Enter a character: ")
# if str1 in str:
#     print(str.find(str1))
#     print(str.rfind(str1))
#     print(str.count(str1))
# else:
#     print("char not found")

# txt = "Python is powerful and Python is popular"
# print(txt.find("Python"))
# print(txt.rfind("Python"))
# res = txt.rfind("Python") - txt.find("Python")
# print(res)

#-------------------------------------------------------------------------------------------

# Checking / Testing String Methods - All of these methods return a Boolean value: True or False

# 12. isalnum() - Checks whether all characters are alphanumeric:
# Letters: A-Z, a-z, Numbers: 0-9, Unicode letters/numbers are also supported
# txt = "Python123"
# print(txt.isalnum())

# 13. isalpha() - Checks whether all characters are alphabetic letters.
# txt = "Python"
# print(txt.isalpha())

# 14. isascii() - Checks whether all characters are ASCII characters.
# txt = "Python123_,.?"
# print(txt.isascii())

# 15. isdecimal() - Checks whether all characters are decimal characters.
# Accepts only decimal digits (0–9) and equivalent Unicode decimal digits (like Arabic-Indic digits).
# Very strict: it won’t accept superscripts, fractions, or other numeric symbols.
# txt = "123"
# print(txt.isdecimal())

# 16. isdigit() - Checks whether all characters are digit characters. accepts superscripts(²) and sub scripts(⅕)
# Accepts all characters that are classified as digits in Unicode.
# This includes decimal digits plus superscripts, subscripts, and other digit forms.
# txt = "⅕"
# print(txt.isdigit())

# 17. isidentifier() -Checks whether a string is a valid Python identifier.
# An identifier can be a name for things such as:
# variables
# functions
# classes

# print("variable".isidentifier())
# print("my_var".isidentifier())
# print("var-able".isidentifier())


# 18. islower() - Checks whether all cased characters are lowercase.
# print("hello".islower())
# print("hEllo".islower())
# print("h1".islower())
# print("H3".islower())

# 19. isnumeric() - Checks whether all characters are numeric.This is broader than isdecimal() and isdigit()
# print("123".isnumeric())
# print("12.3".isnumeric())
# print("-12".isnumeric())
# print("0".isnumeric())

# 20. isprintable() - Checks whether all characters are printable.
# print("Hello World!".isprintable())
# print("Hello\nWorld!".isprintable())
# print("Hello\tWorld!".isprintable())
# print("".isprintable())

# 21. isspace()- Checks whether all characters are whitespace characters.
# space, tab, newline, other Unicode whitespace characters
# print(" ".isspace())
# print("\t".isspace())
# print("\n".isspace())
# print("".isspace())
# print("hello".isspace())
# print("_".isspace())
# print("hello world".isspace())


# 22. istitle() - Checks whether the string follows title-case rules.
# print("Hello World".istitle())
# print("Hello world".istitle())
# print("hello World".istitle())
# print("hello world".istitle())
# print("Hello World 123".istitle())


# 23. isupper() - Checks whether all cased characters are uppercase.
# print("HELLO".isupper())
# print("HELLo".isupper())
# print("HELLO123".isupper())

#----------------------------------------------------------------------------------------------

# Create a string containing "Python123" and check whether it contains only alphanumeric characters.
# txt = "Python123"
# print(txt.isalnum())

# Create a string containing "PythonProgramming" and check whether it contains only alphabets.
# print("PythonProgramming".isalpha())

# Check whether "Python 123!" contains only ASCII characters.
# print("Python 123!".isascii())

# Check whether "123456" contains only decimal characters.
# print("123456".isdecimal())

# Check whether "12345" contains only digit characters.
# print("12345".isdigit())

# Check whether "student_name" is a valid Python identifier.
# print("student_name".isidentifier())

# Check whether "python programming" is lowercase.
# print("python programming".islower())

# Check whether "123456" contains only numeric characters.
# print("123456".isnumeric())

# Check whether "Hello World!" contains only printable characters.
# print("Hello World!".isprintable())

# Create a string containing only spaces and check whether it contains only whitespace.
# print("   ".isspace())

# Check whether "Python Programming" is title case.
# print("Python Programming".istitle())

# Check whether "PYTHON PROGRAMMING" is uppercase.
# print("PYTHON PROGRAMMING".isupper())

#------------------------------------------------------------------------------------------

# 24. center() - Places the string in the center of a specified width by adding padding on both sides.
# string.center(width, fillchar)
# text = "Python"
# print(text.center(10,"_"))

# 25. ljust() - Keeps the string on the left and adds padding to the right.
# text = "Python"
# print(text.ljust(10,"*"))

# 26. rjust() - Keeps the string on the right and adds padding to the left.
# text = "Python"
# print(text.rjust(10,"*"))

# 27. zfill() - Pads a string with zeros (0) on the left until it reaches the specified width.
# text = "1234"
# print(text.zfill(6))

#---------------------------------------------------------------------------------------------------------------------

# 28. lstrip() - lstrip() removes characters from the left/start of the string. By default, it removes whitespace.
# string.lstrip(chars)
# text = "******************Python"
# print(text.lstrip("*"))

# txt = "abcabcabcPython"
# print(txt.lstrip("abc"))


# 29. rstrip() - Removes characters from the right/end of the string. By default, it removes whitespace.
# text = "Python$$$$$$$$"
# print(text.rstrip("$"))

# 30. strip() - Removes matching characters from both the beginning and the end.
# text = "*****Python********"
# print(text.strip("*"))


# 31. removeprefix() - Removes a specific prefix from the beginning of a string.A prefix is something at the beginning.
# text = "HelloPython"
# print(text.removeprefix("Hello"))

# 32. removesuffix() - Removes a specific suffix from the end of a string.A suffix is something at the end.
# text = "Python Programming"
# print(text.removesuffix("ming"))

# lstrip()       → LEFT
# rstrip()       → RIGHT
# strip()        → BOTH
# removeprefix() → EXACT beginning
# removesuffix() → EXACT ending

#---------------------------------------------------------------------------------------------------------------------------------------

# 33. join() - combines multiple strings into one string, placing a separator between them.
# seperator.join(iterable)

# words = ["Python", "is", "easy"]
# result = " ".join(words)
# print(result)

# l = ["1","2","3"]
# print(" ".join(l))


# 34. partition() - Splits a string into exactly three parts based on the first occurrence of a separator.
# string.partition(separator)
# txt = "Python-is-easy"
# print(txt.partition("-"))

# 35. rpartition() - Splits the string into exactly three parts using the last occurrence of the separator.
# txt = "Python-is-easy"
# print(txt.rpartition("-"))

# 36. split() - splits a string into a list of strings based on a separator.
# string.split(separator, maxsplit)
# txt = "Python is easy language"
# print(txt.split(" ", 2))


# 37. rsplit() - plits a string starting from the right side.
# txt = "Python-is-easy-0"
# print(txt.rsplit("-",2))


# 38. splitlines() - Splits a string at line boundaries and returns a list of lines.\n
# \r,\n, \r\n
# string.splitlines()

# txt = "Python\nis\neasy"
# print(txt.splitlines())
# # keepends - splitlines() can optionally keep the line-ending characters.
# print(txt.splitlines(keepends = True))
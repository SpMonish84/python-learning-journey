# Python String Methods - 47 methods


# Case Conversion Methods

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
#--------------------------------------------------------------------------------------------------

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

#------------------------------------------------------------------------------------------------------------

# Checking / Testing Methods

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
#-------------------------------------------------------------------------------------------

# Alignment & Padding Methods

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
#--------------------------------------------------------------------------------------------------------------

# Removing / Stripping Methods

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
#--------------------------------------------------------------------------------------------------------------------------------

# Splitting & Joining Methods

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
#---------------------------------------------------------------------------------------------------------------

# Replacement & Translation Methods

# 39. replace() - returns a new string where all (or a specified number of) occurrences of a substring are replaced with another substring.
# string.replace(old,new)
# txt = "Python are easy"
# print(txt.replace("are","is"))

# string.replace(old, new, count) - we can limit the number of replacements
# txt = "apple apple apple"
# print(txt.replace("apple","banana",2))

# 40. maketrans() - creates a translation table, It does not change the string by itself.The two strings must have the same length.
# text = "abc bac cab"
# table = str.maketrans("abc","123")
# print(text.translate(table))

# 41. translate() - applies a translation table created by maketrans()
# table = str.maketrans("aeiou", "12345")
# text = "education"
# result = text.translate(table)
# print(result)

# deleting characters
# table = str.maketrans("", "", "aeiou")
# text = "programming"
# result = text.translate(table)
# print(result)

#---------------------------------------------------------------------------------------------------------------------------------------------

# Formatting Methods

# 42. format() - replaces {} placeholders in a string with values. You can use multiple placeholders
# "template {}".format(value)
# name = "Monish"
# txt = "Hello my name is {}".format(name)
# print(txt)

# positional arguments
# txt = "Hello I'm {0}, and my age is {1}".format("Monish",21)
# print(txt)

# reuse of same arguments:
# txt = "Helo I'm {0}, my age is {1}, {0} practices Python".format("Monish",21)
# print(txt)

# keyword arguments:
# txt = "Hello I'm {name}, my age is {age}, {name} practices Python".format(name = "Monish", age = 21)
# print(txt)

# mixing positional and keyword arguments
# txt = "Hello I'm {}, my age is {}, lives in {city}.".format(
#     "Monish",
#     21,
#     city = "Bengaluru"
# )
# print(txt)

# formatting numbers
# price = 123.45678
# text = "Price: {:.2f}".format(price)
# print(text)

# number formatting
# d → integer
# f → floating-point
# % → percentage
# , → thousands separator
# b → binary
# o → octal
# x → hexadecimal

# price = 1500000000
# text = "Price {:.2%}".format(price)
# print(text)

# 43. format_map() - works similarly to format(), but instead of supplying separate arguments, it takes a mapping, usually a dictionary.
# string.format_map(mapping)
# data = {
#     "name" : "Monish",
#     "age" : 21
# }
# print("My name is {name}, and age is {age}".format_map(data))
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

# Encoding & Tab Methods

# 44. encode() - converts a Python string (str) into bytes (bytes) using a specified character encoding.
# string.encode(encoding="utf-8", errors="strict")
# txt = "-"
# print(txt.encode(encoding="utf-8"))
# txt.encode(encoding="utf-8", errors=" ") # errors - strict, ignore, replace, xmlcharrefreplace, blackslashreplace
# encoding - utf-8, utf-16, utf-32, ascii, latin-1, cp1252

# 45. expandtabs() - replaces tab characters (\t) with spaces according to a specified tab size.
# string.expandtabs(tabsize=8)
# txt = "Python\tJava"
# print(txt.expandtabs(tabsize = 10))

# Create a string "Python" and encode it using the default encoding.
# txt = "Python ⚡ Programming"
# print(txt.encode(encoding = "utf-8", errors = "strict"))
# print(txt.encode(encoding = "utf-8", errors = "ignore"))
# print(txt.encode(encoding = "ascii", errors = "backslashreplace"))


# Encode "Hello World" using explicitly specified UTF-8 encoding.
# txt = "Hello World"
# print(txt.encode(encoding = "utf-8"))
#------------------------------------------------------------------------------------------------------------------------------------------------------

# 46. startswith() - checks whether a string begins with a specified substring.
# string.startswith(prefix)
# txt = "hello Python Programming"
# # print(txt.startswith("Python"))

# using start and end 
# print(txt.startswith("Python",6))

# multiple prefixes
# print(txt.startswith(("Python", "hello","hi")))

# 47. endswith() - checks whether a string ends with a specified substring.
# string.endswith(suffix)
# print(txt.endswith("Programming"))

# multiple suffixes
# file = "photo.jpg"
# print(file.endswith(("Python",".jpg",".png",".img")))

#----------------------------------------------------------------------------------------------------------------------------------------------
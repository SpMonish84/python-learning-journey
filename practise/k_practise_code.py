# Built in Functions

# 1. Print()
# a = 10
# b = 20
# print(a, b, a+b)

# sep parameter - separator between objects
# print(value1, value2, value3, sep = "seperator")
# print(10, 20, 30, sep = "-")
# print(30, 7, 2004, sep = "/")
# print("A", "B", "C", sep = "|")

# # end parameter - after the entire print output
# print("Hello", end = "")
# print("World")
# print("A", "B", "C", sep = "-", end = "!")

# print return value is none
# file parameter - The file parameter lets you redirect output to another file or stream.
# with open("output.txt", "w") as f:
#     print("Hello, World!", file=f)

# flush parameter -  controls when the output is written (immediately vs. buffered).
# import time
# for i in range(5):
#     print(i, end=" ", flush=True)  # forces immediate output
#     time.sleep(1)

# print("Hello, Python!")
# print("Monish")
# print("age =", 21)
#------------------------------------------------------------------------------------------

# 2.input() -is used to take input from the user through the keyboard.

# a = input("Enter a number: ")
# b = input("Enter another number: ")
# print(a + b)

# name = input("Enter name: ")

# Take the user's name as input and print it.
# name = input("Enter your name: ")
# print(name)

# Take an integer and print its square.
# n = int(input("Enter a number: "))
# print("Square:", n*n)

# Take a number and determine whether it is even or odd.
# n = int(input("Enter a num: "))
# if n % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# Take a number n and print all numbers from 1 to n.
# n = int(input("Enter a num: "))
# for i in range(1, n+1):
#     print(i)
#------------------------------------------------------------------------------

# 3. open() - file handling, is a built-in function used to open a file so that your Python program can read from it,
#  write to it, append to it, or perform other file operations.

# open(file)
# file = open("E:\\PYTHON-1\\student.txt", "w")
# print("Hello, Student", file = file)
# file.close

# file modes
# "r"	Read
# "w"	Write
# "a"	Append
# "x"	Create a new file
# "b"	Binary mode
# "t"	Text mode
# "r+"	Read + write
# "w+"	Write + read
# "a+"	Append + read

# read data from file
# file = open("E:\\PYTHON-1\\student.txt", "r")
# data = file.read()
# print(data)
# file.close

# # write data into file
# file = open("E:\\PYTHON-1\\student.txt", "w")
# file.write("Welcome")
# file.close
# # write from scratch / overwrite existing content

# # add files at end
# file = open("E:\\PYTHON-1\\student.txt", "a")
# file.write(" Monish")
# file.close()

# open("data.txt", "rt")
# t → text
# r → read

# open("image.jpg", "rb")
# b → binary
# r → read

# Text files generally use text mode:
# .txt
# .csv
# .py
# .html
# .json

# Binary files include things like:
# .jpg
# .png
# .mp3
# .mp4
# .pdf
# .exe

# open("data.txt", "r", encoding="utf-8")
# encoding tells Python how the bytes in a text file should be interpreted as characters.
# UTF-8 is a very common encoding and supports a huge range of characters.


# Create a file named test.txt using Python.
# file = open("test.txt", "x")

# Open an existing test.txt file in read mode
# file = open("test.txt", "r")

# Open test.txt in write mode and write "Hello Python" into it.
# file = open("test.txt", "w")
# file.write("Hello Python")
# file.close

# Open test.txt in append mode and add "Learning Python" without deleting the existing content.
# file = open("test.txt", "a")
# file.write("\n Learning Python")
# file.close 

# Open a file, read its contents, print them, and close the file.
# file = open("test.txt", "r")
# data = file.read()
# print(data)
# file.close
#--------------------------------------------------------------------------------------------------------

# Type Conversion
# 4. int() - is a built-in function used to create an integer or convert a compatible value into an integer.

# print(int(float("12.3")))


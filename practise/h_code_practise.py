# Conditional Statements

# 1. Boolean values
# a = 10
# print(a > 5)
# print(a < 5)


# x = True
# y = False
# print(x and y) # F
# print(x or y) # T
# print(not x) # F


# a = 5
# b = 0
# print(bool(a)) # T
# print(bool(b)) # F
# print(a and b) # 0
# print(a or b) # 5


# x = False
# y = True
# # print(x and (10/0))
# # print(y or (10/0))

# a = 7
# b = 3
# print(a > b and b < 5)
# print(a == 7 or b == 10)


# print(True + True) #2
# print(True * 5) #5
# print(False + 10) #10

# word = "python"
# print("py" in word and "on" in word)
# print("java" not in word or "py" in word)


# x = True
# y = False
# z = True
# print((x and y) or (not z))
# print((x or y) and (z))

# 2. Comparison Operators in Conditions

# a = 5
# b = 7
# print(a == b)
# print(a != b)

# x = 10
# y = 20
# print(x > y)
# print(x < y)
# print(x <= 10)
# print(y >= 15)

# num = 15
# if num > 10:
#     print("Greater than 10")
# else:
#     print("Not greater")


# a = 8
# b = 12
# print(a < b and b < 20)
# print(a > 10 or b == 12)

# print(5 == 5.0)     # int vs float
# print("5" == 5)     # str vs int

# x = 25
# if x > 10 and x < 30:
#     print("Between 10 and 30")
# else:
#     print("Outside range")

# print(True == 1)
# print(False == 0)
# print(False != 2)

# 3. Basic if Statement

# if True:
#     print("This runs")   # indented → inside if
# print("Always runs")     # not indented → outside if

# x = 5
# if x > 3:
#     print("x is greater than 3")


# x = 10
# if x > 5:
#     print("Greater")
# print("Done")


# x = 2
# if x > 5:
#     print("Greater")
# print("Done")

# flag = False
# if flag:
#     print("Flag is True")
# print("Outside if")

# num = 7
# if num % 2 == 0:
#     print("Even")
# if num % 2 != 0:
#     print("Odd")

# text = ""
# if text:
#     print("Not empty")
# print("Check complete")

# x = 12
# if x > 10:
#     print("Above 10")
#     if x % 2 == 0:
#         print("Even number")


# 4. if-else Statement

# x = 8
# if x % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# num = 3
# if num > 5:
#     print("Greater")
# else:
#     print("Not greater")

# flag = True
# if flag:
#     print("Flag is True")
# else:
#     print("Flag is False")


# name = "Python"
# if "Py" in name:
#     print("Starts with Py")
# else:
# #     print("Does not start with Py")

# x = 15
# if x > 10:
#     if x % 2 == 0:
#         print("Greater than 10 and Even")
#     else:
#         print("Greater than 10 and Odd")
# else:
#     print("10 or less")


# 5. Multiple Conditions

# x = 12
# if x > 10 and x % 2 == 0:
#     print("Greater than 10 and Even")
# else:
#     print("Condition not met")

# y = 7
# if y < 5 or y % 2 == 1:
#     print("Either less than 5 or Odd")
# else:
#     print("Neither condition met")

# flag = False
# if not flag:
#     print("Flag is False")
# else:
#     print("Flag is True")


# score = 85
# if score >= 90:
#     print("Grade A")
# elif score >= 75:
#     print("Grade B")
# elif score >= 60:
#     print("Grade C")
# else:
#     print("Grade D")

# age = 20
# if age >= 18:
#     if age < 60:
#         print("Adult but not senior")
#     else:
#         print("Senior citizen")
# else:
#     print("Minor")

# 6. Indentation and Code Blocks
# if True:
#     print("Inside if")   # indented → part of if block
# print("Outside if")      # not indented → outside block


# if 5 > 3:
#     print("Condition True")
#     print("Still inside if")
# print("Outside block")

# x = 7
# if x > 5:
#     print("Yes")
# print("Done")


# x = 3
# if x > 5:
#     print("Yes")
# print("Done")


# x = 12
# if x > 10:
#     print("Above 10")
#     if x % 2 == 0:
#         print("Even")
# print("Outside")

# if True:
# print("Hello")   # ❌ Error: not indented

# x = 5
# if x == True:
#     print("Runs")
# else:
#     print("Does not run")


# x = 1
# if x:
#     print("Truthy")        # Runs, because 1 is truthy
# if x == True:
#     print("Equal to True") # Also runs, because 1 == True

# 9: Conditional Expressions with Different Data Types

# x = 0
# if x:
#     print("Non-zero")
# else:
#     print("Zero")

# word = "Python"
# if word:
#     print("Not empty")
# else:
#     print("Empty")

# items = []
# if items:
#     print("Has elements")
# else:
#     print("Empty list")


# data = {"name": "Alice"}
# if data:
#     print("Dictionary not empty")
# else:
#     print("Empty dictionary")


# val = None
# if val:
#     print("Has value")
# else:
#     print("None detected")

# num = 5
# text = ""
# if num and not text:
#     print("num is non-zero and text is empty")

# class MyClass:
#     def __len__(self):
#         return 0

# obj = MyClass()
# if obj:
#     print("Truthy")
# else:
#     print("Falsy because __len__ == 0")



# # 1. Positive, negative, or zero.
# num1 = int(input("Enter a number: "))

# if (num1 > 0):
#     print("Positive Number")
# elif(num1 < 0):
#     print("Negative Number")
# else:
#     print("Zero")

# # 2.Even or odd.
# num = int(input("Enter a number: "))
# if(num % 2 == 0):
#     print("Even")
# else:
#     print("Odd")

# 3. Eligible to vote.
# age = int(input("Enter your age: "))
# if (age >= 18):
#     print("Eligible to Vote")
# else:
#     print("Not eligible to Vote")

# # 4. Pass or fail.
# marks = int(input("Enter the marks: "))
# if (marks >= 35 and marks <= 100):
#     print("Pass")
# else: 
#     print("Fail")


# 5. Greater of two numbers.
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# if (num1 > num2):
#     print("First number is Greater")
# elif (num1 < num2):
#     print("Second number is Greater")
# else:
#     print("Both are equal")


# # 6. Divisible by 5.
# num1 = int(input("Enter a number: "))
# if (num1 % 5 == 0):
#     print("Divisible by 5")
# else:
#     print("Not Divisible by 5")

# 7.Divisible by both 5 and 10.
# num1 = int(input("Enter a number: "))
# if (num1 % 10 == 0):
#     print("Divisible by 5 and 10")
# else: 
#     print("Not Divisible by 5 and 10")

# # 8.Check whether a character is a vowel.
# char = input("Enter a alphabet: ")
# list = ["A","E","I","O","U","a","e","i","o","u"]
# if (char in list):
#     print("character is a vowel.")
# else:
#     print("character is not a vowel.")



# # 9. Greatest of three numbers.
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))

# if (num1 > num2 and num1 > num3):
#     print("First number is greater")
# elif (num2 > num1 and num2 > num3):
#     print("Second number is greater")
# elif (num1 == num2 == num3):
#     print("Numbers are equal")
# else:
#     print("Third number is greater")


# 10. Check leap year.
# num1 = int(input("Enter a number: "))

# if(num1 % 4 == 0):
#     print("Leap year")
# elif(num1 % 100 == 0):
#     print("Not a Leap year")
# elif(num1 % 400 == 0):
#     print("Leap year")
# else:
#     print("Not a Leap year")


# 11. Calculate grade based on marks.
# marks = int(input("Enter the marks: "))

# if (marks <= 100 and marks >= 90):
#     print("Grade A")
# elif(marks < 90 and marks >= 80):
#     print("Grade B")
# elif(marks < 80 and marks >= 70):
#     print("Grade C")
# elif(marks < 70 and marks >= 60):
#     print("Grade D")
# elif(marks < 60 and marks >= 50):
#     print("Grade E")
# elif(marks <= 50):
#     print("Bad")
# else:
#     print("Invalid marks")

# # 12. Check whether a year is a century year.
# year = int(input("Enter a Year: "))
# if (year % 100 == 0):
#     print("century year")
# else:
#     print("Not century year")


# 13. Check whether a number is divisible by 3 or 7.
# num = int(input("Enter a number: "))

# if (num % 3 == 0 and num % 7 == 0):
#     print("Divisible by both 3 and 7")
# elif (num % 3 == 0):
#     print("Divisible by 3")
# elif(num % 7 == 0):
#     print("Divisible by 7")
# else:
#     print("Not Divisible by 3 or 7")


# # 14. Check whether a person is eligible based on age and nationality.
# age = int(input("Enter your age: "))

# if (age >= 18):
#     nationality = input("Enter your nationality: ").lower()
#     if(nationality  == "india"):
#         print("Eligible to Vote")
#     else:
#         print("not eligible")
# else:
#     print("not eligible")

# 15. Login validation using username and password.
# username = "abc@gmail.com"
# password = "test@123"

# user_input = input("Enter your Username: ")
# pass_input = input("Enter your Password: ")
# if (user_input == username and pass_input == password):
#     print("Login Successful")
# else:
#     print("Invalid Username or Password")

# 16. Check whether a character is uppercase, lowercase, digit, or special character.
# char = input("Enter a character: ")
# if char.isupper():
#     print("Upper Case")
# elif char.islower():
#     print("Lower Case")
# elif char.isdigit():
#     print("Digit")
# else:
#     print("Special Character")


# Q1
a conditional statement in python is used to control the flow in the program
there are 3 types of conditional keywords if, else, elif

if(condition)
block of code
else
block of code
here condition is true in the if block the code executes and exits the if else block
if the condition is false in if block it executes the else block and exit the if elese statement

if-elif-else
in this it is used to execute multiple statements in the program,if the if block is false the elif
block will execute or if the elif block is false, the else block is executed


# Q2
if - in the condition is false the it exits the if block and executes the remaining program
if-else - if the condition is false then the else block gets executed


# Q3
if the conditon is true it executes the particular block of code and executes the remaining program

# Q4
the print statement indentation is wrong in this program, because after if condition there should be indentation gap of 4 space or a single tab space

# Q5
if value: determines the truthness, for example value = True, then executes the if block or value = false, it executes the else block
if value == True, checks the equality
# Python Functions

# def hello(): # func definition
#     print("Hello I'm a function") # func body

# hello() # func invocation / call



# def total_sum():
#     a = 10
#     b = 20
#     result = a + b
#     print("Addition of",a ,"and", b, "is:", result)

# total_sum()


# # Create a function that prints "Hello, Python!".
# def greet():
#     print("Hello, Python!")
# greet()

# # Create a function that prints your name.
# def my_name():
#     print("My name is S P Monish")
# my_name()

# # Create a function that prints three lines of your choice.
# def my_choice():
#     print("Hi")
#     print("Hello")
#     print("Welcome")
# my_choice()

# # Create a function that prints a simple welcome message and invoke it.
# def py_welcome():
#     print("Welcome")
# py_welcome()

# # Create a function that prints the numbers 1 to 5.
# def num_count():
#     for i in range(1,6):
#         print(i,end = " ")
# num_count()
# print("\n")

# # Create a function that prints the multiplication table of 5.
# def mul_table():
#     a = 5
#     for i in range(1,11):
#         print(a, "x", i, "=", a*i)
# mul_table()

# # Create a function that prints all even numbers from 1 to 20
# def even_num():
#     for i in range(1, 21):
#         if i % 2 == 0:
#             print(i, end = "  ")
# even_num()
# print("\n")


# # Create a function that uses a loop to calculate and display the sum of numbers from 1 to 10.
# def display_sum():
#     total = 0
#     for i in range(1, 11):
#         total += i
#     print("sum of numbers from 1 - 10 are:", total)
# display_sum()

# # Create a function that checks a fixed number and displays whether it is even or odd.
# def display_even_odd():
#     num = 11
#     if num % 2 == 0:
#         print(num, "- Even")
#     else:
#         print(num, "- Odd")
# display_even_odd()

# # Create one function and invoke it five times.
# def greet():
#     print("Hello, World")

# for i in range(5):
#     greet()

# Create a function that accepts one parameter name and prints a greeting using that name.
# def greet(name):
#     print("Welcome,", name)
# greet("Monish")

# # Create a function that accepts one number and prints its square.
# def square_number(num):
#     print("Square:", num*num)
# square_number(2)

# Create a function that accepts one number and prints whether it is even or odd.
# def even_odd(num):
#     if num % 2 == 0:
#         print(num, "Even")
#     else:
#         print(num, "Odd")
# even_odd(int(input("Enter the num: ")))

# Create a function that accepts one number and prints its multiplication table from 1 to 10.
# def mult_table(num):
#     for i in range(1,11):
#         print(num, "x", i, "=", i*num)
# mult_table(int(input("Enter a number: ")))


# # Create a function that accepts two numbers and prints their sum.
# def total_sum(a, b):
#     print("Sum of", a, "&", b, ":", a+b)
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))
# total_sum(num1,num2)

# # Create a function that accepts two numbers and prints their difference.
# def total_diff(a, b):
#     print("Difference of", a, "&", b, ":", a - b)
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))
# total_diff(num1,num2)

# Create a function that accepts two numbers and prints their product and quotient.
# def product_quotient(a, b):
#     print("Product of", a, "&", b, ":", a * b)
#     print("Quotient of", a, "&", b, ":", a / b)
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))
# product_quotient(num1,num2)


# Create a function that accepts length and width and calculates the area of a rectangle.
# def area_rect(a, b):
#     print("Area of rectangle:", a * b)
# l = int(input("Enter the length of rectangle: "))
# b = int(input("Enter the breadth of rectangle: "))
# area_rect(l, b)

# Create a function that accepts three numbers and prints the largest number.
# def largest_num(a, b, c):
#     if (a == b == c):
#         print("All numbers are equal")
#     elif(a >= b and a >= c):
#         print(a, "is largest")
#     elif(b >= a and b >= c):
#         print(b, "is largest")
#     else:
#         print(c, "is largest")
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))
# largest_num(num1,num2,num3)

#---------------------------------------------------------------------
# # Create a function that returns the number 100
# def display_num():
#     return 100
# print(display_num())

# Create a function that accepts one number and returns its square.
# def square_num(n):
#     return n*n
# res = square_num(5)
# print(res)


# Create a function that accepts one number and returns its cube.
# def cube(n):
#     return (n*n*n)
# res = cube(2)
# print(res)

# # Create a function that accepts two numbers and returns their sum.
# def total_sum(a,b):
#     return (a + b)
# num1 = int(input("Enter a number:" ))
# num2 = int(input("Enter a number:" ))
# res = total_sum(num1, num2)
# print(res)

# # Create a function that accepts two numbers and returns their product.
# def total_product(a,b):
#     return (a * b)
# num1 = int(input("Enter a number:" ))
# num2 = int(input("Enter a number:" ))
# res = total_product(num1, num2)
# print(res)

# Create a function that accepts a number and returns True if it is even and False otherwise.
# def is_even(n):
#     if n % 2 == 0:
#         return True
#     return False
# n = int(input("Enter a number: "))
# res = is_even(n)
# print(res)

# Create a function that accepts a number and returns whether it is positive.
# def is_positive(n):
#     return n > 0
# n = int(input("Enter a number: "))
# res = is_positive(n)
# print(res)


# Create a function that accepts three numbers and returns the largest.
# def is_largest(a, b, c):
#     if a == b == c:
#         return "all are equal"
#     elif a >= b and a >= c:
#         return f"{a} is largest"
#     elif b >= a and b >= c:
#         return f"{b} is largest"
#     else:
#         return f"{c} is largest"

# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# c = int(input("Enter a number: "))
# res = is_largest(a, b, c)
# print(res)

# # Create a function that accepts a person's marks and returns whether they passed or failed.
# def pass_fail(num):
#     if num >= 35 and num <=100:
#         return "Pass"
#     return "Fail"
# num = int(input("Enter a number: "))
# res = pass_fail(num)
# print(res)

# Create a function that accepts N and returns the sum from 1 to N.

# def total_sum(n):
#     total = 0
#     for i in range(1, n + 1):
#         total += i
#     return total
# n = int(input("Enter a number: "))
# res = total_sum(n)
# print(res)

# Create a function that accepts a number and returns the sum of its digits.
# def sum_digits(n):
#     digit = str(n)
#     total = 0
#     for i in digit:
#         total += int(i)
#     return total
# n = int(input("Enter the digits: "))
# res = sum_digits(n)
# print(res)


# Create a function that accepts a number and returns its largest digit.
# def largest_digit(n):
#     digit = str(n)
#     largest = int(digit[0])
#     for i in digit:
#         if (int(i) > largest):
#             largest = int(i)
#     return largest
# n = int(input("Enter the digit: "))
# res = largest_digit(n)
# print(res)


# # # Create two functions:
# # One returns the square of a number.
# # Another returns the cube of a number.
# # Call both and use their returned values in a calculation.

# def square(n):
#     return n*n

# def cube(n):
#     return n*n*n
# num = int(input("Enter the number: "))
# square_res = square(num)
# cube_res = cube(num)

# print("Square:", square_res)
# print("Cube:", cube_res)
# total_sum = square_res + cube_res
# print("Sum of square and cube:", total_sum)

#-------------------------------------------------------------------------
# def greet(name = "User"):
#     print("Welcome", name)

# greet()
# greet("Monish")

# def student(name, age):
#     print("My name is:", name)
#     print("My age is:", age)

# student("Monish",21)
# # student(21, "Monish") positional arguments
# student(name = "Monish", age = 21) # Keyword arguments


# def student(name, age, course):
#     print("My name is:", name)
#     print("My age is:", age)
#     print("My course is:", course)

# student("Monish", course = "CSE", age = 21) # Positional and Keyword arguments
# Note: Positional arguments must come before keyword arguments.

# *args
# def greet(*name):
#     for i in name:
#         print("Hello", i)
# greet("Monish", "Virat", "ABD")
# the *args are variable number of positional arguments stored as a tuple

# def numbers(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total
# res = numbers(10,20,30,40)
# print(res)



# # **kwargs
# def details(**kwargs):
#     for i,j in kwargs.items():
#         print(f"{i}: {j}")
# details(name = "Monish", age = 21, course = "CSE", degree = "B.tech")
# the **kwargs are variable number of keyword arguments stored as a dictionary


# def animals(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# animals(wild = ["lion","tiger","cheetah"], domestic = ["cow", "sheep", "pig"], pet = ["dog","cat","rabbit"])


# # multiple return values
# def calculate(a, b):
#     return a+b,a-b,a*b,a/b,a//b,a**b
# res = calculate(9,4)
# print(res)


# # multiple return values
# def calculate(a, b):
#     return{
#         "add": a + b,
#         "sub": a - b,
#         "mul": a * b,
#         "div": a / b,
#         "floordiv": a // b,
#         "power": a ** b
#             }
# res = calculate(9,4)
# for key,value in res.items():
#     print(f"{key}: {value}")

# func calling other func
# def square(n):
#     return n*n

# def cube(n):
#     return square(n)*n

# def total_sum(n):
#     return square(n) + cube(n)
# res = total_sum(2)
# print(res)

#----------------------------------------------------------------------------------------------------------------
# Create a function get_number() that returns 50. Store the returned value in a variable and print it.
# def get_number():
#     return 50
# res = get_number()
# print(res)

# Create a function test() that uses return without a value. Call the function and observe what it returns.
# def test():
#     return
# test()
# print(type(test()))

# Create a function containing:
# a print() before return
# a return statement
# a print() after return
# Call the function and determine which statements execute.

# def display():
#     print("A")
#     return
#     print("B")
# display()

# Create two functions:
# One containing only return
# One containing only pass
# Call both and determine the difference between their returned values.

# def display_1():
#     return

# def display_2():
#     pass

# display_1()
# display_2()


#Create a function check_age(age).
# If age is greater than or equal to 18, return "Eligible".
# Otherwise, return "Not Eligible"

# def check_age(age):
#     if age >= 18:
#         return "Eligible"
#     return "Not Eligible"
# res = check_age(19)
# print(res)


# -------------------------------------------------------------------------------------
# Create:
# calculate(a, b)
# It should return:
# sum
# difference
# Store both returned values in separate variables.

# def calculate(a,b):
#     return{
#         "add": a+b,
#         "diff": a-b
#     }
# res = calculate(20,10)
# add = res["add"]
# diff = res["diff"]
# print("add:", add)
# print("diff:", diff)

# Return whether the given year is a leap year.
# def is_leap_year(year):
#     if year % 400 == 0:
#         return "leap year"
#     elif year % 100 == 0:
#         return "Not leap year"
#     elif year % 4 == 0:
#         return "leap year"
#     else:
#         return "Not a leap year"
# year = int(input("Enter the year: "))
# res = is_leap_year(year)
# print(res)


# Create:
# square(n)
# and:
# calculate(n)
# calculate() should call square() and then add 10 to the returned result.

# def square(n):
#     return n*n

# def calculate(n):
#     return square(n) + 10

# res = calculate(5)
# print(res)



# Create:
# is_even(n)
# and:
# analyze(n)
# analyze() should call is_even() and use its returned value to determine whether the number is even or odd.

# def is_even(n):
#     if n % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# def analyze(n):
#     return is_even(n)

# num = int(input("Enter the number: "))
# res = analyze(num)
# print(res)


# Assigning func to variable
# def add(a,b):
#     return a+b
# a = add
# print(a(1,2))
# print(a(3,10))

# lambda functions
# lambda arguments: expression
# square = lambda x: x*x
# print(square(5))

# def square(n):
#     return n*n
# print(square(5))

# get_number = lambda : 100
# double = lambda x : x * 2
# add = lambda a,b : a + b
# total_sum = lambda a, b, c : a + b + c

# res = total_sum(5,2,10)
# print(res)
# print(type(res))


#-----------------------------------------------
# Create a lambda function that returns 100.
# numbers = lambda : 100
# print(numbers())


# Create a lambda function that accepts one number and returns its square.
# square = lambda x: x * x
# a = int(input("enter the number: "))
# print(square(a))


# Create a lambda function that accepts one number and returns its cube.
# cube = lambda x: x*x*x
# a = int(input("enter the number: "))
# print(cube(a))


# Create a lambda function that accepts one number and returns its double.
# double = lambda x : x * 2
# a = int(input("enter the number: "))
# print(double(a))


# Create a lambda function that accepts three numbers and returns their average.
# avg_numbers = lambda a,b,c : (a+b+c)//3
# num1 = int(input("enter the number: "))
# num2 = int(input("enter the number: "))
# num3 = int(input("enter the number: "))
# print(avg_numbers(num1,num2,num3))

#-----------------------------------------------
# Create a lambda function that accepts a number and returns "Even" or "Odd".
# even_odd = lambda n: "Even" if n % 2 == 0 else "Odd"
# a = int(input("enter the number: "))
# print(even_odd(a))

# Create a lambda function that accepts a number and returns "Positive", "Negative", or "Zero".
# pos_neg_zero = lambda n :"Positive" if n > 0 else "Negative" 
# a = int(input("enter the number: "))
# print(pos_neg_zero(a))

# Create a lambda function that accepts two numbers and returns the larger number.
# largest_num = lambda m,n: m if m > n else n
# a = int(input("enter the number: "))
# b = int(input("enter the number: "))
# print(largest_num(a,b))

# Create a lambda function that accepts two numbers and returns the smaller number.
# smallest_num = lambda m,n: m if m < n else n
# a = int(input("enter the number: "))
# b = int(input("enter the number: "))
# print(smallest_num(a,b))

# Create a lambda function that accepts a mark and returns "Pass" if the mark is at least 40, otherwise "Fail".
# marks = lambda n: "pass" if n >= 40 else "fail"
# a = int(input("enter the number: "))
# print(marks(a))

# Create a lambda function that accepts an age and returns "Adult" or "Minor".
# age = lambda n: "adult" if n >= 18 else "minor"
# a = int(input("enter the number: "))
# print(age(a))


#Create a lambda function that accepts a number and checks whether it is divisible by 5.
# divisibility = lambda n: "Divisible" if n % 5 == 0 else "Not Divisible"
# a = int(input("enter the number: "))
# print(divisibility(a))


#-----------------------------------------------------------------------
# Create a lambda function that accepts a number and returns its last digit.
# last_digit = lambda n: n % 10
# a = int(input("enter the number: "))
# print(last_digit(a))

# Create a lambda function that accepts two numbers and returns their product.
# product = lambda a,b : a*b
# a = int(input("enter the number: "))
# b = int(input("enter the number: "))
# print(product(a,b))

# Create a lambda function that accepts three numbers and returns the largest.
# largest_number = lambda a,b,c : a if (a >= b and a >= c) else (b if b >= a and b >= c else c) 
# num1 = int(input("enter the number: "))
# num2 = int(input("enter the number: "))
# num3 = int(input("enter the number: "))
# print(largest_number(num1,num2,num3))


# Recursion
# def countdown(n):
#     if n == 0:
#         return
#     print(n)
#     countdown(n-1)

# countdown(10)


# A. Base case -tell us to stop here
# B. Recursive case - where the func calls itself with smaller or simpler problem
# Recursion follows LIFO where 
# Going DOWN
# → recursive calls are created

# Going UP
# → returned values are resolved

# -----------------------------------------------------------------------------
# Create a recursive function that prints numbers from n down to 1.

# def countdown(n):
#     if n == 0:
#         return
#     print(n)
#     countdown(n-1)
# countdown(5)


# Create a recursive function that prints numbers from 1 up to n.
# def count(n):
#     if n == 0:
#         return
    
#     count(n-1)
#     print(n)
# count(5)

# Create a recursive function that prints "Hello" exactly n times.
# def display(n):
#     if n == 0:
#         return
#     print("Hello")
#     display(n-1)
# display(5)


# Create a recursive function that prints all even numbers from n down to 2.
# def even(n):
#     if n < 2:
#         return
#     if n % 2 == 0:
#         print(n)
#         even(n - 2)

# even(10)

# Create a recursive function that prints all odd numbers from n down to 1.
# def odd(n):
#     if n < 1:
#         return
#     if n % 2 != 0:
#         print(n)
#     odd(n - 1)
# odd(11)
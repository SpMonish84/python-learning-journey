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



# practise codes from pynative.

# Practice Problem: Write a Python function that accepts two integer numbers. 
# If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum.

# def prod_sum(x,y):
#     if x * y <= 1000:
#         return x * y
#     else:
#         return x + y
# x = int(input("Enter a number: "))
# y = int(input("Enter a number: "))
# res = prod_sum(x,y)
# print(res)



#----------------------------------------
# Iterate through the first 10 numbers (0–9). 
# In each iteration, print the current number, the previous number, and their sum.

# my code
# for i in range(1,10):
#     print("Current Number",i," Previous Number",i-1," Sum: ", (i+(i-1)))


# another method
# pre_num = 0
# for i in range(0,10):
#     print("Current Number",i," Previous Number",pre_num," Sum: ", i + pre_num )
#     pre_num += i

#-------------------------------------------


# String Indexing and Even Slicing
# Display only those characters which are present at an even index number in given string.


# word = "pynative"
# # print(word[::2])


# size = len(word)
# for i in range(0,size,2):
#     print(word[i],end = " ")

#---------------------------------------------

# Write a function to remove characters from a string starting from index 
# 0 up to n and return a new string.

# word = "pynative"
# size = len(word)
# start = word[0]
# rem = int(input("Enter the index num: "))
# for i in range(0,size):
#     if rem == i:
#         print(word[rem:])

#----------------------------------------

# #  Write a program to swap the values of two variables, a and b, without using a third temporary variable.
# a = 10
# b = 20
# print("Before swap: a =", a, "b =", b)
# a, b = b, a
# print("After swap: a =", a, "b =", b)

#---------------------------------------------

# Write a program that calculates the factorial of a given number
#  (e.g., 5!) using a for loop.

# n = 5
# fact = 1
# for i in range(1,n+1):
#     fact *= i
# print(fact)

#--------------------------------------------------

# # Create a list of 5 fruits. Add a new fruit to the end of the list, then remove the second fruit (at index 1).
# l1 = ["apple", "banana", "cherry", "date", "elderberry"]
# l1.append("fig")
# l1.remove("banana")
# print(l1)

#----------------------------------------------------

# Write a program that takes a string and reverses it (e.g., “Python” becomes “nohtyP”).

# word = "Python"
# print(word[::-1])
    

#------------------------------------------------------

# Write a program to count the total number of vowels (a, e, i, o, u) present in a given sentence.

# sentence = "Learning Python is fun!"
# vowels = 0
# l1 = ["a","e","i","o","u"]
# s1 = sentence.lower()
# for i in s1:
#     if i in l1:
#         vowels += 1
# print(vowels)

#or

# sentence = "Learning Python is fun!"
# vowels = []
# l1 = ["a","e","i","o","u"]
# s1 = sentence.lower()
# for i in s1:
#     if i in l1:
#         vowels.append(i)
# print(len(vowels))


# Given a list of integers, find and print both the largest and the smallest numbers.
# nums = [45, 2, 89, 12, 7]
# largest = nums[0]
# smallest = nums[0]
# for i in nums:
#     if i > largest:
#         largest = i
#     if i < smallest:
#         smallest = i
# print(f"Largest: {largest} Smallest: {smallest}")

# or

# nums = [45, 2, 89, 12, 7]
# largest = max(nums)
# smallest = min(nums)
# print(f"Largest: {largest} Smallest: {smallest}")

#--------------------------------------------------------

# Removing Duplicates from a List
# data = [1, 2, 2, 3, 4, 4, 4, 5]
# l1 = set(data)
# l2 = list(l1)
# # print(type(data))
# print(list(l2))
# print(type(l2))

# or

# data = [1, 2, 2, 3, 4, 4, 4, 5]
# unique_data = list(set(data))
# print(unique_data)
# print(type(unique_data))
#-----------------------------------------------------------

# Write a function to return True if the first and last number of a given list is the same. If the numbers are different, return False.

# def true_false(l1):
#     return l1[0] == l1[-1]
# print(true_false([75, 65, 35, 75, 30]))
# print(true_false([10, 20, 30, 40, 10]))

#-------------------------------------------------------------------

# Iterate through a given list of numbers and print only those numbers which are divisible by 5.
# num_list = [10, 20, 33, 46, 55]
# print("Divisible by 5: ")
# for i in num_list:
#     if i % 5 == 0:
#         print(i,end = " ")

#-------------------------------------------------------------------

# Write a program to find how many times the substring “Emma” appears in a given string.

# x = "Emma is good developer. Emma is a writer"
# target = input("Enter the target to find in sentence: ")
# t_sum = 0
# for i in x.split():
#     if i == target:
#         t_sum += 1
# print(f"{target} appeared {t_sum} times")

# or 

# print(x.count("Emma"))

#--------------------------------------------------------------------

# Print the following pattern where each row contains a number repeated a specific number of times based on its value.

# n = 5
# for i in range(1,n+1):
#     for j in range(i):
#         print(i, end = " ")
#     print("")
#------------------------------------------------------------------


# Write a program to check if a given number is a palindrome (reads the same forwards and backwards).
# num = 121
# a = str(num)
# if a[0::] == a[::-1]:
#     print("Palindrome")
# else:
#     print("Not Pallindrome")

#-------------------------------------------------------------------

# # Create a new list from two given lists such that the new list contains odd numbers from the first list and even numbers from the second list.
# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# l1 = []
# for i in list1:
#     if i % 2 != 0:
#         l1.append(i)
# for j in list2:
#     if j % 2 == 0:
#         l1.append(j)
# print(l1)
#--------------------------------------------------------------

#  Write a program to extract each digit from an integer in the reverse order.
# number = 7536
# while number > 0:
#     digit = number % 10
#     print(digit, end = "")
#     number //= 10
#-----------------------------------------------------------------------


#  Print a multiplication table from 1 to 10 in a formatted grid.
# n = 10
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i*j, end = " ")
#     print("")

#----------------------------------------------------------------

#  Print a downward half-pyramid pattern using stars (*).
# n = 5
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*", end= " ")
#     print("")

# -----------------------------------------------------------------

# Write a function called exponent(base, exp) that returns an integer value of the base raised to the power of the exponent.
# def exponent(base,exp):
#     return base**exp
# base = int(input("Enter the base value: "))
# exp = int(input("Enter the power value: "))
# print(f"{base} raises to the power of {exp}: {exponent(base,exp)}")
#---------------------------------------------------------------------------

# Write a program to print the first 15 terms of the Fibonacci series. The sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones.

# n1, n2 = 0, 1
# for i in range(15):
#     print(n1, end = " ")
#     res = n1+n2
#     n1 = n2
#     n2 = res
#----------------------------------------------------------------------------

# Write a program that takes a year as input and determines if it is a leap year.
# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a Leap year")
# else:
#     print(f"{year} is not a Leap year")

#------------------------------------------------------------------

# Write a program that takes two separate dictionaries and merges them into one single dictionary.
# d1 = {"name": "Alice", "age": 25}
# d2 = {"city": "New York", "job": "Engineer"}
# d1.update(d2)
# print(d1)

#---------------------------------------------------------------------------
# Take two lists and find the elements that appear in both. Use Sets to perform the operation.

# a = [1, 2, 3, 4, 5]
# b = [4, 5, 6, 7, 8]
# print(set(a).intersection(set(b)))

#--------------------------------------------------------------------------------

# Start with a list of 10 numbers. Iterate through them and sort them into two separate lists: one for even numbers and one for odd numbers.

# numbers = [12, 7, 34, 21, 5, 10, 8, 3, 19, 2]
# eve = []
# odd = []
# for i in numbers:
#     if i % 2 == 0:
#         eve.append(i)
# for i in numbers:
#     if i % 2 != 0:
#         odd.append(i)
# print(f"Even numbers: {eve}")
# print(f"Odd numbers: {odd}")

#---------------------------------------------------------------------------------

# Create a list of 5 words. Write a loop that iterates through the list and prints each word alongside its character count.
# words = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
# for word in words:
#     count = 0

#     for ch in word:
#         count += 1
#     print(f"{word} - {count}", end = " ")

# or

# for i in words:
#     print(f"{i}-{len(i)}", end = " ")

#---------------------------------------------------------------------------------

# Write a program that counts how many times each word appears in a given paragraph and stores these counts in a dictionary.

# text = "apple banana apple cherry banana apple"
# frequency = {}
# for word in text.split():
#     if word in frequency:
#         frequency[word] += 1
#     else:
#         frequency[word] = 1
# print(frequency)

#--------------------------------------------------------------------------------

# prime num

# n = 5
# is_prime = True
# for i in range(2,n):
#     if n % i == 0:
#         is_prime = False
#         break
# if is_prime:
#     print("Prime")
# else:
#     print("Not Prime")

# ------------------------------------------------------------------------

# Create a dictionary where the keys are numbers from 1 to 10 and the values are the squares of those numbers (e.g., 2: 4, 3: 9).
# d = {}
# for i in range(1,11):
#     d[i] = i*i
# print(d)

#-------------------------------------------------------------------------

# Ask the user for a sentence. Replace every empty space in that sentence with an underscore (_) and print the final result.
# sen = input("Enter a sentence: ")
# res = sen.replace(" ", "_")
# print(res)

#---------------------------------------------------------------------------------

# Print a downward number pattern where each row starts with a decreasing value.
# n = 5
# for i in range(n,0,-1):
#     for j in range(i):
#         print(i-j, end = " ")
#     print()
#----------------------------------------------------------------------------------------

# Write a program to check if a user-entered string contains any numeric digits. Use a for loop to examine each character.
# user_input = "Python3"
# contains_digit = False

# for char in user_input:
#     if char.isdigit():
#         contains_digit = True
#         break

# print(f"The string '{user_input}' contains digits: {contains_digit}")

#----------------------------------------------------------------------------------------

# Create a countdown timer that starts from a given number and counts down to zero using a while loop.
# n = 6
# while n > 1 :
#     n -= 1
#     print(n, end = " ")
# print("Blast off!")

#---------------------------------------------------------------------------------------------

# Write a program to print the first 10 natural numbers using a while loop. Each number should be printed on a new line.
# num = 0
# while num <= 9:
#     num += 1
#     print(num)

#-------------------------------------------------------------------------------------------


# Write a program to display a message “Done” after the successful execution of a for loop that iterates from 0 to 4.

# for i in range(0,5):
#     print(i)
# print("Done!")

#--------------------------------------------------------------------------------------------

#  Write a program that accepts a number from the user and calculates the sum of all numbers from 1 up to that number.
# n = int(input("Enter a n number: "))
# count = 0
# for i in range(1,n+1):
#     count += i
# print(count)

#-----------------------------------------------------------------------------------------------

# Create a program that takes an integer and prints its multiplication table from 1 to 10.

# n = int(input("Enter a n number: "))
# for i in range(1, 11):
#     print(f"{n} X {i} = {n*i}")
#----------------------------------------------------------------------------------------

# Write a program that takes an integer n and prints the cube of every number from 1 to n in the format Current Number is : 1 and the cube is 1.

# n = int(input("Enter a n number: "))
# for i in range(1, n+1):
#     print(f"Current Number is : {i}  and the cube is {i*i*i}")

#-----------------------------------------------------------------------------------------------

# Given a list of numbers, iterate through it and print numbers that satisfy these conditions:

# The number must be divisible by five.
# If the number is greater than 150, skip it and move to the next.
# If the number is greater than 500, stop the loop entirely.

# num = [12, 75, 150, 180, 145, 525, 50]
# for i in (num):
#     if i > 500:
#         break
#     elif i > 150:
#         continue
#     elif i % 5 == 0:
#         print(i)
#-------------------------------------------------------------------------------------------------

# Given a list of numbers, use a loop to count how many times a specific number (e.g., 10) appears.

# l1 = [10, 20, 10, 30, 10, 40, 50]
# target = 10
# count = 0
# for i in l1:
#     if target == i:
#         count += 1
# print(f"{target} appears {count} times")

#------------------------------------------------------------------------------------------------

#  Given a Python list, use a loop to print only the elements that are located at odd index positions (index 1, 3, 5, etc.).
# l1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# l2 = []
# for i in l1:
#     if i % 2 == 0:
#         l2.append(i)
# print(l2)
#-----------------------------------------------------------------------------------

# Given a list, iterate it in reverse order and print each element.

# l1 = [10, 20, 30, 40, 50]
# rev = []
# for i in l1:
#     rev.insert(0,i)
# print(rev)

# or

# for i in range(len(l1)-1,-1,-1):
#     print(l1[i])

#-----------------------------------------------------------------------

# Reverse a string using a for loop (no slicing)
# a = "python"
# rev = ""
# for i in a:
#     rev = i + rev
# print(rev)

#---------------------------------------------------------------
# Write a program that counts the total number of vowels and consonants in a given sentence, ignoring spaces and special characters.

# sen = input("Enter a sentence: ")

# vowels = "aeiou"
# vow = 0
# con = 0
# for i in sen.lower():
#     if i in vowels:
#         vow += 1
#     elif i.isalpha():
#         con += 1
# print(f"vowels: {vow}, consonents: {con}")

#----------------------------------------------------------

# Write a program to count the total number of digits in a given integer using a while loop.
# a = 12345
# count = 0
# while a != 0:
#     a //= 10
#     count += a
# print(count)

# a = 1234
# count = 0
# sum = 0
# prod = 1

# for i in str(a):
#     int(i)//10
#     count += 1
#     sum += int(i)
#     prod *= int(i)

# print(count)
# print(sum)
# print(prod)
#--------------------------------------------------------------

# Write a program to reverse a given integer number (e.g., 76542 should become 24567).
# n = 76542
# rev = 0
# while n != 0:
#     digit = n % 10
#     rev = (rev * 10)+digit
#     n //= 10
    
# print(rev)
#---------------------------------------------------------------

# Write a program to find the largest and smallest digit within a given integer (e.g., in 75869, the largest is 9 and the smallest is 5).

# n = 75869
# min = 9
# max = 0
# while n != 0:
#     digit = n % 10
#     if digit < min:
#         min = digit
#     if digit > max:
#         max = digit
#     n //= 10
# print(min)
# print(max)

# The Collatz conjecture states that if you start with any positive integer n, and if n is even, divide it by 2; if n is odd, multiply it by 3 and add 1. Repeat the process. The sequence will always eventually reach 1. Write a program to print this sequence for a given number.
# n = int(input("Enter a n number: "))
# print(n, end = " ")
# while n != 1  :
#     if n % 2 == 0:
#         n = n//2
#     else:
#         n = (n*3)+1
#     print(n, end = " ")
#----------------------------------------------------------------------------------------------------

# Write a program to check if a number is an Armstrong number. An Armstrong number (for a 3-digit number) is an integer such that the sum of the cubes of its digits is equal to the number itself (e.g., 153 = 1^3 + 5^3 + 3^3).

# n = 153
# num = str(n)
# power = len(num)
# total = 0

# for i in num:
#     total += int(i)**power

# if total == n:
#     print("Armstrong")
# else:
#     print("Not a Armstrong")
#---------------------------------------------------------------------------

# Write a program to print a right-angled triangle pattern where each row contains increasing numbers up to the row number.
# for i in range(1,6):
    # for j in range(1,i+1):
    #     print(j,end = " ")
    # print()

#--------------------------------------------------------------------------

# Write a program to use for loop to print the following reverse number pattern:
# for i in range(5,0,-1):
#     for j in range(i, 0,-1):
#         print(j, end = " ")
#     print()
#-----------------------------------------------------------------------------

#Write a program to print a pattern of alternate numbers from 1 to 20 (e.g., 1, 3, 5…).
# for i in range(1,21,2):
#     print(i, end = " ")
#----------------------------------------------------------------------

# Write a program to print a triangle pattern where each row consists of the same letter, and the letter changes (increments) with each new row.

# for i in range(64, 70):
#     for j in range(64,i):
#         print(chr(i), end = " ")
#     print()

#----------------------------------------------------------------

# Write a program to print a triangle pattern where each row consists of the same letter, and the letter changes (increments) with each new row.

# for i in range(5):
#     for j in range(5):
#         if i == 0 or i == 5-1 or j == 0 or j == 5-1:
#             print("*", end= " ")
#         else:
#             print(" ", end = " ")
#     print()

#---------------------------------------------------------------------

#  Write a program to print the following pattern using nested loops:

# n = 5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*", end = " ")
#     print()
# for i in range(n-1,0,-1):
#     for j in range(0,i):
#         print("*", end = " ")
#     print()

#-------------------------------------------------------------

# Given a list of numbers, create a new list where each element is the sum of all elements from the original list up to that position.

# l1 = [1, 2, 3, 4]
# l2 = []
# temp = 0
# for i in l1:
#     temp += i
#     l2.append(temp)
# print(l2)

#--------------------------------------------------------------------------------------

# Given a dictionary of student scores, create a new dictionary that only includes students who scored above a certain threshold (e.g., 75).


# s1 = {"Alice": 85, "Bob": 70, "Charlie": 95, "David": 60}
# s2 = {}
# threshold = 75
# for key,values in s1.items():
#     if values >= threshold:
#         s2[key] = values
# print(s2)

#-------------------------------------------------------------------

# Write a program to remove all duplicate values from a list using a loop, maintaining the original order of elements.

# l1 = [1, 2, 2, 3, 4, 4, 4, 5]
# l2 = []
# for i in l1:
#     if i not in l2:
#         l2.append(i)
# print(l2)

# -------------------------------------------------------------------------------------

# Given a list of integers, move all even numbers to the beginning of the list and all odd numbers to the end.

# l1 = [1, 2, 3, 4, 5, 6]
# l2 = []
# for i in l1:
#     if i % 2 == 0:
#         l2.append(i)
# for j in l1:
#     if j%2 != 0:
#         l2.append(j)

# print(l2)
#---------------------------------------------------------------

# Write a program to display the Fibonacci sequence up to 10 terms. The sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones.
# n,n1 = 0,1
# for i in range(0,10):
#     print(n, end = " ")
#     res = n + n1
#     n = n1
#     n1 = res

# ----------------------------------------------------------------

# Write a program to check if a number is a “Perfect Number.” A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding the number itself). For example, 6 is perfect because 1 + 2 + 3 = 6.
# n = int(input("Enter a n number: "))
# temp = 0

# for i in range(1,n):
#     if n % i == 0:
#         temp += i
# if temp == n:
#     print("Perfect Number")
# else:
#     print("Not Perfect Number")

#--------------------------------------------------------------------


#  Manually convert a binary string (e.g., "1101") into its decimal integer equivalent using a loop. Do not use int(binary, 2).
# n = input("Enter a Binary Value: ")
# dec_val = 0
# rev_bin = n[::-1]

# for i in range(len(rev_bin)):
#     if rev_bin[i] == "1":
#         dec_val += 2 ** i

# print(dec_val)
#---------------------------------------------------------------------


# Given a 2D list (matrix), find the row and column index of a target value.

# matrix = [[10, 20], [30, 40], [50, 60]]
# target = 30

# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if matrix[i][j] == target:
#             print(f"Target {target} found at Row: {i}, Column: {j}")

#--------------------------------------------------------------------------


# Write a function called demo() that accepts two parameters: a name and an age. The function should print these values directly to the console.

# def demo(name, age):
#     print(f"My Name is {name}, my age is {age}")
# demo("Monish", 21)

#--------------------------------------------------------------------------

# Create a function func1() such that it can accept a variable number of arguments and print all of them. Whether you pass two numbers or five, the function should handle them all without error.
# def func1(*arguments):
#     print(f"printing values: ")
#     for i in arguments:
#         print(i)

# func1(20, 40, 60)
# func1(80,100)

#------------------------------------------------------------------------------

#  Write a function calculation() that accepts two variables and calculates both addition and subtraction. The function must return both results in a single return statement.
# def calculation(a,b):
#     return a+b,a-b
# res = calculation(40,10)
# print(res)

#------------------------------------------------------------------------------

# Create a function show_employee() that accepts an employee’s name and salary. If the salary is not provided in the function call, the function should automatically assign a default value of 9000.
# def show_employee(name, salary = 9000):
#     print(f"Name: {name}, Salary: {salary}")
# show_employee("Ben", "12000")
# show_employee("Ben")
#--------------------------------------------------------------------------

# Create an outer function that accepts two parameters, a and b. Inside, create an inner function that calculates the addition of a and b. The outer function should then add 5 to that sum and return the final result.

# def calculate(a,b):
#     def add():
#         add = a + b
#         return add
#     return add() + 5
# print(calculate(5,10))

# ------------------------------------------------------------------------------

# Write a recursive function addition() that calculates the sum of numbers from 0 to 10. A recursive function is a function that calls itself to solve smaller instances of the same problem.
# def add(n):
#     if n > 0 :
#         return n + add(n-1)
#     else:
#         return 0
# print(add(5))
#------------------------------------------------------------------------------------

# Assign a different name to the function display_student(name, age) and call it using the new name. For example, assign it to a variable called show_student.
# def display_student(name, age):
#     print(name,age)
# show_student = display_student
# show_student("Monish", 22)

#-------------------------------------------------------------------------------------


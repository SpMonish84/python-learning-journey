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
num = 121
a = str(num)
if a[0::] == a[::-1]:
    print("Palindrome")
else:
    print("Not Pallindrome")
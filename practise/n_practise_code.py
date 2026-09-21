# Python Tuples

# creating tuple
# numbers = (10,20,30)
# print(numbers)
# print(type(numbers))

# numbers = 10,20,30
# print(numbers)
# print(type(numbers))

# empty = ()
# print(type(empty))

# empty = tuple()


# single element tuple
# x = (10,)
# print(type(x))


# tuple characteristics
# ordered - follows a sequence
# num = (10,20,30)

# immutable - once the  tuple is created its elements can not be changed
# num = (10,20,30)
# num[0] = 100 # raises an error

# allow duplicate items
# num = (1,2,3,4,1,5,2,3,1,5,2,3,4,5,2,3,1,3)

# can contain diff data type elements
# num = (12,3.4,5+8j,"Name",True)
# print(num)
# print(type(num))

# indexing - positive index starts with 0 and negative index starts with -1
# numbers = (10,20,30,40,50)
# print(numbers[0])
# print(numbers[-1])
# print(numbers[2])
# print(numbers[-3])


# Slicing - tuple[start:stop:step]
# numbers = (10,20,30,40,50)
# print(numbers[0:3])
# print(numbers[3:5])
# print(numbers[::-1])


# tuples can contain a mutable object
# data = ([1,2],[4,5])
# data[0].append(3)
# print(data)


# accessing tuple elements
# student = ("Monish",21,"CSE")
# name = student[0]
# print(name)

# data = ("Python", (1,"Name",3.2))
# print(data[1][2])


# Iterating over tuples
# num = (10,20,30)
# for i in num:
#     print(num.index(i), i)


# Membership testing - in, not in
# num = (10,20,30,40)
# print(20 in num)
# print(50 not in num)


# Tuple Operators - Concatenation +, Repetition *
# num = (1,2,3)
# num1 = (4,5,6)
# res = num + num1
# print(res)

# num = ()
# for i in range(1,6):
#     num = num +(i,)
# print(num)
# print(type(num))

# num = (1,2,3)
# res = num *3
# print(res)


# Tuple methods count(), index()
# num = (10,20,10,20,30,10,20,40,20,30,10,50,40,30,50,20,40)
# print(num.count(10))

# print(num.index(50))

# tuple packing
# data = (10,20,30)
# first,middle,last = data
# print(first)

# data = (10,20,30,40,50)
# first,*middle,last = data
# print(first)
# print(middle)
# print(last)


# swapping using tuple unpaacking
# a = 10
# b = 20
# a,b = b,a
# print(a)
# print(b)

# Nested Tuples
# data = (
#     (1,2),
#     (3,4),
#     (5,6)
# )

# # access
# print(data[0])
# print(data[0][1])

# iteration
# for row in data:
#     for column in row:
#         print(column)


# Tuple dont have comprehension, it has generator expressions
# res = tuple(x*x for x in range(1,6))
# print(res)


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Q1
# tup = (10,20,30,40)
# print(tup)
# print(type(tup))


# Q2
# tup = ()
# print(type(tup))
# tup = tuple()
# print(type(tup))

# Q3
# tup = (100,)
# print(type(tup))

# Q4
# data = (21,3.4,4+9j,"Name",True)
# print(data[0])
# print(type(data[0]))
# print(data[1])
# print(type(data[1]))
# print(data[2])
# print(type(data[2]))
# print(data[3])
# print(type(data[3]))
# print(data[4])
# print(type(data[4]))

# Q5
# numbers = (10, 20, 30, 40, 50, 60)
# count = 0
# for i in numbers:
#     count += 1
# print(count)


# Q6
# data = (10, 20, 30, 40, 50)
# print(data[0])
# print(data[2])
# print(data[-1])


# Q7
# data = (10, 20, 30, 40, 50)
# print(data[-1])
# print(data[-2])
# print(data[-5])


# Q8
# data = (10, 20, 30, 40, 50, 60, 70)
# print(data[0:3])
# print(data[4:])
# print(data[2:6])
# print(data[1::2])
# print(data[::-1])


# Q9
# data = ("Python", "Java", "C++", "JavaScript", "SQL", "HTML")
# print(data[0])
# print(data[2])
# print(data[3:5])
# print(data[-1])

# Q10
# numbers = (10, 20, 30, 40)
# numbers[2] = 100 # raises error

# Q11
# numbers = (10, 20, 30, 40)
# l1 = list(numbers)
# print(numbers)
# print(l1)
# l1[2] = 100
# print(l1)
# res = tuple(l1)
# print(res)
# print(type(res))
# # OR
# new_num = numbers[:2] + (100,) + numbers[3:]
# print(new_num)

# Q12
# numbers = (10, 20, 30, 40,50)
# new_num = numbers[:2] + numbers[3:]
# print(new_num)


# Q13
# numbers = (10, 20, 30, 40, 50)
# for i in numbers:
#     print(numbers.index(i),i)

# Q14
# numbers = (10, 20, 30, 40, 50)
# for i in numbers:
#     print("Index", numbers.index(i),i)

# Q15
# numbers = (10, 20, 30, 40, 50)
# sum_value = 0
# for i in numbers:
#     sum_value += i
# print(sum_value)

# Q16
# numbers = (12, 7, 9, 20, 34, 15, 18)
# even = 0
# odd = 0
# for i in numbers:
#     if i % 2 == 0:
#         even += 1
#     elif i % 2 != 0:
#         odd += 1
# print(even)
# print(odd)


# Q17
# languages = ("Python", "Java", "C++", "JavaScript")
# lang = input("Enter a programming Language: ")
# if lang in languages:
#     print("Found")
# else:
#     print("Not Found")


# Q18
# languages = ("Python", "Java", "C++", "JavaScript")
# lang = input("Enter a programming Language: ")
# found = False
# for i in languages:
#     if i == lang:
#         found = True
#         break
# if found:
#     print("Found")
# else:
#     print("Not Found")


# Q19
# t1 = (1, 2, 3)
# t2 = (4, 5, 6)
# res = t1 + t2
# print(res)
# print(type(res))

# Q20
# data = ("Python",)
# data1 = ("Python",)*3
# print(data1)
# print(type(data1))



# t1 = 10, 20, 30, 40
# print(t1)
# print(type(t1))


# # Unpack the values into three separate variables:
# a
# b
# c
# Print them.

# numbers = (10, 20, 30)
# a,b,c = numbers
# print(a)
# print(b)
# print(c)


# person = ("Monish", 21, "Bangalore", 8.06)
# Unpack all values into appropriate variables and print them.
# person = ("Monish", 21, "Bangalore", 8.06)
# Name = person[0]
# Age = person[1]
# City = person[2]
# cgpa = person[3]
# print(Name)
# print(Age)
# print(City)
# print(cgpa)


# Create a function that accepts two numbers and returns:
# sum
# difference
# product
# division
# Receive all four values using tuple unpacking.

# def calc(a,b):
#     return a+b,a-b,a*b,a/b
# add,sub,mul,div = calc(10,20)

# print("ADD:", add)
# print("SUB:", sub)
# print("MUL:", mul)
# print("DIV:", div)


# Create a function that accepts a tuple of numbers and returns:
# minimum value
# maximum value
# Receive both values using unpacking.


# def min_max(t1 = (10,20,30,40)):
#     maxi = t1[0]
#     for i in t1:
#         if i > maxi:
#             maxi = i
#     mini = t1[0]
#     for i in t1:
#         if i < mini:
#             mini = i
#     return maxi,mini
# maxi,mini = min_max()

# print("maximum value:", maxi)
# print("minimum value:", mini)




# Create a function that accepts:
# name
# marks in 3 subjects
# Return:
# name
# total
# average
# Store the returned values separately.


# def student_details(Name, m1, m2, m3):
#     total =m1+m2+m3
#     avg = (m1+m2+m3)/3
#     return Name,total,avg

# name = input("Enter Your Name: ")
# mark1 = int(input("Enter marks sub 1: "))
# mark2 = int(input("Enter marks sub 2: "))
# mark3 = int(input("Enter marks sub 3: "))

# name,total_marks,average_marks = student_details(name,mark1,mark2,mark3)
# print("Student Name:", name)
# print("Total Marks:", total_marks)
# print("Average Marks:", average_marks)




# Given:
# numbers = (10, 20, 30, 40)
# Convert it into a list.
# Then add 50.
# Convert it back into a tuple.

# num = (10,20,30,40)
# l1 = list(num)
# l1.append(50)
# res = tuple(l1)
# print(res)




# Ask the user to enter several numbers and store them in a list.
# Convert the final list into a tuple.

# l1 = list(map(int, input("Enter the numbers: ").split()))
# res = tuple(l1)
# print(res)
# print(type(res))




# numbers = (10, 20, 30, 40, 50)
# Remove 30 while keeping the final result as a tuple.

# numbers = (10, 20, 30, 40, 50)
# new_num = numbers[0:2] + numbers[3:]
# print(new_num)
# print(type(new_num))




# Create a generator expression that produces the squares of:
# 1 to 10
# Iterate over the generator and display the values.

# square = tuple(x*x for x in range(1,11))
# print(square)



# A tuple containing squares from 1–10
# A generator expression producing squares from 1–10
# Check their types and understand the difference.


# A tuple containing squares from 1–10
# A generator expression producing squares from 1–10
# Check their types and understand the difference.

# t1 = tuple()
# for x in range(1,11):
#     t1 = t1 + (x*x,)
# print(t1)
# print(type(t1))

# square = (x*x for x in range(1,11))
# print(square)
# print(type(square))




# Find the second-largest distinct value.
# Do not use sort() or sorted().

# num = (10, 25, 7, 40, 15, 40, 30)
# large = num[0]
# sec_large = num[0]
# for i in num:
#     if i > large:
#         sec_large = large
#         large = i
#     elif i > sec_large and i != large:
#         sec_large = i
# print(large)
# print(sec_large)




# Find the second-largest distinct value.
# Do not use sort() or sorted().

# t1 = (10,20,31,20,38,19,50,19,39,10,49,29,10,9,39,4,2,3,4,1,49,49,10,50,49)
# large = t1[0]
# sec_large = t1[0]
# for i in t1:
#     if i > large:
#         sec_large =large
#         large = i
#     elif i > sec_large and i != large:
#         sec_large = i
# print(large)
# print(sec_large)


# Given:
# numbers = (10, 20, 10, 30, 20, 40, 10)
# Create a new tuple containing each value only once.

# numbers = (10, 20, 10, 30, 20, 40, 10)
# # res = set(numbers)
# # print(res)
# new_num = ()
# for i in numbers:
#     found = False
#     for j in new_num:
#         if i == j:
#             found = True
#             break
#     if found == False:
#         new_num = new_num + (i,)
# print(new_num)



# # Given a tuple of numbers, find the number that occurs the most times.
# t1 = (10,30,40,20,10,60,40,20,50,20,10,40,50,20)
# num = int(input("Enter the number to find most times: "))
# count = 0
# for i in t1:
#     if i == num:
#         count += 1
# print(count)


# numbers = (10, 15, 22, 31, 40, 55, 60, 73)
# # Create:
# # even_tuple
# # odd_tuple
# # containing the corresponding numbers.

# even_tuple = ()
# odd_tuple = ()

# for i in numbers:
#     if i % 2 == 0:
#         even_tuple = even_tuple + (i,)
#     elif i % 2 != 0:
#         odd_tuple = odd_tuple + (i,)

# print(even_tuple)
# print(odd_tuple)



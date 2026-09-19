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

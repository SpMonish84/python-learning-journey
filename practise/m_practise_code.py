# Python Lists 

# empty list
# numbers = [] or numbers = list()

# list with ele
# numbers = [10,20,30,40]
# print(numbers)
# print(type(numbers))


# list with diff data type elements
# data_types = [10, 20.5,"Name",True]
# print(data_types)

# list can contain other lists
# l1 = [1,[2,3],4]
# print(l1)


# string as elements in list
# data = ["Name", "Age", "City"]
# print(data)


# lists are ordered - means it follows a sequence
# l1 = [10,20,30]


# lists are mutable - meaning the objects in list can be changed or mutated
# l1 = [10,20,30]
# l1[1] = 21
# print(l1)
# here we didn't create new list we just changed the objects in existing lists

# strings in list are mutable
# l1 = ["Name","Age","City"]
# l1[0] = "Monish"
# print(l1)


# lists allow duplicate elements and its sliceable
# l1 = [10,20,30,10,30,20,10,30,30,10,30,10,20]
# # print(l1)
# print(l1[0:2])


# accessing elements using their index it starts from zero for positive index. and starts for negative index
# l1 = [10,20,30,40,50]
# print(l1[0])
# print(l1[-1])
# print(l1[3])


# accessing nested lists
# l1 = [[10,20],[30,40],[50,60]]
# print(l1[1])
# print(l1[1][1])
# print(l1[0][1])

# slicing lists
# list[start:stop:step]
# l1 = [10,20,30,40,50]
# print(l1[2:])
# print(l1[::-1])


# adding elements
# list.append(object) - will add the exactly one object to the existing list at last
# l1 = []
# l1.append(10)
# # list.extend([object,object]) - will add multiple elements to the existng list at last
# l1.extend([20,30,40])
# print(l1)


# adding elements at specific index
# list.insert(index,object)
# l1 = [10,20,30,50]
# l1.insert(3,40)
# print(l1)

# Updating elements
# l1 = [10,20,40]
# l1[2] = 30
# # update multiple elements using slicing
# l1[1:3] = [200,300]
# print(l1)


# Removing elements

# l1 = [10,20,30,20,30]
# remove() - removes first occurrence of a specified object
# l1.remove(20)
# print(l1)

# pop() - removes and returns a element at specified index
# l1.pop(2)
# print(l1)

# del() - we can delete an element
# del l1[4]
# print(l1)

# clear() - removes all elements from the list
# l1.clear()
# print(l1)


# Iterating over the lists
# for loop
# l1 = [10,20,30,40,50]
# for ele in l1:
#     print(ele)


# Index based iteration
# for ele in range(len(l1)):
#     print(ele, l1[ele])

# while loop
# i = 0
# while i < len(l1):
#     print(l1[i])
#     i += 1


# membership testing
# print(20 in l1)
# print(90 not in l1)
# print(23 in l1)
# print(30 not in l1)


# list operators

# l1 = [10,20]
# l2 = [30,40]
# res = l1 + l2  # creates a separate list with both the list objects
# print(res)


# l1 = [1,2]
# res = l1*3  # creates a new list with duplicate elements from previous list
# print(res)

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# print(matrix[0])
# print(matrix[0][2])
# print(matrix[1][1])

# iterating over nested lists

# for row in matrix:
#     for ele in row:
#         print(ele)




# List comprehension -provides a concise syntax for constructing a list by iterating over an iterable and optionally filtering/transformation elements.
# [expression for item in iterable]

# square = [x * x for x in range(1,5)]
# print(square)


# square = []
# for x in range(1,5):
#     square.append(x*x)
# print(square)


# List comprehension with a condition
# [expression for item in iterable if condition]

# even_num = []
# for i in range(0,22):
#     if i % 2 == 0:
#         even_num.append(i)
# print(even_num)

# even_num = [x for x in range(0,22) if x%2 == 0]
# print(even_num)


# list comprehension with if else
# [expression_if_true if condition else expression_if_false for item in iterable]
# odd = []
# eve = []
# for i in range(1,21):
#     if i % 2 == 0:
#         eve.append(i)
#     else:
#         odd.append(i)
# print(eve)
# print(odd)


# even_odd = ["Even" if x % 2 == 0 else "Odd" for x in range(1,21)]
# print(even_odd)

# even = []
# odd = []
# even_odd = [even.append(x) if x % 2 == 0 else odd.append(x) for x in range(1,21)]
# print(even)
# print(odd)



# Nested List comprehension
# res = [x * y for x in [1,2] for y in [10,20]]
# print(res)


# List Unpacking
# l1 = [10,20,30]
# a,b,c = l1
# print(a)
# print(b)
# print(c)

# extended packing 
# l1 = [10,20,30,40,50]
# first, *middle, last = l1
# print(first)
# print(middle)
# print(last)


# copying lists
# a = [10,20,30]
# b = a
# b.append(40)

# print(a)
# print(b)



# Sorting the list
# l1 = [30,50,20,40,10,80,90,70,60]
# l1.sort() # ascending order
# # l1.sort(reverse = True) # descending order
# print(l1)


#-------------------------------------------------------------------------------------------------------------------------------------------------


# Create a list
# l1 = [10,20,30,40,50] # l1 = list()
# print(l1)

# Access an element
# print(l1[2])

# Access the last element
# print(l1[-1])

# Update an element
# l1[0] = 11
# print(l1)

# Append an element
# l1.append(60)
# print(l1)

# Insert an element
# l1.insert(2,25)
# print(l1)

# Remove an element
# l1.remove(20)
# print(l1)

# Iterate through a list
# for i in l1:
#     print(i)

# i = 0
# while i < len(l1):
#     print(i, l1[i])
#     i += 1


# Find whether an element exists
# print(30 in l1)

# Count elements
# print(len(l1))


# Find sum of elements
# count = 0
# for i in l1:
#     count += i
# print(count)

# Find largest element
# largest = l1[0]
# for i in l1:
#     if i > largest:
#         largest = i
# print(largest)


# Find smallest element
# smallest = l1[0]
# for i in l1:
#     if i < smallest:
#         smallest = i
# print(smallest)
# print(min(l1))

# Count even numbers
# l1 = [1,2,3,4,5,6,7,8,9,10]
# count = 0
# for i in l1:
#     if i % 2 == 0:
#         count += 1
# print(count)


#  Count odd numbers
# count = 0
# for i in l1:
#     if i % 2 != 0:
#         count += 1
# print(count)


# Sum even numbers
# total_sum = 0
# for i in l1:
#     if i % 2 != 0:
#         total_sum += i
# print(total_sum)

# Reverse a list
# print(l1[::-1])

# Create a list of squares
# squares = [x*x for x in range(1,6) ]
# print(squares)

# Extract only positive numbers
# l1 = [-1,10,-2,30,-3,20,-4,60]
# positive = []
# for i in l1:
#     if i > 0:
#         positive.append(i)
# print(positive)

# Remove a particular value
# l1 = [1,2,3,4,5,6,7,8,9,10]
# l1.remove(3)
# print(l1)

# Find second largest
# l1 = [23,12,44,20,49,58,29,48,56,19]
# l1.sort(reverse = True)
# print(l1[1])
# Python Sets

# example
# num = {10,20,30,40}
# print(num)
# print(type(num))

# set with dup elements 
# num = {10,20,10,30,20,10,40,50,30,40,50}
# print(num)

# diff datatypes inside set
# s1 = {1, 2.4,"Name",True,(1,2,3),9+8j,}
# print(s1)

# empty set
# s = set()


# num = [10,20,30,10,30,20,40,20,40,10,30,50,20,40]
# unique_val = list(set(num))
# print(unique_val)
# res = sorted(unique_val)
# print(res)



# Membership testing
# num = {10,20,30,10,30,20,40,20,40,10,30,50,20,40}
# print(20 in num)
# print(80 in num)

# iterating over a set
# num = {10,20,30,10,30,20,40,20,40,10,30,50,20,40}
# for i in num:
#     print(i)



# Adding elements = s.add(x)
# num = {10,20,30,10,30,20,40,20,40,10,30,50,20,40}
# num.add(70)
# num.add(60)
# print(num)

# # Adding multiple elements = s.update([x,x])
# num = {10,20,30,10,30,20,40,20,40,10,30,50,20,40}
# num.update([60,60,60,80,80,70,80])
# print(num)
# # we can also pass diff iterables
# num.update([1,2],(3,4),{5,6})
# print(num)


# Removing elements remove() = s.remove(x)
# num = {10,20,30,10,30,20,40,20,40,10,30,50,20,40}
# num.remove(30) # if ele doesnot exist python raises error
# print(num)

# Removing elements discard() = s.discard(x)
# num = {10,20,30,40,50}
# num.discard(31) # if ele does not exist python raises no error
# print(num)

# pop() - s.pop() - removes and returns an arbitrary ele
# num = {10,40,30,20}
# num.pop()
# print(num)

# clear() clears all element from existing set
# num = {10,20,30,40,50}
# num.clear()
# print(num)

# del - can remove the entire name binding
# num = {10,20,30,40}
# del num
# print(num)

# SET mathematical operations
# A = {1,2,3,4}
# B = {3,4,5,6}
# we can perform union, intersection, difference, symmetric difference

# 1. Union - elements present in A or B or both
# print(A | B)
# print(A.union(B))

# Intersection - elements common in both sets
# print(A & B)
# print(A.intersection(B))

# Difference - elements present in A but not B
# print(A-B)
# print(B-A)
# print(A.difference(B))
# print(B.difference(A))

# Symmetric difference - elements that belong to exactly one of 2 sets but not both
# print(A^B)
# print(A.symmetric_difference(B))

# Set methods for mathematical operations
# Non - Mutating version
# A.union(B)
# A.intersection(B)
# A.difference(B)
# A.symmetric_difference(B)
# these all returns a new set

# Mutating version
# A.update(B)
# A.intersection_update(B)
# A.difference_update(B)
# A.symmetric_difference_update(B)
# these modifies the first set

# A = {1, 2, 3}
# B = {2, 3, 4}
# A.update(B)
# print(A)


# A.intersection_update(B)
# print(A)


# A.difference_update(B)
# print(A)
# B.difference_update(A)
# print(B)


# A.symmetric_difference_update(B)
# print(A)


# A = {1,2}
# B = {1,2,3,4}

# Subset - A set A is a subset of B if every element of A is also present in B.
# print(A <= B)
# print(A.issubset(B))

# proper subset - every ele of A is in B, A and B are not equal
# print(A < B) # True
# A = {1,2}
# B = {1,2}
# print(A < B) # False becoz both are equal

# Super set - A is a superset of B when A contains every element of B
# print(A.issuperset(B))
# print(A >= B)

# Proper Superset - every ele of A is in B, and A has atleast one extra ele that B does not have
# print(A > B)


# Disjoints - two sets are disjoints when they have no common elements
# print(A.isdisjoint(B))


# # equality of sets - 2 sets are equal if they contain same elements, order does not matter
# A = {1,2,3}
# B = {3,1,2}
# print(A == B)

# inequality of sets -  2 sets are not equal if they dont contain same elements
# A  = {1,2,3}
# B  = {1,2,4}
# print(A != B)


# Set comprehensions
# square = {x*x for x in range(6)}
# print(square)
# print(type(square))

# set comprehension with conditions
# even_num = {x for x in range(1,11) if x % 2 == 0}
# print(even_num)


# Set unpacking
# s = {10,20,30}
# a,b,c = s
# print(a)

# s1 = {10,20,30,40,50}
# a,*b,c = s1
# print(b)
# print(a)
# print(c)


# Set - copy()
# a = {1,2,3}
# b = a.copy()
# b.add(4)
# print(a)
# print(b)


# frozenset - immutable version of set
# s = {1,2}
# fs = frozenset(s)
# print(fs)
# print(type(fs))

# d = {
#     frozenset({1,2,3}) : "group"
# }
# print(d)
# print(type(d))


# frozen set operations
# A.union(B) - |
# A.intersection(B) - &
# A.difference(B) - (-)
# A.symmetric_difference(B) - ^


# set and functions
# def find_common(a,b):
#     return a & b
# res = find_common({1,2,3,4},{3,4,5,6})
# print(res)


# set + strings
# letter = "programming"
# unique = set(letter)
# count = len(unique)
# print(count)
# print(unique)


# set + lists
# num = [1,2,3,4,5,6,1,2,3,1,2,3,4,5,3,4,5,4,2,2,1,2,3]
# unique_num = set(num)
# print(unique_num)

# duplicate detection pattern
# num = [1,2,3,4,1,2,3,4,1,4,3,5,6,2,3,4,5,2,6,2,1,4,3,2,5,5,6,6,3,1]
# print(len(num))
# res = len(set(num))
# print(res)
# duplicates are present


# Create a set.
# s = set()
# s1 = {1,2,3,4,5}
# print(s)
# print(type(s))
# print(s1)
# print(type(s1))


# Add an element
# s = set()
# s.add(10)
# s.update([10,20,30,40])
# print(s)

# Remove an element.
# s = {10,20,30,40}
# s.remove(20)
# print(s)
# s.discard(31)
# print(s)

# Check whether an element exists.
# s = {10,20,30,40}
# print(10 in s)
# print(11 in s)
# print(15 not in s)
# print(30 not in s)

# Find the number of unique elements.
# s = {10,20,30,40,20,30,10,20}
# print(len(s))

# Remove duplicates from a list.
# s = {10,20,30,40,20,30,10,20}
# print(s)

# Find whether a list contains duplicates.
# s = [10,20,30,40,20,30,10,20]
# print(len(s))
# res = len(set(s))
# print(res)
# duplicates are present


# Find common elements between two lists.
# A = {1,2,3,4}
# B = {3,4,5,6}
# print(A.intersection(B))
# print(A & B)

# Find elements present only in the first list.
# A = {1,2,3,4}
# B = {3,4,5,6}
# print(A - B)
# print(A.difference(B))


# Find elements present only in the second list.
# A = {1,2,3,4}
# B = {3,4,5,6}
# print(B - A)
# print(B.difference(A))

# Find elements occurring in exactly one list.
# A = {1,2,3,4}
# B = {3,4,5,6}
# print(A.symmetric_difference(B))

# # Find unique characters in a string.
# s = set("programming")
# print(s)


# Count unique characters.
# s = set("programming")
# print(len(s))

# Check whether two strings contain the same unique characters.
# s = set("programming")
# s1 = set("python programming")
# print(s == s1)

# Check whether one list's unique elements are contained in another.
# s = set("programming")
# s1 = set("python programming")
# print(s.issubset(s1))

# Find duplicate values in a list.
# s = [9,2,3,5,3,1,4,6,8,7,5,6,5,7,1,2,3,4,5,6,7,1,3,2,4,1,7,5,6,2,1]
# print(set(s))

# Find values occurring in both datasets.
# s = {1,2,3,4}
# s1 = {3,4,5,6}
# print(s & s1)
# print(s.intersection(s1))

# Find values occurring in exactly one dataset.
# s = {1,2,3,4}
# s1 = {3,4,5,6}
# print(s.symmetric_difference(s1))

# Determine whether two lists are disjoint.
# s = [1,2,3,4]
# s1 = [3,4,5,6]
# a = set(s)
# b = set(s1)
# print(a.isdisjoint(b))

# Determine whether one collection is a subset of another.
# s = {1,2,3,4}
# s1 = {3,4,5,6}
# print(s.issubset(s1))

# Find missing elements using set difference
# s = {1,2,3,4}
# s1 = {3,4,5,6}
# print(s.difference(s1))


# Find common elements among multiple collections.
# s = {1,2,3,4}
# s1 = {3,4,5,6}
# print(s.intersection(s1))

#---------------------------------------------------------------------------------------------------------------------------

# Create a set containing:
# 10, 20, 30, 40, 50
# Print the set and its type.

# s = {10,20,30,40,50}
# print(s)
# print(type(s))



# What will be the final value of numbers?
# numbers = {10, 20, 10, 30, 20, 40, 30}
# Then write a program to print the number of unique elements.

# numbers = {10, 20, 10, 30, 20, 40, 30}
# print(numbers)

# numbers = [10, 20, 10, 30, 20, 40, 30]
# l1 = []
# for i in numbers:
#     count = 0

#     for j in numbers:
#         if i == j:
#             count += 1

#     if count == 1:
#         l1.append(i)
# print(set(l1))



# Create:
# An empty dictionary
# An empty set
# Print their types and explain the difference
# s = set()
# d = {}
# print(s)
# print(type(s))
# print(d)
# print(type(d))


# languages = {"Python", "Java", "C++", "JavaScript"}
# Write a program that checks whether:
# "Python" exists
# "Ruby" exists
# Your output should clearly indicate the result.


# languages = {"Python", "Java", "C++", "JavaScript"}
# a = input("Enter a programming language: ")
# if a in languages:
#     print(f"{a} exists")
# else:
#     print(f"{a} not exists")



# numbers = {10, 20, 30}
# Add 40 and then 50 to the set using the appropriate method.
# Print the final set.

# numbers = {10, 20, 30}
# numbers.add(40)
# print(numbers)
# numbers.add(50)
# print(numbers)


# A = {1, 2}
# A.add("Python")
# print(A)

# B = {1, 2}
# B.update("Python","Pes")
# print(B)



# numbers = {10, 20, 30, 40, 50}
# Remove 30.
# Then attempt to remove 100.
# Do this once using remove() and once using discard().
# Explain the behavioral difference.
# numbers = {10, 20, 30, 40, 50}
# numbers.remove(30)
# print(numbers)

# numbers.remove(100)
# numbers.discard(100)


# numbers = {5, 10, 15, 20, 25}
# Write a for loop that prints every element.
# Then explain why you should not write logic that depends on which element is printed first.

# numbers = {5, 10, 15, 20, 25}
# for i in numbers:
#     print(i)



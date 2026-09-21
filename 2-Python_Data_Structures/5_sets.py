# Python Sets
# Set is a built in python data type used to store a collection of unique items
# 1. Stores only unique elements, duplicates values are automatically removed.
# 2. Unordered collection, so elements do not have a fixed position and cannot be accessed using indexes
# 3. Supports fast search, insertion and deletion operations using hashing internally

s = {1000,50,20}
print(s)
print(id(1))
print(type(s))

# Type casting : set() method is used to convert other datatypes such as lists or tuples into sets
s = set(["a","b","c"])
print(s)

# check unique and immutability
# sets cannot have duplicate values. while you cannot modify the individual elements directly, but still can add or remove elements
s = {"Hello","World","Hello"}
print(s)
#s[1] = "Hi"
#print(s)

# Heterogeneous Element
# sets can store heterogeneous elements in it. a set can store a mixture of str,int,bool etc datatypes

s = {"Hello",1 ,2.6,True,3+5j}
print(s)

# Frozen Sets: an immutable version of a set. its elements cannot be changed after creation, but can perform operations like union, interaction
# and difference. frozenset()
s = set(["a","b","c"])
print("Norma set : ",s)
fs = frozenset(["e","f","g"])
print("Frozen set : ",fs)


# Internal Working of set
# Python sets are implemented using a hash table, similar to dictionaries, where the set elements are stored as keys with dummy values.
# If multiple elements map to the same index, Python handles the collision by storing them in the same bucket.
# Each index in the hash table represents a possible hash value where elements are stored based on their computed hash key.
# When two elements map to the same index, they are linked together using a linked list, forming a chain at that position.
# This chaining mechanism helps efficiently handle collisions, allowing multiple elements to exist at the same hash index without overwriting each other.


# Set Methods : Python set methods are built-in functions used to add, remove, update and perform other operations on sets.
# These methods help manage and manipulate set elements efficiently.

# 1. add() : adds an element to the set
s = {1,2,3}
s.add(4)
print(s)

# 2. clear() : removes all elements from the set
s = {1,2,3}
s.clear()
print(s)

# 3. copy() : returns a shallow copy of the set
s = {1,2,3}
c = s.copy()
print(c)

# 4. difference() or '-': returns a set containig elements present in the first set but not in the second set
a = {1,2,3,4,5}
b = {4,5,6}
print(a.difference(b))

# 5. difference_update() : removes common elements from the original set
a = {1,2,3,4,5}
b = {4,5,6}
a.difference_update(b)
print(a)

# 6. discard() : removes an element from the set if it exists
s = {1,2,3}
s.discard(2)
print(s)

# 7. frozenset(): creates an immutable version of set
s = frozenset([1,2,3])
print(s)

# 8. intersection() or '&'operator: returns common elements from 2 or more sets
a = {1,2,3}
b = {2,3,4}
print(a.intersection(b))

# 9. intersection_update(): updates the set with only the elements that are common to both sets
a = {1,2,3}
b = {2,3,4}
a.intersection_update(b)
print(a)

# 10. isdisjoint(): returns True if 2 sets have no common elements
a = {1,2}
b = {3,4}
print(a.isdisjoint(b))

# 11. issubset(): returns True if all elements of one set are present in another set
a = {1,2}
b = {1,2,3,4}
print(a.issubset(b))

# 12. issuperset(): returns True if a set contains all elements of another set.
a = {1,2,3,4}
b = {1,2}
print(a.issuperset(b))

# 13. pop(): removes and returns a random element from the set
s = {1,2,3}
print(s.pop())
print(s)

# 14. remove(): removes the specified element from the set
s = {1,2,3}
s.remove(2)
print(s)

# 15. symmetric_difference() or '^' operator: returns elements that are present in either set but not in both
a = {1,2,3}
b = {3,4,5}
print(a.symmetric_difference(b))

# 16. symmetric_difference_update(): updates the set with symmetric difference of 2 sets
a = {1,2,3}
b = {3,4,5}
a.symmetric_difference_update(b)
print(a)

# 17. union() or '|'operator : returns a new set containing all unique elements from the sets
a = {1,2,3}
b = {3,4,5}
print(a.union(b))

# 18. update(): adds all elements from another iterable to the set
a = {1,2}
b = {3,4}
a.update(b)
print(a)


# Operators for Sets
# Operators	             Notes
# key in s	         containment check
# key not in s	     non-containment check
# s1 == s2	         s1 is equivalent to s2
# s1 != s2	         s1 is not equivalent to s2
# s1 <= s2	         s1 is subset of s2
# s1 < s2	         s1 is proper subset of s2
# s1 >= s2	         s1 is superset of s2
# s1 > s2	         s1 is proper superset of s2
# s1 | s2	         the union of s1 and s2
# s1 & s2	         the intersection of s1 and s2
# s1 - s2	         the set of elements in s1 but not s2
# s1 ^ s2	         the set of elements in precisely one of s1 or s2
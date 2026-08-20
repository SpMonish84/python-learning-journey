# operators practise codes


# # Q1
# operator are used to used to perform operation on operands and values
# operand the variable values which are used to perform operation are operands
# ex: a = 5, b = 10 , c = a + b, in which a and b are operands and + is the operator

# # Q2
# 10/3 - it does division, but returns the output in floating values
# 10//3 - it also does division, but returns the output in integer values

# # Q3
# % - it is used to return the remainder
# used in programs like finding even odd number and leap year


# # Q4
# x = 10 - the value 10 is assigned to the variable x
# = is a assignment operator used to assign values 

# x == 10 - here the operator is equalto, checking equality of x and 10
# == is a comparison/relational operator, used to check if both values are equal or not


# # Q5
# False - because the logical and if both are True then its true, if both are false its false, if any one is true or false its always false
# True - beacuse in the logical or if both are True its true, if both are false its false and, if any one is true or false its always true
# False - because in the logical not its the opposite , if true its false, if false its True


# # Q6
# & - its bitwise and operator it calculates using the bits
# and - its logical and it returns values in either true or false
# no they are not interchangeable because both are totaly different type of operators each of them has thier own rules and calculations

# # Q7
# 10 & 6
# D -> B 
# 10 - 1010
# 6  - 0110
# bitwise operation
# 1&1 = 1
# 1&0 = 0
# 0&1 = 0
# 0&0 = 0
# so result of 1010&0110 is 0010
# B -> D 
# 0010 = 2


# # Q8
# 10^6
# D -> B
# 10 - 1010
# 6  - 0110
# bitwise operation
# 1&1 = 0
# 1&0 = 1
# 0&1 = 1
# 0&0 = 0
# so result of 1010^0110 is 1100
# B -> D
# 1100 = 12


# # Q9
# ~5
# i use the bitwise not formula for this and solve it
# ~n = -(n+1)
# so, ~5 = -(5+1)
# ~5 = -6
# In Python, the bitwise NOT operator ~ flips all the bits of a number. However, Python integers are stored using two’s complement representation, which is the standard way computers represent signed integers.
# Because of this, the result of ~n is mathematically defined as: ~n = -(n+1)



# # Q10
# ==  - is a relational operator called equal to is used to check if operands are equal or not in a expression,it returns true if both values are same, ele false
# is - is a identity operator is used to check if both variables are referencing the same object in the memory it returns true if both are same, else false

# # Q11
# in - is a membership operator which is used to find element, it returns true if present else false
# not in - is also a membership operator which works opposite to in operator, it returns true if element is not present
# ex: name = "Python" 
# print(P in name) - returns True
# print(0 not in name) - returns True

# # Q12
# x = x + 5 and x += 5
# both are equvivalent for the integer case


# # Q13
# 3.75
# 3
# 3
# 225

# # Q14
# 15
# 20
# 6

# # Q15
# False
# True
# True
# True

# # Q16
# True
# False
# False

# # Q17
# 12 & 10
# 12 - 1100
# 10 - 1010
# ----------
#      1000
# = 8

# 12 | 10 
# 12 - 1100
# 10 - 1010
# ---------
#      1110
# = 14

# 12 ^ 10
# 12 - 1100
# 10 - 1010
# ---------
#      0110
# = 6

# # Q18
# a == b is True because it checks the equality of the object and both variable are refrencing to the same object [1,2,3]
# a is b is false beacuse initialy the x is referenced to [1,2,3] and after that b references to the same object as a
# a == c is True because it checks the equality of the object
# a is c is True because both the a and c are referencing to the same object on the memory


# # Q19
# True
# False
# True
# False

# # Q20

# 7<<2
# 7 - 0111
# shift left side 2 bits
#   0111
# 011100

# = 28

# 7 ^ 5
# 7 - 0111
# 5 - 0101
# --------
#     0010
# = 2

# 7&30
# 7  - 00111
# 30 - 11110
# ----------
#      00110
# = 6

# # Q21
# num1 = int(input("Enter the 1st number: "))
# num2 = int(input("Enter the 2nd number: "))
# total_sum = num1 + num2
# sub = num1 - num2
# mul = num1 * num2
# div = num1 / num2
# floor_div = num1 // num2
# mod = num1 % num2
# expo = num1 ** num2
# print("Addition:", total_sum)
# print("Subtraction:", sub)
# print("Multiplication:", mul)
# print("Division:", div)
# print("Floor division:", floor_div)
# print("Modulu:", mod)
# print("Exponentiation:", expo)


# # Q22
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")

# # Q23
# num = int(input("Enter a number: "))
# if num % 5 == 0 and num % 10 == 0:
#     print("Divisible by both 5 and 10")
# else:
#     print("Not Divisible by both 5 and 10")


# # Q24
# str = input("Enter a word: ")
# if ("a" in str or "z" not in str):
#     print("Exits in the entered string")
# else:
#     print("does not exist")


# # Q25
# list_a = [1,2,3]
# list_b = list_a
# list_c = [1,2,3]

# print(list_a == list_b)
# print(list_a is list_b)
# print(list_a == list_c)
# print(list_a is list_c)

# # Q26
# num1 = int(input("Enter the 1st number: "))
# num2 = int(input("Enter the 2nd number: "))
# bit_and = num1 & num2
# bit_or = num1 | num2
# bit_xor = num1 ^ num2
# print("Bitwise and:", bit_and)
# print("Bitwise or", bit_or)
# print("Bitwise xor", bit_xor)

# ex : num1 = 12, num2 = 15
# &  -> 12 = 1100
#       15 = 1111
# ---------------
#            1100
# = 12

# |  -> 12 = 1100
#       15 = 1111
# ---------------
#            1111
# = 15

# ^  -> 12 = 1100
#       15 = 1111
# ---------------
#            0011
# = 3

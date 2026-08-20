# Operators -  Operators in general are used to perform operations on values and variables.

# #Types of Operators in Python
# 1. Arithmetic Operators
# 2. Comparison Operators
# 3. Logical Operators
# 4. Bitwise Operators
# 5. Assignment Operators
# 6. Identity Operators
# 7. Membership Operators
# 8. Ternary Operator

print("\n")
print("Arithmetic Operators")
#Arithmetic Operators - are used to perform basic mathematical operations like addition, subtraction, multiplication and division.
a = 5
b = 3
#Adds two values
print("Addition : ",a+b)

# Subtracts one value from another
print("Subtraction : ",a-b)

#Multiplies two values
print("Multiply : ",a*b)

#Divides and returns a float value
print("Division : ", a/b)

#Divides and returns the integer value
print("Floor Division : ",a//b)

#Returns the remainder after division
print("Modulus : ",a%b)

#Raises a number to the power of another
print("Exponential : ",a**b)


print("\n")
print("Comparison Operators")
#Comparison Operators - Comparison(or Relational) operators compares values. It either returns True or False according to the condition.
a = 10
b = 5
# Greater than
print(a > b)

# Less than
print(a < b)

# Equal to 
print(a == b)

# Not equal to
print(a !=b )

# Greater than equal to
print(a >= b)

# Less than equal to
print(a <= b)



print("\n")
print("Logical Operators")
# Logical Operators - perform Logical AND, Logical OR and Logical NOT operations. 
# It is used to combine conditional statements.
a = True
b = False
print(a and b)
print(a or b)
print(not a)
print(not b)




print("\n")
print("Bitwise Operators")
#Bitwise Operators - act on bits and perform bit-by-bit operations. These are used to operate on binary numbers.
a = 7
b = 13

#Bitwise AND Operator - Convert Decimal to Binary and calculate it 
# 1&1=1, 1&0,0&1=0, 0&0=0
print(a & b)
#Bitwise OR Operator - Convert Decimal to Binary and calculate it 
# 1|1=1, 1|0,0|1=1, 0|0=0
print(a | b)
#Bitwise XOR Operator - Convert Decimal to Binary and calculate it 
# 1^1=0, 1^0,0^1=1, 0^0=0
print(a ^ b)
#Bitwise NOT Operator - Convert Decimal to Binary and calculate it 
# formula (~n = -(n+1))
print(~a)
#Bitwise Left Shift - Convert Decimal to Binary and calculate it 
# formula (n<<k = nx2^k)
print(a << b)
#Bitwise Right Shift - Convert Decimal to Binary and calculate it 
# formula (n>>k = n//2^k)
print(a >> b)



print("\n")
print("Assignment Operators")
# Assignment Operators -  are used to assign values to the variables. This operator is used to assign the value of the right side of the expression to the left side operand.
a = 3
b = 5
# Addition Assignment Operator - The Addition Assignment Operator is used to add the right-hand side operand with the left-hand side operand and then assigning the result to the left operand.
a += b # a = a + b 
print(a) 
# Subtraction Assignment Operator - The Subtraction Assignment Operator is used to subtract the right-hand side operand from the left-hand side operand and then assigning the result to the left-hand side operand.
a -= b # a = a - b
print(a)
# Multiplication Assignment Operator - The Multiplication Assignment Operator is used to multiply the right-hand side operand with the left-hand side operand and then assigning the result to the left-hand side operand.
a *= b # a = a * b
print(a)
# Division Assignment Operator - The Division Assignment Operator is used to divide the left-hand side operand with the right-hand side operand and then assigning the result to the left operand.
a /= b # a = a / b
print(a)
# Modulus Assignment Operator - The Modulus Assignment Operator is used to take the modulus, that is, it first divides the operands and then takes the remainder and assigns it to the left operand.
a %= b # a = a % b
print(a)
# Floor Division Assignment Operator - The Floor Division Assignment Operator is used to divide the left operand with the right operand and then assigs the result(floor value) to the left operand.
a //= b # a = a // b
print(a)
# Exponentiation Assignment Operator - The Exponentiation Assignment Operator is used to calculate the exponent(raise power) value using operands and then assigning the result to the left operand.
a **= b # a = a ** b
print(a)
# Bitwise AND Assignment Operator - The Bitwise AND Assignment Operator is used to perform Bitwise AND operation on both operands and then assigning the result to the left operand.
a , b = 10 , 20
a &= b # a =  a & b
print(a)
# Bitwise OR Assignment Operator - The Bitwise OR Assignment Operator is used to perform Bitwise OR operation on the operands and then assigning result to the left operand.
a |= b # a = a | b
print(a)
# Bitwise XOR Assignment Operator - The Bitwise XOR Assignment Operator is used to perform Bitwise XOR operation on the operands and then assigning result to the left operand.
a ^= b # a = a ^ b
print (a)
# Bitwise Right Shift Assignment Operator - The Bitwise Right Shift Assignment Operator is used to perform Bitwise Right Shift Operation on the operands and then assign result to the left operand.
a >>= b # a = a >> b
print(a)
# Bitwise Left Shift Assignment Operator - The Bitwise Left Shift Assignment Operator is used to perform Bitwise Left Shift Opertator on the operands and then assign result to the left operand.
a <<= b # a = a << b
print(a)
#Walrus Operator (variable := expression) -  allows you to assign a value to a variable as part of an expression. It helps avoid redundant code when a value needs to be both used and tested in the same expression — especially in loops or conditional statements.
a = True
print(a := False)



print("\n")
print("Identity Operators")
# # Identity Operators - "is" and "is not" are the identity operators and both are used to check if two values are located on the same part of the memory. Two variables that are equal do not imply that they are identical. 
# is   - True if the operands are identical 
# is not - True if the operands are not identical 
a = 10
b = 10
x, y = "hello","hello"
m = [1,2,3]
n = [1,2,3]

# # # IS Operator - The "is" operator checks if two variables point to the same object (same memory location).
print(a is b)
print(x is y)
print(m is n)

# # IS NOT Operator - The "is not" operator checks if two variables point to different objects.
print(a is not b)
print(x is not y)
print(m is not n)




print("\n")
print("Membership Operators")
# Membership Operators - "in" and "not in" are the membership operators that are used to test whether a value or variable is in a sequence.
# in     - True if value is found in the sequence
# not in - True if value is not found in the sequence
a = [1,2,3,4,5]
b = "Python"
c = {1: "virat",2: "abd",3: "gayle"} 

# IN Operator - The "in" operator returns True if the given element exists inside a sequence, otherwise it returns False.
print(0 in a)
print("P" in b)
print(2 in c)
print("virot" in c.values()) 
print(any("z" in value for value in c.values()))
print("\n") 
# NOT IN Operator - The "not in" operator works the opposite of "in" operator, it returns True if the element is not found in a sequence.
print(0 not in a)
print("P" not in b)
print(2 not in c)
print("virot" not in c.values()) 
print(any("a" not in value for value in c.values())) 




print("\n")
print("Ternary Operator")
# Ternary Operator - Ternary operators also known as conditional expressions are operators that evaluate something based on a condition being true or false.
# Syntax :  [on_true] if [expression] else [on_false] 
n = 3
res = "even" if n % 2 == 0 else "odd"
print(res)
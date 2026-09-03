# loop and loop control statements

# # Write a program to print numbers from 1 to 10 using a while loop.
# count = 1 
# while count <= 10:
#     print(count)
#     count += 1


# # Print numbers from 10 to 1 using a while loop.
# count = 10
# while count >= 1:
#     print(count)
#     count -= 1


# # Print all even numbers from 1 to 20.
# c = 1 
# while c <= 20:
#     if c % 2 == 0:
#         print(c)
#     c += 1


# # Print all odd numbers from 1 to 20.
# c = 1
# while c <= 20:
#     if c % 2 != 0:
#         print(c)
#     c += 1

# # Take a number from the user and print its multiplication table from 1 to 10.
# num = int(input("Enter a number: "))
# count = 1
# while count <= 10:
#     print(num,"x",count,"=",num*count)
#     count += 1


# # Take N from the user and find the sum of numbers from 1 to N.
# n = int(input("Enter value of n: "))
# count = 1
# sum = 0
# while count <= n:
#     sum += count
#     count += 1
# print("sum of numbers from 1 to", n, "is:", sum)

# Take N from the user and find the sum of all even numbers from 1 to N.
# n = int(input("Enter value of n: "))
# count = 1
# total = 0
# while count <= n:
#     if count % 2 == 0:
#         total += count
#     count += 1
# print("sum of even numbers from 1 to", n, "is:", total)


# 1.Check positive/negative/zero
# int input - num
# check if num greater than zero print positive
# check if num less than zero print negative
# else print zero
# num = int(input("Enter a number: "))
# if (num > 0):
#     print("Positive")
# elif (num < 0):
#     print("Negative")
# else:
#     print("Zero")

# Positive even
# int input num, check whether the entered number is greater than zero
# if yes its a positive number, else: enter a valid positive number,
# next check if number divided by 2 and its remainder is zero, if yes its a positive even number,
# else its not a positive even number

# num = int(input("Enter a number: "))
# if (num >= 0 ):
#     if(num % 2 == 0):
#         print("Positive Even number")
#     else:
#         print("Not a Positive Even number")
# else:
#     print("Enter a valid positive number")

# Positive odd
# num = int(input("Enter a number: "))
# if (num > 0 ):
#     if(num % 2 != 0):
#         print("Positive Odd number")
#     else:
#         print("Not a Odd number")
# else:
#     print("Enter a valid positive number")

# Negative even
# step1: int input num
# step2: check if entered num is less than zero, if yes continue to next condition
# step3: check if num divided by 2 and remainder is equal to 0, if yes print negative even number, else: not a negative even number
# step4: else print enter a valid negative number
# num = int(input("Enter a number: "))
# if num < 0:
#     if num % 2 == 0:
#         print("Negative even number")
#     else:
#         print("Not a Negative even number")
# else:
#     print("Enter a valid negative number")


# Negative odd
# num = int(input("Enter a number: "))
# if num < 0:
#     if num % 2 != 0:
#         print("Negative Odd number")
#     else:
#         print("Not a Negative Odd number")
# else:
#     print("Enter a valid negative number")


# Positive and divisible by 5
# step1: int input num
# step2: check if entered number is greater than zero, if yes: continue to next conditon, if no: enter a valid positive number
# step3: check if number is divided by 5 and remainder is eqal to zero, if yes: print positive and divisible by 5, else not divisible by 5
# num = int(input("Enter a number: "))
# if num > 0:
#     if num % 5 == 0:
#         print("Positive and divisible by 5")
#     else:
#         print("Not divisible by 5")
# else:
#     print("Enter a valid positive number")


# Positive and divisible by both 3 and 5
# step1: int input num
# step2: check if enterd number is greater than zero, if yes: move to next condtion, if no: enter a valid positive number
# step3: check if number divisible by 3 and 5, if yes: print divsible by 3 and 5, if no: print not divisible by 3 and 5.

# num = int(input("Enter a number: "))
# if num > 0:
#     if num % 3 == 0 and num % 5 == 0:
#         print("Positive, Divisible by both 3 and 5")
#     elif num % 3 == 0:
#         print("Positive, Divisible by 3 but not 5")
#     elif num % 5 == 0:
#         print("Positive, Divisible by 5 but not 3")
#     else:
#         print("Positive, Not divisible by both 3 and 5")
# else:
#     print("Enter a valid positive number")



# 2. Check even/odd without %
# a. with floor division and multiplication
# num = int(input("Enter a number: "))
# if (num // 2)*2 == num:
#     print("Even")
# else:
#     print("Odd")
# b. with bitwise and
# num = int(input("Enter a number: "))
# if (num & 1 == 0):
#     print("Even")
# elif (num & 1 == 1):
#     print("Odd")


# Check multiple numbers
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# if num1 % num2 == 0:
#     print("first number is divisible by second number")
# else:
#     print("first number is not divisible by second number")

# multiple divisors
# num1 = int(input("Enter first number: "))
# num2 = list(map(int, input("Enter multiple numbers to check divisibility: ").split()))

# for num in num2:
#     if num1 % num == 0:
#         print("divisible")
#     else:
#         print("not divisible")


# Count how many even numbers are present
# step1: int input in the form of list 
# step2: iterate through the list using for loop to get all the items in list
# step3: check if numbers in the list is even by, if num divided by 2 and remainder is equal to zero its even else false,
# step4: print the count of even numbers and what are the even numbers
# l1 = list(map(int, input("Enter the numbers: ").split()))
# l2 = []
# count = 0
# for i in l1:
#     if i % 2 == 0:
#         l2.append(i)
#         count += 1
# print("count:", count,"and the numbers are:",l2)


# # Find sum of even numbers
# l1 = list(map(int,input("Enter first number: ").split()))
# total = 0
# for i in l1:
#     if i % 2 == 0:
#         print(i)
#         total += i
# print("sum of even numbers in list:",total)


# Find sum of odd numbers
# l1 = list(map(int, input("Enter the numbers: ").split()))
# total = 0
# for i in l1:
#     if i % 2 != 0:
#         print(i)
#         total += i
# print("sum of odd numbers:", total)

# # Find largest even number
# step1: int input in the form of a list l1
# step2: initialize a empty list l2
# step3: iterate through the list l1 to access all the elements
# step4: check for condition if the numbers in list is even, if even update the even numbers in the list l2 else skip the not even numbers
# step5: initialize a variable largest assigning first element as largest even number in list l2,  now iterate through the list l2 to access all the elements
# step6: now check for the greatest even number by checking with each element and update 
# step7: print the largest even number
# l1 = list(map(int, input("Enter the numbers: ").split()))
# l2 = []
# for i in l1:
#     if i % 2 == 0:
#         print(i)
#         l2.append(i)
# largest = l2[0]
# for i in l2:
#     if i > largest:
#         largest = i
# print("largest even number:", largest)


# # Find smallest odd number
# l1 = list(map(int, input("Enter the numbers: ").split()))
# l2 = []
# for i in l1:
#     if i % 2 != 0:
#         print(i)
#         l2.append(i)
# smallest = l2[0]
# for i in l2:
#     if i < smallest:
#         smallest = i
# print("smallest odd number:", smallest)


# Largest of 2 numbers
# step1: int input num1 and num2
# step2: check that if the num1 is greater than num2
# step3: print num1 is greater, else num2 is greater
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# if num1 > num2:
#     print("first number is greater")
# else:
#     print("second number is greater")


# Largest of 3 numbers
# step1: int input num1,num2,num3
# step2:check if num1 greater than num2 and num3, if yes print num1 is greater else move to next condition
# step4: check if num2 greater than num1 and num3, if yes print num2 is greater else move to next condtion
# step4: print num3 is greater

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))

# if num1 >= num2 and num1 >= num3:
#     print("first number is greater")
# elif num2 >= num1 and num2 >= num3:
#     print("second number is greater")
# else:
#     print("third number is greater")



# Largest odd number
# l1 = list(map(int, input("Enter first number: ").split()))
# l2 = []
# for i in l1:
#     if i % 2 != 0:
#         print(i)
#         l2.append(i)
# largest = l2[0]
# for i in l2:
#     if i > largest:
#         largest = i
# print("Largest odd number: ", largest)



# Second largest number
# l1 = list(map(int, input("Enter first number: ").split()))
# s1 = (sorted(l1, reverse = True))
# print(s1)
# print("Second largest number:", s1[1])

# Third largest number
# l1 = list(map(int, input("Enter numbers: ").split()))
# unique_numbers = list(set(l1))
# unique_numbers.sort(reverse=True)
# print(unique_numbers)

# if len(unique_numbers) >= 3:
#     print("Third largest number:", unique_numbers[2])
# else:
#     print("There is no third largest number (not enough distinct values).")


# # Smallest of 2
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# if num1 < num2:
#     print("first number is smallest")
# elif num1 == num2:
#     print("Both are equal")
# else:
#     print("second number is smallest")

# # Smallest of 3
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))

# if num1 == num2 == num3:
#     print("all the numbers are equal")
# elif num1 <= num2 and num1 <= num3:
#     print("first number is smallest")
# elif num2 <= num1 and num2 <= num3:
#     print("second number is smallest")
# else:
#     print("third number is smallest")


# Smallest among n
# l1 = list(map(int, input("Enter the n numbers: ").split()))
# smallest = l1[0]
# for i in l1:
#     if i < smallest:
#         smallest = i
# print("Smallest among n numbers:", smallest)

# using sorting
# l1 = list(map(int, input("Enter the n numbers: ").split()))
# l2 = sorted(l1)
# print(l2)
# print("Smallest:", l2[0])




# Smallest even number
# l1 = list(map(int, input("Enter the n numbers: ").split()))
# l2 = []
# for i in l1:
#     if i % 2 ==0:
#         print(i)
#         l2.append(i)

# smallest = l2[0]
# for i in l2:
#     if i < smallest:
#         smallest = i
# print("smallest even number:", smallest)




# Smallest odd number
# l1 = list(map(int, input("Enter the n numbers: ").split()))
# l2 = []
# for i in l1:
#     if i % 2 !=0:
#         print(i)
#         l2.append(i)

# smallest = l2[0]
# for i in l2:
#     if i < smallest:
#         smallest = i

# print("smallest odd number:", smallest)

# second smallest
# l1 = list(map(int, input("Enter the n numbers: ").split()))
# l2 = sorted(l1)
# print(l2)
# print("Second Smallest:", l2[1])

# largest digit in a number
# num = int(input("Enter the number: "))
# digit = str(num)
# largest_digit = int(digit[0])
# for char in digit:
#     if int(char) > largest_digit:
#         largest_digit = int(char)

# print("largest digit:", largest_digit)
# print(type(largest_digit))




# Count factors

# step1: input int num
# step2: create a empty list l1 and a count variable to count how many factors are prsesnt
# step3: iterate through the num from 1 to num+1 using range to find the factors move to next condition
# step4: check condition if num divided by the numbers present in between 1 and num+1 and if the remainder is equal to zero update the number in the empty list
# step5: print the factors of num in the empty list
# step6: print the count of how many factors for the num.

# num = int(input("Enter the number to find its factors: "))
# l1 = []
# count = 0
# if(num > 0 and num!= 0):
#     for i in range(1, num + 1):
#         if (num % i == 0):
#             l1.append(i)
# # without built in func to find the elements in sequence
# # for i in l1:
# #     count += 1
# # print(count)
# print("Factors of",num,"are:", l1,"and the count is:", len(l1))


# Sum of factors

# Sum of factors
# step1: int input num
# step2: create a empty list to store the factors of num, count variable to count the factors of num and total variable to store the sum of the factors of num
# step3: iterate through the num using range from 1 to num+1 to find the factors
# step4: check condition if num divided by numbers between num and num+1, if the remainder is equal to zero update the factors in the empty list
# step5: print the updated list with the count of factors of num
# step6: print the total, sum of factors of num

# num = int(input("Enter the number to find its factors: "))
# l1 = []
# total = 0

# if(num > 0):
#     for i in range(1, num + 1):
#         if num % i == 0:
#             l1.append(i)
#     print("Factors of ",num,"are:",l1,"and the count of factors:", len(l1))
#     for i in l1:
#         total += i
#     print("sum of factors of",num,":", total)
        
# else:
#     print("Enter positive number and above zero!")



# Product of factors

# num = int(input("Enter the number to find its factors: "))
# l1 = []
# product = 1
# if(num > 0):
#     for i in range(1, num + 1):
#         if num % i == 0:
#             l1.append(i)
#     print("Factors of", num,"are:", l1, "and the count of factors are:", len(l1))
#     for i in l1:
#         product *= i
#     print("Product of factors of", num, "are:", product)
# else:
#     print("Enter number above zero!")


# Even factors
# num = int(input("Enter the number to find its factors: "))
# l1 = []
# l2 = []
# if(num > 0):
#     for i in range(1, num + 1):
#         if num % i == 0:
#             l1.append(i)
#     print("Factors of", num,"are:", l1, "and the count of factors are:", len(l1))
#     for i in l1:
#         if i % 2 == 0:
#             l2.append(i)
#     print("Even factors of", num,"are:", l2)
            
# else:
#     print("Enter number above zero!")



# # Odd Factors
# num = int(input("Enter the number to find its factors: "))
# l1 = []
# l2 = []
# if(num > 0):
#     for i in range(1, num + 1):
#         if num % i == 0:
#             l1.append(i)
#     print("Factors of", num,"are:", l1, "and the count of factors are:", len(l1))
#     for i in l1:
#         if i % 2 != 0:
#             l2.append(i)
#     print("Odd factors of", num,"are:", l2)
            
# else:
#     print("Enter number above zero!")


# Prime Factors
# num = int(input("Enter the number to find its factors and prime factors: "))
# l1 = []
# l2 = []
# if(num > 0):
#     for i in range(1, num + 1):
#         if num % i == 0:
#             l1.append(i)
#     print("Factors of", num,"are:", l1, "and the count of factors are:", len(l1))

#     for f in l1:
#         if f > 1:
#             is_prime = True
#             for j in range(2, f):
#                 if f % j == 0:
#                     is_prime = False
#                     break
#             if is_prime:
#                 l2.append(f)
#     print("prime factors of", num, "are:", l2)
# else:
#     print("Enter number above zero!")

# prime number
# num = int(input("Enter the number to find prime number or not: "))
# l1 = []
# if (num > 1):
#     for i in range(1, num + 1):
#         if num % i == 0:
#             l1.append(i)
#     if len(l1) == 2:
#         print("Prime number")
#     else:
#         print("Not a prime number")
# else:
#     print("Enter a number above 1")


# prime number
# num = int(input("Enter a number: "))
# if num > 1:
#     # assume prime until proven otherwise
#     is_prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break
    
#     if is_prime:
#         print(num, "is a Prime number")
#     else:
#         print(num, "is Not a prime number")
# else:
#     print("Enter a number greater than 1")
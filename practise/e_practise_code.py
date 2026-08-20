# # Q1
# operator precedance is a priority of the opertor,which will be executed first in a expression 
# according to the priority list
# ex : (a+b)*c in this exoression the first a+b will be executed beacuse its in parenthesis, it has the highest priority among others


# # Q2
# operator associativity is in which direction the expreseeion to be executed its either left to right ot right to left
# if there are 2 same operators are present in the expression based on the associativity the expression is solved
# ex: a**b**c in this example there are 2 same operators based on the associativity it starts from right side and  a**b after this the value will be executed with **c


# # Q3
# i will explain this with an example expression (a+b)**c/d**e in this example the precedance tells the priority
# of the operator which should be exeuted first according to precedance the a+b in parenthesis will be executed first and then the reamaning
# in this Associativity is the direction in which the expression is to be solved there are 2 exponentiation operators for this operator the direction is from right to left
# so first d**e will be solved and then the reamaining
# precendence is used when the expression has multliple operators it tells the whcih operator to be executed
# associativity is used when the expression has same operators repeating it tells in which direction the expression to be solved

# # Q4
# 10+5*2
# step1: 5*2 will be executed so it becomes 10
# step2: 10+10 will be executed so output is 20
# if we print the expression we get 20


# # Q5
# (10+5)*2
# step1: the expression in parenthesis will be executed so 10+5 = 15
# step2: then 15*2 will be executed and output is 30
# after printing we get 30 as output
# the question is different from 4 because in the 4th question there was no parenthesis so according
# to precedence we started with 5*2


# # Q6
# 20/5*2
# step1: we look into the expression and find which operator has highest priority 
# we solve the 20/5 because both the / and * has same priority if priority are same we look into the associativity
# and according to associativity we go from left to right so first 20/5 =4 and then next we solve 4*2
# step2: we solve 4*2 = 8 so when we print the output is 8

# # Q7
# 20 - 5 + 2
# step1: we solve 20-5 because both the + and - has same priority so when we look into assocoativity
# the direction is from left to right so 20-5 = 15 is solved first
# step2: we solve 15+2= 17 so when we print the output we get 17 

# # Q8
# 2**3**2
# in this the priority is same for both the operators because both are same, so we look into
# associativity in which the direction for exponentiation operator is right to left so we solve
# 3**2 = 9 first and we solve the reamining 2**9 so the output will be 512

# # Q9 
# 100/10//2
# in this the priority is same for both the operators because both are same, so we look into
# associativity in which the direction is left to right so we solve 100/10 = 10.0
# and then we solve the remaining expression 10.0//2 = 5 so the total output is 5 because the 
# floor division operator roundoffs the output

# # Q10
# 5+2*3**2
# in this expression according to the priority the exponentiation operator has highest priority
# so we solve 3**2 =9 first and if we look into remaining expression + and * the mltiplication operator 
# has highest priority so 2*9 = 18, and next 5+18 = 23
# when print the output we get 23


# # Q11

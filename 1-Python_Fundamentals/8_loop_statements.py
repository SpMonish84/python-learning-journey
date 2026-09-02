# Loops - are used to execute a block of code repeatedly until a condition is met or all items in a
# sequence are processed. The main types are For loops iterating over sequence and while loops executing code based on condition


# For Loop - used to iterate over a sequence such as list, tuple, string or range. It executes a block of code once for each item in the sequence
n = 4
for i in range(0,n):
    print(i)



# While Loop - repeatedly executes a block of code as long as the given condition remains true.when condition becomes false,
# the line immediately after the loop in program is executed
num = 0
while (num<3):
    num += 1
    print("hi")


# Infinite while loop - runs continuosly beacuse its condition is always true
# while(True):
#    print("Hello")


# Nested loops - a loop inside another loop,the inner loop executes completly for every iteration of the outer loop
for i in range(1,6):
    for j in range(i):
        print(i, end =' ')
        


# Loop control statements - are special statements that help control the execution of loops,they let us modify
# the default behaviour of the loop such as stopping it early, skipping an iteration, or doing nothing temporarily

# Break statement - is used to exit or break out of a loop immediately, before the loop has iterated through all its items 
# or reached its condition.

for i in range(5):
    if i == 3:
        break
    print(i)

i = 0
while i<5:
    if i == 3:
        break
    print(i)
    i += 1



# Continue statement -  that forces to execute the next iteration of loop while skipping the rest of code
# inside the loop for current iteration only

for i in range(5):
    if i == 3:
        continue
    print(i)



# Pass statement - is a null operation or placeholder.used when a statement is syntactically required but we dont 
# want to execute any code.it does nothing but allow us to maintain the structure of program

for i in range(5):
    if i == 3:
        pass
    print(i)
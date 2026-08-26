# Conditional Statements in Python
# Conditional statements are used to control the flow of execution in a program 
# based on specific conditions. They allow programs to execute different blocks 
# of code depending on whether a condition evaluates to True or False.


# if statement - if is used to execute a block of code only when specified condition evaluates to true
age = 20
if age >= 18:
    print("Can vote")


# if else statement - is used to execute one block of coe when the condition is True and another block when cond is False
a = 10
if a <= 12:
    print("Travel for free")
else:
    print("pay money for ticket")

# if-elif-else statement - is used to check multiple conditions in a program 
# executes a block of code when its condition is True after previous condition is False 

b = 25
if b <= 12:
    print("Child")
elif b <= 19:
    print("Teenage")
elif b <= 35:
    print("Young Adult")
else:
    print("Adult")
    

# Nested if-else statement - if-else statement placed inside another if or else block.It is used to check conditions with another condition
c = 70
is_member = True
if age >= 60:
    if is_member:
        print("30% senior discount")
    else:
        print("20% senior discount")
else:
    print("not eligible for senior discount")


# Match case statement - used to compare value against multiple patterns and execute the matching block
# of code. similar to switch case in other prog languages
num = 3
match num:
    case 1:
        print("One")
    case 2|3:
        print("Two or Three")
    case _:
        print("Other number")
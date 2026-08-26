#Immutable Objects - immutable object cannot be changed after it is created.
# list,dict,set,bytearray
name = "Python"
print(id(name))
print(name)
name = "Java"
print(id(name))
print(name)


# Mutable Objects - mutable object can be changed after it is created.
# int,float,bool,complex,str,tuple,frozenset,bytes,range,None
print("\n")
num = [10,20,30]
print(id(num))
print(num)
num.append(40)
print(id(num))
print(num)

#variable : reserved memory location 
#type of variable :
#local variable 
#global variable 

# course="python" #global variable : a variable that is declare outside the function

# def show():
#     course="django"  #local variable : a variable which is declare insdie the function
#     print(course)
    
# show()
# print(course)

# a=30
"""def show():
    v=40 
    print(v,"calling local variable inside the function")
    print(a,"calling global variable inside funciton")
    
show()


print(a,"global variable outside function")
print(v)"""

# a=20
# def show():
#     global a
#     a=a+1
#     print(a)
    
# show()

# a=[1,2,3,4,5]
# b=0
# def show(var): #var=a=[1,2,3,4,5]
#     global b
#     for i in var:
#         b+=i
        
#     print(b)

# show(a)


#nested function: a function inside another function

# def outer():
#     v=20
#     def inner():
#         nonlocal v
#         v+=1
#         print(v)
        
#     inner()
    
# outer()
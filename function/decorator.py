#decorator : it is a function that takes another function as arugment ,add(function)  and return in a nesw function without changing origon

#watch -->


# def outer(func): #show
#     def inner():
#         print("this is inner function")
#         func() #display()
        
        
#     return inner

# @outer
# def show():
#     print("this is argument function")
    
# # show()
# @outer
# def display():
#     print("this is for testing")
    
# display()



#step 1: 
# def show():
#     print("hello world")
#     return "sujan"
    
# print(show())

#step 2 : everything is object in python 
# def show():
#     print("hello")
    
# var=show
# var()

#nested function

# def outer():
#     print("this is outer function ...")
    
#     def inner():
#         print("this is inner function")
        
#     inner()
    
# outer()

#step -4 : a function can take another as argument

# def outer(func): #func=show
#     print("this is outer function ...")
    
#     def inner():
#         print("this is inner function")
#         func() #show()
        
#     inner()
    

# def show():
#     print("this is argument function")
    

# outer(show)


# 
"""def outer(func): #func=show
    print("this is outer function ...")
    
    def inner():
        print("this is inner function")
        func() #show()
        
    return inner #var
    

def show():
    print("this is argument function")
    
var=outer(show) #it assign in inner -->inner=var


var()"""

def outer(func): #func=show
    print("going to divide ...")
    
    def inner(a,b):
        if b==0:
            print("you cannot divide by zero")
            return
        func(a,b)
        
    return inner #var
    
@outer
def show(a,b):
    print(a/b)
    
show(4,2)

@outer
def display(a,b):
    print(a/b)
    
display(7,0)
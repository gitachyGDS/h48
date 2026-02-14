#argument : an argument is a value that is passed to function when we call it 

#type of argument 
# positional argument
#keyword argument
#default argument 
#arbitary argument



# positional argument
# def show(name,age):
#     print(f"my name is {name}")
#     print(f"my age is {age}")
    
# show("ram",88)

#keyword argument

# def show(name,age):
#     print(f"my name is {name}")
#     print(f"my age is {age}")
    
# show(age=99,name="sujan")

#default argument : 

# def show(name,age,school="mangala"):
#     print(f"my name is {name}")
#     print(f"my age is {age}")
#     print(f"school name is {school}")
    
# show("ram",88)

# show("syam",66,"united")

#arbitary argument  : variable-length
#positional arbitary argument : an argument prefix with a single astrisk(*)

# def show(*a):
#     print(a)
#     for i in a:
#         print(i)
    
    
# show("sujan",2,3,4,5,6,7)

def summation(*a):
    b=0
    for i in a:
        b+=i
    print(b)

summation(2,3,4,5,6,7,)

#keyword arbitary argument 


# def show(*a,**b):
#     print(a)
#     for i,j in b.items():
#         print(i,j)
    
# show(1,2,3,4,name="sujan",age=99,email="sujan@gmail.com")



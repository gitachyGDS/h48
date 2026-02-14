#list comprehension: it is used  to weite cleaner and shorter code in single line 

#avoid : deep nested,multiple condition 

#syntax : [expression for item in something]

# a=["sujan","ram","hari","dipendra"]

# op=[5,3,4,8]
# op=[]

# for i in a:
#     op.append(len(i))
    
# print(op)

# op=[len(i) for i in a]
# print(op)

#if statment inside for loop 

# sytanx: [expression for item in something if condition]

# a=["sujan","ram","hari","manoj","syam"]

# op=["sujan","syam"]
# op=[]

# for i in a:
#     if i.startswith("s"):
#         op.append(i)
        
# print(op)

# op=[i.capitalize() for i in a if i.startswith("s")]
# print(op)


#elif statemtent:

# ["true" if condition else "false" for item in something ]

a=[2,4,6,1,3,5,8]
# [even,even,even,odd,odd]

op=["even" if i%2==0 else "odd" for i in a]
print(op)
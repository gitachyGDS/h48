#loop: loop are use to repeat a instruction
#loop is programming structure that repeat a  block of code multiple time base on condition or number of iteration


#type of loop :
#for loop :
# loop which are use to repeat for pre-determine number
#it is used for sequential traversal(list,str,tuple,dict,set,range etc...)

# syntax:

'''
for item in iterable:
    block of code

'''
# friends=["sujan","ram","hari","manoj"]


# for i in friends:  #0,1,2,3
#     print("serving tea to ",i)


#sujan
#ram
#hari
#manoj



# a=(1,2,3,4,5)

# for i in a: #01234
#     print("sujan",i)

# a={
#     "name":"sujan",
#     "age":88
# }

# for i,j in a.items():
#     print(j)

#range(start,end,step)

# for i in range(10): #0,1,2,3,4---9
#     print("sujan",i)

#multiplication table using for loop

'''
2 x 1 =2
2 x 2 =4
2 x 3 =6
2 x 4 =8
2 x 5 =10
2 x 6 =12
2 x 7 =14
2 x 8 =16
2 x 9 =18
2 x 10 =20

'''

# num=int(input("Enter your multipliation number : "))
# for i in range(1,11): 
#     print(f"{num} X {i} = {num*i}")
#     # print(num,"X",i, "=",num*i)
    
    
# if statement inside for loop 

# a=["sujan","ram","hari","syam"]
# # sujan,syam
# # b=["sujan","syam"]
# b=[] #["sujan","syam"]

# for i in a: #sujan
#     if i.startswith("s"):
#         b.append(i)
        
# print(b)

# a=[1,2,3,4,5,6,7,8]
# # op=[2,4,6,8]
# op=[]

# for i in a:
#     if i%2==0:
#         op.append(i)
        
# print(op)


#loop control statement : It is used to change the flow of execution ,skip the iteration or stop excuction

#type of loop control statement 
#pass statement
#break
#continue

#pass statement : pass is null statement that is used future code 


# for i in range(10):
#     pass
    
    
# print("hello sipalaya")

#break : it is used to teminnate the loop when encounter 

# accounts=["ram","sujan","hari","syam"]

# for i in accounts:
#     if i == "sujan":
#         print("your account is available ")
#         break

# for i in range(10):
#     print(i)
#     if i== 5:
#         break

#continue :it is used to stop the current iteration and pass to next iteration

# for i in range(1,10): #1 2 4 5 7 8 
#     if i%3==0:
#         continue
#     print(i)

# names=["sujan","dipendra","gita","ashwin","syam"]


# for i in names:
#     if i.startswith("s"):
#         continue
    
#     print(i)

#else 
a=[1,2,3,0,4,5,6]

for i in a:
    if i==0:
        print("zero is found !!!")
        break 
    
else:
    print("zero is not found")
    
    
    

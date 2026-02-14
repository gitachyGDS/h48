#string formating :
# name="sujan"
# age=77

# result="my name is ",name,"and my age is ",age
# print(result)

# #% string :
# print("my name is %s and my age is %i"%(age,name))

#.formate 

# print("my name is {} and age is {}".format(age,name))

#f-string 
name="sujan"
age=77
price=88.189
result=f"my name is {name:^10} and age is {age} and price is Rs. {price:.1f}"
print(result)
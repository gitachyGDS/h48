#list : list is collection of data items(data structure) which is mutable(changeable),order and allow duplicate value 
 
# a=["sujan",77,23.99,True]


# print(a[1])
# print(a[2:4])
# print(a[0:2:1]) #variable_name[start:end:step]
# a[0]="ram"

# a.append(["syam",'manoj'])
# a.extend(["syam",'manoj'])
# a.insert(1,"syam")
# a.clear()
# del a
# a.pop(1)
# a.remove("sujan")
# print(a)

# print(type(a))
# print(len(a))

# a=[4,5,2,1,3,6]

# # a.sort()
# # b=sorted(a)

# # print(a)
# # print(b)

# # b=a #reference
# b=a.copy() #copy

# shallow copy and deep copy

# a.append("syam")
# print(a)
# print(b)



#nested list : one list inside another list
# a=["biraj",2,3,4]
# v=a[0] #"biraj"
# # v="biraj"
# print(v) #b

# import copy

# a=["ram",2,3,[11,33]]

# b=copy.deepcopy(a)

# a[3].append("sujan")

# print(b) #["ram",2,3,[11,33,"sujan"]]
# print(a) #["ram",2,3,[11,33,"sujan"]]


a=["sujan","ram","hari","manoj"]

v="+".join(a) #"sujan ram hari"

print(v)
print(type(v))
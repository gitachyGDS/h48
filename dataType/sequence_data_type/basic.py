#sequence data types : store the collection of items where each items is in specific order(index)

#string,list,tuple,range

#common use :
#index
#slicing
#repetition
#concatination

# a=[1,2,3]
# b=[1,2,3]

# print(a+b)
# print(a[0])
# print(a[0:2])


#range : it represent an immutable sequence of number 
#syntax :range(start,end,step)

a=range(3,9,2) #range(0,5,1) #3,5,7
print(type(a))
print(a[-1])
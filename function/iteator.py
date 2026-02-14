# iterator :object that contain countable number value(str,list,tuple,range,dict)

# a=[1,2,3,4,5]



# three high order inbuilt function
#map(),filter(),reduce()

#map():it applies a function to each item of iterable 
#syntax : map(function,iterator)

# n=[1,2,3,4,5] #[1,4,9,16,25]

# def show(a): #a=[1,2,3,4,5]
#     return a*a

# var=map(show,n)
# print(list(var))


# var=list(map(lambda a:a*a,n))
# print(var)


#filter() -->Filter item based on the function that return true/false
# n=[1,2,3,4,5] #2,4

# # def show(a):
# #     return a%2!=0

# # var=filter(show,n)
# # print(list(var))


# var=list(filter(lambda a:a%2==0,n))
# print(var)

# a=["sujan","ram","manoj","syam"]

# var=list(filter(lambda a:a.startswith("s"),a))
# print(var)



#reduce :applies a function to reduce is single value
# a=[1,2,3,4,5]

# from functools import reduce

# def show(x,y): #x=1,y=2 -->3+3 -->6+4-->10+5 -->15
#     return x*y 

# var=reduce(show,a)
# print(var)
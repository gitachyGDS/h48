#operator  -->it is just a symbol which is used perform operation between operand


# operand -->a,b,50
# operator --> +,=

# Arithmetic operator

# a=53
# b=7

# print(a+b) #addition
# print(a-b) #substract
# print(a * b) #multiply
# print(a/b) #division
# print(a//b) #floor
# print(a**b) #exponential
# print(a%b) #modulus


#relative operator or comparision operator
# a=20
# b=30 -->


# print( a == b)
# print( a != b)
# print(a > b)
# print(a<b)
# print(a>=b )
# print(a<=b )


#assignment operator  : = ,+= ,-=, /=
# a=30

# # a=a+1
# a -= 5
# print(a)


#logical operator : and, or ,not

# a=20
# b=30

# # print(a<b and a==b) #True and False
# # print(True and True)

# print(a<b or a==b)
# print(False or False)

# print(not a>b)

#membership operator (in ,not in)
# a=["sujan",1,2,3,4]
# # a="my name is sujan"

# print(40 not in a)


#identity operator (is ,is not)

a=[1,2,3] #456792
b=a[:]
# b=[1,2,3]
c=[1,2,3]

print(a == c)
print(a is b)

# print((a is b) is c)
# # print(a is not b)

# print(id(20))
# print(id(a))
# print(id(b))

# print(a == b) #True
# print(a is b) #False


#bitwise operator ( & , | , ~)
#it is individual of bit of integer

# a=12 #
# b=13

# print(a & b)
# print(a | b)
# print(~ a)

# 00001100
# # 11110011
# 1100
#   +1
# ------
# 1101

# -13



# #8421
# 1100
# 1101
# -----
# 1101



print(2**3**2)


#precendence 
#()
#exponential (**) -->right to  left
#*,/,//,%  -->left to right 
#+,- -->left right

a=3-2+5

a=2*3**3//4 # 2*27//4 -->54//4 -->13.44
print(a)
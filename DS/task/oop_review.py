import math
# print(dir(math))
print(len(dir(math)))#67
print(math.sqrt(25))#5.0

print(math.e)#2.718281828459045
print(math.pi)#3.141592653589793
print(math.log(10,10))#1.0
print(math.factorial(5))#120
print(math.sin(0))#0.0
print(math.pow(3,3))#27.0

import math as m 
print(m.floor(4.111111))#4
print(m.ceil(4.111111))#5


# #one hack:
print(int(5.00000))#5
print(float(5))#5.0 float //output come into float 

print(36/6)#6.0 float // output come into come into float 
print(36//6)#6 int// output come into int 
print(36%6)#0 int// output come into int // giving remender 



# # create a custom math classs:
class CustomMath:
    
    def __init__(self):
        self.pie=math.pi
        self.e=math.e
    
    def fact(self,num):
        product=1
        for i in range(1,num+1):
            product=product*i
        return product
    def maximum(self,num):
        return max(num)
    def minimum(self,num):
        return min(num)
    
    def power(self,num1,num2):
        return num1**num2
    
    def floor_ceil(self,num):
        if type(num) == float:
            ceil=int(num+1)
            floor=int(num)
            return floor,ceil

        else:
            return num,num    


    def round(self,num):
        return round(num)   
    def sqrt(self,num):
        
        return int(math.sqrt(num))

m=CustomMath()
print(m.pie)
print(m.e)
print(m.fact(3))#6
print(m.maximum([3,4,5,6,7,8,9]))#9
print(m.minimum([3,4,5,6,7,8,9]))#3
print(m.floor_ceil(4.111111))#(4, 5)
print(m.floor_ceil(6))#(6, 6)
print(m.round(2.999))#3
print(m.round(2.000))#2

print(m.power(2,3))#8
print(m.sqrt(25))#5.0



#self:
class Demo:
    def __init__(self):
        print(id(self))
# s=Demo()
# print(id(s))        

a=Demo()
print(id(a))
f=Demo()
print(id(f))
        
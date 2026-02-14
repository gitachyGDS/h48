#Programming paradigms support by python:

#procedural programming : variable,function,loop
#functional programmin : focus on function rather object ==list(map(lamda)
#decalarative :
#OOP :it organize  all model in object

#OOP : Object Oriented Programming 
#it map in real world sceanrios
#it match our variable in real world concept
#python use class and object to represent real world concpt

#class :blueprint of object,template of creating object
#object :instance of class 


#class is group of attribute and method 

#attribute : it represent variable that contain the value 
#method : it is similar to function that perform specific task

'''
syntax : 

class ClassName:
    #class 
    
ob=ClassName()
'''
#class ->reserved keyword  Stduent -->className
# class Student:
#     def __init__(self):  #it is special type method which is used to initlize value into variable
#         self.name="sujan"  #attribute
#         self.age=45
        
#     def show(self): #method
#         print(f"my name is {self.name}")
        
# ob=Student() #object
# ob2=Student()


# class Student:
#     def __init__(abc,name,age):  #it is special type method which is used to initlize value into variable
#         abc.name=name  #attribute
#         abc.age=age
        
#     '''self : it refer to the object :default variable that contain current object'''
#     def show(hhhh): #method
#         print(f"my name is {hhhh.name}")
#         print(f"my age is {hhhh.age}")
        
# R1=Student("sujan",66) #object
# # R1.show()
# print(id(R1))
# R2=Student("sujan",66)
# print(id(R2))

#attribute : product_name,qty,price
#method : total_price

# class Shop:
#     def __init__(self,name,qty,price):
#         self.name=name
#         self.qty=qty 
#         self.price=price 
        
#     def total_price(self):
#         total=self.qty*self.price 
#         print(f"your product is {self.name} and total price is Rs.{total}")
        
        
        
# pen=Shop("pen",5,10)
# pen.total_price()

# book=Shop("book",4,500)
# book.total_price()

# circle
#attribute :radius #-4
#area , perimeter


# class Circle:
#     def __init__(self,radius):
#         assert radius>0,f"{radius} cannot be negative"
        
#         self.radius = radius 

#     def areaperimeter(self):
#         if self.radius < 0:
#             print("Cannot have a -ve value")
#         else:
#             area = self.radius**2*3.14
#             perimeter = self.radius*2*3.14
#             print(f"Area of circle of radius {self.radius} is {area} and perimeter is {perimeter}")
#     def perimeter(self):
#         print(2*self.radius*3.14)

# rad=Circle(12)
# rad.radius=45
# print(rad.radius)
# rad.perimeter()
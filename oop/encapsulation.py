#encapsulation : the process of wrapping data(attribute) and method (function)  with in single in unit

#main purpose : 
#it is used to hide the data ,protected data ,control access of data 

#to achhieve encapulsation we use access modifier and propertory decorator

#access modifier : restrict   variable and method  access from globally by making private and protected

#accessor 
#public accessor : attribute and methods are accessbile from outside the class
#private accecssor : attribute and method are accessible with only that class : __variable_name
#protected accessor : attribute and method are accessible only with in class and subclass
#_variable_name


"""
class A():
    def __init__(self):
        self.name="sujan"
        
    def show(self):
        print(f"my name is {self.name}")
        
        
ob=A()


class B():
    def display(self):
        print("this is display data",ob.name)
        
b=B()
b.display()"""

#private accessor 
# class A():
#     def __init__(self):
#         self.__name="sujan"
        
#     def __show(self):
#         print(f"my name is {self.__name}")
        
#     def display(self):
#         self.__show()
        
        
# ob=A()
# print(ob.__dict__)

# # ob.__show()
# ob.display()


# class B():
#     def display(self):
#         print("this is display data",ob.__name)
        
# b=B()
# b.display()


#protected accessor

# class A():
#     def __init__(self):
#         self._name="sujan" #protected variable 
        
#     def show(self):
#         print(f"my name is {self._name}")
        
        
# ob=A()

# print(ob._name)


# class B():
#     def display(self):
#         print("this is display data",self._name)
        
# b=B()
# b.display()


#property decorator  : it allow you to access method like attribute


# class Cirlce():
#     def __init__(self,radius):
#         self.__radius=radius
    
#     @property
#     def radius(self):
#         print(f"given radius is  {self.__radius}")
        
#     @radius.setter
#     def radius(self,value):
#         if value>0:
#             self.__radius=value
#         else:
#             raise ValueError("radius cannot be negative")
        
#     @property
#     def area(self):
#         print(3.14*self.__radius**2)
        
        
   
        
# ob=Cirlce(5)

# ob.radius
# ob.radius=-10
# ob.radius
# ob.area


# -->Circle
# ob.radius (property decorator) __ 45
#ob.radiuse=10
#ob.area -->


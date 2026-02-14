#abstraction : the process of handling complexity by hidding uncessarry data from user  and provide only service

# from hide import show


# show(3,4)

# show(8,8)

# abstract class : blueprint of other class

#abstract  class --> a class that contain one or more abstract method is called abstract class
#abstract method -->a method that has declaration but doesnot implementation


from abc import ABC,abstractmethod

class A(ABC):
    
    @abstractmethod
    def show(self):
        pass
    
    @abstractmethod
    def register(self):
        pass
    
    # def main(self): #concrete method
    #     print("here some code")
    
    
class B(A):
    def display(self):
        print("hello world")
        
    def show(self):
        print("this is show class")
        
    def register(self):
        print("successfully register")
        
ob=B()
ob.display()
ob.show()
ob.main()


# class C(A):
#     def hello(self):
#         print("hello sipalaya")
        
#     def show(self):
#         print("asdf")
        
# ob=C()
# ob.hello()
    
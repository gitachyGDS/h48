#four fundamental concept of oop:
#inheritance :class that inherit all method and attribute from another existing class

#base class -->parent class 
#derived class -->child class

# Type of inheritance
# single inheritance
#single level(multi-level inheritance)
#multiple inheritance
#hierachical inheritance
#hybrid


#single inheritance

"""class A(): #parent
    def show1(self):
        print(" i have a feature one ")
        

class B(A): #child class 
    
    def show2(self):
        print("i have a feature two")
        
ob=B()
ob.show2()
ob.show1()"""

#single-level inheritance
"""
class A(): #grandd-parent
    def show1(self):
        print(" i have a feature one ")
        

class B(A): #parent 
    
    def show2(self):
        print("i have a feature two")
        
class C(B): #child
    def show3(self):
        print(" i have a feature 3")
        
ob=C()
ob.show3()
ob.show2()
ob.show1()"""

#multiple inheritance (mixin)
"""class A():  #father
    def show1(self):
        print(" i have a feature one ")
        

class B(): #mother 
    
    def show2(self):
        print("i have a feature two")
        
class C(A,B):#child
    def show3(self):
        print("i have a featuree 3")
        
ob=C()    
ob.show3()
ob.show1()
ob.show2()"""

#hierachical inheritance
class A(): #parent
    def show1(self):
        print(" i have a feature one ")
        

class B(A): #child class 
    
    def show2(self):
        print("i have a feature two")
        
class C(A): #child 
    def show3(self):
        print("i have a feature 3")
        
ob1=C()
ob1.show3()
ob1.show1()

ob2=B()
ob2.show2()
ob2.show1()
        
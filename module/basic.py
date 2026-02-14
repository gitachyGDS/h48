'''
module :  file that contain python code(variable,function,class, etc) that can be reused  in other python program


#main purpose:
code reusability
code organaize

Type module : 
#built in module  :precodded by python
#user define module 
#External module 


scripts
module

package : folder1-->__init__.py
                --> module.py
                -->module1.py
                -->module2.py
            
libriry -->folder -->package 1
                  -->package 2
                  -->package 3

'''

# import random
# print(random.choices([1,2,3],k=2))

# import keyword
# print(keyword.kwlist)

# import calendar

# print(calendar.month(2025,11))
# print(calendar.calendar(2025))


# from datetime import datetime

# print(datetime.now().time())


# import math
# print(dir(math))

# from math import sqrt as a

# c=a(36)
# c=factorial(5)
# # 1.00001 1.2 1.3-------- 1.9
# # c=math.floor(3.999)
# c=ceil(3.00001)
# # c=round(3.267,2)
# # var=math.radians(30)
# # c=math.sin(var)
# print(c)



from  file import *

print(names)
print(show(2,3))
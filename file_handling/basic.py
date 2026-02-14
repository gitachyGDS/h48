'''
file handling :

file :collection of data and information to store data permanent
type of file : 
text file --> used to store in form character : .py,.txt,csv,.html
binary file --> user to store in form byte : image,video

file handling : python perform some function such as :create,read,write,appen,delete


process of file handling :
-->file open
-->perform some operation
-->close file 

syntax :

f_object =open("file_path","mode")

mode : purpose of opening that file 
c -->create
r -->read
w -->write
a -->append
r+ -->read and write
w+ -->write and read
a+ -->write and read

'''

# f=open("msg.txt",'w+')

# print(f.read(10))
# print(f.readline())
# print(f.readlines())
# print(f.read())


# f.write("okey sipalaya")
# f.write("\ni want to learn django")
# print(f.read(10))
# f.write("okey sipalaya")



"""
try:
    f=open("msg.txt",'w')
    print(f.read(10))
finally:
    f.close()
print(f.closed)"""


# with statment :

# with open("msg.txt",'r') as f:
#     print(f.read(10))
    
# print(f.closed)

#tell & seek 

# f=open("msg.txt",'r')


# print(f.read(10))
# print(f.tell())
# f.seek(0)
# print(f.tell())
# print(f.read(20))


# import os 
# os.remove("msg.txt")


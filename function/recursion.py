#recursion : a function calling itself again and again to complete a value 



# def show(n): #n=5
#     if n==5:
#         return 
#     print("hello world",n)
#     show(n+1)
    
# show(0)

#hello world 0
#hello world 1
#hello world 2
#hello world 3
#hello world 4


# import sys 
# sys.setrecursionlimit(5000)
# print(sys.getrecursionlimit())



# 5! = 5*4*3*2*1 = 5*4!
# 4! =4*3*2*1 = 4* 3!
# 3! =3*2*1
# n! = n * (n-1)!

"""def fact(n):  #n=3
    if n==1 or n==0:
        return 1
    
    return n * fact(n-1) #5*4*3*2*1

print(f"given number  factorical is {fact(5)}")
    """
    
    
a=123 # 3 +12=3+2+1
6789 # 9+678 -->9+8+67 -->9+8+7+6 # n%10 +n//10
 
print(a%10)
print(a//10)


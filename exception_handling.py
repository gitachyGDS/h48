'''
exception_handling :it is the process of responding unexcepted event when programm is run

syntax:

try:
   block of code 
   
except: 
    error message
    
    



'''
# try:
#     def show():
#         print(2+2)
        
#     show()
    
# except:
#     print("some error is occur")

# print("some imp code is here .....")



'''
types of error :
complile time error 
logical error 

run time error:
TypeError
IndexError
ZeroDivisionError:
KeyError
ValueError


'''
"""try:
    def show():
        print(4/0)
        # print("22")
        
    show()
# except ZeroDivisionError:
#     print("value cannot divide by zero")
# except TypeError:
#     print("differnt str and int cannot be divide")
# except:
#     print("some error ")

except Exception as e:
    print(f"Error {e}")

"""

# try:
#     code 
    
# except:
#     error messsage
    
# finally:
#     always excuted

#finally : always excuted 

def show():
    try:
        print("hello this is working"[111])
        
    except:
        print("some error occur")
        return 1
        
    
    finally:
        print("some imp code is here")
        
show()
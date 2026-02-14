"""1. Write a program that will convert celsius value to fahrenheit. """
# celsius = float(input("Enter the celsius value: "))

# farhenheit = (celsius * 9/5) + 32 
# print(f"Converted value of {celsius} C = {farhenheit} F")



"""2. Write a program to find the euclidean distance between two coordinates.Take both the      
 coordinates from the user as input.For two points in a 2-dimensional space (x1,y1) and (x2,y2), the 
 formula is: d = √ (x2 – x1)2 + (y2 – y1)2"""
# x1 = float(input("Enter the x-coordinate of the first point: "))
# y1 = float(input("Enter the y-coordinate of the first point: "))

# x2= float(input("Enter the x-coordinate of the second point: "))
# y2 = float(input("Enter the y-coordinate of the second point: "))

# distance = ((x2 -x1)**2 + (y2-y1)**2)**0.5
# print(f"Distance Between two point is: {distance:.3f}")           


"""3  Write a program to find the sum of squares of first n natural numbers where n will be provided by 
 the user. 
 Hint : the sum of the squares of first n natural numbers = n(n+1)(2n+1)/6"""
# n = int(input("Enter the value of n: "))
# sum = n * (n+1) *(2*n+1)/6
# print(f"the total sum of squares of first n natural numbers is:{sum:.2f}")


"""
 Given 2 fractions, find the sum of those 2 fractions.Take the numerator and denominator values of 
 the fractions from the user."""

# num1 = int(input("Enter the numerator of the first fraction: "))
# deno1 =int(input("Enter the denominator of the first fraction:"))

# num2 = int(input("Enter the number of the second fraction: "))
# deno2 = int(input("Enter the denominator of the second fraction: "))

# sum_num = (num1 * deno2) + (num2 * deno1)
# sum_deno = deno1 * deno2

# print("The sum of the two fractions is: ", sum_num, "/", sum_deno)



""" Q5: Write a program that take a user input of three angles and will find out whether it can form a triangle or not. 
#Hint: sum of all angles is 180 and all angles are positive """

# a=int(input("Enter first angle:"))
# b=int(input("Enter second angle:"))
# c=int(input("Enter third angle:"))

# if a+b+c==180  and a>0 and b>0 and c>0:
#     print("Yes, the angles can form a triangle")
# else:
#     print("No, the angles can't form a triangle.")

''' first angle:90
Enter second angle:45
Enter third angle:45
Yes, the angles can form a triangle'''

"""Enter first angle:12
Enter second angle:77
Enter third angle:98
No, the angles can't form a triangle."""



"""Q6: Write a program that will take user input of cost price and selling price and determines whether its  .
a loss or a profit. 
# """

# cost_price=float(input("Enter the cost price (cp):"))
# selling_price=float(input("Enter the selling price(sp):"))

# if selling_price>cost_price:
#     profit = selling_price - cost_price
#     print(f"you made a profit of :{profit}")
# elif cost_price>selling_price:
#     loss = cost_price - selling_price
#     print(f"you incurred a loss of :{loss}")
# else:
#     print("either profit nor  loss!")



"""Q7: Write a menu-driven program - take user input for options
 1) 1 cm to ft , 
 2)km to miles  
 3) usd to nrs  
4) exit     
Hint 
1 cm = 0.032ft 
1km = 0.62miles 
1 USD = 135 NRS
"""

user=int(input("Choose the conversion option:"))
if user==1:
    cm=float(input("Enter the value in cm:"))
    ft= cm * 0.032
    print(f"The converted value of  {cm} cm  = {ft} ft.")
elif user==2:
    km=float(input("Enter the value in km:"))
    miles= km * 0.62
    print(f"Converted value of {km} km  = {miles} miles.")
elif user==3:   
    usd=float(input("Enter the value in USD :"))
    nrs=usd*135
    print(f" Converted value of {usd} USD = {nrs} NRS.")
elif user==4:
    print("Exit the program.")

"""
Qn-8) Check if a number is divisible by 2 and 3 or both  
# """
# user=int(input("Enter a number:"))
# if user % 2 ==0 and user % 3 ==0:
#     print(f"{user} is divisible by both 2 and 3.")

# elif user % 2 ==0:
#     print(f"{user} is divisible by 2.")
# elif user % 3==0:
#     print(f"{user} is divisible by 3.")
# else:
#     print(f"{user} is not divisible by either 2 or 3.")

"""
Enter a number:297
297 is divisible by 3.

Enter a number:36
36 is divisible by both 2 and 3.

Enter a number:32
32 is divisible by 2.

    Enter a number:25
25 is not divisible by either 2 or 3.
    """

""" Qn-9) Implement a basic calculator that performs addition, subtraction, multiplication, and division 
based on user choice.     """

# num1=float(input("Enter first number:"))
# operation=input("Enter the operation (+, -, *, /):")
# num2=float(input("Enter second number:"))


# operation=input("Enter the operation (+, -, *, /):")

# if operation=='+':
#     results = num1+ num2
#     print (f"The results of addition is :{results}")
# elif operation =='-':
#     print = num1 - num2
#     print (f'The results of subtraction is :{results}')
# elif operation == '%':
#     results = num1 * num2
#     print(f" The results of multiplication is :{results}")
# elif operation =='/':
#     results = num1 / num2
#     print(f'The results of division is :{results}')
# else :
#     print("Invalid operation selected.")
"""
Enter first number:7
Enter the operation (+, -, *, /):+
Enter second number:4
The results of addition is :11.0"""

""""
Q10) Calculate the percentage and grade based on the total marks and individual subject marks ,the 
system is based on 5 subjects, and the student must have at least 35 marks in each subject to pass. 
percentage >= 90  A grade 
percentage >= 75: B grade 
percentage >= 50:C grade 
percentage < 50: F grade 
"""

s1= int(input("Enter marks of Nepali:"))
s2= int(input("Enter marks of Math:"))
s3= int(input("Enter marks of Social:"))
s4= int(input("Enter marks of English:"))
s5= int(input("Enter marks of Science:"))


if s1<35 or s2<35 or s3<35 or s4<35 or s5<35:
    print("You have failed the exam due to insufficient marks in one or more subjects.")    

else:
    total_marks = s1 + s2 + s3 + s4 + s5

    percentage = (total_marks / 500) * 100
    print(f"Your total marks are :{total_marks}")
    print(f"Your percentage is :{percentage:.2f}%")
if percentage >=90:
    grade ="A"
    print(f"Your grade is :{grade}")

elif percentage >=75:
    grade ="B"
    print(f"Your grade is :{grade}")
elif percentage >=50:
    grade ="C"
    print(f"Your grade is :{grade}")
else:
    grade ="F"
    print(f"Your grade is :{grade}")

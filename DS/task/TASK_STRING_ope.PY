"""Python Tasks Strings 
Strings : 

1. Extract Initials from Full Name 
Given a full name like "Pushpa Raj Giri", write code to return "PRG"."""

# user=input("Enter your full name:")
# names=user.split()
# initials= ""
# for name in names:
#     initials += name[0].upper()# for upper case

# initials += "."
# print(initials)

"""Enter your full name:gita chy
GC.
"""
"""
 2. Email Domain Checker 
If an email (e.g., "sita@gmail.com") ends with "@gmail.com", print "Personal 
email", else print "Work email". 
"""

# email=input("Enter your email address:")
# if email.endswith("@gmail.com"):
#     print(f'{email} is Personal Email') 
# else:
#     print("Work Email")

    
"""
Enter your email address:rohan.shrestha@xyzcompany.com
Work email

Enter your email address:gitachy@gmail.com
Personal Email
"""
#######
"""3. Shorten Product Description 
From a product description like "Brand New Samsung Galaxy S21 Ultra - 256GB", 
extract only the first 20 characters and add "...". 
"""

# product=input("Enter your product description:")
# short_description = product[:20]+ "..."

# print("Shortened description:",short_description)


"""4. Check Substring Presence in Address 
Given an address string (e.g., "Kathmandu-32, Bagmati"), check if "Kathmandu" is in 
the address. 
"""

##is not is --> id check 
##in not in--> membership check

# address= 'Kathmandu-32, Bagmati'
# if "Kathmandu" in address:
#     print("Kathmandu is in the address.")
# else:
#     print("Kathmandu is not in the address.")## use in perator to check membership

"""
5. Generate User ID 
From full name and birth year (e.g., "Saroj Giri", 2000), create user ID like: 
"Saroj2000". 

# """
# name=input("Enter your Full Name:")
# birth_year=input("Enter your birth year:")
# first_name=name.split()[0]
# user_id=first_name+birth_year
# print("Generated User ID:",user_id)


"""
Enter your Full Name:gita chy
Enter your birth year:2006
Generated User ID: gita2006
"""


"""6. Log Message Format 
Given log: "ERROR: File Not Found - data.csv", extract the file name "data.csv" 
# using slicing. """

# log="ERROR: File Not Found - data.csv"
# dash_index=log.index("-")#'_' ko index find garne
# file_name=log[dash_index+2:]#slicing
# print(f'Extract file name :{file_name}')
# #Extract file name :data.csv


"""7. Standardize Phone Number Format 
Given "9801234567", format it as "(980)-123-4567" using indexing and string 
manipulation."""

# user=int(input("Enter your phone number:"))
# part1=str(user)[0:3]
# part2=str(user)[3:6]
# part3=str(user)[6:]
# formatted_number = f"({part1})-{part2}-{part3}"
# print(f'Formatted Phone Number :{formatted_number }')

#Enter your phone number:9801234567
# Formatted Phone Number :(980)-123-4567
# Enter your phone number:9822952923
# Formatted Phone Number :(982)-295-2923


""""8. Mask Aadhar/SSN Number 
Given a string like "1234-5678-9101", show only the last 4 digits as "XXXX-XXXX
9101". """

# id = "1234-5678-9101"
# masked_id = "XXXX-XXXX-" + id[-4:]
# print(f'Masked ID:{masked_id }')

#Masked ID:XXXX-XXXX-9101

# mask_id = input("Enter your Aadhar/SSN number:")
# masked_id = "xxxx-xxxx-" + mask_id[-4:]
# print(f'Masked ID:{masked_id }')

# Enter your Aadhar/SSN number:1234-5678-9101
# Masked ID:xxxx-xxxx-9101

"""9. Check if Feedback Contains a Keyword 
From feedback like "The service was excellent and fast.", check if "fast" is 
present using in, and return a matching score out of 5."""

# feedback = "The service was excellent and fast."
# keyword = "fast"
# if keyword in feedback:
#     score =5
# else: 
#     score = 0

# print(f'Matching Score: {score}/5')

"""10. Check if User is from Nepal 
From user’s address like "John, New Road, Pokhara, Nepal", detect if the user is 
from Nepal using if and in. """

# address = "John, New Road, Pokhara, Nepal" 
# if "Nepal" in address:
#     print("User is from Nepal.")
# else:
#     print("User is not from Nepal.")



# user= input("Enter your address:")
# user_lower = user.lower()
# if "nepal" in user_lower:
#     print("User is from Nepal.")    
# else:
#     print("User is not from Nepal.")


"""11. Extract Area Code from Email ID 
From "john.doe.pkr123@gmail.com", extract "pkr" assuming the area is always 
between last . and numbers. """

# email="john.doe.pkr123@gmail.com"
# sp_email=email.split(".")
# ind_email=sp_email[-2]
# Area_code=""

# for i in ind_email:
#     if i.isdigit():  #digits@haru aayo bhanee break garxa
#         break  
#     else:
#      Area_code+=i
# print(f"The area code of user is {Area_code}.")#The area code of user is pkr.


"""12. Check Gender from ID Prefix 
If a national ID starts with "M-", it's Male, "F-" is Female, else print "Unknown". 
Example: "F-2394023". """

# national_id = "F-2394023"
# if national_id.startswith("M-"):
#     print("Male")
# elif national_id.startswith("F-"):
#     print("Female")
# else:
#     print("Unknown")

"""13. Redact Offensive Words in Comment 
Given a string: "This is such a stupid service.", replace "stupid" with "****" 
using slicing or replace()."""

# word="This is such a stupid service."
# redacted_word=word.replace("stupid","****") 
# print(f'Redacted Word: {redacted_word}')

"""14. Extract Hashtags from a Tweet 
Given: "Enjoying the #Dashain vibes in #Kathmandu", extract all words starting 
with #."""

# tweet = "Enjoying the #Dashain vibes in #Kathmandu"
# words = tweet.split()
# hastags = [word for word in words if word.startswith("#")]
# print("Extracted Hashtags:", hastags)

# Extracted Hashtags: ['#Dashain', '#Kathmandu']

"""15. Extract Country Code from International Phone 
Given "+977-9801234567", extract the country code (+977) and the local number 
separately. """

# phone_number = "+977-9801234567"
# country_code, local_number = phone_number.split("-")
# print(f'Country Code: {country_code}, Local Number: {local_number}')
# # Country Code: +977, Local Number: 9801234567

"""16. Smart Truncate of Sentences 
Truncate a long string after 100 characters without cutting a word in between. Add 
"..." if it was cut. """


# text="a string is a sequence of characters. In programming, strings are used to represent text data. They can include letters, numbers, symbols, and spaces. Strings are typically enclosed in quotation marks, either single (' ') or double (" ")."
# if len(text) > 100:
#     truncated = text[:100]
#     last_space = truncated.rfind(" ")
#     truncated = truncated[:last_space] + "..."
# else:truncated = text 
# print("Truncated Text:", truncated)


"""Truncated Text: a string is a sequence of characters. In programming, strings are used to represent text data. They..."""


"""17. Validate Strong Password 
A password must: 
 Be at least 8 characters 
 Contain at least one number 
 Contain one uppercase letter 
 Contain special character 
Validate using if-else and in."""

###“Copied for demo” ✅

# # Step 1: User बाट password input लिने
# password = input("Enter your password: ")

# # Step 2: Special characters define गर्ने
# special_chars = "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|`~"

# # Step 3: Condition 1 - Length check
# if len(password) < 8:
#     print("Password too short! Must be at least 8 characters.")
# else:
#     # Step 4: Condition 2 - Check for number
#     has_number = False
#     for char in password:
#         if char.isdigit():
#             has_number = True
#             break
#     if not has_number:
#         print("Password must contain at least one number.")
#     else:
#         # Step 5: Condition 3 - Check for uppercase
#         has_upper = False
#         for char in password:
#             if char.isupper():
#                 has_upper = True
#                 break
#         if not has_upper:
#             print("Password must contain at least one uppercase letter.")
#         else:
#             # Step 6: Condition 4 - Check for special character
#             has_special = False
#             for char in password:
#                 if char in special_chars:
#                     has_special = True
#                     break
#             if not has_special:
#                 print("Password must contain at least one special character.")
#             else:
#                 # If all conditions pass
#                 print("Strong password! ✅")


# password = input("Enter your password: ")
# special_chars = "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|`~"
# if len(password) < 8:
#     print("Password too short! Must be at least 8 characters.")
# elif not any(char.isdigit() for char in password):
#     print("Password must contain at least one number.")
# elif not any(char.isupper() for char in password):
#     print("Password must contain at least one uppercase letter.")
# elif not any(char in special_chars for char in password):
#     print("Password must contain at least one special character.")
# else:
#     print("Strong password! ✅")





# try for simplification:
# password= input("Enter your password: ")
# special_char="!@#$%^&*()-_=+[]{};:'\",.<>?/\\|`~"
# if len(password)<8:
#        print("Password to short! must be at least 8 characters.")
# elif not any (char.isdigit() for char in password):  
#     print("Password must contain at least one number.") 

# elif not any(char.isupper() for char in password):
#     print("Password must contain at least one uppercase letter.")

# elif not any(char in special_char for char in password):
#     print("Password must contain at least one special character.") 
# else:
#     print("Strong password! ")      

"""
18. Extract Year from Event Title 
From event names like "Startup World Cup Nepal 2025", extract the year using 
slicing and conditional logic. 
"""

# event_name = "Startup world Cup Nepal 2025"
# year = event_name.split()[-1]
# if year.isdigit() and len(year) == 4:
#     print(f'Extracted  year: {year}')

# else:
#     print("No valid year found in the event name.")


"""
19. Detect Language from Message Prefix 
From message: "[EN] Welcome to Sipalaya", check prefix ([EN], [NP], [JP]) and 
print language in full. 
# """
# message = input("Enter your message:")
# prefix = message[:4]
# if prefix == "[EN]":
#        print("language is English.")
# elif prefix == "[NP]":
#         print("language is Nepali.")
# elif prefix == "[JP]":
#         print("language is Japanese.")
# else:
#         print("Unknown language prefix.")
    
"""20. Summarize Customer Review 
Given a review like "I absolutely loved the food and the ambience, but the 
service was a bit slow." 
If "loved" or "great" or "amazing" present → Positive 
If "slow" or "bad" → Negative 
Else → Neutral"""


#keyword based method 
# review = "I absolutely loved the food and the ambience, but the service was a bit slow." 
# if "loved" in review or "great" in review or "amazing" in review:
#     print("Customer gives Postive Review")
# elif "slow" in review or "bad" in review:
#     print("Customers gives negative Review")
# else:
#     print("Customers gives Netural Review")


"""count multiple keywords / scoring method """

# review = "I absolutely loved the food and the ambience, but the service was a bit slow."

# positive_keywords = ["loved", "great", "amazing"]
# negative_keywords = ["slow", "bad"]
# score = 0
# for keyword in positive_keywords:
#     if keyword in review:
#         score +=1
# for keyword in negative_keywords:
#     if keyword in review:
#         score -=1
# if score >0:
#     print("Customer gives positive review")
# elif score < 0:
#     print("Customers gives negative review")

# else:
#     print("Customers gives neutral review")                  


# #next  method 
# reviews="I absolutely loved the food and the ambience, but the service was a bit slow."
# sentiment=[]

# if "loved" in reviews or "great" in reviews or "amazing"in reviews:
#     sentiment.append("Positive")
#     if "slow" in reviews or "bad" in reviews:
#         sentiment.append("Negative")

#         if not sentiment:#if Positive and Negative reviews xina vane mtra execute hunxa

#             sentiment.append("Neutral")

# print(f"The reviews sentiment is {",".join(sentiment)}")#The reviews senti ment is Positive,Negative    

"""
Operators: 
1. Age Eligibility Check (Comparison Operator) 
Given an age age = 17, check if the user is eligible to vote (18+). Print "Eligible" or 
"Not Eligible". 
"""
# age = int(input("Enter your age:"))
# if age >= 18:
#     print("Eligible to vote.")
# elif age >=0:
#     print("Not Eligible to vote.")
# else:
#     print("Invalid age.")

"""
2. Compare Product Prices (Relational Operators) 
Given two product prices price1 = 999, price2 = 1199, print which product is 
cheaper. 
# """
# price1 = 999
# price2 = 1199
# if price1 < price2:
#     print("Product 1 is cheaper.")
# elif price1 > price2:
#     print("Product 2 is cheaper.")
# else:
#     print("Both products are equally priced.")

"""
    3. Check If Number is Even (Modulus Operator) 
Given user_id = 1023, determine if the ID is even or odd using %.
# """
# user_id = 1023
# if user_id % 2 == 0:
#     print("User ID is even.")
# else:
#     print("User ID is odd.")


"""
4. Discount Condition Check (Logical AND) 
If customer_type == "Gold" and purchase_amount > 5000, apply a 20% discount. 
Use if with and. 
# """
# item="Gold"
# amount=5500

# if item=="Gold" and amount >5000:
#     print(f"Congrats!! u get 20%  discount ,so your product is:{item} and total_pay amount is {(amount)-(amount*20)//100}.")#Congrats!! u get 20%  discount ,so your product is:Gold and total_pay amount is 4400.

# else:
#     print("Sorry!! u don't get discount")



"""
5. Check If a Letter Is a Vowel (in Operator) 
Given a character c = 'e', check if it’s a vowel using in.
# """
# C = 'e'
# C=C.lower()
# if C in 'aeiou':
#     print("It's a vowel.")
# else:
#     print("It's not a vowel.")


"""
6. Password Match (Equality Operator) 
Check if entered password input_pass matches stored password db_pass. Show 
"Access Granted" or "Access Denied". 
# """
# input_pass= input("Enter your password:")
# db_pass="P@ssw0rd123"
# if input_pass == db_pass:
#     print("Access Granted")
# else:
#     print("Access Denied")

"""
7. User Activity Bonus (Compound Assignment) 
If a user performs an activity, increase their score by 10 using +=.
# """
# score = 50 #initial score
# activity_performed = True #
# if activity_performed: # # user activity status

#     score += 10 ## compound assignment, score = score + 10
#     print(f"New score: {score}")

"""
8. Salary Grade Evaluation (Comparison + Logical OR) 
If salary is less than 20,000 or job title is "Intern", print "Junior Grade".
"""

# salary = 1500000
# job_title = "Intern"
# if salary < 20000 or job_title == "Intern":
#     print("Junior Grade")
    
# else:
#     print("Senior Grade")



"""9. Credit Eligibility (Nested if + Logical) 
If age > 21 and income > 30000, check if credit_score > 700 to approve credit."""

# age = int(input ("Enter your age:"))
# income = int(input ("Enter your income:"))


# if age > 21 and income >30000:
#     credit_score = int(input ("Enter your credit score:"))
#     if credit_score > 700:
#         print("Credit Approved.")
#     else:
#         print("Credit Not approved. ")
# else:
#     print("your age and income is not eligible for credit. ")


"""
11. Data Cleaning: Replace Negative with 0 (Ternary Operator) 
If a value in dataset is negative (e.g., x = -10), use x = 0 if x < 0 else x.
# """
# x = int(input("Enter a value:"))
# if x < 0:
#     x = 0
# else:
#     x = x
# print(f"New value: {x}")


# Enter a value:-40
# New value: 0

# Enter a value:10
# New value: 10

"""
12. Compare Dates as Strings (Relational Operator) 
Given two dates: "2025-06-01" and "2024-12-31", check which date is later using > 
operator. 
# """
# date1 = "2025-06-01"
# date2 = "2024-12-31"

# if date1 > date2:
#     print(f"{date1} is later than {date2}.")
# else:
#     print(f"{date2} is later than {date1}.")

#2025-06-01 is later than 2024-12-31.

"""
13. Dynamic Bonus Allocation (Ternary + Logical) 
If sales > 5000 and employee_type == 'Full-Time', bonus = 1000 else 500. 
"""# Dynamic Bonus Allocation (Full if-else version)

# # User input
# sales = int(input("Enter sales: "))
# employee_type = input("Enter employee type (Full-Time / Part-Time): ")

# # Check conditions
# if sales > 5000:
#     if employee_type.lower() == 'full-time':
#         bonus = 1000
#         print(f"You get bonus: {bonus}")
#     else:
#         bonus = 500
#         print(f"You get bonus: {bonus}")
# else:
#     bonus = 500
#     print(f"You get bonus: {bonus}")

# ## ternary opearator
# bonus = 1000 if sales > 5000 and employee_type.lower().replace(" ", "-") == 'full-time' else 500
# print(f"You get bonus: {bonus}")

"""
14. Find the Median of Three Numbers (Chained Comparisons) 
Given a, b, and c, use chained comparisons and logical operators to find the median 
value.
# """
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))


# if (a >= b and a <= c ) or (a >= c and a <= b):
#     median = a
# elif (b >= a and b <= c) or (b >= c and b <= a):
#     median = b
# else:
#     median = c

# print(f"The median value is: {median}")
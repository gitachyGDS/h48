"""Problem 1: Create Short Form from initial character 
Given a string create short form of the string from Initial character. Short form should be capitalised. 
     Example: 
     Input:Data science mentorship program 
    Output:DSMP"""

# text= input("Enter the string:")
# words = text.split()
# short_form =""
# for word in words:
#     short_form += word[0].upper()
# print(F"Short form of the given string is:{short_form}")
    #print("Short form of the given string is:", short_form)


"""
Problem 2: Append second string in the middle of first string 
             Input:  first string :will 
             Second string: do 
             Expected Output:widoll
"""
# fstring=input("Enter the first string:")
# sstring=input("Enter the second string:")
# mid=len(fstring)//2
# print(mid)
# print(fstring[:mid] + sstring + fstring[mid:])

"""Enter the first string:will
Enter the second string:do
2
widoll
"""

"""Problem 3:Given string contains a combination of the lower and upper case letters. Write a program 
to arrange the characters of a string so that all lowercase letters should come first. 
       Input:   str1 = PyNaTive 
       Expected Output: yaivePNT"""


# string=input("Enter the string:")
# lowercase=""
# uppercase=""
# for char in string:
#     if char.islower():
#         lowercase += char 
#     else:
#         uppercase += char
#         # lowercase="". join(sorted(lowercase))  #IF SORTING IS NEEDED
#         # uppercase="". join(sorted(uppercase)) #IF SORTING IS NEEDED
#         results = lowercase + uppercase

# print("The arranged string is:", results)
"""
Enter the string:PyNaTive 
The arranged string is: yaivePNT"""


"""Problem 4:
Take a alphanumeric string input and print the sum and average of the digits that appear in 
the string, ignoring all other characters. 
        Input:hel123O4every093 
        Output: 
         Sum: 22 
         Avg: 2.75
#          """
# user=input("Enter the alphanumeric string:")
# sum=0
# count=0
# for char in user:
#     if char.isdigit():
#         sum += int(char)
#         count +=1
# if count>0:
#     avg= sum / count
# else:
#     avg=0

# print("Sum:",sum)
# print("Avg:",avg)

"""Enter the alphanumeric string:hel123O4every093 
Sum: 22
Avg: 3.142857142857143"""


"""Problem 5:
 Removal of all characters from a string except integers 
      input = 'I am 25 years and 10 months old' 
      Expected Output:2510 """

# user=input("Enter the string:")
# result=""
# for char in user:
#     if char.isdigit():
#         result += char
# print("The result is:",result)

"""Enter the string:I am 25 years and 10 months old
The result is: 2510"""



"""Problem 6: Check whether the string is Symmetrical. 
Statement: Given a string. the task is to check if the string is symmetrical or not. A string is said to be 
symmetrical if both the halves of the string are the same. 
Example 1: 
Input: khokho 
Output: The entered string is symmetrical"""


# user=input("Enter the string:")
# length = len(user)
# mid = length // 2
# first_half = user[:mid]
# if length % 2 == 0:
#     second_half = user[mid:]
# else:
#     second_half = user[mid + 1:]

# if first_half == second_half:
#     print("The entered string is symmetrical")
# else:
#     print("The entered string is not symmetrical")


"""Problem 7: Reverse words in a given String 
Statement: We are given a string and we need to reverse words of a given string. 
Example 1: 
Input: my name is saroj 
Output: saroj is name my 
Example 2: 
input: geeks quiz practice code 
Output: code practice quiz geeks"""

# user=input("Enter the string:")
# user= user.split()


# reversed_string =' '.join(user[::-1])
# print("Reversed string is:",reversed_string)



"""
Problem 8: 
Find uncommon words from two Strings. 
Statement:
Given two sentences as strings A and B. The task is to return a list of all    uncommon words. 
A word is uncommon if it appears exactly once in any one of the sentences, and does not appear in the 
other sentence. 
Note: A sentence is a string of space-separated words. Each word consists only of 
lowercase letters. 

Example 1: 
Input: A = "apple banana mango" 
B = "banana fruits mango" 
Output: 
['apple', 'fruits']
"""

# user1=input("Enter the first string:")
# user2=input("Enter the second string:")
# set1=set(user1.split())
# set2=set(user2.split())
# uncommon_words = list((set1 - set2) | (set2 - set1))

# print(uncommon_words)




"""Problem 9:
 Word location in String. 
Statement:Find a location of a word in a given sentence. 
Example 1: 
Input: 
Sentence: We can learn data science through sipalaya mentorship program. 
word: sipalaya 
Output: 
Location of the word is 7. 
Note- Don't use index/find functions"""

# sentence = "We can learn data science through sipalaya mentorship program."
# words = sentence.split()

# find_word = input("Enter the word to find its location: ")
# position = 0

# for i, w in enumerate(words, start=1):  # i = position number
#     if w.lower() == find_word.lower():   # case insensitive search
#         position = i                      # Correct position
#         break

# if position != 0:
#     print("Location of the word is", position)
# else:
#     print("Word not found")


"""Problem 10: Write a program that can remove all the duplicate characters from a string. User will 
provide the input. 
Input: s = 'aaaabbbbbccccdddeeeeffff' 
Output: abcdef """

# s = input("Enter a string: ")
# seen = set()
# result = ""
# for ch in s:
#     if ch not in seen:
#         result += ch
#         seen.add(ch)
# print(f'The final value of the string is :{result}')


# List Problems: 
"""
Problem 1: Add new item to list after a specified item 
Write a program to add item 7000 after 6000 in the following Python List 
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40] 
Output:[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
"""

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
# print(list1)



"""Problem 2:
Running Sum(Cumulative sum) on list (Write a program to print a list after performing running sum 
on it. 
Input: list1 = [1,2,3,4,5,6] 
Output: [1,3,6,10,15,21]
"""

# list1 = [1,2,3,4,5,6]
# running_sum = []
# current_sum = 0
# for num in list1:
#     current_sum += num
#     running_sum.append(current_sum)
# print(running_sum)



"""Problem 3:
Find list of common unique items from two list. and show in increasing order 
Input: 
num1 = [23,45,67,78,89,34] 
num2 = [34,89,55,56,39,67] 
Output: [34, 67, 89]"""

# num1 = [23, 45, 67, 78, 89,34]
# num2 = [34, 89, 55, 56, 39, 67]
# comm_items = list(set(num1) & set(num2))
# num_list=sorted(comm_items)
# print(f'The common values are :{num_list}')

"""Output: [34, 67, 89]"""


"""Problem 4: Write a program that can perform union operation on 2 lists 
Example: 
Input: 
[1,2,3,4,5,1] 
[2,3,5,7,8] 
Output: 
[1,2,3,4,5,7,8]"""

# num1 = [1,2,3,4,5,1]
# num2 = [2,3,5,7,8]
# num_list=sorted(list(set(num1) | set(num2)))
# print(f'The union values are :{num_list}')


"""Problem 5: Write a program that can find the max number of each row of a matrix 
Example: 
Input: [[1,2,3],[4,5,6],[7,8,9]] 
Output: [3,6,9]
"""

# list1 = [[1,2,3],[4,5,6],[7,8,9]]
# max_values = []
# for row in list1:
#     max_values.append(max(row))
# print(f'The max values of each row are :{max_values}')




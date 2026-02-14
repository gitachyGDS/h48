# Write a Python program that:

# Takes a sentence as input from the user

# Counts and displays the number of words in the sentence
# input="my name is sujan"
# output="total word in sentence is 4"

# var= input("Enter your sentence : ")
# b=var.split() #["my","name","is","sujan"]
# print(f"total word in sentence is {len(b)}")


# Write a Python program that takes a sentence as input and give a new string with the words 
# in reverse order, while maintaining each word's original form.

# Input:  "Hello World! Python is awesome"
# Output: "awesome is Python World! Hello"

# Input:  "SingleWord"
# Output: "SingleWord"




# var="Hello World! Python is awesome" #"sujan is name my"
# b=var.split() #["my","name","is","sujan"]
# c=b[::-1] #["sujan","is","name","my"]
# print(" ".join(c)) #"sujan is name my"


# Write a Python program that takes a list of numbers and give the second largest number in the list
# input=[4,5,1,4,2,3,8,9,11,55,0,9]
# output=11


a=[11,109,3,5,1,2,7]
a.sort() #[1,2,3,5,7,11]

print(a[-2])

# English to Nepali Dictionary
# o Create a simple English to Nepali dictionary using python dictionaries
# o Allow the user to enter English word and display their Nepali
# tranlations
# o Handle cases where the word is not found in the dictionary

words={
    "mother":"आमा",
    "sujan":"सुजन",
    "love":"माया",
    
}

user=input("Enter yoru word to translate into nepali : ")
v=words.get(user,"word is not found")
print(v)
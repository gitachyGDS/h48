# Project: Sissor ,Papper ,Rock game
import random

print("Welcome to Sissor ,Papper ,Rock game!!!")
print('''
      Choose one the following
      S-Scissor| R- Rock|P - Papper
      
      
      Rule :
      S beats P
      P beats R
      R beats S
            
      ''')

user=input("Enter your valid choice['S','P','R']: ").strip().upper()
computer=random.choice(['S','P','R'])


print(f"Your choice is {user}")
print(f"computer choice is {computer}")

if (user == 'S' and computer == 'P') or (user == 'P' and computer == 'R') or \
    (user == 'R' and computer == 'S'):
    print("You won !!!!")
    
elif user == computer:
    print("it's a draw")
    
elif user not in ['S','P','R']:
    print("Invalid input!, please try again ")
    
else:
    print("computer won!!!!")


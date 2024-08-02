# Rock, Paper and Scissor Game
import random
r = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
p = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
s = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Welcome to Rock, Paper and Scissor Game !")
user=int(input("Type: 1 for Rock, 2 for Paper , 3 for Scissor :\n"))
computer=random.randint(1,3)
print("You Choose :")
if (user==1):
    print(r)
elif (user==2):
    print(p)
elif (user==3):
    print(s)
else:
    print("Invalid Input!")

if (user==1 or user==2 or user==3):
    print("Computer Choose :")
    if (computer == 1):
        print(r)
    elif (computer == 2):
        print(p)
    elif (computer == 3):
        print(s)
    if (user == computer):
        print("It's a Draw!")
    elif (user == 1 and computer == 2):
        print("You Lose!")
    elif (user == 1 and computer == 3):
        print("You Win!")
    elif (user == 2 and computer == 1):
        print("You Win!")
    elif (user == 2 and computer == 3):
        print("You Lose!")
    elif (user == 3 and computer == 1):
        print("You Lose!")
    elif (user == 3 and computer == 2):
        print("You Win!")
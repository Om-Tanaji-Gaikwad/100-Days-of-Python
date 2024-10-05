# Guess the number Game
import random
print("Welcome to Guess the number Game !!!")
num=random.randint(1,100)
print("Hint :The number is between 1 to 100.")
level=input("Choose difficulty level - (hard or easy) :\n").lower()
if level == "easy":
    i = 10
    print(f"You choose {level} as difficulty level.")
elif level == "hard":
    i = 5
    print(f"You choose {level} as difficulty level.")
else:
    print("Invalid Input!")
    i=0
while 0<i:
    print(f"You have {i} guesses left")
    guess=int(input("Enter your guess :\n"))
    if guess==num:
        print("Your guess is right\nYou Won!")
        break
    elif guess<num:
        print("Your guess is lower than the number")
    elif guess>num:
        print("Your guess is higher than the number")
    i-=1
    if i==0:
        print("You run out of guesses.\nYou Lose!")
        break

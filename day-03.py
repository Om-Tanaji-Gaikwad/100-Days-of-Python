#Treasure Island choice game
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`." ` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
\n\n\n''')
print("Welcome to Treasure Island!!!")
print("You have to make multiple choices to find the Treasure")
print("You came across a road. Where you want to go ? (left or right)")
a=input()
if (a=="left"):
    print("You have came across a lake. What do you want to do ? (swim or wait)")
    b=input()
    if (b=="wait"):
        print("After sometime a boat came and took you to other side of lake.")
        print("You came across a blood thirsty and hungry lion. What do you want to do ?(run or pet or climb)")
        c=input()
        if (c=="pet"):
            print("You tried to pet lion and BOOM!!! He was a guardian of the treasure and He was waiting for kind and worthy person for treasure.")
            print("He gave you a chance to choose a room between three rooms with three different colours on each.")
            print("What will you choose? (red or yellow or blue)")
            d=input()
            if (d=="red"):
                print("You choose red, in that room there was Treasure!!!.")
                print("Congratulations! You won the Game !\nThanks for playing Game!!")
            elif (d=="yellow"):
                print("You choose yellow, in that room there was intense fire you were burned to death.\nGame Over!!! Better luck next time.\nThanks for playing Game!!")
            elif (d=="blue"):
                print("You choose blue, in that room there was intense coldness you were freezed to death.\nGame Over!!! Better luck next time.\nThanks for playing Game!!")
            else:
                print("Invalid Input")
        elif (c=="run"):
            print("You out runned and got eaten by the lion.\nGame Over!!! Better luck next time.\nThanks for playing Game!!")
        elif (c=="climb"):
            print("You climbed a tree,tree branch broke and you got eaten by the lion.\nGame Over!!! Better luck next time.\nThanks for playing Game!!")
        else:
            print("Invalid Input")
    elif (b=="swim"):
        print("You tried to swim and got eaten by the crocodiles.\nGame Over!!! Better luck next time.\nThanks for playing Game!!")
    else:
        print("Invalid Input")
elif (a=="right"):
    print("You fell in a hole and died.\nGame Over!!! Better luck next time.\nThanks for playing Game!!")
else :
    print("Invalid Input")
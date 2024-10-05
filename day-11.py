# BlackJack / 21 Game (Capstone Project)

import random
continue_play=True
while continue_play==True:
    play=input("\n\nDo you want to play Blackjack Game?(y-yes or n-no) :\n").lower()
    if play=="y":
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        a = random.choices(cards,k=2)
        b = random.choices(cards,k=1)
        computer_choice=random.choices(cards,k=2)
        print(f"Your cards :{a}, score:{sum(a)}")
        print(f"Computer's First card is {computer_choice[1]}")
        run=True
        while(run==True):
            pick_card = input("\nDo you want to pick another card?(y-yes or n-no) :\n").lower()
            if pick_card=="y":
                a+=b
                print(f"Your cards :{a}, score:{sum(a)}")
                if sum(a)>21:
                    run=False
                else:
                    print(f"Computer's First card is {computer_choice[1]}")
            else:
                run=False
        if sum(a)>21:
            print("Your score is exceded 21 , You lost")
        else:
            print(f"Your score is {sum(a)}\nComputer's score is {sum(computer_choice)}")
            if sum(a) < sum(computer_choice):
                print("You Lose!")
            elif sum(a) > sum(computer_choice):
                print("You Win !")
    else:
        continue_play=False
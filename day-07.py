# Hangman Game
import random
words=["apple","orange","mango"]
chosen_word =random.choice(words)
a=['''
      _______
     |/      |
     |      (_)
     |      /|/
     |       |
     |      / /
     |
    _|___
   '''
    ,
   '''
    _______
     |/      |
     |      (_)
     |      /|/
     |       |
     |       
     |
    _|___
   '''
   ,
   '''
    _______
     |/      |
     |      (_)
     |      /|/
     |       
     |      
     |
    _|___
   '''
    ,
   '''
   _______
     |/      |
     |      (_)
     |       |
     |       
     |      
     |
    _|___
   '''
   ,
   '''
   _______
     |/      |
     |      (_)
     |      
     |       
     |      
     |
    _|___
   '''
   ,
   '''
   _______
     |/      |
     |       |
     |    
     |       
     |      
     |
    _|___
   '''
   ,
   '''
   _______
     |/      
     |      
     |      
     |       
     |      
     |
    _|___
   ''']
word_length=len(chosen_word)
display=""
for letter in range(word_length):
    display+="_"
print(display)
lives=6
game_over=False
correct_letters=[]
while not game_over:
    guess = input("Enter your guess : ").lower()

    display2 = ""
    for letter in chosen_word:
        if letter == guess:
            display2 += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display2+= letter
        else:
            display2 += "_"
    if guess not in chosen_word:
        lives=lives-1
        print(f"You have chosen {guess}, is not in the word.\nLives left = {lives}")
    if guess in chosen_word:
        print(f"You have chosen {guess}, is in the word.\nLives left = {lives}")
    print(display2)
    print(a[lives])
    if lives==0:
        game_over=True
        print("You lose!")
    if "_" not in display2:
        game_over=True
        print("You win!")

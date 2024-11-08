# U.S. States Game

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image ="day_25_blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data=pandas.read_csv("day_25_50_states.csv")
all_states=data.state.to_list()
guessed_states=[]

while len(guessed_states)<50:
    answer_state=screen.textinput(title=f"{len(guessed_states)}/50 States Correct",prompt="What's another states name").title()

    if answer_state=="Exit":
        missing_states=[]
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("day_25_states_to_learn")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state == answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_state)




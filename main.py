import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

# reading data
data = pd.read_csv("50_states.csv")
all_states = data['state'].to_list()
guessed_states = []

while len(guessed_states)<50:
    answer_state = screen.textinput(title = f"{len(guessed_states)}/50 States Correct",
                                    prompt="Guess Another State Name").title()
    if answer_state == 'Exit':
        # states to learn.csv
        states_dict = {
            'states': [state for state in all_states if state not in guessed_states]
        }
        learn_states = pd.DataFrame(states_dict)
        learn_states.to_csv('learn_states.csv')
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)





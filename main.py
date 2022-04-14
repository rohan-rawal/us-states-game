import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
data = pd.read_csv("50_states.csv")
states = data["state"]
states = states.to_list()

name_of_state = turtle.Turtle()
name_of_state.hideturtle()
name_of_state.penup()
name_of_state.speed('fastest')
score = 0
while states:
    answer_state = screen.textinput(title=f"{score}/50 Guess the state", prompt="What's another State's name?")
    answer = answer_state.title()

    if answer == "Exit":
        break
    if answer in states:
        score += 1
        states.remove(answer)
        x_cor = int(data[data.state == answer].get("x").values)
        y_cor = int(data[data.state == answer].get("y").values)
        name_of_state.goto(x_cor, y_cor)
        name_of_state.write(answer, align='center')
    
    
states_missed = pd.Series(states)
states_missed.to_csv("states_to_learn.csv")
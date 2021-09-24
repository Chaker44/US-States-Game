from turtle import Screen, Turtle
from tkinter import messagebox
import pandas as pd

FONT = ("Arial", 10, 'normal')
screen = Screen()
screen.setup(width=800, height=500)
screen.title("States Game")
screen.bgpic("blank_states_img.gif")
data = pd.read_csv("50_states.csv")
names_of_the_states = data["state"].to_list()
number_of_state_count = 0
states_user = []
text = Turtle()
text.hideturtle()
while len(states_user) < 50:
    user_input = screen.textinput(
        title="  type exit to end the game" ,
        prompt=f"{number_of_state_count}/50 states found").title()
    if user_input == "Exit":
        missing_states_dict = {
            "states": names_of_the_states
        }
        serie_of_missing_states = pd.DataFrame(missing_states_dict)
        serie_of_missing_states.to_csv("Missing States.csv")
        break
    if user_input in names_of_the_states:
        number_of_state_count += 1
        row_state_chosen = data[data["state"] == user_input]
        position_in_the_map = (int(row_state_chosen["x"]), int(row_state_chosen["y"]))
        text.penup()
        text.goto(position_in_the_map)
        text.write(f"{row_state_chosen.state.item()}", font=FONT, align="center")
        states_user.append(user_input)
        index_of_state = names_of_the_states.index(user_input)
        names_of_the_states.pop(index_of_state)
    elif user_input in states_user:
        messagebox.showinfo(title="Warning", message="State already mentionned ")
    else:
        messagebox.showinfo(title="Wrong answer", message=f"{user_input} is not a state")

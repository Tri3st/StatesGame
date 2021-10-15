import turtle
from data_manager import DataManager

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

player_name = screen.textinput(title="YOUR NAME", prompt="Please enter your name..")
data_manager = DataManager(player_name)

while True:

  answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?")
  check_answer(answer_state)



turtle.mainloop()
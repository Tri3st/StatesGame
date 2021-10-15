import pandas
from player import Player

class DataManager:
  def __init__(self, player_name):
    self.data = pandas.read_csv("50_states.csv")
    self.states_list = self.data['state'].to_list()
    self.player = Player(player_name)
  

def check_answer(state):
  if state in self.states_list:
    #correct draw name in picture
    player.right_answer()
  else:
    #incorrect try again
    player.wrong_asnwer()
  #update score

def score_string():
  return f"{self.player}"
class Player:
  MAX_TURNS = 50
  
  def __init__(self, name):
    self.name = name
    self.score = 0
    self.turn = 0

  def right_answer(self):
    self.score += 1
    self.turn += 1

  def wrong_answer(self):
    self.turn += 1

  def __repr__(self):
    return f"{self.name} - score {self.score}/{self.turn}"

  def __str__(self):
    return f"{self.score}/{self.turn}"
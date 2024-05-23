from interface import EntityInterface

class Player(EntityInterface):
  def __init__(self, nickname):
    self.nickname = nickname
  
  def to_json(self):
    return { "nickname": self.nickname }

test = Player("root")
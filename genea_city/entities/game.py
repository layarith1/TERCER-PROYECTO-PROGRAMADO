from interface import EntityInterface

class Game(EntityInterface):
  def __init__(self, name):
    self.name = name

  def to_json(self):
    return { "name": self.name }
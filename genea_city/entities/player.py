class Player:
  def __init__(self, iD, name, gender, age):
    self.id = iD
    self.name = name
    self.gender = gender
    self.age = age
    self.alive = None

    self.father = None
    self.mother = None
    self.house = None

    self.couple = None
    self.childs = []

  def get_married(self, ihnabitant):
    print(ihnabitant)

  def have_a_child(self):
    pass
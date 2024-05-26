class House:
  def __init__(self, iD, x_axis, y_axis, occupants):
    self.id = iD
    self.x_axis = x_axis
    self.y_axis = y_axis
    self.occupants = occupants

    self.residents = []
  
  def add_residents(self, resident):
    pass
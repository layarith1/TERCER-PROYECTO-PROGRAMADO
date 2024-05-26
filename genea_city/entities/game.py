from datetime import date

class Game:
  def __init__(self, name, owner_id):
    self.name = name
    self.owner_id = owner_id
    self.created_at = date.today()
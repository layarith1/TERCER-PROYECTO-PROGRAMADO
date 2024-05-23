from engines import loader, writter
import os

class JOrm:
  def __init__(self, json_file, json_array):
    self.json_file = os.path.join(os.getcwd(), "data", json_file)
    self.json_array = json_array
    self.json_data = loader(self.json_file)

  def insert(self, data):
    self.json_data[self.json_array].append(data)
    writter(self.json_file, self.json_data)

  def delete(self, value):
    updated_data = list(filter(lambda record: record["id"] != value, self.json_data[self.json_array]))
    self.json_data[self.json_array] = updated_data
    writter(self.json_file, self.json_data)

  def find(self, value):
    return list(filter(lambda record: record["id"] == value, self.json_data[self.json_array]))

  def get_all(self):
    return self.json_data[self.json_array]
  
  def autoincrement(self):
    return self.json_data[self.json_array][-1]['id']+1
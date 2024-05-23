import json

def loader(json_file):
  with open(json_file, "r") as file:
    json_data = json.load(file)
  return json_data

def writter(json_file, json_data):
  with open(json_file, "w") as file:
    json.dump(json_data, file, indent=4)
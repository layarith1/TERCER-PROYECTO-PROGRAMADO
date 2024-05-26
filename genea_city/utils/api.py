from envs import get_env
import requests

def fetcher(url):
  response = requests.get(url=url)
  if (response.status_code == 200):
    return response.json()

def get_houses(x_axis, y_axis):
  url = f"{get_env("API_URL")}/getHouses/?x={x_axis}&y={y_axis}"
  data = fetcher(url=url)
  print(data)

def get_houses_residents(house_id):
  url = f"{get_env("API_URL")}/getHousesResidents/?houseId={house_id}"
  data = fetcher(url=url)
  print(data)

def get_inhabitant_information(inhabitant_id):
  url = f"{get_env("API_URL")}/getInhabitantInformation/?id={inhabitant_id}"
  data = fetcher(url=url)
  print(data)

def create_ihnabitant_union(inhabitant1_id, inhabitant2_id, new_house_x_axis, new_house_y_axis):
  url = f"{get_env("API_URL")}/createInhabitantUnion/?idInhabitant1={inhabitant1_id}&idInhabitant2={inhabitant2_id}&newHouseXPostition={new_house_x_axis}&newHouseYPostition={new_house_y_axis}"
  data = fetcher(url=url)
  print(data)

def create_children(name, inhabitant_id, gender, age):
  url = f"{get_env("API_URL")}/createChildren/?name={name}&idInhabitant={inhabitant_id}&gender={gender}&age={age}"
  data = fetcher(url=url)
  print(data)
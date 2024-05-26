from dotenv import load_dotenv
import os

load_dotenv()

def get_env(variable):
  return os.getenv(variable)
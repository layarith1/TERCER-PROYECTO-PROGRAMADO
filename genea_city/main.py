from dotenv import load_dotenv
import os

load_dotenv()

print("Hello World!")
print(os.getenv("MESSAGE"))
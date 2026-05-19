from dotenv import load_dotenv
import os

load_dotenv()

LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')
USERNAME = os.getenv('USERNAME')
INCORRECT_PASSWORD = os.getenv('INCORRECT_PASSWORD')
import os
from dotenv import load_dotenv


load_dotenv()  # take environment variables from .env.
config = os.environ.copy()

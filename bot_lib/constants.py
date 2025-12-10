from os import getenv
from typing import Text
from discord import Interaction
from dotenv import load_dotenv; load_dotenv()


TOKEN: Text = getenv('TOKEN')

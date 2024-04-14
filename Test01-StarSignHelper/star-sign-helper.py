import os
import openai
import tiktoken
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())  # read local .env file

openai.api_key = os.getenv('OPENAI_API_KEY')

class StarSignHelper():
    def __init__(self) -> None:
        self._nickname = ''
        self._birthday = ''

    def set_input(self, nickname, birthday):
        self._nickname = nickname
        self._birthday = birthday
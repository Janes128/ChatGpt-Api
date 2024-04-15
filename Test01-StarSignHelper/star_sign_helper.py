import os
import openai
import tiktoken
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())  # read local .env file

openai.api_key = os.getenv('API_KEY')

class StarSignHelper():
    def __init__(self) -> None:
        self._nickname = ''
        self._birthday = ''

        #openai.api_key = os.environ.get('OPENAI_API_KEY')

    def set_input(self, nickname, birthday):
        self._nickname = nickname
        self._birthday = birthday

    def generate_output(self):
        messages =  [  
            {'role':'system', 
            'content':"""You are an assistant who\
            responds in the style of Dr Seuss.\
            And output should be html structure."""},    
            {'role':'user', 
            'content':"""write me a very short poem\
            about a happy carrot"""},  
        ] 
        response = self.get_completion_from_messages(messages, temperature=1)
        print(messages)
        print(response)
        return response

    def get_completion_from_messages(self,
                                     messages, 
                                     model="gpt-3.5-turbo", 
                                     temperature=0, 
                                     max_tokens=500):
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=temperature, # this is the degree of randomness of the model's output
            max_tokens=max_tokens, # the maximum number of tokens the model can ouptut 
        )
        return response.choices[0].message["content"]
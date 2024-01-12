import openai
from dotenv import load_dotenv
from os import getenv
load_dotenv()

class ModelGpt:
    def __init__(self):
        self.api = getenv('OPENAI_API_KEY')

    def get_request(self, role, prompt):
        openai.api_key = self.api
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-1106",
            messages=[
                {"role": "system", "content": role},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content']

    def __str__(self) -> str:
        return "Model Gpt for request"
import os
from openai import OpenAI
from dotenv import load_dotenv
from function import GetOpenQData,Fetch,finish
from utils import get_completion

load_dotenv("./.env")

api_key = os.getenv("OPENAI_KEY")


def assist_res(msg):
  client = OpenAI(api_key=api_key)
  functionCalls = [GetOpenQData,Fetch,finish]

  messages=[
    {"role": "system", "content": "You answer questions - short and sweet."},
    {"role": "user", "content": f"{msg}"},
 ]

  message = get_completion(messages.copy(),functionCalls,client,'gpt-4o-mini')

  print(message)
  return message
# for testing on ipykernel vscode
# assist_res('give me stat about finance in qatar')








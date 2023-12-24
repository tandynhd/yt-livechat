import os
from dotenv import load_dotenv
load_dotenv()

# Set your OpenAI API key
# api_key = os.getenv("OPENAI_API_KEY")
api_key = "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"

from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)
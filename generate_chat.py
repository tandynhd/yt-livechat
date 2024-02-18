import os
from dotenv import load_dotenv
import openai

load_dotenv()

# Set your OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client with your API key
openai.api_key = api_key

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "assistant",
            "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair.",
        },
        {
            "role": "user",
            "content": "Compose a poem that explains the concept of recursion in programming.",
        },
    ],
)

print(completion.choices[0].message["content"])

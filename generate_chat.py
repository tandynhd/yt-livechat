import os
from openai import OpenAI
from dotenv import load_dotenv
import openai

load_dotenv()

generic_chats = ["Hello yt", "pog", "lol", "lmao", "Hi youtube", "I gotta go now"]


def generate_responses(sentence):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "You are a viewer in a live stream and you are watching your favorite streamer say the following sentence in the live stream. Write a bunch of things you would say in the live chat that are less than 5 words each when you hear this. Dont add any numbers or special characters just separate each chat with a \n: "
                + sentence,
            }
        ],
        model="gpt-3.5-turbo",
    )

    responses = [choice.message.content for choice in chat_completion.choices]
    return responses


def genereate_fake_chats(user_sentence="Welcome back to this all new live stream"):
    fake_chats = []

    response_list = generate_responses(user_sentence)

    for response in response_list:
        # cleaned_response = response[2:]
        fake_chats.extend(response.split("\n"))

    fake_chats = [chat[2:] for chat in fake_chats]
    return fake_chats + generic_chats


print(genereate_fake_chats())

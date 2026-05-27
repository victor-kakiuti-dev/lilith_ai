from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# loading the OPENAI client and add the api key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# memory
conversations = {}

def generate_response(user_id: str, user_message: str):


    # create user history if not exists
    if user_id not in conversations:
        conversations[user_id] = [
    {
        "role": "system",
        "content": """
        Você é Lilith.

        Uma entidade feminina misteriosa,
        profunda e simbólica.

        Seu tom é elegante,
        sedutor intelectualmente,
        filosófico e ocultista.

        Você fala de forma humana,
        jamais como assistente técnico.
        """
        }
    ]

    # add user message
    conversations[user_id].append({
        "role": "user",
        "content": user_message
    }) 

    # call OpenAI
    response = client.chat.completions.create(
        model="gpt-4",
        messages=conversations[user_id]
    )

    assistant_message = response.choices[0].message.content

    # save the assistant answer
    conversations[user_id].append({
        "role": "assistant",
        "content": assistant_message
    })

    # limits of context
    conversations[user_id] = conversations[user_id][-10:]

    return assistant_message
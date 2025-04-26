from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
chat = client.chats.create(model="gemini-2.0-flash")


def stream_ai_response(user_input):
    # Yield chunks of the AI response as they come.
    response = chat.send_message_stream(user_input)
    for chunk in response:
        yield chunk.text  # <-- yield small parts
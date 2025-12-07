# main.py
import requests
import json
import os
from typing import List, Dict
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

# KEY = os.getenv('API_KEY')


client = Groq(api_key=os.getenv("API_KEY"))

def get_reply(user_input):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",   # FREE + FAST
            messages=[
                {"role": "system", "content": "You are a helpful chatbot."},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"


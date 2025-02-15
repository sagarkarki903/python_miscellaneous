import os
from dotenv import load_dotenv
from groq import Groq
load_dotenv()

# Set API key manually (only for testing)
API_KEY = os.getenv("AI_CHABI")

client = Groq(api_key=API_KEY)

chat_completion = client.chat.completions.create(
    messages=[{"role": "user", "content": "How many countries are there?"}],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)

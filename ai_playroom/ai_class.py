import os
from dotenv import load_dotenv
from groq import Groq

class GroqChatbot:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("AI_CHABI")

        if not self.api_key:
            raise ValueError("API Key is missing! Check your .env file.")

        self.client = Groq(api_key=self.api_key)

        # 🧠 Custom memory (can be expanded later)
        self.custom_memory = {
            "Sagar": "Sagar is a talented software developer with expertise in AI and automation. He enjoys learning about finance and entrepreneurship. He plays guitar and sings too. ",
            "Karki": "Karki is a last name commonly associated with Nepal and South Asia. It is often used as a surname by various communities."
        }

    def chat(self, user_message):
        # 🛠️ Check if user mentions a known entity and inject info
        for name, fact in self.custom_memory.items():
            if name.lower() in user_message.lower():
                user_message += f"\n\nAdditional Context: {fact}"

        chat_completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": user_message}],
            model="llama-3.3-70b-versatile",
        )
        return chat_completion.choices[0].message.content

# Debugging
if __name__ == "__main__":
    bot = GroqChatbot()
    response = bot.chat("Tell me about Sagar")
    print("AI:", response)

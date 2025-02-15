from ai_class import GroqChatbot

bot = GroqChatbot()

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    response = bot.chat(user_input)
    print("Llama:", response)

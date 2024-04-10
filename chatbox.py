class RuleBasedChatbot:
    def __init__(self):
        self.rules = {
            "hi": "Hello! How can I assist you today?",
            "how are you?": "I'm just a bot, but thank you for asking!",
            "bye": "Goodbye! Have a great day!"
        }

    def respond(self, user_input):
        user_input = user_input.lower()
        response = self.rules.get(user_input, "I'm sorry, I don't understand that.")
        return response

if __name__ == "__main__":
    chatbot = RuleBasedChatbot()
    print("Welcome to the Rule-Based Chatbot!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Bot: Goodbye!")
            break
        else:
            response = chatbot.respond(user_input)
            print("Bot:", response)

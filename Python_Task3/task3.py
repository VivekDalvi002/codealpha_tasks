import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses
patterns = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]),
    (r"how are you?", ["I'm just a chatbot, but I'm here to chat!", "I'm good! How about you?"]),
    (r"what is your name?", ["I'm a chatbot, created just for you!", "Call me ChatBot"]),
    (r"bye|goodbye", ["Goodbye!", "See you later!", "Have a great day!"]),
    (r"(.*)", ["That's interesting!", "Tell me more!", "Hmm..."])
]

# Create chatbot instance
chatbot = Chat(patterns, reflections)

# Start conversation
print("Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "exit", "quit"]:
        print("Chatbot: Goodbye!")
        break
    response = chatbot.respond(user_input)
    print(f"Chatbot: {response}")

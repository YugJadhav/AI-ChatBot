import nltk
from nltk.tokenize import word_tokenize
from datetime import datetime
import random

nltk.download('punkt')

jokes = [
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Parallel lines have so much in common. It’s a shame they’ll never meet.",
    "Why don’t skeletons fight each other? They don’t have the guts."
]

user_name = ""

def preprocess(text):
    return word_tokenize(text.lower())

def get_intent(tokens):
    if "name" in tokens:
        return "name"
    if "joke" in tokens:
        return "joke"
    if "time" in tokens:
        return "time"
    if any(w in tokens for w in ["hi", "hello", "hey"]):
        return "greeting"
    if any(w in tokens for w in ["bye", "exit", "quit"]):
        return "farewell"
    return "unknown"

def respond(intent, tokens):
    global user_name
    if intent == "greeting":
        return "Hi there! What's your name?"
    elif intent == "name":
        if "your" in tokens:
            return "I'm ChatBot, your NLTK assistant."
        else:
            user_name = input("Bot: What should I call you?\nYou: ")
            return f"Nice to meet you, {user_name}!"
    elif intent == "joke":
        return random.choice(jokes)
    elif intent == "time":
        return f"It's {datetime.now().strftime('%I:%M %p')}."
    elif intent == "farewell":
        return "Goodbye! See you again."
    else:
        return "I didn't understand that."

def chatbot():
    print("Hello! I'm NLTK ChatBot. (Type 'exit' to quit)\n")
    while True:
        msg = input("You: ")
        if msg.lower() in ["exit", "bye", "quit"]:
            print("Bot: Goodbye!")
            break
        tokens = preprocess(msg)
        intent = get_intent(tokens)
        print("Bot:", respond(intent, tokens))

if __name__ == "__main__":
    chatbot()
    

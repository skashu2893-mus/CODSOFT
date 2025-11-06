# CODSOFT Task 1 - Chatbot with Rule-Based Responses
# Author: Shaik Ashu
# Date: 06-Nov-2025

import datetime
import time

def slow_print(text):
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(0.03)
    print()

def chatbot_response(text):
    text = text.lower()

    if "hi" in text or "hello" in text:
        return "Hello! How can I help you?"
    
    elif "how are you" in text:
        return "I'm good! Thanks for asking. How about you?"
    
    elif "your name" in text:
        return "I'm a simple chatbot created by Shaik Ashu."
    
    elif "time" in text:
        now = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {now}."
    
    elif "date" in text:
        today = datetime.date.today().strftime("%B %d, %Y")
        return f"Today's date is {today}."
    
    elif "codsoft" in text:
        return "CODSOFT is an internship platform that helps students grow with real projects."
    
    elif "internship" in text:
        return "CODSOFT provides internships in AI, Web Development and more!"
    
    elif "ai" in text or "artificial intelligence" in text:
        return "AI means Artificial Intelligence — machines that can think and learn."
    
    elif "thank" in text:
        return "You're welcome!"
    
    elif "bye" in text or "exit" in text:
        return "Goodbye! Have a nice day!"
    
    else:
        return "Sorry, I didn’t get that. Please try again."

print("CODSOFT Chatbot 🤖")
print("Type 'bye' to end the chat.")
print("------------------------------------")

while True:
    user = input("You: ")
    if "bye" in user.lower():
        slow_print("Bot: Goodbye! 👋")
        break
    reply = chatbot_response(user)
    print("Bot:", end=" ")
    slow_print(reply)
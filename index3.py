
# index3.py
# AI Chatbot with NLP in Python

import random
import string
import nltk
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download NLTK data (only first time)
nltk.download('punkt')
nltk.download('wordnet')

# Sample corpus for chatbot
corpus = """
Hello! I am your AI chatbot.
I can answer questions related to Python, AI, and Machine Learning.
Python is a programming language created by Guido van Rossum.
Machine Learning is a subset of AI that allows computers to learn from data.
Artificial Intelligence is the simulation of human intelligence by machines.
Natural Language Processing helps computers understand human language.
You can ask me questions about technology, programming, and AI.
If you say goodbye, I will exit the chat.
"""

# Preprocessing
sent_tokens = nltk.sent_tokenize(corpus)
lemmer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmer.lemmatize(token.lower()) for token in tokens if token not in string.punctuation]

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower()))

# Greeting responses
GREETING_INPUTS = ["hello", "hi", "greetings", "sup", "what's up", "hey"]
GREETING_RESPONSES = ["Hi there!", "Hello!", "Hey!", "Hi! How can I help you?"]

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

# Chatbot response
def chatbot_response(user_input):
    user_input = user_input.lower()
    if user_input in ['bye', 'exit', 'quit']:
        return "Goodbye! Have a great day!"

    if greeting(user_input) is not None:
        return greeting(user_input)

    sent_tokens.append(user_input)
    vectorizer = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = vectorizer.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]

    sent_tokens.pop()  # remove user input from corpus
    if req_tfidf == 0:
        return "I'm sorry! I don't understand."
    else:
        return sent_tokens[idx]

# Main loop
print("AI Chatbot: Hello! I am here to help. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Bot:", response)
    if response.lower().startswith("goodbye"):
        break

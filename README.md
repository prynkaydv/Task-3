# Task-3
AI CHATBOT WITH NLP

## 🤖 AI Chatbot with NLP (Python)

This project implements a *simple AI chatbot* using *Natural Language Processing (NLP)* techniques in Python.
It can respond to greetings, answer predefined knowledge-based queries, and handle basic conversation in natural language.

---

### 🚀 Features

* *Interactive Chat*: Responds to user input in real-time via the terminal.
* *NLP Preprocessing*:

  * Tokenization with *NLTK*
  * Lemmatization to reduce words to their base form
  * Stopword filtering
* *TF-IDF Vectorization*:

  * Converts text to numerical features for similarity comparison.
* *Cosine Similarity*:

  * Matches the most relevant response from the chatbot’s knowledge base.
* *Custom Greetings & Exit Commands*:

  * Responds to greetings with predefined friendly messages.
  * Ends the conversation when the user types "bye", "exit", or "quit".

---

### 🛠 Technologies Used

* *Python* – Core programming language
* *NLTK* – Natural Language Processing toolkit
* *scikit-learn* – TF-IDF vectorization & similarity
* *NumPy* – Numerical computations

---

### 📂 How It Works

1. *Knowledge Base*

   * A sample text corpus is defined with facts about Python, AI, ML, and NLP.

2. *Text Preprocessing*

   * Tokenizes sentences.
   * Lemmatizes words to their root form.
   * Removes punctuation and stopwords.

3. *User Interaction Loop*

   * Reads input from the user.
   * If it’s a greeting, responds with a friendly message.
   * Otherwise, finds the most similar sentence in the corpus using *TF-IDF* and *cosine similarity*.
   * Returns the matching response or says it doesn’t understand.

4. *Exit Handling*

   * Stops the chat when the user enters an exit command.

---

### ▶ How to Run

bash
# Install dependencies
pip install nltk scikit-learn numpy

# Run the chatbot
python index3.py


The first time you run, NLTK will download required resources (punkt, wordnet).

---

### 💬 Example Conversation

```
AI Chatbot: Hello! I am here to help. Type 'bye' to exit.
You: hi
Bot: Hello!
You: what is python
Bot: Python is a programming language created by Guido van Rossum.
You: bye
Bot: Goodbye! Have a great day!
``


# AI ChatBot using NLTK – Task 3

This is a simple rule-based chatbot built using **Python** and the **Natural Language Toolkit (NLTK)** as part of my internship task. It can respond to greetings, tell jokes, tell the time, and answer simple questions like "What's your name?"

---

## Features

- Greets the user
- Tells the current time
- Responds to questions like:
  - "What is your name?"
  - "Tell me a joke"
  - "How are you?"
  - "Bye"
- Understands text using NLTK's tokenizer

---

## Technologies Used

- **Python**
- **NLTK** (Natural Language Toolkit)
- **datetime** (to show time)
- **random** (to select random jokes)

---

## Installation

Install the required package:

```bash
pip install nltk
```

Download required NLTK data:

```python
import nltk
nltk.download('punkt')
```

---

## How to Run

1. Open your terminal or IDE
2. Run:

```bash
python main.py
```

---

## Sample Interaction

```
Hello! I'm NLTK ChatBot. (Type 'exit' to quit)

You: hi
Bot: Hello! How can I assist you?

You: tell me a joke
Bot: Why did the scarecrow win an award? Because he was outstanding in his field!

You: what time is it?
Bot: The current time is 08:45 PM.

You: bye
Bot: Goodbye! Have a great day!
```
---
This chatbot is built only using **NLTK**, without internet-based modules like Wikipedia. It is rule-based and suitable for basic text interactions.
"""
chatbot.py
----------
Rule-Based Chatbot Logic Module.

Contains all chatbot rules and response functions.
No Machine Learning, No AI APIs — Pure Python if-else logic.
"""

import random
from datetime import datetime


# ─────────────────────────────────────────────
#  Response Pools (multiple replies per intent)
# ─────────────────────────────────────────────

GREETING_RESPONSES = [
    "Hello! 👋 Welcome to the Rule-Based AI Chatbot.\nHow can I help you today?",
    "Hey there! 😊 Great to see you!\nWhat can I do for you?",
    "Hi! 👋 I'm your friendly Rule-Based Chatbot.\nFeel free to ask me anything!",
    "Good to see you! 🌟 I'm here and ready to chat.\nHow can I assist you?",
]

HOW_ARE_YOU_RESPONSES = [
    "I'm doing great, thank you for asking! 😄\nHow about you?",
    "I'm functioning perfectly! All systems go! 🤖\nHow are you doing?",
    "Feeling fantastic as always! 😊 Ready to help you!",
]

THANKS_RESPONSES = [
    "You're welcome! 😊 Happy to help!",
    "Anytime! 🌟 That's what I'm here for!",
    "No problem at all! Let me know if you need anything else. 😄",
    "My pleasure! 🤖 Feel free to ask more questions!",
]

UNKNOWN_RESPONSES = [
    "I'm sorry, I don't understand that yet. Please ask another question. 🤔",
    "Hmm, I'm not sure how to respond to that. Try asking something else! 😅",
    "I'm still learning! That's a bit beyond my current rules. 🤖",
    "I don't have a response for that yet. Could you rephrase it? 💭",
]


# ─────────────────────────────────────────────
#  Knowledge Base (topic → response)
# ─────────────────────────────────────────────

KNOWLEDGE_BASE = {
    "python": (
        "🐍 Python is a high-level, easy-to-learn programming language.\n\n"
        "It is widely used in:\n"
        "  • Web Development (Django, Flask)\n"
        "  • Artificial Intelligence & Machine Learning\n"
        "  • Data Science & Analytics\n"
        "  • Automation & Scripting\n"
        "  • Scientific Computing\n\n"
        "Created by Guido van Rossum in 1991, Python values\n"
        "readability and simplicity above all else."
    ),
    "ai": (
        "🤖 Artificial Intelligence (AI) is the simulation of\n"
        "human intelligence by computer systems.\n\n"
        "Key areas of AI include:\n"
        "  • Machine Learning (ML)\n"
        "  • Natural Language Processing (NLP)\n"
        "  • Computer Vision\n"
        "  • Robotics\n"
        "  • Expert Systems\n\n"
        "Fun fact: This chatbot uses rule-based logic,\n"
        "the original form of AI! 😊"
    ),
    "programming": (
        "💻 Programming is the art of giving instructions\n"
        "to a computer to perform tasks.\n\n"
        "Popular programming languages:\n"
        "  • Python — AI, Data Science, Web\n"
        "  • JavaScript — Web & App Development\n"
        "  • Java — Enterprise & Android\n"
        "  • C/C++ — Systems & Game Dev\n"
        "  • SQL — Database Management\n\n"
        "Tip: Start with Python — it's beginner-friendly!"
    ),
    "chatbot": (
        "🤖 A Chatbot is a software program that simulates\n"
        "human conversation through text or voice.\n\n"
        "Types of chatbots:\n"
        "  • Rule-Based — Uses if-else logic (like me!)\n"
        "  • AI/ML-Based — Uses trained models\n"
        "  • Hybrid — Combines both approaches\n\n"
        "I am a Rule-Based chatbot built with Python\n"
        "and CustomTkinter for the GUI. 😊"
    ),
    "technology": (
        "🔬 Technology refers to the application of scientific\n"
        "knowledge for practical purposes.\n\n"
        "Modern tech trends include:\n"
        "  • Artificial Intelligence (AI)\n"
        "  • Cloud Computing\n"
        "  • Internet of Things (IoT)\n"
        "  • Blockchain\n"
        "  • Augmented & Virtual Reality\n"
        "  • Quantum Computing\n\n"
        "Technology is shaping the future every single day!"
    ),
    "computer": (
        "🖥️ A computer is an electronic device that processes\n"
        "data according to a set of instructions (programs).\n\n"
        "Key components:\n"
        "  • CPU — Central Processing Unit (the 'brain')\n"
        "  • RAM — Random Access Memory (short-term)\n"
        "  • Storage — HDD/SSD (long-term memory)\n"
        "  • GPU — Graphics Processing Unit\n"
        "  • Motherboard — Connects everything\n\n"
        "Computers have revolutionized every field of human work!"
    ),
    "machine learning": (
        "🧠 Machine Learning is a subset of AI where systems\n"
        "learn from data to improve their performance.\n\n"
        "Types of ML:\n"
        "  • Supervised Learning\n"
        "  • Unsupervised Learning\n"
        "  • Reinforcement Learning\n\n"
        "Note: This chatbot does NOT use ML —\n"
        "it relies purely on rule-based logic! ✅"
    ),
    "internet": (
        "🌐 The Internet is a global network of interconnected\n"
        "computers that communicate using standard protocols.\n\n"
        "Key services on the Internet:\n"
        "  • World Wide Web (WWW)\n"
        "  • Email\n"
        "  • Online Streaming\n"
        "  • Cloud Computing\n"
        "  • Social Media\n\n"
        "The Internet was publicly launched in 1991!"
    ),
    "data science": (
        "📊 Data Science is an interdisciplinary field that\n"
        "extracts insights from structured and unstructured data.\n\n"
        "Tools used in Data Science:\n"
        "  • Python & R (programming)\n"
        "  • Pandas & NumPy (data manipulation)\n"
        "  • Matplotlib & Seaborn (visualization)\n"
        "  • Scikit-learn (machine learning)\n"
        "  • SQL (database querying)\n\n"
        "Data Science is one of the hottest careers of the decade!"
    ),
}


# ─────────────────────────────────────────────
#  Time-Aware Greeting Helper
# ─────────────────────────────────────────────

def get_time_greeting():
    """Return a greeting based on the current hour of the day."""
    hour = datetime.now().hour
    if 5 <= hour < 12:
        return "Good Morning! ☀️"
    elif 12 <= hour < 17:
        return "Good Afternoon! 🌤️"
    elif 17 <= hour < 21:
        return "Good Evening! 🌙"
    else:
        return "Good Night! 🌟"


# ─────────────────────────────────────────────
#  Exit Command Checker
# ─────────────────────────────────────────────

def is_exit_command(user_input: str) -> bool:
    """
    Check if the user typed an exit command.

    Args:
        user_input (str): The user's input string.

    Returns:
        bool: True if exit command, False otherwise.
    """
    exit_keywords = ["exit", "quit", "bye", "goodbye", "see you", "farewell"]
    return any(keyword in user_input for keyword in exit_keywords)


# ─────────────────────────────────────────────
#  Main Response Generator
# ─────────────────────────────────────────────

def get_response(user_input: str) -> tuple[str, bool]:
    """
    Generate a rule-based response for the given user input.

    Uses a cascading if-elif-else structure to match user input
    against predefined rules. No ML or external APIs are used.

    Args:
        user_input (str): The raw text input from the user.

    Returns:
        tuple[str, bool]: (response_text, should_exit)
            - response_text: The chatbot's reply string.
            - should_exit: True if the app should close after showing reply.
    """
    # Normalize: lowercase and strip whitespace
    text = user_input.strip().lower()

    # ── Guard: empty input ──────────────────────────────────────
    if not text:
        return "Please type a message first! 😊", False

    # ── EXIT commands ────────────────────────────────────────────
    if is_exit_command(text):
        return (
            "Goodbye! 👋 It was great chatting with you!\n"
            "Have a wonderful day! See you next time! 😊",
            True
        )

    # ── GREETINGS ────────────────────────────────────────────────
    greeting_keywords = ["hi", "hello", "hey", "hiya", "howdy",
                         "good morning", "good afternoon", "good evening",
                         "good night", "greetings", "what's up", "sup"]
    if any(text == kw or text.startswith(kw) for kw in greeting_keywords):
        return random.choice(GREETING_RESPONSES), False

    # ── NAME / IDENTITY ───────────────────────────────────────────
    if any(phrase in text for phrase in ["your name", "who are you",
                                          "what are you", "introduce yourself",
                                          "tell me about yourself"]):
        return (
            "I'm the Rule-Based AI Chatbot! 🤖\n\n"
            "I was built using Python and CustomTkinter.\n"
            "I respond to your messages using predefined\n"
            "conditional rules — no ML, no AI APIs!\n\n"
            "Ask me about Python, AI, Programming,\n"
            "Chatbots, Technology, or Computers! 😊"
        ), False

    # ── HOW ARE YOU ───────────────────────────────────────────────
    if any(phrase in text for phrase in ["how are you", "how do you do",
                                          "are you okay", "you okay",
                                          "how's it going", "how are things"]):
        return random.choice(HOW_ARE_YOU_RESPONSES), False

    # ── WHAT CAN YOU DO ───────────────────────────────────────────
    if any(phrase in text for phrase in ["what can you do", "your features",
                                          "help me", "what do you know",
                                          "capabilities", "commands",
                                          "what can i ask"]):
        return (
            "Here's what I can help you with! 📋\n\n"
            "💬 Greetings & Small Talk\n"
            "❓ Answer basic questions about me\n"
            "📚 Topics I know about:\n"
            "   • Python\n"
            "   • Artificial Intelligence (AI)\n"
            "   • Programming\n"
            "   • Chatbots\n"
            "   • Technology\n"
            "   • Computers\n"
            "   • Machine Learning\n"
            "   • Data Science\n"
            "   • Internet\n\n"
            "Just type a topic and I'll explain it! 🚀"
        ), False

    # ── THANK YOU ─────────────────────────────────────────────────
    if any(phrase in text for phrase in ["thank you", "thanks", "thank u",
                                          "thx", "ty", "appreciate",
                                          "grateful"]):
        return random.choice(THANKS_RESPONSES), False

    # ── JOKES ─────────────────────────────────────────────────────
    if any(phrase in text for phrase in ["joke", "make me laugh",
                                          "funny", "tell me a joke"]):
        jokes = [
            "Why do programmers prefer dark mode?\n"
            "Because light attracts bugs! 🐛😄",

            "Why did the Python programmer get confused?\n"
            "Because they had too many indentations! 🐍😄",

            "A SQL query walks into a bar and sees two tables.\n"
            "It walks up to them and asks: 'Can I join you?' 😄",

            "Why don't scientists trust atoms?\n"
            "Because they make up everything! ⚛️😄",

            "I asked an AI if it could pass the Turing Test.\n"
            "It said: 'Maybe.' I'm still not sure... 🤖😄",
        ]
        return random.choice(jokes), False

    # ── TIME / DATE ───────────────────────────────────────────────
    if any(phrase in text for phrase in ["time", "date", "today",
                                          "what day", "current time",
                                          "what is the time"]):
        now = datetime.now()
        return (
            f"📅 Current Date & Time:\n\n"
            f"   Date : {now.strftime('%A, %B %d, %Y')}\n"
            f"   Time : {now.strftime('%I:%M:%S %p')}\n\n"
            f"{get_time_greeting()}"
        ), False

    # ── KNOWLEDGE BASE (topics) ───────────────────────────────────
    for topic, response in KNOWLEDGE_BASE.items():
        # Match if user input contains the topic keyword
        if topic in text:
            return response, False

    # ── COMPLIMENTS (User is kind to the bot) ────────────────────
    if any(phrase in text for phrase in ["good bot", "nice", "awesome",
                                          "great", "amazing", "excellent",
                                          "cool", "love you", "you are great"]):
        return (
            "Aww, thank you so much! 😊💙\n"
            "You just made my circuits smile! 🤖✨\n"
            "Is there anything else I can help you with?"
        ), False

    # ── INSULTS / NEGATIVE FEEDBACK ──────────────────────────────
    if any(phrase in text for phrase in ["stupid", "dumb", "useless",
                                          "bad bot", "hate you",
                                          "worst", "terrible"]):
        return (
            "I'm sorry to hear that. 😔\n"
            "I'm just a simple rule-based bot with limited\n"
            "knowledge. I'll try to do better!\n\n"
            "Is there something specific I can help with? 😊"
        ), False

    # ── AGE ───────────────────────────────────────────────────────
    if any(phrase in text for phrase in ["how old", "your age", "age"]):
        return (
            "I don't really have an age! 🤖\n"
            "I was coded into existence and don't experience\n"
            "time the way humans do.\n\n"
            "But if you count from when my code was written,\n"
            "I'm brand new! ✨"
        ), False

    # ── CREATOR ───────────────────────────────────────────────────
    if any(phrase in text for phrase in ["who made you", "who created you",
                                          "who built you", "your creator",
                                          "your developer"]):
        return (
            "I was built by a Python developer as a\n"
            "university project! 🎓\n\n"
            "Tech used to create me:\n"
            "  • Python 3.x\n"
            "  • CustomTkinter (for the GUI)\n"
            "  • Pure if-else logic (no ML/AI APIs)\n\n"
            "Pretty cool for a rule-based bot, right? 😊"
        ), False

    # ── FALLBACK (Unknown input) ──────────────────────────────────
    return random.choice(UNKNOWN_RESPONSES), False

# 🤖 Rule-Based AI Chatbot

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-5.2+-6366F1?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![No ML](https://img.shields.io/badge/No%20ML%20%2F%20No%20AI%20APIs-✅-success?style=for-the-badge)

**A modern, clean, fully offline Rule-Based AI Chatbot built with Python and CustomTkinter.**  
No Machine Learning. No OpenAI. No external APIs. 100% pure Python conditional logic.

</div>

---

## 📋 Table of Contents

- [Description](#-description)
- [Features](#-features)
- [Technologies Used](#-technologies-used)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [How to Run](#-how-to-run)
- [How to Use](#-how-to-use)
- [Screenshots](#-screenshots)
- [Future Improvements](#-future-improvements)

---

## 📖 Description

This project is a **Rule-Based AI Chatbot** built entirely with Python. It responds to predefined user inputs using `if-elif-else` conditional logic — no machine learning, no APIs, no internet connection required.

The chatbot features a **modern GUI** built with [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter), featuring chat bubbles, dark mode, typing animations, timestamps, and a clean color palette suitable for a portfolio or university submission.

---

## ✨ Features

### 💬 Chat Features
| Feature | Description |
|---|---|
| **Greeting Recognition** | Responds to `hi`, `hello`, `hey`, `good morning/afternoon/evening` |
| **Basic Q&A** | Answers questions about name, how-are-you, capabilities |
| **Knowledge Topics** | Python, AI, Programming, Chatbots, Technology, Computers, ML, Data Science, Internet |
| **Jokes** | Tells programming & tech jokes |
| **Date & Time** | Shows current date and time |
| **Exit Command** | `exit`, `quit`, `bye` closes the app gracefully |
| **Unknown Input** | Friendly fallback message for unrecognized inputs |
| **Continuous Conversation** | Runs indefinitely until exit command |

### 🖥️ GUI Features
| Feature | Description |
|---|---|
| **Chat Bubbles** | User messages right (blue), Bot messages left (gray) |
| **Robot Avatar** | 🤖 emoji avatar next to every bot message |
| **Timestamps** | Every message shows the time it was sent |
| **Typing Animation** | "Bot is typing…" indicator before each response |
| **Dark Mode** 🌙 | Toggle between Light and Dark themes |
| **Scrollable Chat** | Auto-scrolls to latest message |
| **Enter Key Shortcut** | Press `Enter` to send messages |
| **Auto-clear Input** | Input field clears after sending |
| **Clear Chat Button** | Clear history with a confirmation dialog |
| **Exit Button** | Exit with a confirmation dialog |
| **Window Icon** | Custom robot icon in the title bar |
| **Responsive** | Window is resizable and maintains layout |
| **Welcome Message** | Time-aware greeting shown on startup |

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python 3.x** | Core programming language |
| **CustomTkinter 5.2+** | Modern GUI framework (built on Tkinter) |
| **Tkinter (built-in)** | Message dialogs (messagebox) |
| **threading** | Non-blocking typing animation |
| **datetime** | Timestamps and time-aware greetings |
| **random** | Multiple varied responses per intent |

> ✅ **No Machine Learning**  
> ✅ **No OpenAI / Gemini / HuggingFace APIs**  
> ✅ **No LangChain or any NLP library**  
> ✅ **Works completely offline**

---

## 📁 Project Structure

```
RuleBasedChatbot/
│
├── main.py          # Entry point — run this file
├── chatbot.py       # Rule-based logic (if-else responses)
├── ui.py            # GUI — all CustomTkinter widgets & layout
│
├── assets/
│   └── robot.png    # Robot icon for window titlebar
│
├── requirements.txt # Python dependencies
└── README.md        # This file
```

### File Responsibilities

| File | Responsibility |
|---|---|
| `main.py` | Checks dependencies, launches the app |
| `chatbot.py` | All chatbot rules, response pools, knowledge base |
| `ui.py` | All GUI code — widgets, themes, event handlers |
| `assets/robot.png` | Window icon image |

---

## 💾 Installation

### Prerequisites
- Python 3.8 or higher installed on your system
- `pip` package manager

### Step 1 — Clone or Download the Project

```bash
# If using Git:
git clone https://github.com/your-username/RuleBasedChatbot.git
cd RuleBasedChatbot

# Or simply download and extract the ZIP file
```

### Step 2 — (Recommended) Create a Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- `customtkinter` — Modern GUI framework
- `Pillow` — Image support for window icon (optional)

---

## ▶️ How to Run

```bash
python main.py
```

The chatbot window will open automatically.

> **Windows users:** You can also double-click `main.py` if Python is associated with `.py` files.

---

## 💬 How to Use

| You type... | Bot responds with... |
|---|---|
| `hi` / `hello` / `hey` | A friendly greeting |
| `what is your name` | Bot's identity and description |
| `how are you` | A positive status reply |
| `what can you do` | List of capabilities |
| `tell me about python` | Explanation of Python |
| `tell me about ai` | Overview of Artificial Intelligence |
| `tell me about programming` | Languages and tips |
| `tell me about chatbots` | Chatbot types and how this one works |
| `tell me about technology` | Modern tech trends |
| `tell me about computers` | Computer components |
| `tell me a joke` | A programming joke |
| `what time is it` | Current date and time |
| `thank you` | You're welcome response |
| `exit` / `quit` / `bye` | Goodbye message + app closes |
| *(anything else)* | "I don't understand that yet" |

### Keyboard Shortcuts
| Shortcut | Action |
|---|---|
| `Enter` | Send message |
| 🌙 Dark button | Toggle dark/light mode |
| 🗑 Clear button | Clear chat history (with confirmation) |
| ✕ Exit button | Close the app (with confirmation) |

---

## 📸 Screenshots

> *Run the application to see the live UI!*

| Light Mode | Dark Mode |
|---|---|
| *(screenshot placeholder)* | *(screenshot placeholder)* |

---

## 🚀 Future Improvements

Here are features that could be added in future versions:

| Feature | Description |
|---|---|
| **Fuzzy Matching** | Handle typos using `difflib` or `fuzzywuzzy` |
| **File-based Rules** | Load responses from a JSON/YAML config file |
| **Chat Export** | Save conversation history to a `.txt` or `.pdf` file |
| **Multi-language** | Support greetings in multiple languages |
| **Text-to-Speech** | Speak bot responses using `pyttsx3` |
| **Custom Themes** | Let users pick accent colors |
| **Sound Effects** | Play a soft chime when a message is sent |
| **History Search** | Search through past messages |
| **Emoji Picker** | Built-in emoji selector for input |

---

## 👨‍💻 Author

Built as a **university assignment** demonstrating:
- Python GUI development with CustomTkinter
- Software architecture (separation of concerns)
- Clean code practices and documentation
- Rule-based AI systems

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<div align="center">

Made with ❤️ and Python 🐍

</div>

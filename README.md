# AI ChatBot Assistant 🤖

An intelligent AI-powered chatbot with a clean, responsive GUI built using PyQt5 and Google's Gemini API.
It streams AI-generated messages in real-time, creating a natural, human-like conversation experience.

## 📚 Table of Contents

- About
- Features
- Tech Stack
- Setup Instruction
- Usage
- Video Walkthrough
- Folder Structure
- Future Improvements
- License

## 📖 About

AI ChatBot Assistant is a desktop chat application that lets users interact with an AI in real-time.
The chatbot streams its responses character-by-character to simulate real typing, delivering a more engaging and dynamic chat experience.

## ✨ Features

- 📡 Real-time streaming of AI responses
- 🎨 Modern, clean GUI using PyQt5
- 🧹 Clear Chat button to reset the conversation
- ⚡ Fast message typing simulation
- 🔒 Environment-based API key management

## Tech Stack 🛠

- Python 3.10+
- PyQt5
- Google Gemini API

## Setup Instructions 🛠️

1. Clone the Repository
```bash
git clone https://github.com/your-username/ai-chat-assistant.git
cd ai-chat-assistant
```

2. Create a virtual environment and activate it
```bash
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up your environment variables Create a .env file in the root directory:
```bash
GEMINI_API_KEY=your_api_key_here
```

5. Run the application
```bash
python gui.py
```
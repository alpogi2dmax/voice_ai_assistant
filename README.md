# Mini Voice AI Assistant (CLI)

A simple command-line voice AI assistant in Python with wake word detection using Picovoice Porcupine.

## Features

- Listens continuously for a wake word (default: "computer")
- After wake word is detected, records your voice input
- Transcribes speech to text
- Sends text to GPT for a response
- Speaks out the response via TTS
- Exit by saying "exit", "quit", or pressing Ctrl+C

## Requirements

- Python 3.7+
- See `requirements.txt` (example below)

## Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/yourusername/mini-voice-ai.git
   cd mini-voice-ai

2. Create and activate a virtual environment

   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/lINUX
   venv\Scripts\activate      # Windows

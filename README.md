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

3. Install dependencies

   ```bash
   pip install -r requirements.txt

4. Get a free Porcupine Access Key:

   - Sign up at https://console.picovoice.ai/
   - Create a Porcupine project and copy your Access Key

5. Add your Access Key to main.py (replace "YOUR_ACCESS_KEY_HERE")

   ```python

   porcupine = pvporcupine.create(
      access_key = "YOUR_ACCESS_KEY_HERE",
      keywords=["computer"]
   )

## Usage

Run the assistant:

```bash

python main.py

   * The app willl isten for the wake word "computer".
   * After the wake word, speak your comman or question.
   * To quit, say "exit", "quit", or press Ctrl+c.
   

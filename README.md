# Behind The Code — AI Assistant

A Python terminal assistant powered by Groq, using `openai/gpt-oss-120b`. Responses stream to the terminal and conversation history is kept while the program runs.

## Setup

Install Python 3.10 or newer, then run:

```bash
git clone https://github.com/dasunravihansa/Behind-The-Code.git
cd Behind-The-Code
python -m pip install -r requirements.txt
```

In your local `main.py`, replace `PASTE_YOUR_GROQ_API_KEY_HERE` with your Groq API key from https://console.groq.com/keys. Keep your real key private; do not commit the edited key to GitHub.

## Run

```bash
python main.py
```

Type your question and press Enter. Type `exit` to quit.

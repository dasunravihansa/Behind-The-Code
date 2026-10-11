from groq import Groq

# ==================================
# Behind The Code - AI Assistant
# ==================================

# Replace with your private API key (do not commit your real key to GitHub).
API_KEY = "PASTE_YOUR_GROQ_API_KEY_HERE"

MODEL = "openai/gpt-oss-120b"

client = Groq(api_key=API_KEY)

# Conversation history
history = [
    {
        "role": "system",
        "content": (
            "You are a helpful AI assistant "
            "created for Behind The Code. "
            "Explain things clearly and "
            "help users with programming."
        )
    }
]


def ask_ai(question):
    history.append({
        "role": "user",
        "content": question
    })

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=history,
            temperature=0.6,
            max_completion_tokens=1024,
            stream=True
        )

        print("\nAI: ", end="", flush=True)
        full_response = ""

        for chunk in response:
            content = chunk.choices[0].delta.content
            if content:
                print(content, end="", flush=True)
                full_response += content

        print("\n")

        history.append({
            "role": "assistant",
            "content": full_response
        })

    except Exception as error:
        history.pop()
        print("\nError:", error)


def main():
    print("=" * 40)
    print("     BEHIND THE CODE")
    print("       AI ASSISTANT")
    print("=" * 40)

    print("\nModel:", MODEL)
    print("Type 'exit' to quit.\n")

    while True:
        question = input("You: ").strip()

        if question.lower() == "exit":
            print("\nGoodbye!")
            break

        if not question:
            continue

        ask_ai(question)


if __name__ == "__main__":
    main()

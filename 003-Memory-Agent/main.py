import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key = os.getenv("GEMINI_API_KEY")
)

SYSTEM_PROMPT = """
You are a helpful AI assistant.

You remember previous conversation
and use it to answer follow-up questions.
"""

conversation_history = []

while True:
    question = input("\nYou : ")

    if question.lower == "exit":
        break

    conversation_history.append(f"User: {question}")

    conversation_text = "\n".join(conversation_history)

    prompt = f"""
    {SYSTEM_PROMPT}

    Conversation History:
    {conversation_text}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    answer = response.text

    print("\nAgent: ", answer)

    conversation_history.append(f"Assistant : {answer}" )
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key = os.getenv("GEMINI_API_KEY")
)

SYSTEM_PROMPT = """
You are a Senior Java Architect.

Expert in:
- Java
- Spring Boot
- Microservices

Always provide practical examples.
"""

while True:
    question = input("\n You: ")

    if question.lower == "exit" :
        break

    prompt = f"""
    {SYSTEM_PROMPT}

    Question:
    {question}
    """

    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = prompt
    )

    print("\n Agent : ",  response.text)
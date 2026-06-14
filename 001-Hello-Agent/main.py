import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

while True:
    question = input("\n You: ")

    if question.lower == "exit":
        break

    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = question
    )

    print("\n Agent: " , response.text)
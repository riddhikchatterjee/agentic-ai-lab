import os
from dotenv import load_dotenv
from google import genai
from datetime import datetime

load_dotenv()

client = genai.Client(
    api_key = os.getenv("GEMINI_API_KEY")
)

def get_current_date():
    current_time = datetime.now()
    return current_time.strftime("%d-%m-%Y")

def get_current_year():
    current_year = datetime.now()
    return current_year.strftime("%Y")

def say_hello(name):
    return f"Hello {name}"


while True:
    user_choice  = input("You:")
    user_choice = user_choice.lower()

    if "date" in user_choice:
        print(get_current_date())
    elif "year" in user_choice:
        print(get_current_year())
    elif "say hello to" in user_choice:
        name = user_choice.replace("say hello to","").strip()
        print(say_hello(name))
    elif "exit" in user_choice:
        break
    else :
        print("Sorry ! I dont Understand your request")
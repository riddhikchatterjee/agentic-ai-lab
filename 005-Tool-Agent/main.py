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
    user_choice  = input("""
    Please enter your choice :
    1. Current Date
    2. Current Year
    3. Say Hello
    4. Exit
    """)

    if user_choice == "1":
        print(get_current_date())
    elif user_choice == "2":
        print(get_current_year())
    elif user_choice == "3":
        name = input("\n whats your name:")
        print(say_hello(name))
    elif user_choice == "4":
        break;
    else :
        print(""" Invalid option!!!
        Please choose from the menu""")
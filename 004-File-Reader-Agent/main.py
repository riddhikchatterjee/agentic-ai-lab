import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key = os.getenv("GEMINI_API_KEY")
)

#print("File Reader started")

file_path = input("\nEnter the file path :")

try:
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

        print("\nFile loaded successfully")
        print("""\nFile loaded successfully.

            Choose an action:

            1. Summarize
            2. Analyze
            3. Extract Key Points
            4. Explain Like I'm a Beginner
            5. Custom Question
        """)

        choice = input("\nEnter Option:")

        if choice == "1":
            instruction = "Summarize this document."

        elif choice == "2":
            instruction = "Analyze this document."

        elif choice == "3":
            instruction = "Extract the key points from this document."

        elif choice == "4":
            instruction = "Explain this document as if teaching a beginner."

        elif choice == "5":
            instruction = input(
                "Enter your question about the document: "
            )

        else:
            print("Invalid option selected.")
            exit()

        
        
        prompt = f"""
        {instruction}
        Document:
        {content}
        """
        print("\nProcessing document...\n")
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        print("\nAgent: ",response.text)





except FileNotFoundError:
    print("Check file path")

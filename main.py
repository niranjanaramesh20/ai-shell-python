import os
import subprocess
from google import genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the Gemini API client
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY is not set")

client = genai.Client(api_key=api_key)

while True:
    user_input = input("ai-shell>")
   
    if user_input.lower() == "exit":
        break

    prompt = f"""
    You are a Linux shell assistant.

    Convert the user's input into exactly ONE valid Linux shell command.

    Rules:
    - Output ONLY the command
    -No markdown
    -No explanations
    -No comments
    -No backticks

    Request: {user_input}
    """
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    
    command = response.text.strip()
    print(f"Suggested command: {command}")

    confirm = input("Run command? (y/n): ")

    if confirm.lower() == "y":
        subprocess.run(command, shell=True)

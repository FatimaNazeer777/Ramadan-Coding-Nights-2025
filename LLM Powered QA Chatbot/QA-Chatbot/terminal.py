import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel(model_name="gemini-2.0-flash")
while True:
    user_input = input("Enter your question: OR type 'exit' to quit: ")
    response = model.generate_content(user_input)
    print(response.text)
    if user_input.lower() == "exit":
        print("Thank you for using the Gemini AI model")
        break
response = model.generate_content(user_input)
print(response.text)

import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

model = genai.GenerativeModel(
    os.getenv("MODEL")
)

question = """
Je suis ingénieur maintenance.
Analyse une pompe centrifuge industrielle
et propose une AMDEC simplifiée.
"""

response = model.generate_content(question)

print(response.text)
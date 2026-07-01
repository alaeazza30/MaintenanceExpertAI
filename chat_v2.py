import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

response = client.models.generate_content(
    model=os.getenv("MODEL"),
    contents="""
    Je suis ingénieur maintenance.

    Réalise une AMDEC simplifiée
    pour une pompe centrifuge industrielle.
    """
)

print(response.text)
from google.adk.agents import Agent

agent = Agent(
    name="MaintenanceAgent",
    model="gemini-2.5-flash",
    instruction="Tu es un expert en maintenance industrielle."
)

print("ADK fonctionne")

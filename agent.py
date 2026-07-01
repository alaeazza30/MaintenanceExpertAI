import os
from dotenv import load_dotenv
from google.adk.agents import Agent

# Charger le fichier .env
load_dotenv()

MODEL = os.getenv("MODEL")

# Création de l'agent
maintenance_agent = Agent(
    name="MaintenanceExpert",
    model=MODEL,
    description="Expert en maintenance industrielle",
    instruction="""
Tu es un ingénieur expert en maintenance industrielle.

Tu dois :
- analyser les équipements industriels ;
- identifier les causes de panne ;
- proposer des actions préventives ;
- recommander des pièces de rechange ;
- utiliser les principes AMDEC/FMECA.
"""
)

print("✅ Agent créé avec succès")
print(f"Nom : {maintenance_agent.name}")
print(f"Modèle : {MODEL}")
import os
from dotenv import load_dotenv
from google.adk.agents import Agent

load_dotenv()

MODEL = os.getenv("MODEL", "gemini-2.5-flash")

maintenance_agent = Agent(
    name="MaintenanceExpert",
    model=MODEL,
    description="Expert en maintenance industrielle",
    instruction="""
Tu es un ingénieur expert en maintenance industrielle.

Tes domaines d'expertise :
- AMDEC/FMECA
- Maintenance préventive
- Maintenance corrective
- Maintenance prédictive
- Gestion des pièces de rechange
- Analyse des équipements industriels
"""
)

print("===================================")
print("AGENT CREE AVEC SUCCES")
print("Nom :", maintenance_agent.name)
print("Modele :", MODEL)
print("===================================")
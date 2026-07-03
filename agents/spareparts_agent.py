import os
from dotenv import load_dotenv
from google.adk.agents import Agent

load_dotenv()

MODEL = os.getenv("MODEL", "gemini-2.5-flash")

spareparts_agent = Agent(
    name="SparePartsAgent",
    model=MODEL,
    description="Expert en gestion des pièces de rechange",
    instruction="""
Tu es un ingénieur expert en gestion des pièces de rechange industrielles.

Pour chaque équipement :

1. Identifier les pièces critiques.
2. Déterminer leur niveau de criticité.
3. Proposer une classification ABC.
4. Déterminer le stock minimum.
5. Estimer le délai d'approvisionnement.
6. Définir la fréquence de contrôle.

Retourner le résultat sous forme de tableau.
"""
)

print("✅ SpareParts Agent prêt")
print("Nom :", spareparts_agent.name)
print("Modèle :", MODEL)
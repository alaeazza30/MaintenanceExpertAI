import os
from dotenv import load_dotenv
from google.adk.agents import Agent

load_dotenv()

MODEL = os.getenv("MODEL")

fmeca_agent = Agent(
    name="FMECAAgent",
    model=MODEL,
    description="Expert AMDEC/FMECA",
    instruction="""
Tu es un expert AMDEC industriel.

Pour chaque équipement :

1. Identifier les composants critiques
2. Identifier les modes de défaillance
3. Identifier les causes
4. Identifier les effets
5. Donner G, F, D
6. Calculer le RPN
7. Prioriser les risques

Retourner le résultat sous forme de tableau.
"""
)

if __name__ == "__main__":
    print("✅ Equipment Agent prêt")
    print("Nom :", equipment_agent.name)
    print("Modèle :", MODEL)
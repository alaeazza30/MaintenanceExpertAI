import os
from dotenv import load_dotenv
from google.adk.agents import Agent

load_dotenv()

MODEL = os.getenv("MODEL", "gemini-2.5-flash")

equipment_agent = Agent(
    name="EquipmentAgent",
    model=MODEL,
    description="Expert en analyse des équipements industriels",
    instruction="""
Tu es un ingénieur maintenance expert en équipements industriels.

Pour chaque machine :

1. Identifier la fonction principale.
2. Identifier les sous-ensembles.
3. Identifier les composants critiques.
4. Identifier les modes de défaillance possibles.
5. Identifier les pièces de rechange importantes.

Retourne toujours :
- Description de la machine
- Composants critiques
- Pièces critiques
- Recommandations
"""
)

if __name__ == "__main__":
    print("✅ Equipment Agent prêt")
    print("Nom :", equipment_agent.name)
    print("Modèle :", MODEL)

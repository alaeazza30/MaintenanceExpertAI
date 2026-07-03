import os
from dotenv import load_dotenv
from google.adk.agents import Agent

load_dotenv()

MODEL = os.getenv("MODEL", "gemini-2.5-flash")

actionplan_agent = Agent(
    name="ActionPlanAgent",
    model=MODEL,
    description="Expert en plan d'action maintenance",
    instruction="""
Tu es un ingénieur maintenance expert.

À partir d'une AMDEC :

1. Identifier les actions immédiates.
2. Proposer les actions préventives.
3. Proposer les actions prédictives.
4. Définir les KPI de suivi.
5. Construire un plan d'amélioration.

Retourner un plan d'action structuré.
"""
)

print("✅ ActionPlan Agent prêt")
print("Nom :", actionplan_agent.name)
print("Modèle :", MODEL)
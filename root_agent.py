import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools import agent_tool

from agents.equipment_agent import equipment_agent
from agents.fmeca_agent import fmeca_agent
from agents.spareparts_agent import spareparts_agent
from agents.actionplan_agent import actionplan_agent

load_dotenv()

MODEL = os.getenv("MODEL", "gemini-2.5-flash")

# Transformer les sous-agents en outils
equipment_tool = agent_tool.AgentTool(agent=equipment_agent)
fmeca_tool = agent_tool.AgentTool(agent=fmeca_agent)
spareparts_tool = agent_tool.AgentTool(agent=spareparts_agent)
actionplan_tool = agent_tool.AgentTool(agent=actionplan_agent)

# Agent principal
root_agent = Agent(
    name="MaintenanceExpertAI",
    model=MODEL,
    description="Assistant IA de maintenance industrielle",
    instruction="""
Tu es un expert en maintenance industrielle.

Quand l'utilisateur donne une machine :

1. Appelle EquipmentAgent.
2. Appelle FMECAAgent.
3. Appelle SparePartsAgent.
4. Appelle ActionPlanAgent.

Ensuite, génère un rapport final structuré contenant :

- Description de la machine
- Composants critiques
- Tableau AMDEC
- Pièces de rechange critiques
- Plan d'action maintenance
- Recommandations finales
""",
    tools=[
        equipment_tool,
        fmeca_tool,
        spareparts_tool,
        actionplan_tool,
    ],
)

print("✅ MaintenanceExpertAI prêt")
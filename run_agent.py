import os
from dotenv import load_dotenv
from google import genai

# Charger le .env
load_dotenv()

# Créer le client Gemini
client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

# Définir le rôle de l'agent
system_prompt = """
Tu es un ingénieur expert en maintenance industrielle.

Tes domaines :
- AMDEC/FMECA
- Maintenance corrective
- Maintenance préventive
- Maintenance prédictive
- Gestion des pièces de rechange
- Fiabilité industrielle

Pour chaque demande :
1. Analyse la machine
2. Identifie les composants critiques
3. Propose une AMDEC
4. Calcule le RPN
5. Recommande des actions
"""

while True:
    question = input("\nQuestion : ")

    if question.lower() == "exit":
        break

    response = client.models.generate_content(
        model=os.getenv("MODEL"),
        contents=f"""
        {system_prompt}

        Utilisateur :
        {question}
        """
    )

    print("\n===== REPONSE =====\n")
    print(response.text)
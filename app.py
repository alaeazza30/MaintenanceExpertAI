import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# Charger les variables d'environnement
load_dotenv()

# Créer le client Gemini
client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

MODEL = os.getenv("MODEL", "gemini-2.5-flash")

# Interface
st.set_page_config(
    page_title="MaintenanceExpertAI",
    page_icon="🔧",
    layout="wide"
)

st.title("🔧 MaintenanceExpertAI")
st.subheader("Assistant IA de maintenance industrielle")

machine = st.text_input(
    "Entrez le nom de la machine :",
    placeholder="Ex : Pompe centrifuge"
)

if st.button("Analyser"):

    if machine == "":
        st.warning("Veuillez saisir une machine.")
    else:

        with st.spinner("Analyse en cours..."):

            prompt = f"""
Tu es un ingénieur expert en maintenance industrielle.

Analyse la machine suivante :

{machine}

Fournis la réponse avec la structure suivante :

# Description
Décris brièvement la machine.

# Composants critiques
Liste les composants critiques.

# AMDEC simplifiée
Présente un tableau contenant :
- Composant
- Défaillance
- Cause
- Effet
- G
- F
- D
- RPN

# Pièces critiques
Liste les pièces de rechange importantes.

# Plan d'action
Propose :
- maintenance préventive
- maintenance prédictive
- recommandations
"""

            response = client.models.generate_content(
                model=MODEL,
                contents=prompt
            )

            st.markdown(response.text)
import streamlit as st
import requests

st.set_page_config(
    page_title="Test Communication Katakana",
    page_icon="🔧"
)

st.title("Test Communication Frontend-Backend")

# Saisie utilisateur
phrase = st.text_input("Entrez une phrase :")

if st.button("Envoyer au backend"):
    # Envoyer la phrase au backend Flask
    response = requests.post(
        "http://backend-container:5000/convert",
        json={"phrase": phrase}
    )

    if response.status_code == 200:
        resultat = response.json().get("reply", "Erreur de réception")

        st.write("Réponse du backend :")
        st.write(resultat)
    else:
        st.error("Erreur lors de l'appel au backend.")

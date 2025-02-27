import streamlit as st
import requests

st.set_page_config(
    page_title="Convertisseur Hiraganas",
    page_icon="🗼"
)

st.title("Convertisseur d'alphabet grec vers Hiraganas")

# Saisie utilisateur
phrase = st.text_input("Entrez une phrase :")

if st.button("Convertir"):
    # Envoyer la phrase au backend Flask
    response = requests.post(
        "http://backend-container:5000/convert",
        json={"phrase": phrase}
    )

    if response.status_code == 200:
        resultat = response.json().get("reply", "Erreur de réception")

        st.write("Conversion en Hiraganas :")
        st.write(resultat)
    else:
        st.error("Erreur lors de l'appel au backend.")

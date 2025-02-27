from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import requests
import json

# Modèle de requête
class PhraseRequest(BaseModel):
    phrase: str

# Création du router FastAPI
hiraganas_router = APIRouter()

OLLAMA_URL = "http://ollama:11434/api/generate"

@hiraganas_router.post("/convert")
async def convert_to_hiragana(request: PhraseRequest):
    phrase = request.phrase
    print("Message reçu du frontend :", phrase)

    # Prompt personnalisé
    prompt = f"""Instruction :
Write each syllable one after the other as it is pronounced, using only Hiragana, NOT Katakana ("bonjour" → ぼんじゅる ). DON'T TRANSLATE THE WORDS, JUST THE SYLLABLES AND CONVERT THEM TO HIRAGANAS.
I don't want notes in the chat.

### Input:
{phrase}

### Response:
"""

    try:
        # Envoi de la requête à Ollama
        response = requests.post(OLLAMA_URL, json={"model": "llama3", "prompt": prompt}, stream=True)
        response.raise_for_status()  # Vérifie si la requête a échoué

        ai_reply = ""

        # Lecture du flux JSON ligne par ligne
        for line in response.iter_lines():
            if line:
                try:
                    json_data = json.loads(line)  # Convertit chaque ligne en JSON
                    ai_reply += json_data.get("response", "")  # Concatène la réponse
                except json.JSONDecodeError:
                    print("Erreur JSON, ligne ignorée :", line)

        if not ai_reply:
            ai_reply = "Désolé, je n'ai pas pu répondre à votre message."

        print("Réponse extraite de l'IA :", ai_reply)
        return {"reply": ai_reply}

    except requests.RequestException as e:
        print(f"Erreur lors de la communication avec Ollama: {e}")
        raise HTTPException(status_code=500, detail="Erreur de communication avec l'IA.")

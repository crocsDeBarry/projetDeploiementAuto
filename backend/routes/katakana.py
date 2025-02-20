from fastapi import APIRouter
from pydantic import BaseModel
import ollama

# Définir un modèle de données pour la requête (optionnel mais recommandé pour FastAPI)
class PhraseRequest(BaseModel):
    phrase: str

# Créer un router FastAPI pour les routes liées à katakana
katakana_router = APIRouter()

# Route POST pour traiter la conversion en hiragana
@katakana_router.post("/convert")
async def convert_to_hiragana(request: PhraseRequest):
    phrase = request.phrase
    print("Message reçu du frontend :", phrase)
    
    # Prompt personnalisé pour transformer le texte en hiragana
    prompt = f"""Instruction :
Write each syllable one after the other as it is pronounce, using only Hiragana, NOT Katakana ("bonjour" → ぼんじゅる ). DON'T TRANSLATE THE WORDS JUST THE SYLLABLES AND CONVERT THEM TO HIRAGANAS.
I don't want notes in the chat 

### Input:
{phrase}

### Response:
"""
    try:
        # Appel à l'IA (Ollama) avec le prompt personnalisé
        response = ollama.chat(model="llama3.1", messages=[{"role": "user", "content": prompt}])
        print("Réponse de l'IA :", response)
        
        # Extraire la réponse de l'IA
        ai_reply = response.get('message', {}).get('content', "Désolé, je n'ai pas pu répondre à votre message.")
        print("Réponse extraite de l'IA :", ai_reply)
        
        return {"reply": ai_reply}
    except Exception as e:
        print(f"Erreur lors de la communication avec Ollama: {e}")
        raise HTTPException(status_code=500, detail="Erreur lors de la communication avec l'IA.")

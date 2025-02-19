from fastapi import APIRouter
from pydantic import BaseModel

# Définir un modèle de données pour la requête (optionnel mais recommandé pour FastAPI)
class PhraseRequest(BaseModel):
    phrase: str

# Créer un router FastAPI pour les routes liées à katakana
katakana_router = APIRouter()

# Route POST pour traiter les messages envoyés depuis le frontend
@katakana_router.post("/convert")
async def convert_to_katakana(request: PhraseRequest):
    phrase = request.phrase  # Récupère la phrase à partir de la requête

    # Afficher le message reçu dans la console
    print(f"Message reçu du frontend : {phrase}")

    # Retourner une réponse simple au frontend
    return {"message": f"Message reçu : {phrase}"}

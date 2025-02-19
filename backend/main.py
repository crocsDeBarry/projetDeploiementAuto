from fastapi import FastAPI
from routes.katakana import katakana_router  # Importer le router depuis le module de routes

app = FastAPI()

# Enregistrer le router dans l'application FastAPI
app.include_router(katakana_router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=5000)

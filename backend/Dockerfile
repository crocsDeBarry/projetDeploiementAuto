# Utiliser une image officielle Python 3.12 slim
FROM python:3.12-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt dans l'image
COPY requirements.txt .

# Installer les dépendances à partir du fichier requirements.txt
RUN pip install -r requirements.txt

# Copier tous les fichiers de l'application dans l'image
COPY . .

# Exposer le port 8000 (port par défaut d'Uvicorn)
EXPOSE 5000

# Commande de démarrage de l'application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]

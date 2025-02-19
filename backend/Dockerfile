# Utilisez une image de base Python 3.12
FROM python:3.12-slim

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Installez uv
RUN python -m pip install uv

# Copiez tous les fichiers du projet dans le conteneur
COPY . /app/

# Synchronisez les dépendances avec uv
RUN uv sync

# Exposez le port sur lequel l'application va écouter
EXPOSE 5000

# Commande pour lancer l'application
CMD ["uv", "run", "main:app", "--host", "0.0.0.0", "--port", "5000"]
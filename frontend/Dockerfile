# Utiliser une image de base légère avec Python
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt dans l'image
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install -r requirements.txt

# Copier tous les fichiers de l'application dans l'image
COPY . .

# Exposer le port 8501 (port par défaut de Streamlit)
EXPOSE 8501

# Lancer l'application Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

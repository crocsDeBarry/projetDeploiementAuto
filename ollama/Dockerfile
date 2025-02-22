# Utiliser une image de base légère (par exemple, Alpine)
FROM ubuntu:20.04

# Installer les dépendances nécessaires pour Ollama
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Télécharger et installer Ollama (ajuste le lien si nécessaire)
RUN curl -sSL https://ollama.com/download/ollama-linux-x64.zip -o ollama.zip \
    && unzip ollama.zip -d /usr/local/bin \
    && rm ollama.zip

# Exposer un port (si nécessaire pour la communication entre les containers)
EXPOSE 11434

# Commande pour démarrer Ollama (ajuste selon les besoins)
CMD ["ollama", "start"]

# Projet Deploiement Automatique
Pour ce projet, nous avons choisi d'utiliser le modèle LLaMA 3 afin de transcrire un mot français en hiragana tout en préservant au maximum sa prononciation. Par exemple, "bonjour" deviendra → ぼんじゅる (bonjūru)

## Prérequis

- Docker Hub installé
- WSL installé 
- Un GPU (recommandé)

## Installation

1. Lancer Docker Hub
2. Cloner le projet :
   
   ```bash
   git clone https://github.com/crocsDeBarry/projetDeploiementAuto.git
   cd projetDeploiementAuto
   docker-compose up -build -d

Cela devrait télécharger les différents éléments et afficher les images et les containers dans Docher Hub
Attention : le modèle d'intelligence artificielle peut prendre un peu de temps à s'installer, on peut vérifier son installation dans le container d'Ollama
On devarit donc avoir trois container et trois images :
- frontend
- backend
- ollama

Une fois cela fait il ne reste plus qu'à tester l'application sur [notre localhost](http://localhost:8501/)

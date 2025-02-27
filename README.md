# Projet de Déploiement Automatique avec Docker

Ce projet contient un **frontend Streamlit** et un **backend FastAPI**. Il est conçu pour être déployé et exécuté via **Docker Compose**. L'objectif principal est de fournir une interface utilisateur (UI) interactive pour tester la communication entre le frontend et le backend.

## Pré-requis

- **Docker** et **Docker Compose** doivent être installés sur votre machine.  
  Si ce n'est pas déjà fait, vous pouvez installer Docker en suivant la documentation officielle :  
  [Installation de Docker](https://docs.docker.com/get-docker/)

- **Suffisamment de RAM** : Assurez-vous que votre machine dispose de **minimum 16 Go de RAM**. Si vous utilisez Ollama pour des modèles lourds, il est important d'avoir suffisamment de mémoire pour éviter des problèmes de performance.

---

## Installation et Exécution

1. **Clonez ce repo** :
   ```bash
   git clone <url-du-repository>
   cd <nom-du-dossier-du-repository>
    ```

2. **Lancez les containers avec Docker Compose** :
   À la racine du projet, exécutez la commande suivante pour construire et démarrer les containers en arrière-plan (en mode détaché) :
   ```bash
   docker compose up --build -d
    ```
    
   Cette commande :
   - **Construit** les images Docker à partir des Dockerfiles du **frontend** et du **backend**.
   - **Lance** les services dans des containers séparés.

   ⚠️ **Attention** : Cette étape peut nécessiter une **quantité suffisante de RAM**. Assurez-vous que votre machine dispose de suffisamment de ressources pour éviter des problèmes lors de l'exécution des containers.

3. **Accédez à l'interface utilisateur** :
   Une fois les containers en cours d'exécution, vous pouvez accéder à l'application Streamlit via votre navigateur à l'adresse suivante :
   http://localhost:8501

   Cette adresse ouvrira l'interface du frontend, où vous pourrez interagir avec l'application et tester la communication entre le **frontend** et le **backend**.
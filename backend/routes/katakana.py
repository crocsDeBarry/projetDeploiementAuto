from flask import Blueprint, request, jsonify

# Créer un blueprint pour les routes liées à katakana
katakana_bp = Blueprint('katakana', __name__)

# Route POST pour traiter les messages envoyés depuis le frontend
@katakana_bp.route('/convert', methods=['POST'])
def convert_to_katakana():
    data = request.get_json()
    phrase = data.get("phrase", "")

    # Afficher le message reçu dans la console
    print(f"Message reçu du frontend : {phrase}")

    # Retourner une réponse simple au frontend
    return jsonify({"message": f"Message reçu : {phrase}"})

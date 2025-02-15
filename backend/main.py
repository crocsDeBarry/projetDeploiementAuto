from flask import Flask
from routes.katakana import katakana_bp

app = Flask(__name__)

# Enregistrer le blueprint
app.register_blueprint(katakana_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

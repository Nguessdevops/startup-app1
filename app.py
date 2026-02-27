from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenue sur l'app de la startup !"

@app.route('/produits')
def produits():
    return "Liste de nos produits"

@app.route('/contact')
def contact():
    return "Contactez nous ici"

if __name__ == '__main__':
    debug_mode = os.environ.get('FLASK_DEBUG', 'False') == 'True'
    app.run(host='0.0.0.0', port=5000, debug=debug_mode)
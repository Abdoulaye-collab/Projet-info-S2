from flask import Flask, jsonify, send_from_directory
import requests

application = Flask(__name__, static_folder='static', static_url_path='')

CLÉ_API_NEWS = ' b741529903424b0ca280b6e9d8f7c32d'  # Remplace par ta vraie clé API

ENTREPRISES = ['Google', 'Apple', 'Facebook', 'Amazon', 'Microsoft', 'Tesla']

@application.route('/')
def accueil():
    return send_from_directory(application.static_folder, 'index.html')

@application.route('/api/actualites-entreprises')
def actualites_entreprises():
    actualites = {}
    for entreprise in ENTREPRISES:
        url = f'https://newsapi.org/v2/everything?q={entreprise}&language=fr&sortBy=publishedAt&apiKey={CLÉ_API_NEWS}'
        réponse = requests.get(url)
        données = réponse.json()
        actualites[entreprise] = données.get('articles', [])[:5]
    return jsonify(actualites)

if __name__ == '__main__':
    application.run(debug=True)

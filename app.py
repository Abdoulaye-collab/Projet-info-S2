from flask import Flask, jsonify, send_from_directory
import requests

app = Flask(__name__, static_folder='../static', static_url_path='')

NEWS_API_KEY = 'b741529903424b0ca280b6e9d8f7c32d'  # Remplace ici

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/tesla-news')
def tesla_news():
    url = f'https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)

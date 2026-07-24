from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)


@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

@app.route('/suggestions', methods=['POST'])
def add_suggestion():
    data = request.get_json()
    text = data.get('text', '').strip()

    if not text:
        return jsonify({'error': 'Порожнє повідомлення'}), 400

   
    suggestions = []
    if os.path.exists('suggestions.json'):
        with open('suggestions.json', 'r', encoding='utf-8') as f:
            suggestions = json.load(f)

    suggestions.append(text)

    with open('suggestions.json', 'w', encoding='utf-8') as f:
        json.dump(suggestions, f, ensure_ascii=False, indent=2)

    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
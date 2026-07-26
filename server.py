from flask import Flask, request, jsonify
import json
import os

import os

DATA_DIR = os.path.join(os.path.expanduser('~'), 'portfolio_data')
os.makedirs(DATA_DIR, exist_ok=True)

COUNTER_FILE = os.path.join(DATA_DIR, 'counter.json')
GUESTBOOK_FILE = os.path.join(DATA_DIR, 'guestbook.json')
SUGGESTIONS_FILE = os.path.join(DATA_DIR, 'suggestions.json')
app = Flask(__name__)

COUNTER_FILE = 'counter.json'
GUESTBOOK_FILE = 'guestbook.json'


@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response


@app.route('/suggestions', methods=['POST'])
def add_suggestion():
    data = request.get_json()
    text = data.get('text', '').strip()

    if not text:
        return jsonify({'error': 'Порожнє повідомлення'}), 400

    suggestions = []
    if os.path.exists(SUGGESTIONS_FILE):
        with open(SUGGESTIONS_FILE, 'r', encoding='utf-8') as f:
            suggestions = json.load(f)

    suggestions.append(text)

    with open('SUGGESTIONS_FILE', 'w', encoding='utf-8') as f:
        json.dump(suggestions, f, ensure_ascii=False, indent=2)

    return jsonify({'status': 'ok'})


@app.route('/counter', methods=['GET'])
def get_counter():
    count = 0
    if os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, 'r', encoding='utf-8') as f:
            count = json.load(f).get('count', 0)

    count += 1

    with open(COUNTER_FILE, 'w', encoding='utf-8') as f:
        json.dump({'count': count}, f)

    return jsonify({'count': count})


@app.route('/guestbook', methods=['GET'])
def get_guestbook():
    entries = []
    if os.path.exists(GUESTBOOK_FILE):
        with open(GUESTBOOK_FILE, 'r', encoding='utf-8') as f:
            entries = json.load(f)
    return jsonify(entries)


@app.route('/guestbook', methods=['POST'])
def add_guestbook():
    data = request.get_json()
    name = data.get('name', '').strip() or 'Анонім'
    text = data.get('text', '').strip()

    if not text:
        return jsonify({'error': 'Порожнє повідомлення'}), 400

    entries = []
    if os.path.exists(GUESTBOOK_FILE):
        with open(GUESTBOOK_FILE, 'r', encoding='utf-8') as f:
            entries = json.load(f)

    entries.append({'name': name, 'text': text})

    with open(GUESTBOOK_FILE, 'w', encoding='utf-8') as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)

    return jsonify({'status': 'ok'})


if __name__ == '__main__':
    app.run(port=5000, debug=True)
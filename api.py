#!/usr/bin/env python
from flask import Flask, request, jsonify
from main import match_regex
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/match', methods=['POST'])
def process():
    data = request.get_json()
    if 'input' not in data:
        return jsonify({'error': 'No input string provided'})

    result = match_regex(data['input'])

    for key, value in result.items():
        if value is True:
            result[key] = "Accepted"
        elif value is False:
            result[key] = "Rejected"

    return jsonify({'output': result})

if __name__ == '__main__':
    app.run(debug=True)

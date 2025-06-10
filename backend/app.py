from flask import Flask, request, jsonify
import os
import sqlite3
import pandas as pd
import openai

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400
    openai.api_key = os.getenv('OPENAI_API_KEY')
    if not openai.api_key:
        return jsonify({'error': 'OpenAI API key not configured'}), 500
    try:
        response = openai.ChatCompletion.create(
            model='gpt-4',
            messages=[{'role': 'user', 'content': user_message}]
        )
        reply = response.choices[0].message['content']
        return jsonify({'reply': reply})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

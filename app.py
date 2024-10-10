# app.py
from flask import Flask, render_template, request, jsonify
from lexer import analyze_lexically

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text', '')

    # Llamar a la función de análisis léxico
    tokens = analyze_lexically(text)

    return jsonify({'tokens': tokens})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, jsonify
from lexer import create_lexer

app = Flask(__name__)
lexer = create_lexer()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text', '')
    lexer.input(text)

    tokens = []
    for tok in lexer:
        tokens.append({
            'type': tok.type,
            'value': tok.value,
            'line': tok.lineno,
            'position': tok.lexpos
        })

    return jsonify({'tokens': tokens})

if __name__ == '__main__':
    app.run(debug=True)

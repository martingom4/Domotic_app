# lexer.py

# Diccionarios para representar la tabla de símbolos
COMANDOS = {
    "encender": "Indica que se debe encender un dispositivo.",
    "apagar": "Indica que se debe apagar un dispositivo.",
    "ajustar": "Indica que se debe modificar un parámetro (brillo, volumen, temperatura)."
}

DISPOSITIVOS = {
    "luz": "Representa una luz que puede ser encendida, apagada o ajustada en brillo.",
    "termostato": "Representa un dispositivo de control de temperatura.",
    "altavoz": "Representa un dispositivo de audio que puede ser ajustado en volumen."
}

def analyze_lexically(text):
    """
    Analiza la cadena de entrada y la descompone en tokens.
    """
    tokens = []
    words = text.split()
    position = 0

    for word in words:
        token_info = {
            "value": word,
            "line": 1,
            "position": position,
            "length": len(word)
        }

        if word in COMANDOS:
            token_info["type"] = "COMANDO"
            token_info["description"] = COMANDOS[word]
        elif word in DISPOSITIVOS:
            token_info["type"] = "DISPOSITIVO"
            token_info["description"] = DISPOSITIVOS[word]
        elif word.isdigit():
            number = int(word)
            if 0 <= number <= 100:
                token_info["type"] = "VALOR_NUMERICO"
                token_info["description"] = f"Rango de valores de 0 a 100 para ajustar parámetros (brillo o volumen): {number}"
            else:
                token_info["type"] = "ERROR"
                token_info["description"] = f"Valor numérico fuera de rango: {number}"
        else:
            token_info["type"] = "ERROR"
            token_info["description"] = f"Token no reconocido: {word}"

        tokens.append(token_info)
        position += len(word) + 1  # +1 para contar el espacio después de cada palabra

    return tokens

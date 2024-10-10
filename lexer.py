import ply.lex as lex

# Lista de tokens
tokens = (
    'COMANDO',
    'DISPOSITIVO',
    'VALOR_NUMERICO',
)

# Definición de expresiones regulares para cada tipo de token
t_COMANDO = r'encender|apagar|ajustar'
t_DISPOSITIVO = r'luz|termostato|altavoz'

# Para identificar valores numéricos de 0 a 100
def t_VALOR_NUMERICO(t):
    r'\d+'
    t.value = int(t.value)
    # Validar que el número esté entre 0 y 100
    if 0 <= t.value <= 100:
        return t
    else:
        print(f"Error: El número {t.value} está fuera del rango permitido (0-100).")
        t.lexer.skip(1)

# Ignorar espacios en blanco y tabulaciones
t_ignore = ' \t'

# Manejo de errores
def t_error(t):
    print(f"Caracter no reconocido: {t.value[0]}")
    t.lexer.skip(1)

# Función para crear el lexer
def create_lexer():
    lexer = lex.lex()
    return lexer

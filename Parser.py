import ply.lex as lex
import ply.yacc as yacc
import keyboard

no_error = 0

# Lista de nombres de tokens
tokens = (
    'PRINT',
    'NUMBER',
    'OPER',
    'STR',
    'VAR',
    'LDEL',
    'RDEL',
    'EQUAL',
    'TYPE',
    'CONDICION',
)

# Expresiones regulares para tokens
t_NUMBER = r'\d+(\.\d+)?'
t_OPER = r'[-+*/<>]'
t_STR = r'(\"([^\\\n]|(\\.))*?\")|(\'([^\\\n]|(\\.))*?\')'
t_LDEL = r'[({\[]'
t_RDEL = r'[)}\]]'
t_EQUAL = r'(=|\+=|-=)'
# Función para tratar palabras reservadas
def t_PRINT(t):
    r'\bprint\b'
    return t

def t_CONDICION(t):
    r'(if|do)'
    return t

# Función para manejar los tipos de dato
def t_TYPE(t):
    r'(INT|int|FLO|flo|BOL|bol)'
    return t

# Función para tratar nombres de variables
def t_VAR(t):
    r'[a-zA-Z]\w*'
    return t

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Función para manejar errores léxicos
def t_error(t):
    global no_error
    print("Error léxico: Carácter inesperado: '%s'" % t.value[0])
    no_error += 1
    t.lexer.skip(1)

# Crear el analizador léxico
lexer = lex.lex()

# Guarda una cadena a analizar
print("Ingresa la cadena a escanear:")
data = input()

# Prueba!
lexer.input(data)

# Almacenar tokens
token_list = []  # Lista para almacenar los nombres de los tokens

while True:
    tok = lexer.token()
    if not tok:
        break  # No hay más datos
    token_list.append(tok.type)

print("Selecciona los resultados deseados:\n1: Resultados simples\n2: Resultados detallados.\n")
op = input()

if op == "1":
    # Imprimir los tokens en la misma línea, separados por espacios
    print("Tokens detectados:")
    print(" ".join(token_list))
    print("Erorres detectados:", no_error)
else:
    lexer.lexpos = 0
    while True:
        tok = lexer.token()
        if not tok: 
            break
        print("Tipo de token:", tok.type, "\nCaracteres:", tok.value, "\nNumero de linea:", tok.lineno, "\n")

print("Presione cualquier tecla para continuar...")
keyboard.read_key()

#PARSER

 

# Define la gramática
def p_program(p):
    '''
    program : assignment
            | print_statement
            | conditional_statement
            | comp
    '''

def p_assignment(p):
    '''
    assignment : TYPE VAR EQUAL expression
    '''
    print("Assignment statement valid!")

def p_expression_arithmetic(p):
    '''
    expression : expression OPER expression
               | NUMBER
    '''
    print("Arithmetic expression valid!")

def p_print_statement(p):
    '''
    print_statement : VAR LDEL STR RDEL
                     | PRINT LDEL STR RDEL
    '''
    print("Print statement valid!")


def p_conditional_statement(p):
    '''
    conditional_statement : CONDICION VAR EQUAL NUMBER CONDICION print_statement
    '''
    print("Conditional statement valid!")

def p_comp(p):
    '''
    comp : VAR EQUAL NUMBER
    '''
    print("comp statement valid!")

# Definir la regla para manejar errores sintácticos

def p_error(p):
    global no_error
    if p:
        print(f"Error sintáctico en línea {p.lineno}, posición {p.lexpos}: Token inesperado '{p.value}'")
    else:
        print("Error sintáctico: Fin de entrada inesperado")
    no_error += 1

# Construir el parser
parser = yacc.yacc()

# Prueba el analizador sintáctico
result = parser.parse(data)
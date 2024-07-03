from ply import lex

reserved = {
    'break'   : 'BREAK',
    'case'    : 'CASE',
    'continue': 'CONTINUE',
    'default' : 'DEFAULT',
    'do'      : 'DO',
    'else'    : 'ELSE',
    'enum'    : 'ENUM',
    'extern'  : 'EXTERN',
    'for'     : 'FOR',
    'goto'    : 'GOTO',
    'if'      : 'IF',
    'return'  : 'RETURN',
    'struct'  : 'STRUCT',
    'switch'  : 'SWITCH',
    'typedef' : 'TYPEDEF',
    'union'   : 'UNION',
    'volatile': 'VOLATILE',
    'while'   : 'WHILE',
    'auto'    : 'AUTO_TYPE',
    'bool'    : 'BOOLEAN_TYPE',
    'char'    : 'CHAR_TYPE',
    'const'   : 'CONST',
    'double'  : 'DOUBLE_TYPE',
    'float'   : 'FLOAT_TYPE',
    'int'     : 'INT_TYPE',
    'NULL'    : 'NULL',
    'long'    : 'LONG_TYPE',
    'short'   : 'SHORT_TYPE',
    'signed'  : 'SIGNED_TYPE',
    'static'  : 'STATIC',
    'string'  : 'STRING_TYPE',
    'unsigned': 'UNSIGNED_TYPE',
    'void'    : 'VOID',
}

tokens = [
    'AND', 'BOOLEAN', 'CHAR', 'COLON', 'COMMA', 'COMMENT', 'DEFINE', 'DIVIDE', 
    'DOT', 'ENDERECO', 'EQUALS', 'EQUIVALENT', 'FLOAT', 'FORMAT_SPECIFIER', 
    'GE', 'GT', 'HEADER', 'INCLUDE', 'INTEGER', 'LARROW', 'LBRACES', 'LE', 
    'LPAREN', 'LSBRACES', 'LT', 'MINUS', 'MINUSMINUS', 'NE', 'NOT', 'OR', 
    'PERCENT', 'PLUS', 'PLUSPLUS', 'POWER', 'RARROW', 'RBRACES', 'RPAREN', 
    'RSBRACES', 'SEMICOLON', 'SHARP', 'STRING', 'TIMES', 'VARIABLE'

] + list(reserved.values())

t_ignore = ' \t\n'

t_AND = r'&&'
t_BOOLEAN = r'(true)|(false)'
t_CHAR = r'\'.*?\''
t_COLON = r':'
t_COMMA = r'\,'
t_COMMENT = r'(//.*)|(/\*([^*]|(\*+[^*/]))*\*+/)'
t_DEFINE = r'(\#define)'
t_DIVIDE = r'/'
t_DOT = r'\.'
t_ENDERECO = r'&'
t_EQUALS = r'='
t_EQUIVALENT = r'=='
t_FLOAT = r'((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))'
t_GE = r'>='
t_GT = r'>'
t_HEADER = r'<.*>'
t_INCLUDE = r'(\#include)'
t_INTEGER = r'\d+'
t_LARROW = r'<-'
t_LBRACES = r'\{'
t_LE = r'<='
t_LPAREN = r'\('
t_LSBRACES = r'\['
t_LT = r'<'
t_MINUS = r'-'
t_MINUSMINUS = r'--'
t_NE = r'!='
t_NOT = r'!'
t_OR = r'\|\|'
t_PERCENT = r'%'
t_PLUS = r'\+'
t_PLUSPLUS = r'\+\+'
t_POWER = r'\^'
t_RARROW = r'->'
t_RBRACES = r'\}'
t_RPAREN = r'\)'
t_RSBRACES = r'\]'
t_SEMICOLON = r'\;'
t_SHARP = r'\#'
t_STRING = r'"(?:\\.|[^\\"])*"'
t_TIMES = r'\*'


def t_error(t):
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'VARIABLE')
    return t

lexer = lex.lex()

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as file:
            data = file.read()
        lexer.input(data)
        for tok in lexer:
            print(tok)

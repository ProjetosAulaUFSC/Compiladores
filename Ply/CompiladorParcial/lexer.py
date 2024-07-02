from ply import lex

reserved = {
    'break': 'BREAK',
    'case': 'CASE',
    'class': 'CLASS',
    'continue': 'CONTINUE',
    'default': 'DEFAULT',
    'do': 'DO',
    'else': 'ELSE',
    'enum': 'ENUM',
    'extern': 'EXTERN',
    'for': 'FOR',
    'goto': 'GOTO',
    'if': 'IF',
    'return': 'RETURN',
    'struct': 'STRUCT',
    'switch': 'SWITCH',
    'typedef': 'TYPEDEF',
    'union': 'UNION',
    'volatile': 'VOLATILE',
    'while': 'WHILE',
    'auto': 'AUTO_TYPE',
    'bool': 'BOOLEAN_TYPE',
    'char': 'CHAR_TYPE',
    'const': 'CONST',
    'double': 'DOUBLE_TYPE',
    'float': 'FLOAT_TYPE',
    'int': 'INT_TYPE',
    'NULL': 'NULL',
    'long': 'LONG_TYPE',
    'short': 'SHORT_TYPE',
    'signed': 'SIGNED_TYPE',
    'static': 'STATIC',
    'string': 'STRING_TYPE',
    'unsigned': 'UNSIGNED_TYPE',
    'void': 'VOID_TYPE',
}

tokens = [
    'EQUALS', 'PLUS', 'MINUS', 'TIMES', 'POWER', 'DIVIDE',
    'LPAREN', 'RPAREN', 'LT', 'LE', 'GT', 'GE', 'NE', 'DEFINE',
    'COMMA', 'INTEGER', 'FLOAT', 'STRING', 'VARIABLE',
    'SEMICOLON', 'RBRACES', 'LBRACES', 'LSBRACES', 'FORMAT_SPECIFIER',
    'RSBRACES', 'DOT', 'ENDERECO', 'NOT', 'EQUIVALENT', 'COMMENT',
    'PLUSPLUS', 'MINUSMINUS', 'RARROW', 'LARROW', 'PERCENT', 'INCLUDE',
    'SHARP', 'AND', 'BOOLEAN', 'HEADER', 'CHAR', 'COLON'
] + list(reserved.values())

t_ignore = ' \t\n'

t_EQUALS = r'='
t_EQUIVALENT = r'=='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_POWER = r'\^'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_RBRACES = r'\}'
t_LBRACES = r'\{'
t_SEMICOLON = r'\;'
t_LSBRACES = r'\['
t_RSBRACES = r'\]'
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'>='
t_NOT = r'!'
t_NE = r'!='
t_COMMA = r'\,'
t_DOT = r'\.'
t_COLON = r':'
t_ENDERECO = r'&'
t_AND = r'&&'
t_SHARP = r'\#'
t_PLUSPLUS = r'\+\+'
t_MINUSMINUS = r'--'
t_RARROW = r'->'
t_LARROW = r'<-'
t_PERCENT = r'%'
t_HEADER = r'<.*>'

t_INTEGER = r'\d+'
t_FLOAT = r'((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))'
t_CHAR = r'\'.*?\''
t_BOOLEAN = r'(true)|(false)'
t_COMMENT = r'(/\*(.|\n)*?\*/)|(//.*)'
t_STRING = r'"(?:\\.|[^\\"])*"'
t_INCLUDE = r'(\#include)'
t_DEFINE = r'(\#define)'

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
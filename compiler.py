from ply import lex
from ply import yacc

class Id_Type:
    def __init__(self, id, type):
        self.type = type
        self.id = id

symbol_table = []

reserved = {
    'break': 'BREAK',
    'case': 'CASE',
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
    'void': 'VOID',
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
t_NE = r'\!='
t_NOT = r'\!'
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
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'VARIABLE')
    if t.value == 'None':
        t.type = 'VARIABLE'  # Treat 'None' as a variable identifier
    return t

lexer = lex.lex()

def type_of_constant(value):
    if isinstance(value, bool):
        return 'BOOLEAN'
    elif isinstance(value, int):
        return 'INT'
    elif isinstance(value, float):
        return 'FLOAT'
    elif isinstance(value, str) and len(value) == 1:
        return 'CHAR'
    elif isinstance(value, str):
        return 'STRING'
    else:
        return 'UNKNOWN'

def p_program(p):
    '''program : include_block define_block enum_block struct_block function_block statement_block'''

def p_include_block(p):
    '''include_block : INCLUDE HEADER include_block
                     | empty'''
    if p[1] == None: print("Empty Include_Block")
    else: print("Include_Block")

def p_define_block(p):
    '''define_block : DEFINE VARIABLE type SEMICOLON define_block
                    | empty'''

def p_enum_block(p):
    '''enum_block : ENUM LBRACES enum_values RBRACES enum_block
                  | empty'''

def p_enum_values(p):
    '''enum_values : enum_values VARIABLE COMMA
                   | enum_values VARIABLE
                   | empty'''

def p_struct_block(p):
    '''struct_block : STRUCT VARIABLE LBRACES struct_values RBRACES struct_block
                    | empty'''

def p_struct_values(p):
    '''struct_values : struct_values type VARIABLE SEMICOLON
                     | empty'''

def p_function_block(p):
    '''function_block : function function_block
                      | empty'''
    if p[1] == None: print("Empty Function_Block")
    else: print("Function_Block")

def p_function(p):
    '''function : type VARIABLE LPAREN parameters RPAREN LBRACES statement_block return_block RBRACES'''
    print("Function", p[1], p[2])

def p_return_block(p):
    '''return_block : RETURN expression SEMICOLON
                    | empty'''
    if p[1] == None: print("Empty Return_Block")
    else: print("Return_Block")

def p_parameters(p):
    '''parameters : type VARIABLE COMMA parameters
                  | type VARIABLE
                  | empty'''
    print("Parameters")
    if p[1] == None: print("Empty Parameters")

def p_statement_block(p):
    '''statement_block : statement statement_block
                       | empty'''
    if len(p) == 3:
        print(f"Statement Block: {p[1]} {p[2]}")
    else:
        print("Empty Statement Block")

def p_statement(p):
    '''statement : declaration
                 | if_block
                 | for_loop
                 | while_loop
                 | do_while
                 | switch
                 | expression SEMICOLON'''
    if p[1] == None: print("F NO CHAT")
    if len(p) == 3:  # This means it's an expression statement
        p_expression_check(p[1])

def p_declaration(p):
    '''declaration : type VARIABLE EQUALS expression SEMICOLON
                   | type VARIABLE SEMICOLON'''
    var_type = p[1]
    var_name = p[2]
    
    if any(var.id == var_name for var in symbol_table):
        print(f"Semantic error: Variable '{var_name}' already declared.")
    else:
        symbol_table.append(Id_Type(var_name, var_type))
        print(f"Declared variable '{var_name}' of type '{var_type}'.")

def p_if_block(p):
    '''if_block : IF LPAREN expression RPAREN LBRACES statement_block RBRACES if_block
               | IF LPAREN expression RPAREN statement if_block
               | ELSE LBRACES statement_block RBRACES
               | ELSE statement
               | empty'''
    if p[1] == 'if':
        print("If statement")
    elif p[1] == 'else':
        print("Else statement")
    elif p[1] is None:
        print("Empty If/Else")
    else: print("AAAAAAAAAAAAAAAAAA")
    p[0] = "if_block"

def p_for_loop(p):
    '''for_loop : FOR LPAREN declaration expression SEMICOLON expression RPAREN statement'''

def p_while_loop(p):
    '''while_loop : WHILE LPAREN expression RPAREN statement'''

def p_do_while(p):
    '''do_while : DO statement WHILE LPAREN expression RPAREN SEMICOLON'''

def p_switch(p):
    '''switch : SWITCH LPAREN expression RPAREN LBRACES cases RBRACES'''

def p_cases(p):
    '''cases : case cases
             | default cases
             | empty'''

def p_case(p):
    '''case : CASE expression COLON statement_block BREAK SEMICOLON'''

def p_default(p):
    '''default : DEFAULT COLON statement_block'''

def p_expression(p):
    '''expression : expression operator expression
                  | LPAREN expression RPAREN
                  | constant
                  | VARIABLE'''
    if len(p) == 2:
        if any(var.id == p[1] for var in symbol_table):
            var_name = p[1]
            p[0] = next(var.type for var in symbol_table if var.id == var_name)
        else:
            print(f"Semantic error: Variable '{p[1]}' not declared before use.")
            p[0] = 'UNKNOWN'
    elif len(p) == 4 and p[2] in ['+', '-', '*', '/']:
        if p[1] != p[3]:
            print(f"Semantic error: Type mismatch in expression '{p[1]} {p[2]} {p[3]}'.")
        p[0] = p[1]

def p_expression_check(expression):
    '''expression_check : expression'''
    if isinstance(expression, str) and not any(var.id == expression for var in symbol_table):
        print(f"Semantic error: Variable '{expression}' not declared before use.")

def p_operator(p):
    '''operator : PLUS
                | MINUS
                | TIMES
                | DIVIDE
                | EQUALS
                | POWER
                | LT
                | LE
                | GT
                | GE
                | NE
                | EQUIVALENT
                | AND
                | OR
                | PLUSPLUS
                | MINUSMINUS
                | PERCENT
                | RARROW
                | LARROW
                | SEMICOLON
                | ENDERECO'''
    print(f"Operator: {p[1]}")

def p_constant(p):
    '''constant : BOOLEAN
                | CHAR
                | FLOAT
                | INTEGER
                | STRING
                | NULL'''
    print(f"Constant: {p[1]}")

def p_type(p):
    '''type : AUTO_TYPE
            | BOOLEAN_TYPE
            | CHAR_TYPE
            | DOUBLE_TYPE
            | FLOAT_TYPE
            | INT_TYPE
            | LONG_TYPE
            | SIGNED_TYPE
            | SHORT_TYPE
            | STRING_TYPE
            | UNSIGNED_TYPE
            | VOID'''
    p[0] = p[1]

def p_empty(p):
    'empty :'

def p_error(p):
    print(f"Syntax error at {p.value!r}")

def p_array(p):
    '''array : LSBRACES INTEGER RSBRACES array
             | empty'''

parser = yacc.yacc()

if __name__ == "__main__":
    import sys
    import logging
    logging.basicConfig(
        level=logging.INFO,
        filename="parselog.txt"
    )
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as file:
            data = file.read()
        lexer.input(data)
        print("\nParsing:")
        parser.parse(data, debug=logging.getLogger())
        for a in symbol_table:
            print(a.id, a.type)

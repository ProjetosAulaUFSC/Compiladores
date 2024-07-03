from ply import yacc
from lexer import tokens

def p_include_block(p):
    '''include_block : INCLUDE HEADER SEMICOLON include_block
                     | empty'''
    pass

def p_define_block(p):
    '''define_block : DEFINE VARIABLE type SEMICOLON define_block
                    | empty'''
    pass

def p_enum_block(p):
    '''enum_block : ENUM LBRACES enum_values RBRACES'''
    pass

def p_struct_block(p):
    '''struct_block : STRUCT VARIABLE LBRACES struct_values RBRACES'''
    pass

def p_struct_values(p):
    '''struct_values : struct_values type VARIABLE SEMICOLON
                     | empty'''
    pass

def p_if_else(p):
    '''if_else : IF LPAREN expression RPAREN statement ELSE statement
               | IF LPAREN expression RPAREN statement'''
    pass

def p_for(p):
    '''for : FOR LPAREN expression SEMICOLON expression SEMICOLON expression RPAREN statement
           | FOR LPAREN expression SEMICOLON expression SEMICOLON expression RPAREN'''
    pass

def p_while(p):
    '''while : WHILE LPAREN expression RPAREN statement
             | WHILE LPAREN expression RPAREN'''
    pass

def p_do_while(p):
    '''do_while : DO statement WHILE LPAREN expression RPAREN SEMICOLON'''
    pass

def p_switch(p):
    '''switch : SWITCH LPAREN expression RPAREN LBRACES cases RBRACES'''
    pass

def p_cases(p):
    '''cases : case cases
             | default cases
             | empty'''
    pass

def p_case(p):
    '''case : CASE expression COLON statement'''
    pass

def p_default(p):
    '''default : DEFAULT COLON statement'''
    pass

def p_expression(p):
    '''expression : expression operator expression
                  | LPAREN expression RPAREN
                  | constant'''
    pass

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    print(f"Syntax error at {p.value!r}")

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
            | VOID
            '''
    
def p_constant(p):
    '''constant : BOOLEAN
                | CHAR
                | FLOAT
                | INTEGER
                | NULL
                | STRING
    '''

def p_function(p):
    '''function : type VARIABLE LPAREN parameters RPAREN LBRACES statement RBRACES'''

def p_parameters(p):
    '''parameters : type VARIABLE COMMA parameters
                  | type VARIABLE
                  | empty'''

def p_statement(p):
    '''statement : statement
                 | empty'''

def p_operators(p):
    '''operators : AND
                 | COLON
                 | COMMA
                 | COMMENT
                 | DIVIDE
                 | DOT
                 | ENDERECO
                 | EQUALS
                 | EQUIVALENT
                 | GE
                 | GT
                 | LARROW
                 | LBRACES
                 | LE
                 | LPAREN
                 | LSBRACES
                 | LT
                 | MINUS
                 | MINUSMINUS
                 | NE
                 | PERCENT
                 | PLUS
                 | PLUSPLUS
                 | POWER
                 | RARROW
                 | RBRACES
                 | RPAREN
                 | RSBRACES
                 | SEMICOLON
                 | SHARP
                 | TIMES
    '''

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
        parser.parse(data, debug=logging.getLogger())

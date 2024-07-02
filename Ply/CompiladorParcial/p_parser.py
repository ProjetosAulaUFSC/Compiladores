from ply import yacc
from lexer import tokens

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
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression POWER expression
                  | expression LT expression
                  | expression LE expression
                  | expression GT expression
                  | expression GE expression
                  | expression NE expression
                  | expression EQUIVALENT expression
                  | expression AND expression
                  | expression PLUSPLUS
                  | expression MINUSMINUS
                  | expression PERCENT
                  | expression RARROW
                  | expression LARROW
                  | expression ENDERECO
                  | LPAREN expression RPAREN
                  | INTEGER
                  | FLOAT
                  | BOOLEAN
                  | CHAR
                  | STRING
                  | VARIABLE'''
    pass

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    print(f"Syntax error at {p.value!r}")

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

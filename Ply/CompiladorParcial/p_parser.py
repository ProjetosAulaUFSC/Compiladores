from ply import yacc
from lexer import tokens

def p_program(p):
    '''program : include_block define_block enum_block struct_block function_block statement_block'''
    pass

def p_include_block(p):
    '''include_block : INCLUDE HEADER include_block
                     | empty'''
    pass

def p_define_block(p):
    '''define_block : DEFINE VARIABLE type SEMICOLON define_block
                    | empty'''
    pass

def p_enum_block(p):
    '''enum_block : ENUM LBRACES enum_values RBRACES enum_block
                  | empty'''
    pass

def p_enum_values(p):
    '''enum_values : enum_values VARIABLE COMMA
                   | enum_values VARIABLE
                   | empty'''
    pass

def p_struct_block(p):
    '''struct_block : STRUCT VARIABLE LBRACES struct_values RBRACES struct_block
                    | empty'''
    pass

def p_struct_values(p):
    '''struct_values : struct_values type VARIABLE SEMICOLON
                     | empty'''
    pass

def p_function_block(p):
    '''function_block : function function_block
                      | empty'''
    pass

def p_function(p):
    '''function : type VARIABLE LPAREN parameters RPAREN LBRACES statement_block return_block RBRACES'''
    pass

def p_return_block(p):
    '''return_block : RETURN expression SEMICOLON
                    | empty'''
    pass

def p_parameters(p):
    '''parameters : type VARIABLE COMMA parameters
                  | type VARIABLE
                  | empty'''
    pass

def p_statement_block(p):
    '''statement_block : statement statement_block
                       | empty'''
    pass

def p_statement(p):
    '''statement : if_else
                 | for
                 | while
                 | do_while
                 | switch
                 | expression SEMICOLON'''
    pass

def p_if_else(p):
    '''if_else : IF LPAREN expression RPAREN statement ELSE statement
               | IF LPAREN expression RPAREN statement'''
    pass

def p_for(p):
    '''for : FOR LPAREN expression SEMICOLON expression SEMICOLON expression RPAREN statement'''
    pass

def p_while(p):
    '''while : WHILE LPAREN expression RPAREN statement'''
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
    '''case : CASE expression COLON statement SEMICOLON BREAK SEMICOLON'''
    pass

def p_default(p):
    '''default : DEFAULT COLON statement'''
    pass

def p_expression(p):
    '''expression : expression operator expression
                  | LPAREN expression RPAREN
                  | constant
                  | COMMENT
                  | VARIABLE'''
    pass

def p_operator(p):
    '''operator : PLUS
                | MINUS
                | TIMES
                | DIVIDE
                | POWER
                | LT
                | LE
                | GT
                | GE
                | NE
                | EQUIVALENT
                | AND
                | PLUSPLUS
                | MINUSMINUS
                | PERCENT
                | RARROW
                | LARROW
                | ENDERECO'''
    pass

def p_constant(p):
    '''constant : BOOLEAN
                | CHAR
                | FLOAT
                | INTEGER
                | NULL
                | STRING'''
    pass

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

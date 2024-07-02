# main.py
from lexer import lexer
from p_parser import parser

# Para testar o lexer e parser
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as file:
            data = file.read()
        print("Tokens:")
        lexer.input(data)
        for tok in lexer:
            print(tok)
        print("\nParsing:")
        parser.parse(data)

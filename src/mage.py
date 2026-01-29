import keywords
import sys

#### TOKEN TYPES ####
TT_STRING = "STRING"
TT_KEYWORD = "KEYWORD"

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value
    def __repr__(self):
        return f"{self.type} : {self.value}"
    
class Lexer:
    def __init__(self):
        pass
    def read_file(self, file):
        tokens = []

        buffer = ""

        for character in file:
            buffer += character
            if buffer == " " or buffer == "\n":
                buffer = ""
            elif buffer in keywords.keywords:
                tokens.append(Token(TT_KEYWORD, buffer))
                buffer = ""
            elif character == '"' and len(buffer) > 1:
                tokens.append(Token(TT_STRING, buffer))
                buffer = ""
            elif character == ";":
                buffer = ""
        
        return tokens
        
class Mage:
    def __init__(self):
        self.lexer = Lexer()
    def run(self, code):
        with open(code, 'r') as f:
            print(self.lexer.read_file(f.read()))

mage = Mage()
mage.run(sys.argv[1])
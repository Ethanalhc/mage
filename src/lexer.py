import keywords

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
        line = []

        buffer = ""

        for i, character in enumerate(file):
            buffer += character
            if buffer == " " or buffer == "\n":
                buffer = ""
            elif buffer in keywords.keywords:
                line.append(Token(TT_KEYWORD, buffer))
                buffer = ""
            elif character == '"' and len(buffer) > 1:
                line.append(Token(TT_STRING, buffer))
                buffer = ""
            elif character == ";":
                tokens.append(line)
                line = []
                buffer = ""
        
        return tokens
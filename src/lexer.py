# Import Statements
import keywords

# Define Token Types
TT_STRING = "STRING"
TT_KEYWORD = "KEYWORD"

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value
    def __repr__(self):
        return f"{self.type} : {self.value}"
        # __repr__ defines how the class should show up when printed
    
class Lexer:
    def __init__(self):
        pass
    def read_file(self, file):
        tokens = []
        line = []

        buffer = "" # Buffer stores the currently stored word

        for character in file:
            buffer += character
            if buffer == " " or buffer == "\n": # Clears whitespace
                buffer = ""
            elif buffer in keywords.keywords: # Checks for keywords
                line.append(Token(TT_KEYWORD, buffer))
                buffer = ""
            elif character == '"' and len(buffer) > 1: # Checks for strings
                line.append(Token(TT_STRING, buffer.strip('"')))
                buffer = ""
            elif character == ";": # Makes ";" finish a line
                tokens.append(line)
                line = []
                buffer = ""
        
        return tokens
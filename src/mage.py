import lexer
import parser
        
class Mage:
    def __init__(self):
        self.lexer = lexer.Lexer()
        self.parser = parser.Parser()
    def run(self, code):
            tokens = self.lexer.read_file(code)
            print(self.parser.parse(tokens))
import lexer
import parser
import interpreter
        
class Mage:
    def __init__(self):
        self.lexer = lexer.Lexer() # Creates the lexer and parser instances
        self.parser = parser.Parser()
        self.interpreter = interpreter.Interpreter()
    def run(self, code):
        tokens = self.lexer.read_file(code)
        ast = self.parser.parse(tokens)
        self.interpreter.interpret(ast)


            # Runs the program using the instances
import keywords
import stdlib

class Interpreter:
    def interpret(self, ast):
        for line in ast:
            for node in line:
                func = keywords.functions[node.opcode]
                func(*node.operands)
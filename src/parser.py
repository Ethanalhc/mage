import lexer
import keywords

class Node:
    def __init__(self, opcode=None, operands=[]):
        self.opcode = opcode
        self.operands = operands
    def __repr__(self):
        return f"{self.opcode} : {self.operands}"

class Parser:
    def __init__(self):
        pass
    def parse(self, tokens):
        ast = []
        for line in tokens:
            ln = []

            current_node = Node()
            if line == None:
                continue
            for pos, token in enumerate(line):
                if pos == 0 and token.type != lexer.TT_KEYWORD:
                    print("Error: No Keyword!")
                    break
                elif token.type == lexer.TT_KEYWORD:
                    current_node.opcode = keywords.keywords.index(token.value)
                elif token.type == lexer.TT_STRING:
                    current_node.operands.append(token.value)
                
                if len(current_node.operands) == keywords.args_amount[current_node.opcode]:
                    ln.append(current_node)
                    current_node = Node()
            
            ast.append(ln)
        return ast

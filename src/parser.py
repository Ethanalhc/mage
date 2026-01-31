import lexer
import keywords

class Node:
    def __init__(self, opcode=None, operands=None):
        self.opcode = opcode
        self.operands = operands or [] # Operands will be set as an empty list unless operands are defined beforehand.
    def __repr__(self):
        return f"{self.opcode} : {self.operands}"
        # __repr__ defines how the class should show up when printed

class Parser:
    def __init__(self):
        pass
    def parse(self, tokens):
        ast = [] # AST is short for abstract syntax tree which shows the interpreter the order in which to run the program
        for line in tokens:
            ln = []

            current_node = Node() # Stores the currently handled Node

            if line == None:
                continue

            for pos, token in enumerate(line):
                if pos == 0 and token.type != lexer.TT_KEYWORD: # If the line doesn't start with a keyword throw an error
                    print("Error: No Keyword!")
                    break

                elif token.type == lexer.TT_KEYWORD: # If the token is a keyword update the current node to the appropriate keyword
                    current_node.opcode = keywords.keywords.index(token.value)

                elif token.type == lexer.TT_STRING: # If the token is a string add it as an argument to the current node
                    current_node.operands.append(token.value) 
                
                if len(current_node.operands) == keywords.args_amount[current_node.opcode]: # When the current node has enough arguments add it to the line and reset the current node
                    ln.append(current_node)
                    current_node = Node()
            
            ast.append(ln)
            
        return ast

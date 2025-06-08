
import re

class Parser:
    def parse(self, source_code):
        lines = source_code.strip().splitlines()
        ast = []
        for line in lines:
            line = line.strip().rstrip(';')
            if line.startswith("let "):
                var, expr = line[4:].split('=', 1)
                ast.append(("assign", var.strip(), expr.strip()))
            elif line.startswith("print("):
                var = line[6:-1].strip()
                ast.append(("print", var))
        return ast

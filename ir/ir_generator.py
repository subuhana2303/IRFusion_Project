
class IRGenerator:
    def generate(self, ast):
        ir = []
        for node in ast:
            if node[0] == "assign":
                _, var, expr = node
                ir.append(f"{var} = {expr}")
            elif node[0] == "print":
                _, var = node
                ir.append(f"PRINT {var}")
        return ir

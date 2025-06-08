
class CodeGenerator:
    def generate(self, ir_list):
        lines = ["#include <stdio.h>", "int main() {"]
        declared = set()

        for stmt in ir_list:
            if stmt.startswith("PRINT"):
                var = stmt.split()[1]
                lines.append(f'    printf("%d\\n", {var});')
            else:
                var = stmt.split('=')[0].strip()
                if var not in declared:
                    lines.append(f"    int {stmt.strip()};")
                    declared.add(var)
                else:
                    lines.append(f"    {stmt.strip()};")

        lines.append("    return 0;")
        lines.append("}")
        return "\n".join(lines)

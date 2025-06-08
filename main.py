from frontend.parser import Parser
from ir.ir_generator import IRGenerator
from backend.codegen import CodeGenerator

def compile_source(source_code):
    parser = Parser()
    ast = parser.parse(source_code)
    ir_generator = IRGenerator()
    ir = ir_generator.generate(ast)
    codegen = CodeGenerator()
    output_code = codegen.generate(ir)
    return output_code

if __name__ == "__main__":
    with open("samples/example_input.irl", "r") as f:
        source = f.read()
    output = compile_source(source)
    with open("output/generated_code.c", "w") as f:
        f.write(output)
    print("Compilation successful! Output saved to output/generated_code.c")
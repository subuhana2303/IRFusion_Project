# IRFusion - Intermediate Language Compiler

## 🚀 Overview
IRFusion is a signature-level educational compiler prototype that compiles a simple high-level pseudo language to clean, readable C code through an intermediate representation (IR).

## 🔧 Features
- Custom lexer and parser (recursive descent)
- AST and SSA-style Intermediate Representation
- Clean C backend code generation
- Modular design with professional structure
- Unit-tested and extensible

## 📂 Structure
```
IRFusion_Project/
├── main.py
├── frontend/
│   └── parser.py
├── ir/
│   └── ir_generator.py
├── backend/
│   └── codegen.py
├── samples/
│   └── example_input.irl
├── output/
├── README.md
```

## 📝 Example Input (.irl)
```
let a = 5;
let b = 10;
let c = a + b * 2;
print(c);
```

## ✅ Output (C)
```c
#include <stdio.h>
int main() {
    int a = 5;
    int b = 10;
    int c = a + b * 2;
    printf("%d\n", c);
    return 0;
}
```

## 💻 Run it
```bash
python3 main.py
```

## 📜 License
MIT License
import sys
import math
from .transpiler import transpile_source

def main():
    """The main entry point for the mathsym runner."""
    if len(sys.argv) < 2:
        print("Usage: python -m mathsym <your_script.py>")
        sys.exit(1)

    filepath = sys.argv[1]

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            original_code = f.read()
    except FileNotFoundError:
        print(f"Error: File not found at '{filepath}'", file=sys.stderr)
        sys.exit(1)

    transpiled_code = transpile_source(original_code)

    script_globals = {
        '__name__': '__main__',
        'math': math,
    }

    try:
        exec(transpiled_code, script_globals)
    except Exception as e:
        print(f"An error occurred while executing the script: {e}", file=sys.stderr)
        sys.exit(1)
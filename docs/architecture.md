# Architecture: The `mathsym` Runner

This document outlines the technical architecture for the `mathsym` library, which is built on a **command-line runner pattern**. This approach is chosen to overcome Python's parsing limitations while providing a user-friendly experience.

## 1. Core Concept

The user invokes `mathsym` from the command line, passing their script as an argument. The `mathsym` tool reads the user's script *as plain text*, transpiles the math symbols into valid Python code *in memory*, and then executes the resulting code.

This avoids the standard Python parser's `SyntaxError` on unknown symbols because the interpreter never sees the original, symbol-laden code.

## 2. Execution Flow

The process works as follows:

```mermaid
graph TD
    A[User runs<br/>`mathsym my_script.py`] --> B{mathsym.cli:main()};
    B --> C{Read `my_script.py` as text};
    C --> D[transpiler.transpile_source(code)];
    D --> E{Transpiled Python code<br/>(in-memory string)};
    E --> F[Python's `exec()` function];
    F --> G[Output of script];
```

## 3. Entry Points

To provide a convenient user interface, we will support two standard entry points:

### a) The Console Script (`mathsym ...`)

- **Mechanism**: A `[project.scripts]` entry in `pyproject.toml` creates a direct `mathsym` command during `pip install`.
- **File**: `mathsym.exe` (Windows) or `mathsym` (Unix)
- **Target**: This script directly calls the `main()` function in `mathsym/cli.py`.

### b) The Module Runner (`python -m mathsym ...`)

- **Mechanism**: Python's `-m` flag looks for a `__main__.py` file inside the specified package.
- **File**: `mathsym/__main__.py`
- **Target**: This file imports and calls the same `main()` function from `mathsym/cli.py`, acting as a bridge.

## 4. Key Modules

- **`pyproject.toml`**: Configures the project and defines the `mathsym` console script entry point.
- **`mathsym/cli.py`**: Contains the `main()` function. It handles command-line arguments, file I/O, and orchestrates the transpilation and execution process.
- **`mathsym/__main__.py`**: Enables the `python -m mathsym` invocation.
- **`mathsym/transpiler.py`**: Contains the core `transpile_source()` function, which performs the symbol-to-text replacements.
- **`mathsym/symbols.py`**: A centralized dictionary defining the mapping from unicode symbols to their Python equivalents. 
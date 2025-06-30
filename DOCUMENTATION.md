# `mathsym`: In-Depth Technical Documentation

This document provides a detailed technical explanation of the `mathsym` library, its architecture, and its inner workings.

## 1. The Goal and the Core Challenge

**The Goal**: To allow developers to write Python code using familiar, Unicode mathematical symbols (e.g., `√`, `∑`, `≠`) to create code that is more readable and closer to standard mathematical notation.

**The Core Challenge**: The standard Python interpreter cannot execute code containing these symbols. When Python starts to run a script, the first thing it does is parse the text into a valid structure. A line like `c = √(a²)` will cause an immediate `SyntaxError` before any library code (like `import mathsym`) could ever run to fix it. This is a classic "chicken-and-egg" problem.

## 2. The Solution: The "Runner" Architecture

To solve the parsing problem, we can't use a standard library import. Instead, `mathsym` is designed as a **runner**. We give control to our library *first*, which then prepares the code for the standard interpreter.

This is achieved by running scripts via the command:
```bash
python -m mathsym your_script.py
```

This command tells Python to run the `mathsym` module's entry point (`__main__.py`) and pass `your_script.py` as an argument. Our code is now in control. It can read, transform, and then execute the user's script.

### The Workflow

Here is a high-level diagram of the entire process from user code to execution:

```mermaid
graph TD
    subgraph "User's Action"
        A[User writes code in `my_script.py`<br/>`import mathsym`<br/>`c = √(a² + b²)`] --> B{User runs in terminal<br/>`python -m mathsym my_script.py`};
    end

    subgraph "The `mathsym` Transpilation Pipeline"
        C["`cli.py` receives control"] --> D["Reads `my_script.py`'s content"];
        D --> E{"Calls `transpile_source()`"};
        E --> F["1. Tokenize source code<br/>e.g., `['c', '=', '√', '(', 'a', '²', ...]`"];
        F --> G["2. Intelligently replace symbols<br/>`'√'` becomes `'math.sqrt'`<br/>`'²'` becomes `'**2'`<br/>(Strings & comments are ignored)"];
        G --> H["3. Reconstruct code with `untokenize`<br/>(Preserves all original whitespace)"];
        H --> I["4. Prepend `import math` header"];
        I --> J["Final, standard Python code is ready<br/>`import math`<br/>`c = math.sqrt(a**2 + b**2)`"];
    end
    
    subgraph "Execution"
        J --> K["`cli.py` executes the<br/>transpiled code using `runpy`"];
    end

    B --> C;
```

## 3. The Transpilation Pipeline: A Deep Dive

The magic happens inside the `transpile_source` function in `mathsym/transpiler.py`.

### The Flaw of Simple Replacement
Our first implementation used a simple `string.replace()` loop. This approach had a critical flaw: it would replace symbols even when they appeared inside string literals or comments, corrupting them.

```python
# This would be incorrectly changed
print("The symbol for pi is π") 
# -> print("The symbol for pi is math.pi")
```

### The `tokenize` Solution
To fix this, the transpiler uses Python's powerful built-in `tokenize` module. This module parses a string of Python code into a stream of `TokenInfo` objects. Each token has a `type` (like `NAME`, `OP`, `STRING`, or `COMMENT`) and the `string` it represents.

The transpilation process is as follows:

1.  **Generate Tokens**: We feed the source code into `tokenize.generate_tokens`.
2.  **Selective Replacement**: We iterate through the list of tokens. We only perform a replacement if a token meets two conditions:
    *   Its type is `tokenize.NAME` or `tokenize.OP`.
    *   Its string exists as a key in our `MASTER_SYMBOL_MAP`.
    If these conditions are met, we create a new token with the replacement value. Otherwise, we keep the original token. This ensures strings, comments, and other code structures are never altered.
3.  **Reconstruct Code with `untokenize`**: Manually joining the token strings back together would lose all the original formatting and whitespace. The `tokenize.untokenize()` function is the perfect tool for this job. It takes our new list of tokens and masterfully reconstructs the source code with all the original spacing preserved.
4.  **Add Header**: Finally, we prepend `import math` to the top of the transpiled code, ensuring that functions like `math.pi` and `math.sqrt` are available.

## 4. Design Details

### `import mathsym` vs. `import math`
This is a key point of the design:
*   `import mathsym`: This line is a **convention for the developer**. It acts as a clear signal that the file contains special syntax and must be run with the `mathsym` runner. The transpiler itself ignores this line.
*   `import math`: This line is **added by the transpiler** to the final, generated code. It ensures the code is valid, standard Python that can be executed by any interpreter.

### Modular Symbol Mappings
The symbol mappings are not stored in one giant file. They are organized by category into separate files within the `mathsym/mappings/` directory (e.g., `SetTheorySymbols.py`, `GreekSymbols.py`).

The `__init__.py` file in that directory is responsible for importing all these individual dictionaries and merging them into a single `MASTER_SYMBOL_MAP`, which the transpiler then uses for its lookups. This design makes it clean and easy to add new symbols or entire new categories of symbols without touching the core transpiler logic.
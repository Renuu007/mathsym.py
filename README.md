# `mathsym` 🐍✨

**Write Python with the beauty of mathematical notation.**

`mathsym` is a Python utility that allows you to use unicode mathematical symbols (like `√`, `π`, `∑`, `≠`) directly in your Python code. It transpiles your math-enabled code on the fly into standard, executable Python.

## The Problem
Python is powerful, but its syntax can feel verbose for math-heavy domains. Code filled with `math.sqrt`, `**2`, and `my_sum` can look very different from the clean formulas in a textbook.

## The `mathsym` Solution
With `mathsym`, you can write code that looks like the math you're trying to model.

### Before `mathsym`:
```python
import math

# Pythagorean theorem
c = math.sqrt(a**2 + b**2)
```

### With `mathsym`:
```python
# Pythagorean theorem
c = √(a² + b²)
```

## How to Use
`mathsym` works as a command-line runner. You write your code with symbols in a standard `.py` file, and run it like this:

```bash
python -m mathsym your_script.py
```

## Current Status
This project is currently in **Phase 2** of development. The core runner is functional, and we are actively expanding the library of supported symbols.

See `docs/symbols.md` for a full list of implemented and planned symbols.

https://www.rapidtables.com/math/symbols/index.html

## License
This project is licensed under the MIT License. See the `LICENSE` file for details. 
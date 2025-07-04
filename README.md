<div align="center">
  <h1 style="border-bottom: none;">
    mathsym 🐍✨
  </h1>
</div>



[![PyPI version](https://badge.fury.io/py/mathsym.svg)](https://badge.fury.io/py/mathsym)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Write Python with the beauty of mathematical notation.**

`mathsym` is a Python utility that allows you to use unicode mathematical symbols (like `√`, `π`, `∑`, `≠`) directly in your Python code. It transpiles your math-enabled code on the fly into standard, executable Python.

---

## 📖 Table of Contents
- [The Problem](#-the-problem)
- [The `mathsym` Solution](#-the-mathsym-solution)
- [Installation](#-installation)
- [How to Use](#-how-to-use)
- [Project Roadmap](#-project-roadmap)
- [Known Issues](#-known-issues)
- [Contributing](#-contributing)
- [License](#-license)

---

## 😫 The Problem
Python is powerful, but its syntax can feel verbose for math-heavy domains. Code filled with `math.sqrt`, `**2`, and `my_sum` can look very different from the clean formulas in a textbook.

## ✨ The `mathsym` Solution
With `mathsym`, you can write code that looks like the math you're trying to model.

### Before `mathsym`:
```python
import math

# Pythagorean theorem
c = math.sqrt(a**2 + b**2)
```

### With `mathsym`:
```python
# The import signals to developers that this is a mathsym file.
import mathsym

# Pythagorean theorem
c = √(a² + b²)
```

For a full list of currently supported symbols, see the [**Symbol Reference**](docs/symbols.md).

---

## 📦 Installation

This package is not yet available on PyPI. To install it locally for development, clone the repository and use `pip`:

```bash
git clone https://github.com/VinsmokeSomya/mathsym.py.git
cd mathsym.py
pip install -e .
```

---

## 🚀 How to Use
`mathsym` works as a command-line runner. You write your code with symbols in a standard `.py` file, and run it from your terminal:

```bash
python -m mathsym your_script.py
```

See the `examples/` directory for runnable demo files.

---

## 🗺️ Project Roadmap

This project is currently in **Phase 2** of development. The core runner is functional, and we are actively expanding the library of supported symbols.

- ✅ **Phase 1**: Core runner and transpiler MVP.
- 🚧 **Phase 2**: Expand symbol library & improve transpiler safety.
- 📝 **Phase 3**: Interactive support (Jupyter Magic, REPL).
- 📝 **Phase 4**: Linter integration & IDE extensions.

See `docs/plan.md` and `docs/issues_and_solutions.md` for more details.

---

## ⚠️ Known Issues

### Linter and IDE Errors
Because `mathsym` uses syntax that is not standard Python, your IDE's linter (the tool that shows red squiggly lines) will report syntax errors.

**This is expected behavior.**

The linter only understands standard Python and has no knowledge of the `mathsym` runner. The code will execute correctly when run with `python -m mathsym`, but it will look like an error in your editor. Our long-term goal is to develop an IDE extension to resolve this.

---

## 🙌 Contributing
We welcome contributions! Please see our `CONTRIBUTING.md` file for details on how to set up your development environment, run tests, and submit a pull request.

---

## 📜 License
This project is licensed under the MIT License. See the `LICENSE` file for details. 

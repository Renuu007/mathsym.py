# Development Plan

This document outlines the phased development plan for `mathsym`.

## Phase 1: Core Runner and Transpiler
*Goal: Establish a minimum viable product.*

- [ ] **Setup project structure**: Create `mathsym/` directory and `pyproject.toml`.
- [ ] **Create entry points**: Implement `mathsym/cli.py` and `mathsym/__main__.py`.
- [ ] **Define initial symbols**: Create `mathsym/symbols.py` with a basic mapping (e.g., `π` -> `math.pi`, `√` -> `math.sqrt`).
- [ ] **Build the transpiler**: Implement the core replacement logic in `mathsym/transpiler.py` using `tokenize`.
- [ ] **End-to-end test**: Ensure `python -m mathsym examples/demo.py` works.

## Phase 2: Advanced Symbol Mapping & Features
*Goal: Expand functionality and robustness.*

- [ ] **Expand symbol library**: Add more mappings for calculus, linear algebra, and set theory (`∇`, `∂`, `∑`, `∏`, `⊗`, `∪`, `∩`).
- [ ] **Context-aware transpiling**: Improve transpiler to handle more complex cases (e.g., distinguishing unary operators from binary ones).
- [ ] **Configuration**: Allow users to extend or override symbol mappings with a config file.

## Phase 3: Interactive & Ecosystem Integration
*Goal: Make `mathsym` useful in interactive environments.*

- [ ] **Jupyter/IPython Magic**: Develop a `%mathsym` magic command to transpile and run code in a notebook cell.
- [ ] **REPL**: Create a simple `mathsym-repl` for a live, interactive session.

## Phase 4: Packaging and Documentation
*Goal: Prepare the library for public release.*

- [ ] **Unit Tests**: Write comprehensive tests for the transpiler and CLI.
- [ ] **User Documentation**: Write clear documentation on how to use `mathsym`, including all supported symbols.
- [ ] **Packaging**: Configure `pyproject.toml` for a PyPI release.
- [ ] **Publish**: Publish the package to the Python Package Index. 
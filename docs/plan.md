# Development Plan

This document outlines the phased development plan for `mathsym`.

**Current Status**: We have completed Phase 1 and are now actively working on tasks in Phase 2 and Phase 4. The core engine is stable, and work is focused on expanding symbols, tests, and documentation.

## Phase 1: Core Runner and Transpiler
*Goal: Establish a minimum viable product.*
**Status: ✅ COMPLETE**

- [x] **Setup project structure**: Create `mathsym/` directory and `pyproject.toml`.
- [x] **Create entry points**: Implement `mathsym/cli.py` and `mathsym/__main__.py`.
- [x] **Define initial symbols**: Create `mathsym/symbols.py` with a basic mapping (e.g., `π` -> `math.pi`, `√` -> `math.sqrt`).
- [x] **Build the transpiler**: Implement the core replacement logic in `mathsym/transpiler.py` using `tokenize`.
- [x] **End-to-end test**: Ensure `python -m mathsym examples/demo.py` works.

## Phase 2: Advanced Symbol Mapping & Features
*Goal: Expand functionality and robustness.*
**Status: 🚧 IN PROGRESS**

- [🚧] **Expand symbol library**: Add more mappings for calculus, linear algebra, and set theory (`∇`, `∂`, `∑`, `∏`, `⊗`, `∪`, `∩`).
- [🚧] **Context-aware transpiling**: Improve transpiler to handle more complex cases (e.g., distinguishing unary operators from binary ones).
- [ ] **Configuration**: Allow users to extend or override symbol mappings with a config file.

## Phase 3: Interactive & Ecosystem Integration
*Goal: Make `mathsym` useful in interactive environments.*
**Status: 📝 NOT STARTED**

- [ ] **Jupyter/IPython Magic**: Develop a `%mathsym` magic command to transpile and run code in a notebook cell.
- [ ] **REPL**: Create a simple `mathsym-repl` for a live, interactive session.

## Phase 4: Packaging and Documentation
*Goal: Prepare the library for public release.*
**Status: 🚧 IN PROGRESS**

- [🚧] **Unit Tests**: Write comprehensive tests for the transpiler and CLI.
- [🚧] **User Documentation**: Write clear documentation on how to use `mathsym`, including all supported symbols.
- [ ] **Packaging**: Configure `pyproject.toml` for a PyPI release.
- [ ] **Publish**: Publish the package to the Python Package Index. 
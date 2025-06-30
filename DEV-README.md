# `mathsym` Developer README

Welcome, contributor! This document is the central hub for developers working on the `mathsym` project. For user-facing information, please see the main [`README.md`](README.md).

## Project Goal

Our goal is to create a Python utility that allows for the use of Unicode mathematical symbols directly in code, making it more readable and intuitive for mathematicians, scientists, and engineers.

## Key Resources & Documentation

- **Symbol Reference**: We use [RapidTables Math Symbols](https://www.rapidtables.com/math/symbols/index.html) as a primary source for identifying standard mathematical symbols and their meanings.
- **Project Roadmap**: The high-level development plan is in [`docs/plan.md`](docs/plan.md).
- **Current Tasks**: The active to-do list for the current development phase is in [`docs/todolist.md`](docs/todolist.md).
- **Technical Deep Dive**: A detailed explanation of the runner architecture and transpilation process is in [`DOCUMENTATION.md`](DOCUMENTATION.md).
- **Contribution Guidelines**: Instructions for submitting code are in [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Getting Started with Development

1.  **Fork and Clone**: Fork the repository and clone it to your local machine.
2.  **Set up a Virtual Environment**:
    ```bash
    # On Windows
    python -m venv venv
    venv\Scripts\activate

    # On macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  **Install in Editable Mode**: This allows you to test your changes immediately.
    ```bash
    pip install -e .
    ```
4.  **Run the Test Suite**: Before making changes, ensure all tests pass.
    ```bash
    python -m unittest discover tests
    ```

## Project Structure Overview

- `mathsym/`: The core library source code.
  - `mappings/`: Contains all the individual symbol map files.
  - `transpiler.py`: The heart of the library; handles the token-based code translation.
  - `cli.py`: The command-line interface logic.
  - `__main__.py`: The entry point for the `python -m mathsym` runner.
- `docs/`: All project documentation, plans, and specifications.
- `tests/`: The unit test suite.
- `examples/`: Sample scripts demonstrating `mathsym` usage.
- `.github/`: Contains community health files like the pull request template.
- `pyproject.toml`: The project definition and build configuration file. 
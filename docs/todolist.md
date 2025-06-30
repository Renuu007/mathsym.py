# `mathsym` To-Do List

This is the task list for the initial development phase of `mathsym`.

## Phase 1: Core Runner and Transpiler

- [ ] **Task 1**: Initialize the project structure.
  - [ ] Create the main `mathsym/` directory.
  - [ ] Create an empty `mathsym/__init__.py`.

- [ ] **Task 2**: Create the `pyproject.toml` file.
  - [ ] Define project metadata (`name`, `version`).
  - [ ] Add the `[project.scripts]` section to define the `mathsym` command.

- [ ] **Task 3**: Create the symbol mapping file.
  - [ ] Create `mathsym/symbols.py`.
  - [ ] Add a dictionary with a few initial symbols: `π`, `√`, `²`, `³`.

- [ ] **Task 4**: Implement the core transpiler logic.
  - [ ] Create `mathsym/transpiler.py`.
  - [ ] Write a `transpile_source` function that uses Python's `tokenize` module to replace symbols from the map.

- [ ] **Task 5**: Implement the CLI runner.
  - [ ] Create `mathsym/cli.py` with a `main` function.
  - [ ] The `main` function should read a file path, call the transpiler, and execute the result with `exec()`.

- [ ] **Task 6**: Implement the module runner entry point.
  - [ ] Create `mathsym/__main__.py`.
  - [ ] It should import `main` from `cli.py` and call it.

- [ ] **Task 7**: Create a test case.
  - [ ] Create an `examples/` directory.
  - [ ] Create `examples/demo.py` with some math symbols to test the runner.

- [ ] **Task 8**: End-to-End Test.
  - [ ] Run `python -m mathsym examples/demo.py` from the root and verify the output.
  - [ ] Perform a local install (`pip install .`) and test the `mathsym examples/demo.py` command. 
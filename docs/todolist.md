# `mathsym` Current To-Do List

This document tracks the active development tasks for the project. The original to-do list for Phase 1 is complete. This new list focuses on the goals for Phase 2 and 4.

## Phase 2: Advanced Symbol Mapping & Features

- [ ] **Task 1: Expand Symbol Library**
  - [ ] Review `AlgebraSymbols.py` and add more common symbols.
  - [ ] Review `Calculus_AnalysisSymbols.py` and add more common symbols.
  - [ ] Review `GeometrySymbols.py` and add more common symbols.
  - [ ] Review `LogicSymbols.py` and add more common symbols.

- [ ] **Task 2: Research Advanced Transpiling Cases**
  - [ ] Research potential edge cases where the tokenizer might need more context (e.g., distinguishing a minus sign from a negative number).
  - [ ] Create new test cases that would fail if the context is wrong.

- [ ] **Task 3: Implement Configuration File Support**
  - [ ] Design a format for a user configuration file (e.g., `mathsym.toml` or `.mathsymrc`).
  - [ ] Implement logic to find and load this file to allow users to add their own custom symbol mappings.

## Phase 4: Packaging and Documentation

- [ ] **Task 1: Expand Test Suite Coverage**
  - [ ] Create a dedicated test file for each symbol category (e.g., `test_algebra_symbols.py`, `test_set_theory_symbols.py`).
  - [ ] Write a test to ensure every single symbol in the `MASTER_SYMBOL_MAP` is correctly transpiled.

- [ ] **Task 2: Finalize Documentation**
  - [ ] Create a script to auto-generate a table of all supported symbols for `docs/symbols.md` to ensure it's always up to date.
  - [ ] Review all documentation for clarity and completeness.

- [ ] **Task 3: Prepare for PyPI Release**
  - [ ] Add classifiers, author information, and other necessary metadata to `pyproject.toml`.
  - [ ] Ensure the `LICENSE` and `README.md` are finalized. 
# Known Issues & Planned Solutions

This document outlines known limitations of `mathsym` and the proposed long-term solutions to address them. These represent future development goals beyond the core MVP.

---

## 1. Linter and IDE Integration

### The Problem
Standard Python linters, which are integrated into most code editors, do not recognize `mathsym`'s extended unicode syntax. As a result, they flag valid `mathsym` code with `SyntaxError` warnings (e.g., red squiggly lines). While the code runs correctly with our runner, this provides a poor developer experience.

#### Symptom: "Unused Import" Warning
A common side-effect of this issue is that linters will flag the `import mathsym` line with an "unused import" warning (e.g., Pylance's `reportUnusedImport`).

- **Why it happens**: The linter is technically correct. In a standard Python file, the `import mathsym` statement doesn't provide any functions or variables that are directly accessed (e.g., `mathsym.foo()`).
- **Its real purpose**: The import's purpose is not for the code itself, but as a clear signal to the **developer** that the file must be executed with the `mathsym` runner.
- **Workaround**: This warning can typically be suppressed on a case-by-case basis by adding a `# noqa: F401` comment to the line, but this is a manual fix.

### Solution A: User-Side Configuration (The "Good" Solution)

We can research and provide documentation for how users can configure their specific editors to ignore syntax errors in files that use the `mathsym` library.

**Implementation Plan:**
1.  **Research**: Investigate the configuration options for popular linters like `Pylint`, `Flake8`, and the one built into VS Code (`Pylance`).
2.  **Develop Configurations**: Create sample configuration files (e.g., `.pylintrc`, `pyproject.toml`, VS Code's `settings.json`). A common approach is to define a rule that disables syntax checking on a file-by-file basis if a line like `import mathsym` is detected.
3.  **Document**: Create a `LINTER_CONFIG.md` document with clear, step-by-step instructions for each supported editor, explaining how to apply the settings.

**Pros:**
- Empowers users to fix the issue in their own environment.
- Does not require building a full extension.

**Cons:**
- Places the configuration burden on the end-user.
- We would need to maintain configurations for multiple, ever-changing editors and tools.

### Solution B: Custom IDE Extension (The "Gold Standard" Solution)

The most seamless and professional solution is to build a dedicated IDE extension (e.g., for VS Code, which is the most popular).

**Implementation Plan:**
1.  **Language Server Protocol (LSP)**: The core of a modern IDE extension is a language server. We would need to build a `mathsym-language-server`.
2.  **Transpilation Hook**: The language server's primary job would be to intercept the code from the editor. Before passing it to the standard Python linter for analysis, it would first run the code through our `mathsym` transpiler in memory.
3.  **Provide Clean Code to Linter**: The linter would receive the fully-transpiled, standard Python code. It would see `math.sqrt(a**2)` instead of `√(a²)`, and would therefore report no syntax errors.
4.  **Syntax Highlighting (Bonus)**: The extension could also provide enhanced syntax highlighting, perhaps rendering supported unicode symbols in a distinct color to improve readability.

**Pros:**
- Provides a perfect, zero-configuration experience for the end-user.
- The "it just works" solution that is expected of professional-grade tools.

**Cons:**
- **High Complexity**: This is a major engineering effort and a separate project in its own right. It requires knowledge of IDE extension APIs and the Language Server Protocol.
- **Maintenance**: The extension would need to be maintained in parallel with the core `mathsym` library. 
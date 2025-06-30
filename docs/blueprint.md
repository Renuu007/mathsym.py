# Blueprint: `mathsym`

## 1. Vision

To allow mathematicians, scientists, and engineers to write Python code that closely mirrors standard mathematical notation, making the code more expressive, readable, and intuitive.

## 2. Problem Statement

Python's strict rules for identifiers prevent the use of common mathematical symbols (e.g., `∇`, `∂`, `∑`, `√`, `π`). This forces developers to use verbose ASCII equivalents (`grad`, `partial`, `sum`, `sqrt`, `pi`), which can make complex formulas look cluttered and disconnected from their source material in textbooks and papers.

## 3. Core Objective

Create a Python library named `mathsym` that, when used as a runner (`python -m mathsym <script>`), enables the direct use of mathematical symbols as variables and operators within a standard `.py` file.

## 4. Key Features

- **Symbol-to-Identifier Mapping**: Transpile unicode math symbols into valid Python identifiers (e.g., `∇f` → `grad(f)`).
- **Symbol-to-Operator/Function Mapping**: Transpile unicode operators and symbols into Python's operators or function calls (e.g., `A ∪ B` → `A | B`, `√x` → `math.sqrt(x)`).
- **Seamless Execution**: Allow users to run their math-enabled scripts with a single command, without a visible, intermediate file-generation step.
- **Standard Tooling**: The library will be invoked as a standard command-line tool (`mathsym <script>`) or module runner (`python -m mathsym <script>`).
- **Extensibility**: Allow users to easily add or modify symbol mappings. 
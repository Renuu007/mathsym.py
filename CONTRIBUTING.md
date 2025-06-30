# Contributing to `mathsym`

First off, thank you for considering contributing! `mathsym` is an open-source project, and we welcome any contributions, from bug reports to new features.

## Ways to Contribute
- **Reporting Bugs**: If you find a bug, please open an issue and provide as much detail as possible, including the code that caused the bug and the error message.
- **Suggesting Enhancements**: If you have an idea for a new feature or an improvement to an existing one, open an issue to start a discussion.
- **Pull Requests**: If you want to contribute code, we welcome pull requests.

## Development Setup

To get started with development, you'll need to set up a local environment.

1.  **Fork and Clone the Repository**:
    ```bash
    git clone https://github.com/YOUR_USERNAME/mathsym.py.git
    cd mathsym.py
    ```

2.  **Create a Virtual Environment**:
    It's highly recommended to work in a virtual environment.
    ```bash
    # On Windows
    python -m venv venv
    venv\Scripts\activate

    # On macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install in Editable Mode**:
    This command will install the project in "editable" mode, so any changes you make to the source code will be immediately reflected when you run the tool.
    ```bash
    pip install -e .
    ```

4.  **Install Developer Dependencies**:
    We will add developer dependencies like `pytest` here in the future.
    ```bash
    # pip install -r requirements-dev.txt (coming soon)
    ```

## Running Tests

Before submitting a pull request, please ensure that all tests pass. We use `pytest` for our testing framework.

```bash
# (Coming soon)
pytest
```

## Submitting a Pull Request

1.  Create a new branch for your feature or bugfix:
    ```bash
    git checkout -b my-new-feature
    ```
2.  Make your changes and commit them with a clear message.
3.  Push your branch to your fork:
    ```bash
    git push origin my-new-feature
    ```
4.  Open a pull request from your fork to the main `mathsym.py` repository. Please fill out the pull request template with the required information.

Thank you for your contribution! 
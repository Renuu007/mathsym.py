import unittest
import math
from mathsym.transpiler import transpile_source

class TestTranspiler(unittest.TestCase):

    def test_basic_symbol_transpilation(self):
        """
        Tests the replacement of a basic math symbol (π).
        """
        code = "x = π"
        # The transpiler adds 'import math' and replaces π with math.pi
        expected_code = "import math\n\nx = math.pi"
        transpiled_code = transpile_source(code)
        self.assertEqual(transpiled_code.strip(), expected_code)

    def test_set_theory_operator_transpilation(self):
        """
        Tests that set theory symbols are transpiled to their
        corresponding Python operators (e.g., ∩ -> &).
        """
        code = "C = A ∩ B"
        expected_code = "import math\n\nC = A & B"
        transpiled_code = transpile_source(code)
        self.assertEqual(transpiled_code.strip(), expected_code)

        code = "D = A ∪ B"
        expected_code = "import math\n\nD = A | B"
        transpiled_code = transpile_source(code)
        self.assertEqual(transpiled_code.strip(), expected_code)

    def test_no_replacement_in_strings(self):
        """
        Tests that symbols inside string literals are not replaced.
        """
        code = 'print("The value of π is approximately 3.14")'
        # The transpiler should NOT change the string
        expected_code = 'import math\n\nprint("The value of π is approximately 3.14")'
        transpiled_code = transpile_source(code)
        self.assertEqual(transpiled_code.strip(), expected_code)


if __name__ == '__main__':
    unittest.main() 
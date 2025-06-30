import io
import tokenize
from .mappings import MASTER_SYMBOL_MAP

def transpile_source(source_code: str) -> str:
    """
    Reads Python source code and replaces unicode symbols with their
    ASCII equivalents based on the MASTER_SYMBOL_MAP.
    """
    # Prepend the necessary imports
    header = "import math\n\n"

    # A simple, direct replacement strategy.
    # This is less safe than tokenizing if symbols could appear in strings,
    # but it's more direct for this use case.
    for symbol, replacement in MASTER_SYMBOL_MAP.items():
        source_code = source_code.replace(symbol, replacement)
    
    return header + source_code
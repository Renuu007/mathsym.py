import io
import tokenize
from .mappings import MASTER_SYMBOL_MAP

def transpile_source(source_code: str) -> str:
    """
    Reads Python source code and replaces unicode symbols with their
    ASCII equivalents based on the MASTER_SYMBOL_MAP.

    This version uses the `tokenize` module to avoid replacing
    symbols inside strings or comments, and `untokenize` to
    preserve original spacing.
    """
    header = "import math\n\n"
    
    tokens = tokenize.generate_tokens(io.StringIO(source_code).readline)
    new_tokens = []
    for token in tokens:
        if token.type in (tokenize.NAME, tokenize.OP) and token.string in MASTER_SYMBOL_MAP:
            # Create a new token with the replacement string
            new_string = MASTER_SYMBOL_MAP[token.string]
            new_token = tokenize.TokenInfo(token.type, new_string, token.start, token.end, token.line)
            new_tokens.append(new_token)
        else:
            new_tokens.append(token)

    transpiled_code = tokenize.untokenize(new_tokens)

    return header + transpiled_code
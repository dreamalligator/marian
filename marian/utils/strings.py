import re

FIRST_CAP_RE = re.compile('(.)([A-Z][a-z]+)')
ALL_CAP_RE = re.compile('([a-z0-9])([A-Z])')

def snake_case(name):
    """takes a PascalCase input string and converts to snake_case."""
    split_str = FIRST_CAP_RE.sub(r'\1_\2', name)
    return ALL_CAP_RE.sub(r'\1_\2', split_str).lower()

def hlt(input_str, color='\x1b[1;32m'):
    """highlight the string."""
    return f'{color}{input_str}\x1b[0m'

def warn(input_str):
    return hlt(input_str, color='\033[93m')

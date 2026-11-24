"""Inspect Python's reserved keywords."""

import keyword

# Keywords have special meaning in Python and cannot be used as identifiers.
print("Python keywords:")
print(keyword.kwlist)

# Check a word without writing invalid Python syntax such as `for = 10`.
candidate = "for"
print(f"Is '{candidate}' a keyword? {keyword.iskeyword(candidate)}")

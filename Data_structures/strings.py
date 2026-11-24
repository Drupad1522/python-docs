"""Examples of creating, indexing, slicing, and changing strings."""

# Strings can use single, double, or triple quotes.
single_quoted = 'abcdefgh'
double_quoted = "abcdefgh"
multiline = """My name is
Drupad"""
print("Single-quoted string:", single_quoted)
print("Double-quoted string:", double_quoted)
print("Triple-quoted string:\n", multiline)

# String indexes start at zero; negative indexes count from the end.
text = "hello, world!"
print("\nFirst character:", text[0])
print("Last character:", text[-1])
print("First character from the end:", text[-len(text)])

# Slicing uses text[start:end:step]; the end position is excluded.
welcome = "Hi, welcome"
print("\nFirst five characters:", welcome[:5])
print("Every second character in a slice:", welcome[1:6:2])

# Strings are iterable, so a for loop visits each character in sequence.
print("\nLoop through characters:")
for character in single_quoted:
    print(character)

# len() returns the number of characters in the string.
print("\nString length:", len(single_quoted))

# Case conversion methods return new strings; they do not change the original.
sample = "abcd"
print("Uppercase:", sample.upper())
print("Lowercase:", sample.upper().lower())

# strip() removes matching characters from the beginning and end.
print("\nWhitespace stripping:")
text_with_spaces = " python program "
print(repr(text_with_spaces.strip()))
print("Strip characters:", "python program".strip("py"))

# replace() returns a copy with the requested text substituted.
phrase = "python programming"
print("\nReplacement:", phrase.replace("python", "java"))

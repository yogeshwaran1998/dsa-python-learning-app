"""
Variables, Primitive Types, and Strings - Implementation Guide
=============================================================
Comprehensive Python implementations covering variables, primitive types,
type conversion, None, and string operations commonly tested in interviews.
"""

from typing import List, Optional


# =============================================================================
# SECTION 1: VARIABLES
# =============================================================================

# Creating variables - Python automatically determines the type
name = "Alice"          # String variable
age = 30                # Integer variable
price = 19.99           # Float variable
is_active = True        # Boolean variable

# Multiple assignment - assign same value to multiple variables
x = y = z = 0           # All three are now 0

# Swapping variables (Pythonic way - no temp variable needed)
a, b = 1, 2
a, b = b, a             # Now a=2, b=1

# Underscores for readability in large numbers
population = 7_000_000_000    # Same as 7000000000
price = 1_999_99              # Same as 199999

# Checking variable type using type() - returns the class
print(type(name))             # <class 'str'>
print(type(age))              # <class 'int'>
print(type(price))             # <class 'float'>
print(type(is_active))         # <class 'bool'>


# =============================================================================
# SECTION 2: PRIMITIVE TYPES
# =============================================================================

# Integer - whole numbers (arbitrary precision in Python)
positive_int = 42
negative_int = -10
zero = 0
binary_int = 0b1010            # Binary: 10
hex_int = 0xFF                 # Hexadecimal: 255
octal_int = 0o77               # Octal: 63

# Float - decimal numbers (IEEE 754 double precision)
regular_float = 3.14
scientific = 1.5e10             # 1.5 * 10^10 = 15000000000.0
small_float = 1e-5             # 0.00001

# Boolean - True or False (must be capitalized in Python)
is_valid = True
is_empty = False

# String - sequence of Unicode characters
single_quote = 'Hello'
doubleHello_quote = ""
multiline = """This is a
multi-line string"""
raw_string = r"C:\Users\name"  # Raw string - escapes ignored

# Type checking with isinstance() - preferred over type() == ...
print(isinstance(age, int))           # True
print(isinstance(price, float))        # True
print(isinstance(name, str))           # True
print(isinstance(is_active, bool))     # True


# =============================================================================
# SECTION 3: TYPE CONVERSION
# =============================================================================

# String to Integer
str_to_int = int("42")                 # 42
str_to_int_base2 = int("1010", 2)       # 10 (binary to decimal)
str_to_int_base16 = int("FF", 16)       # 255 (hex to decimal)

# Integer to String
int_to_str = str(42)                    # "42"

# Integer to Float
int_to_float = float(42)                # 42.0

# Float to Integer - truncates towards zero (not rounded!)
float_to_int = int(3.7)                 # 3 (loses decimal part)
float_to_int2 = int(-3.7)               # -3

# String to Float
str_to_float = float("3.14")            # 3.14
str_to_float_scientific = float("1e10")  # 10000000000.0

# Convert to Boolean - falsy values: 0, 0.0, "", [], {}, None
bool_from_int = bool(1)                 # True
bool_from_zero = bool(0)                # False
bool_from_string = bool("hello")        # True
bool_from_empty_string = bool("")       # False
bool_from_list = bool([1, 2, 3])         # True
bool_from_empty_list = bool([])         # False
bool_from_none = bool(None)             # False

# Implicit type conversion (type coercion)
result = 10 + 3.14                       # 13.14 (int + float = float)
result2 = True + 5                       # 6 (True = 1)
result3 = False + 5                      # 5 (False = 0)

# Using round() for proper rounding
rounded = round(3.7)                     # 4
rounded_precise = round(3.14159, 2)      # 3.14 (rounded to 2 decimals)


# =============================================================================
# SECTION 4: NONE TYPE
# =============================================================================

# None represents absence of value - singleton object
result = None

# Checking for None - use "is None" not "== None"
if result is None:
    print("No result available")

# Use case: function that may not return anything
def find_item(items: List[int], target: int) -> Optional[int]:
    """Find index of target in list, return None if not found."""
    for index, item in enumerate(items):
        if item == target:
            return index
    return None  # Explicitly return None when not found

# Safely handle None return values
index = find_item([1, 2, 3], 5)
if index is not None:
    print(f"Found at index {index}")
else:
    print("Item not found")

# None vs empty - different semantics
empty_list = []             # Valid empty container
no_list = None              # No list provided

# Practical example: optional parameters
def process_data(data=None):
    """Handle optional parameter with None default."""
    if data is None:
        data = []           # Use default empty list
    # Process data...


# =============================================================================
# SECTION 5: STRING SLICING
# =============================================================================

s = "Hello, World!"

# Basic slicing - [start:stop] - stop is EXCLUSIVE
first_five = s[0:5]          # "Hello"
first_five_simplified = s[:5]  # Same - omit start

# From index 7 to end
rest = s[7:]                # "World!"

# Full string copy
full_copy = s[:]            # "Hello, World!"

# Negative indexing - starts from end
last_char = s[-1]           # "!" (last character)
last_five = s[-5:]          # "orld!"
everything_but_last = s[:-1]  # "Hello, World"

# Step slicing - [start:stop:step]
every_second = s[::2]       # "HloWrd" (characters at even indices)
every_third = s[::3]        # "Hlool!"

# Reverse string using negative step
reversed_string = s[::-1]   # "!dlroW ,olleH"

# Advanced slicing examples
word = "Python"
first_two = word[:2]         # "Py"
last_two = word[-2:]        # "on"
middle_removed = word[1:-1]  # "ytho" (without first and last)


# =============================================================================
# SECTION 6: F-STRINGS (FORMATTED STRING LITERALS)
# =============================================================================

name = "Alice"
age = 30
score = 95.567

# Basic f-string - embed variables directly
greeting = f"Hello, {name}!"           # "Hello, Alice!"
info = f"{name} is {age} years old"   # "Alice is 30 years old"

# Format specifiers for numbers
formatted_score = f"{score:.2f}"      # "95.57" (2 decimal places)
formatted_score3 = f"{score:.1f}"     # "95.6"
zero_padded = f"{age:05d}"            # "00030" (5 digits, zero-padded)
thousands = f"{1000000:,}"             # "1,000,000" (thousands separator)

# Width specification
right_aligned = f"{age:>5}"            # "   30" (right-aligned in 5 chars)
left_aligned = f"{age:<5}"             # "30   " (left-aligned)
centered = f"{age:^5}"                 # "  30  " (centered)

# Expressions inside f-strings
calc = f"{age * 2}"                   # "60"
conditional = f"{'adult' if age >= 18 else 'minor'}"  # "adult"

# Calling methods inside f-strings
method_call = f"{name.upper()}"       # "ALICE"
method_call2 = f"{name.lower()}"      # "alice"

# F-strings with datetime
from datetime import datetime
now = datetime.now()
formatted_date = f"{now:%Y-%m-%d}"    # "2024-01-15"
formatted_time = f"{now:%H:%M:%S}"    # "14:30:45"


# =============================================================================
# SECTION 7: SPLIT AND JOIN
# =============================================================================

# split() - split string into list
text = "apple,banana,cherry"
fruits = text.split(",")              # ["apple", "banana", "cherry"]

# split() with maxsplit parameter - limit number of splits
limited = "a,b,c,d".split(",", 2)     # ["a", "b", "c,d"]

# split() without arguments - split on whitespace
words = "hello    world".split()      # ["hello", "world"]

# splitlines() - split on line breaks
lines = "line1\nline2\r\nline3".splitlines()  # ["line1", "line2", "line3"]

# join() - join list into string (opposite of split)
words_to_join = ["apple", "banana", "cherry"]
joined_comma = ",".join(words_to_join)   # "apple,banana,cherry"
joined_space = " ".join(words_to_join)   # "apple banana cherry"
joined_newline = "\n".join(words_to_join) # "apple\nbanana\ncherry"

# Efficient string building - NEVER use + in loops!
# WRONG: O(n^2) time complexity
 inefficient = ""
 for word in words_to_join:
     inefficient += word      # Creates new string each iteration

# CORRECT: O(n) using join
efficient = "".join(words_to_join)  # "applebananacherry"

# Practical example: parsing CSV-like data
csv_line = "john,30,NYC"
parts = csv_line.split(",")
name_from_csv, age_from_csv, city_from_csv = parts


# =============================================================================
# SECTION 8: OTHER STRING METHODS
# =============================================================================

s = "  Hello, World!  "

# Case conversion methods
print(s.upper())                      # "  HELLO, WORLD!  "
print(s.lower())                      # "  hello, world!  "
print(s.title())                      # "  Hello, World!  "
print(s.capitalize())                 # "  hello, world!  "

# Whitespace handling
print(s.strip())                      # "Hello, World!" (removes both ends)
print(s.lstrip())                     # "Hello, World!  "
print(s.rstrip())                     # "  Hello, World!"

# Search methods
s2 = "Hello, World!"
print(s2.find("World"))               # 7 (index, -1 if not found)
print(s2.index("World"))              # 7 (raises ValueError if not found)
print(s2.count("l"))                  # 3 (count occurrences)
print(s2.startswith("Hello"))        # True
print(s2.endswith("!"))              # True

# Replace
print(s2.replace("World", "Python"))  # "Hello, Python!"

# Split into characters
chars = list("hello")                 # ["h", "e", "l", "l", "o"]

# Partition - splits into 3 parts: before, separator, after
result = "hello world".partition(" ")  # ("hello", " ", "world")
# Useful when you need exactly 3 parts

# String checking methods
print("123".isdigit())                # True
print("abc".isalpha())                # True
print("abc123".isalnum())             # True
print("hello world".isspace())        # False
print("hello world".split())          # ["hello", "world"]


# =============================================================================
# SECTION 9: PRACTICAL INTERVIEW PATTERNS
# =============================================================================

def reverse_string(s: str) -> str:
    """Reverse a string - common interview question."""
    return s[::-1]                     # Simple and Pythonic

def is_palindrome(s: str) -> bool:
    """Check if string is palindrome."""
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def count_characters(s: str) -> dict:
    """Count frequency of each character."""
    from collections import Counter
    return dict(Counter(s))

def is_anagram(s1: str, s2: str) -> bool:
    """Check if two strings are anagrams."""
    return sorted(s1.lower()) == sorted(s2.lower())

def most_common_char(s: str) -> str:
    """Find most common character in string."""
    from collections import Counter
    if not s:
        return ""
    counter = Counter(s.lower())
    return counter.most_common(1)[0][0]

def title_case(s: str) -> str:
    """Convert string to title case."""
    return s.title()

def remove_whitespace(s: str) -> str:
    """Remove all whitespace from string."""
    return "".join(s.split())


# =============================================================================
# SECTION 10: DEMONSTRATION
# =============================================================================

if __name__ == "__main__":
    # Run demonstrations
    print("=== Variables ===")
    print(f"name = {name}, type = {type(name)}")

    print("\n=== Type Conversion ===")
    print(f"int('42') = {int('42')}")
    print(f"str(42) = {str(42)}")
    print(f"float(42) = {float(42)}")

    print("\n=== String Slicing ===")
    print(f"s = '{s}'")
    print(f"s[:5] = '{s[:5]}'")
    print(f"s[::-1] = '{s[::-1]}'")

    print("\n=== F-Strings ===")
    print(f"f'Hello, {name}!' = 'Hello, {name}!'")
    print(f"f'{{score:.2f}}' = '{score:.2f}'")

    print("\n=== Split and Join ===")
    print(f"'apple,banana'.split(',') = {['apple', 'banana', 'cherry']}")
    print(f"' '.join(['hello', 'world']) = {' '.join(['hello', 'world'])}")

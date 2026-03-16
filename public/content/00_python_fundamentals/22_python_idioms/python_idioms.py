"""
Python Idioms - Implementation and Examples
===========================================
Comprehensive Python implementations demonstrating idiomatic
Python patterns for interviews and clean code.
"""

from typing import List, Dict, Any, Tuple


# =============================================================================
# SECTION 1: WALRUS OPERATOR (:=)
# =============================================================================

"""
The walrus operator (:=) assigns and returns a value in a single expression.
Introduced in Python 3.8.

Key benefit: Avoids repeated calculations and reduces lines of code.
"""


def walrus_in_while():
    """
    Use walrus operator in while loops to read and check in one expression.

    Without walrus:
        line = f.readline()
        while line:
            process(line)
            line = f.readline()

    With walrus:
        while (line := f.readline()):
            process(line)
    """
    # Simulating file reading with a list
    lines = ["line1", "line2", ""]  # Empty string represents EOF
    idx = 0

    while idx < len(lines):
        line = lines[idx]
        idx += 1
        if not line:
            break
        print(f"Processing: {line}")


def walrus_in_comprehension():
    """
    Use walrus in list comprehensions to avoid repeated calculations.

    Without walrus:
        results = [expensive(x) for x in items if expensive(x) > 0]

    With walrus:
        results = [y for x in items if (y := expensive(x)) > 0]
    """

    def expensive_operation(x):
        """Simulate expensive function."""
        print(f"Computing for {x}...")
        return x * 2

    items = [1, 2, 3, 4, 5]

    # Without walrus - calculates expensive_operation twice
    # This would print twice per iteration
    print("\nWithout walrus (commented out to avoid double computation):")
    # results = [expensive_operation(x) for x in items if expensive_operation(x) > 2]

    # With walrus - calculates once
    print("\nWith walrus:")
    results = [y for x in items if (y := expensive_operation(x)) > 2]
    print(f"Results: {results}")


def walrus_in_conditional():
    """
    Use walrus in if conditions for cleaner code.

    Without walrus:
        match = pattern.search(text)
        if match:
            process(match.group())

    With walrus:
        if (match := pattern.search(text)):
            process(match.group())
    """

    text = "The answer is 42"

    # Simulating regex search
    def mock_search(s):
        if "answer" in s:
            return "found"
        return None

    # Without walrus
    match = mock_search(text)
    if match:
        print(f"Found: {match}")

    # With walrus - assignment in condition
    if (result := mock_search(text)):
        print(f"Found with walrus: {result}")


def walrus_avoid_repeated_call():
    """
    Use walrus to avoid calling function multiple times.

    Without walrus - function called twice
    if calculate() > threshold:
        do_something(calculate())

    With walrus - function called once
    if (val := calculate()) > threshold:
        do_something(val)
    """

    call_count = 0

    def get_value():
        nonlocal call_count
        call_count += 1
        return 42

    threshold = 40

    # Without walrus - calls function twice
    call_count = 0
    if get_value() > threshold:
        pass
    print(f"Without walrus: {call_count} calls")

    # With walrus - calls function once
    call_count = 0
    if (val := get_value()) > threshold:
        pass
    print(f"With walrus: {call_count} calls")


# =============================================================================
# SECTION 2: CHAINED COMPARISONS
# =============================================================================

"""
Python allows chaining comparison operators.
a < b < c is equivalent to (a < b) and (b < c)

This is more efficient and readable than using 'and'.
"""


def chained_comparison_basics():
    """Demonstrate basic chained comparisons."""

    x = 5

    # Traditional way
    if x > 0 and x < 10:
        print("x is between 0 and 10")

    # Chained comparison - cleaner
    if 0 < x < 10:
        print("x is between 0 and 10 (chained)")

    # With <=
    if 0 <= x <= 10:
        print("x is in range [0, 10]")


def chained_comparison_with_all_equal():
    """Check if all values are equal."""

    a, b, c = 5, 5, 5

    if a == b == c:
        print("All equal")

    # Ascending order check
    a, b, c = 1, 2, 3
    if a < b < c:
        print("Strictly increasing")

    # Mixed operators
    a, b, c = 1, 2, 2
    if a <= b <= c:
        print("Non-decreasing")


def chained_comparison_efficiency():
    """
    Chained comparisons are more efficient because:
    1. Each comparison is evaluated only once
    2. Short-circuit evaluation works properly

    For: 0 < x < 10
    - If x <= 0, the x < 10 part is never evaluated
    """


# =============================================================================
# SECTION 3: VARIABLE SWAPPING
# =============================================================================

def swap_basic():
    """Basic variable swap - no temp variable needed."""

    a, b = 1, 2
    print(f"Before: a={a}, b={b}")

    # Single line swap
    a, b = b, a
    print(f"After: a={a}, b={b}")


def swap_multiple():
    """Swap multiple variables at once."""

    a, b, c = 1, 2, 3
    print(f"Before: a={a}, b={b}, c={c}")

    # Rotate: a becomes b, b becomes c, c becomes a
    a, b, c = c, a, b
    print(f"After: a={a}, b={b}, c={c}")


def swap_in_sorting():
    """Swapping in sorting algorithms."""

    arr = [3, 1, 2]

    # Bubble sort example using swapping
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap using tuple unpacking
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print(f"Sorted: {arr}")


def conditional_swap():
    """Swap based on condition."""

    a, b = 5, 3

    # Swap if a > b
    if a > b:
        a, b = b, a

    print(f"After conditional swap: a={a}, b={b}")


# =============================================================================
# SECTION 4: MULTIPLE ASSIGNMENT (TUPLE UNPACKING)
# =============================================================================

def unpack_basics():
    """Basic tuple unpacking."""

    # Unpack tuple
    point = (10, 20)
    x, y = point
    print(f"x={x}, y={y}")

    # Unpack list
    first, last = ["Alice", "Bob"]
    print(f"first={first}, last={last}")


def extended_unpacking():
    """Extended unpacking with * operator."""

    # First and rest
    first, *rest = [1, 2, 3, 4, 5]
    print(f"first={first}, rest={rest}")

    # First, middle, last
    first, *middle, last = [1, 2, 3, 4, 5]
    print(f"first={first}, middle={middle}, last={last}")

    # Pack remaining
    *prefix, last = [1, 2, 3, 4]
    print(f"prefix={prefix}, last={last}")

    # Ignore values
    a, _, c = [1, 2, 3]
    print(f"a={a}, c={c}")


def unpack_with_enumerate():
    """Use unpacking with enumerate."""

    items = ["a", "b", "c"]

    # Unpack index and value
    for i, item in enumerate(items):
        print(f"{i}: {item}")


def unpack_with_zip():
    """Use unpacking with zip."""

    names = ["Alice", "Bob"]
    ages = [25, 30]

    # Unpack paired values
    for name, age in zip(names, ages):
        print(f"{name} is {age}")


def unpack_nested():
    """Unpack nested structures."""

    # Nested tuple
    nested = (1, (2, 3))
    a, (b, c) = nested
    print(f"a={a}, b={b}, c={c}")

    # List of tuples
    pairs = [(1, 2), (3, 4)]
    for a, b in pairs:
        print(f"a={a}, b={b}")


# =============================================================================
# SECTION 5: CONDITIONAL EXPRESSIONS (TERNARY)
# =============================================================================

def ternary_basic():
    """Basic ternary operator."""

    age = 20
    status = "adult" if age >= 18 else "minor"
    print(f"Status: {status}")


def ternary_in_assignments():
    """Use ternary in assignments."""

    a, b = 10, 20

    # Max value
    max_val = a if a > b else b

    # With None default
    value = None
    result = value if value is not None else "default"
    print(f"Result: {result}")

    # Using or (simpler for None/0/"")
    value = ""
    result = value or "default"
    print(f"Result with or: {result}")


def nested_ternary():
    """Nested ternary expressions."""

    score = 85

    # Nested ternary
    grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D"
    print(f"Grade: {grade}")

    # More readable version
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "D"


# =============================================================================
# SECTION 6: ENUMERATE AND ZIP
# =============================================================================

def enumerate_demo():
    """Demonstrate enumerate."""

    fruits = ["apple", "banana", "cherry"]

    # Basic enumerate
    for i, fruit in enumerate(fruits):
        print(f"{i}: {fruit}")

    # Start from 1
    for i, fruit in enumerate(fruits, start=1):
        print(f"{i}. {fruit}")

    # With list of tuples
    items = [("a", 1), ("b", 2)]
    for i, (key, value) in enumerate(items):
        print(f"{i}: {key}={value}")


def zip_demo():
    """Demonstrate zip."""

    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]

    # Basic zip
    for name, age in zip(names, ages):
        print(f"{name}: {age}")

    # Different lengths - stops at shortest
    names_short = ["Alice", "Bob"]
    for name, age in zip(names_short, ages):
        print(f"{name}: {age}")

    # Create dictionary
    d = dict(zip(names, ages))
    print(f"Dict: {d}")

    # Zip multiple
    scores = [95, 88, 92]
    for name, age, score in zip(names, ages, scores):
        print(f"{name}: age={age}, score={score}")


def enumerate_and_zip():
    """Combine enumerate and zip."""

    list1 = ["a", "b", "c"]
    list2 = [1, 2, 3]

    for i, (a, b) in enumerate(zip(list1, list2)):
        print(f"{i}: {a} -> {b}")


# =============================================================================
# SECTION 7: COMPREHENSIONS
# =============================================================================

def list_comprehension():
    """List comprehensions."""

    # Basic
    squares = [x**2 for x in range(10)]
    print(f"Squares: {squares}")

    # With condition
    evens = [x for x in range(10) if x % 2 == 0]
    print(f"Evens: {evens}")

    # Nested
    matrix = [[i*j for j in range(3)] for i in range(3)]
    print(f"Matrix: {matrix}")


def dict_comprehension():
    """Dictionary comprehensions."""

    # Basic
    squares = {x: x**2 for x in range(5)}
    print(f"Squares dict: {squares}")

    # From two lists
    keys = ["a", "b", "c"]
    values = [1, 2, 3]
    d = dict(zip(keys, values))
    print(f"From zip: {d}")

    # Filter existing
    d = {"a": 1, "b": -2, "c": 3}
    positive = {k: v for k, v in d.items() if v > 0}
    print(f"Positive: {positive}")


def set_comprehension():
    """Set comprehensions."""

    # Basic
    unique = {x for x in [1, 2, 2, 3, 3, 3]}
    print(f"Unique: {unique}")

    # With condition
    evens = {x for x in range(10) if x % 2 == 0}
    print(f"Evens: {evens}")


def comprehension_flatten():
    """Flatten nested list using comprehension."""

    nested = [[1, 2], [3, 4], [5, 6]]

    # Flatten
    flat = [x for sublist in nested for x in sublist]
    print(f"Flattened: {flat}")

    # Another way
    flat2 = sum(nested, [])
    print(f"Flattened2: {flat2}")


# =============================================================================
# SECTION 8: USEFUL ONE-LINERS
# =============================================================================

def useful_one liners():
    """Useful one-liner patterns."""

    # Reverse string
    s = "hello"
    reversed_s = s[::-1]
    print(f"Reversed: {reversed_s}")

    # Get first/last
    items = [1, 2, 3, 4, 5]
    first = items[0]
    last = items[-1]
    print(f"First: {first}, Last: {last}")

    # Check all/any
    nums = [1, 2, 3, 4, 5]
    all_positive = all(x > 0 for x in nums)
    any_zero = any(x == 0 for x in nums)
    print(f"All positive: {all_positive}, Any zero: {any_zero}")

    # Merge dictionaries
    d1 = {"a": 1, "b": 2}
    d2 = {"b": 3, "c": 4}
    # Python 3.9+: merged = d1 | d2
    merged = {**d1, **d2}
    print(f"Merged: {merged}")

    # Count occurrences
    items = [1, 2, 2, 3, 3, 3]
    from collections import Counter
    counts = Counter(items)
    print(f"Counts: {counts}")


# =============================================================================
# SECTION 9: PRACTICAL INTERVIEW PATTERNS
# =============================================================================

def two_pointers_pattern():
    """Two pointers pattern using tuple unpacking."""

    arr = [1, 2, 3, 4, 5]
    left, right = 0, len(arr) - 1

    while left < right:
        # Process elements
        print(f"Left: {arr[left]}, Right: {arr[right]}")
        left += 1
        right -= 1


def sliding_window_pattern():
    """Sliding window using unpacking."""

    arr = [1, 2, 3, 4, 5]
    window_size = 3

    for i in range(len(arr) - window_size + 1):
        window = arr[i:i + window_size]
        print(f"Window: {window}")


def group_by_pattern():
    """Group by using dict comprehension."""

    items = ["apple", "banana", "apricot", "blueberry"]

    # Group by first letter
    grouped = {}
    for item in items:
        key = item[0]
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(item)

    print(f"Grouped: {grouped}")

    # Using defaultdict
    from collections import defaultdict
    grouped = defaultdict(list)
    for item in items:
        grouped[item[0]].append(item)
    print(f"Grouped with defaultdict: {dict(grouped)}")


# =============================================================================
# SECTION 10: TESTING AND DEMO
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("PYTHON IDIOMS - TEST DEMO")
    print("=" * 60)

    # Section 1: Walrus Operator
    print("\n--- Section 1: Walrus Operator ---")
    walrus_in_while()
    walrus_in_comprehension()
    walrus_in_conditional()
    walrus_avoid_repeated_call()

    # Section 2: Chained Comparisons
    print("\n--- Section 2: Chained Comparisons ---")
    chained_comparison_basics()

    # Section 3: Variable Swapping
    print("\n--- Section 3: Variable Swapping ---")
    swap_basic()
    swap_multiple()

    # Section 4: Multiple Assignment
    print("\n--- Section 4: Multiple Assignment ---")
    unpack_basics()
    extended_unpacking()

    # Section 5: Ternary
    print("\n--- Section 5: Ternary ---")
    ternary_basic()
    nested_ternary()

    # Section 6: Enumerate and Zip
    print("\n--- Section 6: Enumerate and Zip ---")
    enumerate_demo()
    zip_demo()

    # Section 7: Comprehensions
    print("\n--- Section 7: Comprehensions ---")
    list_comprehension()
    dict_comprehension()

    # Section 8: One-liners
    print("\n--- Section 8: Useful One-liners ---")
    useful_one liners()

    # Section 9: Interview Patterns
    print("\n--- Section 9: Interview Patterns ---")
    two_pointers_pattern()
    group_by_pattern()

    print("\n" + "=" * 60)
    print("All demos completed!")
    print("=" * 60)

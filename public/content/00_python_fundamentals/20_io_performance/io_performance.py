"""
I/O Performance - Implementation and Examples
===========================================
Fast input/output techniques for competitive programming
and large-scale data processing in Python.
"""

import sys
import time
from typing import List, Optional


# =============================================================================
# SECTION 1: SLOW VS FAST INPUT COMPARISON
# =============================================================================

def slow_input_demo():
    """
    Demonstration of slow input methods.

    input() is slow because:
    1. It reads from sys.stdin (text mode)
    2. It adds extra processing (prompt, etc.)
    3. It flushes after each call
    """
    # This is slow for large inputs
    # n = int(input())
    # arr = [int(input()) for _ in range(n)]

    # Better but still not optimal
    # n = int(sys.stdin.readline())
    # arr = [int(sys.stdin.readline()) for _ in range(n)]

    pass


def fast_read_all_integers() -> List[int]:
    """
    Read all integers from stdin efficiently.

    Technique: Read entire input at once, split, and convert.
    This is the fastest method for competitive programming.

    Time Complexity: O(n) where n is total input size
    """
    # Read entire input as bytes
    data = sys.stdin.buffer.read()

    # Split on whitespace (space, newline, etc.)
    # This returns list of byte strings
    tokens = data.split()

    # Convert to integers
    numbers = [int(token) for token in tokens]

    return numbers


def fast_read_with_iter() -> List[int]:
    """
    Read all integers using iterator pattern.

    More memory efficient for very large inputs as it
    doesn't create intermediate list of strings.
    """
    # Create iterator from bytes
    data = sys.stdin.buffer.read().split()
    it = iter(data)

    # Get first number (e.g., n)
    n = int(next(it))

    # Read n more integers
    arr = [int(next(it)) for _ in range(n)]

    return arr


def generator_ints():
    """
    Generator that yields integers one at a time.

    Use this when you need to process integers
    lazily without storing them all in memory.
    """
    for token in sys.stdin.buffer.read().split():
        yield int(token)


# =============================================================================
# SECTION 2: LINE-BY-LINE INPUT PATTERNS
# =============================================================================

def read_single_int() -> int:
    """Read a single integer."""
    return int(sys.stdin.readline())


def read_multiple_ints() -> List[int]:
    """Read multiple integers from one line."""
    return list(map(int, sys.stdin.readline().split()))


def read_ints_unknown_count() -> List[int]:
    """
    Read all remaining integers from input.

    Use when you don't know how many integers are left
    but want to read them all.
    """
    return list(map(int, sys.stdin.read().split()))


def read_lines(n: int) -> List[str]:
    """
    Read n lines of input.

    Args:
        n: Number of lines to read

    Returns:
        List of strings (stripped of newline characters)
    """
    lines = []
    for _ in range(n):
        line = sys.stdin.readline()
        # Remove trailing newline but preserve other whitespace
        lines.append(line.rstrip('\n'))
    return lines


def read_grid(rows: int, cols: int) -> List[List[int]]:
    """
    Read integer matrix/grid.

    Example input:
    3 4
    1 2 3 4
    5 6 7 8
    9 10 11 12

    Returns:
        2D list of integers
    """
    grid = []
    for _ in range(rows):
        row = list(map(int, sys.stdin.readline().split()))
        grid.append(row)
    return grid


def read_char_grid(rows: int) -> List[List[str]]:
    """
    Read grid of characters (like a maze).

    Example input:
    ABC
    DEF
    GHI

    Returns:
        2D list of characters
    """
    grid = []
    for _ in range(rows):
        line = sys.stdin.readline().strip()
        grid.append(list(line))
    return grid


# =============================================================================
# SECTION 3: FAST OUTPUT TECHNIQUES
# =============================================================================

def slow_output_example():
    """
    Demonstrates slow output - avoid this in competitive programming.

    Each print() call has overhead:
    - String formatting
    - Buffer flush
    - Newline handling
    """
    # SLOW - avoid in tight loops
    # for i in range(10000):
    #     print(i)


def fast_output_basic():
    """
    Basic fast output - build string and print once.

    Using join is much faster than multiple print calls.
    """
    numbers = list(range(1000))

    # Build output string
    output = '\n'.join(str(x) for x in numbers)

    # Print once
    print(output)


def fast_output_with_map():
    """
    Fast output using map().

    map() is slightly faster than generator expression
    in some cases.
    """
    numbers = list(range(1000))

    # Using map - convert to strings, join
    output = '\n'.join(map(str, numbers))

    print(output)


def fast_output_with_list():
    """
    Fast output using list comprehension.

    List comprehension can be faster than map for simple cases.
    """
    numbers = list(range(1000))

    # Build list of strings first
    output_lines = [str(x) for x in numbers]
    output = '\n'.join(output_lines)

    print(output)


def sys_stdout_write():
    """
    Using sys.stdout.write() for maximum speed.

    This is the fastest method but doesn't add
    automatic newline or flush.
    """
    numbers = list(range(1000))

    # Write each number with newline
    for i in numbers:
        # write() doesn't add newline automatically
        sys.stdout.write(str(i) + '\n')

    # Note: No flush needed, Python flushes on newline by default


def format_output():
    """
    Different string formatting methods.

    f-strings are recommended for Python 3.6+
    """
    name = "Alice"
    age = 30
    score = 95.5

    # f-string (Python 3.6+) - Recommended
    print(f"{name} is {age} years old with score {score}")

    # Format method
    print("{} is {} years old".format(name, age))

    # Positional arguments
    print("{0} is {1} years old".format(name, age))

    # Named arguments
    print("{n} is {a} years old".format(n=name, a=age))

    # % formatting - Old style
    print("%s is %d years old" % (name, age))

    # Width and precision
    print(f"Score: {score:.2f}")  # Two decimal places
    print(f"Pi: {3.14159:.4f}")   # Four decimal places


# =============================================================================
# SECTION 4: PRACTICAL COMPETITIVE PROGRAMMING TEMPLATES
# =============================================================================

def solve_simple():
    """
    Simple competitive programming template.

    Use for problems with simple input format:
    - First line: n (number of elements)
    - Remaining lines: n integers
    """
    # Read all data at once
    data = sys.stdin.buffer.read().split()
    it = iter(data)

    n = int(next(it))
    arr = [int(next(it)) for _ in range(n)]

    # Process (example: find max)
    result = max(arr) if arr else 0

    # Output
    print(result)


def solve_multi_test():
    """
    Template for multiple test cases.

    Input format:
    T
    n1
    a1 a2 ... an1
    n2
    b1 b2 ... bn2
    ...
    """
    data = sys.stdin.buffer.read().split()
    it = iter(data)

    t = int(next(it))  # Number of test cases

    results = []

    for _ in range(t):
        n = int(next(it))
        arr = [int(next(it)) for _ in range(n)]

        # Process each test case
        result = sum(arr)
        results.append(str(result))

    # Print all results at once
    print('\n'.join(results))


def solve_with_queries():
    """
    Template for problems with queries.

    Input format:
    n q
    arr[0..n-1]
    q queries (each on single line)
    """
    data = sys.stdin.buffer.read().split()
    it = iter(data)

    n = int(next(it))
    q = int(next(it))

    arr = [int(next(it)) for _ in range(n)]

    # Process queries
    results = []
    for _ in range(q):
        query_type = int(next(it))

        if query_type == 1:
            # Example query type 1
            results.append("processed")
        elif query_type == 2:
            # Example query type 2
            results.append("processed")

    print('\n'.join(results))


# =============================================================================
# SECTION 5: FILE I/O OPERATIONS
# =============================================================================

def read_file_basic():
    """
    Basic file reading.

    Always use context manager (with statement)
    to ensure file is properly closed.
    """
    with open('input.txt', 'r') as f:
        content = f.read()
    return content


def read_file_lines():
    """Read file line by line."""
    lines = []
    with open('input.txt', 'r') as f:
        for line in f:
            # line includes newline, use .strip() to remove
            lines.append(line.strip())
    return lines


def read_file_buffered():
    """
    Read large file with buffering.

    Useful for very large files that don't fit in memory.
    """
    with open('large_file.txt', 'r') as f:
        # Read in chunks of 8192 bytes
        while True:
            chunk = f.read(8192)
            if not chunk:
                break
            # Process chunk
            pass


def write_file():
    """Write to file."""
    output_data = ["line1", "line2", "line3"]

    with open('output.txt', 'w') as f:
        # Write all at once
        f.write('\n'.join(output_data))


def append_to_file():
    """Append to existing file."""
    with open('log.txt', 'a') as f:
        f.write("new entry\n")


def read_write_binary():
    """Read and write binary files."""
    # Read binary
    with open('data.bin', 'rb') as f:
        data = f.read()

    # Modify (example: reverse)
    modified = data[::-1]

    # Write binary
    with open('output.bin', 'wb') as f:
        f.write(modified)


# =============================================================================
# SECTION 6: PERFORMANCE UTILITIES
# =============================================================================

class InputReader:
    """
    Efficient input reader class.

    Provides convenient methods for reading different
    types of input in competitive programming.
    """

    def __init__(self):
        """Initialize with all data read into memory."""
        self.data = sys.stdin.buffer.read().split()
        self.index = 0

    def next_int(self) -> int:
        """Read next integer."""
        val = int(self.data[self.index])
        self.index += 1
        return val

    def next_str(self) -> str:
        """Read next string."""
        val = self.data[self.index].decode()
        self.index += 1
        return val

    def next_ints(self, n: int) -> List[int]:
        """Read n integers."""
        result = []
        for _ in range(n):
            result.append(int(self.data[self.index]))
            self.index += 1
        return result

    def has_next(self) -> bool:
        """Check if more data available."""
        return self.index < len(self.data)


class OutputWriter:
    """
    Efficient output writer class.

    Collects output and prints once at the end.
    """

    def __init__(self):
        self.output = []

    def write(self, value):
        """Add value to output."""
        self.output.append(str(value))

    def writeln(self, value):
        """Add value with newline."""
        self.output.append(str(value))

    def flush(self):
        """Print all collected output."""
        sys.stdout.write('\n'.join(self.output))


# =============================================================================
# SECTION 7: TESTING AND DEMO
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("I/O PERFORMANCE - TEST DEMO")
    print("=" * 60)

    # Demo of different output methods
    print("\n--- Output Formatting ---")
    format_output()

    # Demo of file operations
    print("\n--- File I/O ---")

    # Create test file
    test_data = "5\n1 2 3 4 5\nhello\nworld"
    with open('test_input.txt', 'w') as f:
        f.write(test_data)

    # Read test file
    with open('test_input.txt', 'r') as f:
        content = f.read()
    print(f"Test file content: {content}")

    # Clean up
    import os
    os.remove('test_input.txt')

    # Demo InputReader class
    print("\n--- InputReader Demo ---")
    # Create mock input
    mock_input = "10\n1 2 3 4 5 6 7 8 9 10"
    # Simulate reading (normally this comes from stdin)
    original_stdin = sys.stdin

    print("InputReader would read from stdin in real usage")

    # Demo OutputWriter
    print("\n--- OutputWriter Demo ---")
    writer = OutputWriter()
    writer.write("First")
    writer.write("Second")
    writer.writeln("Third with newline")
    # In real usage: writer.flush()

    print("Output would be flushed to stdout in real usage")

    print("\n--- Performance Notes ---")
    print("1. Use sys.stdin.buffer.read() for large inputs")
    print("2. Convert types in batch, not in loops")
    print("3. Build output string and print once")
    print("4. Use join() instead of multiple print() calls")
    print("5. For files: use context managers (with statement)")

    print("\n" + "=" * 60)
    print("Demo completed!")
    print("=" * 60)

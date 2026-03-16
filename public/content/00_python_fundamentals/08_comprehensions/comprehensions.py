"""
Comprehensions - Implementation and Examples
============================================
Comprehensive Python implementations covering list, dict, set comprehensions,
generator expressions, and the yield keyword. Practical for interviews.
"""

from typing import List, Dict, Set, Generator, Any, Iterator
from collections import defaultdict, Counter
import itertools


# =============================================================================
# SECTION 1: LIST COMPREHENSIONS
# =============================================================================

def list_comprehension_basic():
    """
    Basic list comprehension examples.
    List comprehension: [expression for item in iterable]

    Time: O(n) where n is the number of items in the iterable
    Space: O(n) for storing the result list
    """
    # Example 1: Square all numbers from 0 to 9
    # Creates [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    squares = [x**2 for x in range(10)]
    print(f"Squares 0-9: {squares}")

    # Example 2: Create list of even numbers from 0 to 19
    # Using condition to filter: only include if x % 2 == 0
    evens = [x for x in range(20) if x % 2 == 0]
    print(f"Even numbers 0-19: {evens}")

    # Example 3: Convert all strings to uppercase
    words = ['hello', 'world', 'python']
    upper_words = [word.upper() for word in words]
    print(f"Uppercase: {upper_words}")

    # Example 4: Nested comprehension - flatten a 2D matrix
    # This iterates over each row, then each element in the row
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    flat = [num for row in matrix for num in row]
    print(f"Flattened matrix: {flat}")

    # Example 5: Conditional expression (ternary in comprehension)
    # FizzBuzz style: replace multiples of 3 with 'Fizz', 5 with 'Buzz'
    fizzbuzz = ['Fizz' if x % 3 == 0 else 'Buzz' if x % 5 == 0 else x for x in range(1, 16)]
    print(f"FizzBuzz 1-15: {fizzbuzz}")

    # Example 6: Multiple conditions
    # Squares of numbers that are even AND less than 10
    result = [x**2 for x in range(20) if x % 2 == 0 if x < 10]
    print(f"Even squares < 10: {result}")

    return squares, evens, upper_words, flat, fizzbuzz, result


def list_comprehension_with_indices():
    """
    Using enumerate within list comprehensions to get both index and value.

    Time: O(n) where n is the length of the iterable
    Space: O(n) for storing results
    """
    # Create list of (index, value) tuples for non-empty strings
    words = ['apple', 'banana', 'cherry', '']
    indexed = [(i, word) for i, word in enumerate(words) if word]
    print(f"Non-empty with indices: {indexed}")
    # Output: [(0, 'apple'), (1, 'banana'), (2, 'cherry')]

    # Get index of first occurrence of each character in a string
    text = "hello"
    # Keep track of first occurrence only using dictionary
    seen = {}
    first_indices = [seen.setdefault(c, i) for i, c in enumerate(text)]
    print(f"First indices: {first_indices}")

    return indexed


def list_comprehension_practice_problems():
    """
    Common interview-style problems using list comprehensions.

    These patterns frequently appear in technical interviews.
    """
    # Problem 1: Extract digits from a string
    # Input: "a1b2c3" -> Output: [1, 2, 3]
    s = "a1b2c3"
    digits = [int(c) for c in s if c.isdigit()]
    print(f"Digits in '{s}': {digits}")

    # Problem 2: Get all pairs (i, j) where i < j from list
    # Input: [1, 2, 3] -> Output: [(1,2), (1,3), (2,3)]
    nums = [1, 2, 3]
    pairs = [(nums[i], nums[j]) for i in range(len(nums)) for j in range(i+1, len(nums))]
    print(f"All pairs: {pairs}")

    # Problem 3: Matrix transposition using nested list comprehension
    # Input: [[1,2,3], [4,5,6]] -> Output: [[1,4], [2,5], [3,6]]
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = [[matrix[r][c] for r in range(rows)] for c in range(cols)]
    print(f"Transposed matrix: {transposed}")

    # Problem 4: Get all substring lengths for a string
    # Each substring of length k
    text = "abcde"
    k = 3
    substrings = [text[i:i+k] for i in range(len(text) - k + 1)]
    print(f"All length-{k} substrings: {substrings}")

    return digits, pairs, transposed, substrings


# =============================================================================
# SECTION 2: DICTIONARY COMPREHENSIONS
# =============================================================================

def dict_comprehension_basic():
    """
    Dictionary comprehension examples.
    Syntax: {key_expression: value_expression for item in iterable}

    Time: O(n) for creating dictionary with n entries
    Space: O(n) for storing the dictionary
    """
    # Example 1: Create dictionary mapping numbers to their squares
    # {0: 0, 1: 1, 2: 4, 3: 9, ...}
    squares_dict = {x: x**2 for x in range(10)}
    print(f"Squares dictionary: {squares_dict}")

    # Example 2: Create dictionary from two lists using zip
    keys = ['a', 'b', 'c', 'd']
    values = [1, 2, 3, 4]
    combined = {k: v for k, v in zip(keys, values)}
    print(f"Combined dict: {combined}")

    # Example 3: Swap keys and values
    original = {'a': 1, 'b': 2, 'c': 3}
    swapped = {v: k for k, v in original.items()}
    print(f"Swapped dict: {swapped}")

    # Example 4: Filter existing dictionary - keep only values > threshold
    scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 95}
    passed = {name: score for name, score in scores.items() if score >= 80}
    print(f"Passed students: {passed}")

    # Example 5: Multiple conditions in dictionary comprehension
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Map numbers to 'even'/'odd' and only include multiples of 3
    result = {x: 'even' if x % 2 == 0 else 'odd' for x in numbers if x % 3 == 0}
    print(f"Multiples of 3: {result}")

    return squares_dict, combined, swapped, passed, result


def dict_comprehension_advanced():
    """
    Advanced dictionary comprehension patterns.
    """
    # Pattern 1: Count character frequency in a string
    text = "hello world"
    # Using dict comprehension with count - inefficient but clear
    char_count = {char: text.count(char) for char in set(text)}
    print(f"Character count (inefficient): {char_count}")

    # Better approach using Counter (shown in later section)

    # Pattern 2: Create nested dictionary
    # Group words by first letter
    words = ['apple', 'apricot', 'banana', 'blueberry', 'cherry']
    by_first_letter = {letter: [w for w in words if w[0] == letter]
                      for letter in sorted(set(w[0] for w in words))}
    print(f"By first letter: {by_first_letter}")

    # Pattern 3: Dictionary with complex keys (tuples)
    # Map (row, col) to value in a matrix
    matrix = [[1, 2, 3], [4, 5, 6]]
    matrix_dict = {(r, c): matrix[r][c]
                   for r in range(len(matrix))
                   for c in range(len(matrix[0]))}
    print(f"Matrix as dict: {matrix_dict}")

    # Pattern 4: Default value for missing keys
    # Using setdefault pattern
    d = {}
    items = [('a', 1), ('b', 2), ('a', 3)]
    d = {k: d.get(k, 0) + v for k, v in items}
    print(f"Aggregated: {d}")  # {'a': 4, 'b': 2}

    return char_count, by_first_letter, matrix_dict, d


def dict_from_lists():
    """
    Create dictionaries from lists - common interview pattern.
    """
    # Method 1: Using zip (most common)
    keys = ['name', 'age', 'city']
    values = ['Alice', 30, 'NYC']
    d = dict(zip(keys, values))
    print(f"From zip: {d}")

    # Method 2: Using dict comprehension with enumerate
    values = ['a', 'b', 'c', 'd']
    indexed = {i: v for i, v in enumerate(values)}
    print(f"With enumerate: {indexed}")

    # Method 3: Invert a dictionary (swap keys and values)
    original = {1: 'a', 2: 'b', 3: 'c'}
    inverted = {v: k for k, v in original.items()}
    print(f"Inverted: {inverted}")

    # Handle duplicate values when inverting
    original_with_duplicates = {1: 'a', 2: 'b', 3: 'a'}
    # Last key wins for duplicate values
    inverted_dups = {v: k for k, v in original_with_duplicates.items()}
    print(f"Inverted with dups: {inverted_dups}")

    # To preserve all keys, use defaultdict
    inverted_all = defaultdict(list)
    for k, v in original_with_duplicates.items():
        inverted_all[v].append(k)
    print(f"Inverted all: {dict(inverted_all)}")

    return d, indexed, inverted, inverted_all


# =============================================================================
# SECTION 3: SET COMPREHENSIONS
# =============================================================================

def set_comprehension_basic():
    """
    Set comprehension examples.
    Syntax: {expression for item in iterable}
    Note: Duplicates are automatically removed.

    Time: O(n) for creating set
    Space: O(n) for storing unique elements
    """
    # Example 1: Unique squares
    squares = {x**2 for x in range(-5, 6)}
    print(f"Unique squares: {squares}")
    # Note: 4 and -4 both map to 16, so only one 16 in result

    # Example 2: Unique characters in string
    text = "hello world"
    unique_chars = {c for c in text}
    print(f"Unique chars in '{text}': {unique_chars}")

    # Example 3: Unique vowels in text
    vowels = {'a', 'e', 'i', 'o', 'u'}
    text = "hello world how are you"
    found_vowels = {c for c in text.lower() if c in vowels}
    print(f"Vowels found: {found_vowels}")

    # Example 4: Intersection of two lists using set comprehension
    list1 = [1, 2, 3, 4, 5, 6]
    list2 = [4, 5, 6, 7, 8, 9]
    common = {x for x in list1 if x in list2}
    print(f"Common elements: {common}")

    # Example 5: Set difference
    only_in_list1 = {x for x in list1 if x not in list2}
    print(f"Only in list1: {only_in_list1}")

    # Example 6: Words with unique first letters
    words = ['apple', 'banana', 'cherry', 'avocado', 'blueberry']
    unique_first = {w[0] for w in words}
    print(f"Unique first letters: {unique_first}")

    return squares, unique_chars, found_vowels, common, only_in_list1, unique_first


def set_comprehension_with_conditions():
    """
    Set comprehensions with filtering conditions.
    """
    # Get all prime numbers up to n using set comprehension
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = {x for x in range(2, 50) if is_prime(x)}
    print(f"Primes up to 50: {primes}")

    # Get all perfect squares that are also even
    squares_even = {x**2 for x in range(10) if (x**2) % 2 == 0}
    print(f"Even squares: {squares_even}")

    # Get all lengths that appear more than once
    words = ['hi', 'hello', 'hey', 'bye', 'goodbye', 'hi']
    # Count each length, then get lengths that appear > 1 time
    from collections import Counter
    length_counts = Counter(len(w) for w in words)
    repeated_lengths = {length for length, count in length_counts.items() if count > 1}
    print(f"Repeated word lengths: {repeated_lengths}")

    return primes, squares_even, repeated_lengths


# =============================================================================
# SECTION 4: GENERATOR EXPRESSIONS
# =============================================================================

def generator_expression_basic():
    """
    Generator expression examples.
    Key difference from list comprehension: lazy evaluation

    List comprehension: [x**2 for x in range(10)]  -> Creates full list immediately
    Generator:         (x**2 for x in range(10))  -> Creates generator object

    Time to create: O(1) - just creates the generator object
    Time to iterate: O(n) - yields one value at a time
    Space: O(1) - only stores current value
    """
    # Example 1: Create generator expression
    gen = (x**2 for x in range(10))
    print(f"Generator object: {gen}")
    print(f"Type: {type(gen)}")

    # Example 2: Lazy evaluation - values computed on demand
    # Nothing is computed until we iterate
    large_gen = (x**2 for x in range(1000000))

    # Example 3: Using with sum() - efficient for large sequences
    # Only generates values as needed
    sum_squares = sum(x**2 for x in range(1000))
    print(f"Sum of squares 0-999: {sum_squares}")

    # Example 4: Using with max(), min()
    result = max(x for x in range(10) if x % 2 == 0)
    print(f"Max even: {result}")

    # Example 5: Using next() to manually iterate
    gen = (x**2 for x in range(5))
    print(f"First: {next(gen)}")  # 0
    print(f"Second: {next(gen)}")  # 1
    print(f"Third: {next(gen)}")  # 4

    # Example 6: Generator can only be iterated once!
    gen = (x for x in range(3))
    first_pass = list(gen)
    second_pass = list(gen)  # Empty! Generator exhausted
    print(f"First pass: {first_pass}, Second pass: {second_pass}")

    return sum_squares, result, first_pass, second_pass


def generator_vs_list():
    """
    Comparison: When to use generator vs list comprehension.

    Generator: Large data, memory-constrained, iterate once
    List: Need to iterate multiple times, need index access
    """
    import sys

    # Memory comparison
    # List of first 1000 squares: stores all 1000 integers
    squares_list = [x**2 for x in range(1000)]
    list_size = sys.getsizeof(squares_list)
    print(f"List size: {list_size} bytes")

    # Generator: only stores the generator object (~100 bytes)
    squares_gen = (x**2 for x in range(1000))
    gen_size = sys.getsizeof(squares_gen)
    print(f"Generator size: {gen_size} bytes")

    # Use case: Processing large file line by line
    # With list: loads entire file into memory
    # With generator: processes one line at a time

    # Example: First n matching items
    # Find first 5 even squares
    gen = (x**2 for x in range(100) if x % 2 == 0)
    first_five = list(itertools.islice(gen, 5))
    print(f"First 5 even squares: {first_five}")

    return list_size, gen_size, first_five


def generator_expressions_in_functions():
    """
    Using generator expressions effectively with built-in functions.
    """
    # Example 1: sum() with generator - efficient
    # Computes sum without storing all values
    total = sum(x**3 for x in range(100))
    print(f"Sum of cubes: {total}")

    # Example 2: any() - returns True if any element is truthy
    has_even = any(x % 2 == 0 for x in range(5, 10))
    print(f"Has even: {has_even}")

    # Example 3: all() - returns True if all elements are truthy
    all_positive = all(x > 0 for x in range(1, 5))
    print(f"All positive: {all_positive}")

    # Example 4: filterfalse() - keep items where condition is False
    odds = list(itertools.filterfalse(lambda x: x % 2 == 0, range(10)))
    print(f"Odd numbers: {odds}")

    # Example 5: accumulate() - running sum/product
    running_sum = list(itertools.accumulate([1, 2, 3, 4, 5]))
    print(f"Running sum: {running_sum}")

    return total, has_even, all_positive, odds, running_sum


# =============================================================================
# SECTION 5: YIELD AND GENERATOR FUNCTIONS
# =============================================================================

def yield_basic():
    """
    Generator functions using yield keyword.
    Unlike regular functions that return once, generators can yield multiple times.
    """
    def count_up_to(n):
        """
        Generator that yields numbers from 1 to n.
        Each call to next() resumes execution after last yield.
        """
        i = 1
        while i <= n:
            yield i
            i += 1

    # Create generator object
    gen = count_up_to(5)

    # Iterate using next()
    print(f"First: {next(gen)}")  # 1
    print(f"Second: {next(gen)}")  # 2
    print(f"Third: {next(gen)}")   # 3

    # Or iterate using for loop
    for num in count_up_to(3):
        print(f"Count: {num}")

    return


def yield_with_send():
    """
    Using send() to pass values INTO a running generator.
    Two-way communication with generators.
    """
    def echo_generator():
        """
        Generator that receives values and yields them back.
        """
        while True:
            # yield pauses and returns value, then receives from send()
            received = yield
            print(f"Received: {received}")

    # Create generator
    gen = echo_generator()

    # Start the generator (must call next() first to reach first yield)
    next(gen)

    # Now send values
    gen.send("Hello")
    gen.send("World")

    return


def infinite_generator():
    """
    Generators can represent infinite sequences - impossible with lists.
    """
    def fibonacci():
        """
        Infinite Fibonacci sequence generator.
        Never terminates, yields values on demand.
        """
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    # Create generator - no computation yet
    fib = fibonacci()

    # Get first 10 Fibonacci numbers
    result = [next(fib) for _ in range(10)]
    print(f"First 10 Fibonacci: {result}")

    # Can also iterate with for (but must break!)
    def first_n_fibonacci(n):
        fib = fibonacci()
        for _ in range(n):
            yield next(fib)

    print(f"Next 5: {list(first_n_fibonacci(5))}")

    return result


def yield_from():
    """
    yield from - delegate to subgenerator.
    Allows flattening nested generators.
    """
    def flatten(nested):
        """Flatten a nested iterable using yield from."""
        for item in nested:
            if isinstance(item, (list, tuple)):
                yield from flatten(item)
            else:
                yield item

    # Flatten nested structure
    nested = [1, [2, [3, 4], 5], [6, 7]]
    flat = list(flatten(nested))
    print(f"Flattened: {flat}")

    # Alternative without yield from
    def flatten_manual(nested):
        for item in nested:
            if isinstance(item, (list, tuple)):
                for subitem in flatten_manual(item):
                    yield subitem
            else:
                yield item

    print(f"Manual flatten: {list(flatten_manual(nested))}")

    return flat


def generator_pipeline():
    """
    Chaining generators for efficient data processing.
    Each stage processes data lazily as needed.
    """
    def integers():
        """Generate infinite sequence of integers."""
        i = 1
        while True:
            yield i
            i += 1

    def squares(gen):
        """Transform generator to yield squares."""
        for x in gen:
            yield x ** 2

    def less_than(gen, n):
        """Filter generator to values less than n."""
        for x in gen:
            if x < n:
                yield x
            else:
                break  # Can early terminate!

    # Chain: integers -> squares -> filter < 100
    result = list(less_than(squares(integers()), 100))
    print(f"Squares < 100: {result}")

    # Equivalent using generator expressions
    result2 = list(x**2 for x in range(1, 100) if x**2 < 100)
    print(f"Using expressions: {result2}")

    return result


def generator_with_state():
    """
    Generators maintain state between yields.
    Useful for stateful iterations.
    """
    def running_average():
        """
        Generator that maintains running average.
        """
        total = 0
        count = 0
        while True:
            value = yield
            if value is None:  # Handle send(None)
                break
            total += value
            count += 1
            yield total / count

    # Create generator
    avg_gen = running_average()
    next(avg_gen)  # Start

    # Send values and get running average
    print(f"Avg after 10: {avg_gen.send(10)}")  # 10.0
    print(f"Avg after 20: {avg_gen.send(20)}")  # 15.0
    print(f"Avg after 30: {avg_gen.send(30)}")  # 20.0
    print(f"Avg after 40: {avg_gen.send(40)}")  # 25.0

    return


# =============================================================================
# SECTION 6: PRACTICAL INTERVIEW PATTERNS
# =============================================================================

def interview_patterns():
    """
    Common patterns seen in technical interviews.
    """
    # Pattern 1: Using dict comprehension for frequency counting
    # Better: use Counter, but comprehension works too
    from collections import Counter
    text = "hello world"
    freq = {c: text.count(c) for c in set(text)}
    print(f"Freq dict: {freq}")

    # Better approach with Counter
    freq_counter = Counter(text)
    print(f"Counter: {freq_counter}")

    # Pattern 2: Grouping with defaultdict
    words = ['cat', 'car', 'dog', 'dig', 'elephant']
    grouped = defaultdict(list)
    for word in words:
        grouped[len(word)].append(word)
    print(f"Grouped by length: {dict(grouped)}")

    # Pattern 3: Using zip to create dictionary from keys and values
    keys = ['a', 'b', 'c']
    values = [1, 2, 3]
    d = dict(zip(keys, values))
    print(f"Zipped: {d}")

    # Pattern 4: Filtering with set comprehension
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    unique_to_list1 = {x for x in list1 if x not in list2}
    print(f"Unique to list1: {unique_to_list1}")

    # Pattern 5: Matrix operations with list comprehension
    matrix = [[1, 2, 3], [4, 5, 6]]
    # Sum of all elements
    total = sum(sum(row) for row in matrix)
    print(f"Matrix sum: {total}")

    # Sum of each row
    row_sums = [sum(row) for row in matrix]
    print(f"Row sums: {row_sums}")

    return freq, freq_counter, grouped, d, unique_to_list1, total


# =============================================================================
# SECTION 7: TESTING AND DEMO
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("COMPREHENSIONS - TEST DEMO")
    print("=" * 60)

    # Section 1: List Comprehensions
    print("\n--- List Comprehensions ---")
    list_comprehension_basic()
    list_comprehension_with_indices()
    list_comprehension_practice_problems()

    # Section 2: Dictionary Comprehensions
    print("\n--- Dictionary Comprehensions ---")
    dict_comprehension_basic()
    dict_comprehension_advanced()
    dict_from_lists()

    # Section 3: Set Comprehensions
    print("\n--- Set Comprehensions ---")
    set_comprehension_basic()
    set_comprehension_with_conditions()

    # Section 4: Generator Expressions
    print("\n--- Generator Expressions ---")
    generator_expression_basic()
    generator_vs_list()
    generator_expressions_in_functions()

    # Section 5: Yield and Generators
    print("\n--- Yield and Generators ---")
    yield_basic()
    yield_with_send()
    infinite_generator()
    yield_from()
    generator_pipeline()
    generator_with_state()

    # Section 6: Interview Patterns
    print("\n--- Interview Patterns ---")
    interview_patterns()

    print("\n" + "=" * 60)
    print("All tests completed!")
    print("=" * 60)

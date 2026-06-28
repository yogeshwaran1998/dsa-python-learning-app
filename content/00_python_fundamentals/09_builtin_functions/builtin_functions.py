"""
Built-in Functions - Implementation and Examples
================================================
Comprehensive Python implementations covering map, filter, reduce, enumerate,
zip, all/any, and min/max with key. Practical for interviews.
"""

from typing import List, Dict, Tuple, Callable, Any, Iterator
from functools import reduce
from collections import Counter


# =============================================================================
# SECTION 1: MAP FUNCTION
# =============================================================================

def map_basic():
    """
    Map function examples.
    map(function, iterable) - applies function to each item in iterable

    Time Complexity: O(n) where n is the length of iterable
    Space Complexity: O(n) for the result (map returns lazy iterator in Python 3)

    Note: In Python 3, map returns an iterator, not a list!
    """
    # Example 1: Basic map with lambda
    # Square all numbers from 0 to 9
    numbers = list(range(10))
    squares = list(map(lambda x: x ** 2, numbers))
    print(f"Original: {numbers}")
    print(f"Squares: {squares}")

    # Example 2: Map with built-in function
    # Convert all strings to uppercase
    words = ['hello', 'world', 'python']
    upper_words = list(map(str.upper, words))
    print(f"Upper: {upper_words}")

    # Example 3: Map with custom function
    def cube(x):
        """Cube a number."""
        return x ** 3

    cubes = list(map(cube, range(5)))
    print(f"Cubes: {cubes}")

    # Example 4: Multiple iterables
    # Add corresponding elements from two lists
    list1 = [1, 2, 3, 4]
    list2 = [10, 20, 30, 40]
    sums = list(map(lambda x, y: x + y, list1, list2))
    print(f"Element-wise sum: {sums}")

    # Example 5: Map with three iterables
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [7, 8, 9]
    combined = list(map(lambda x, y, z: x + y + z, a, b, c))
    print(f"Three-way sum: {combined}")

    # Example 6: Pairing corresponding elements
    # (Python 2's map(None, ...) is replaced by zip in Python 3)
    result = list(zip([1, 2, 3], ['a', 'b', 'c']))
    print(f"Zipped tuples: {result}")

    return squares, upper_words, cubes, sums, combined


def map_vs_list_comprehension():
    """
    Compare map vs list comprehension performance and readability.

    In general:
    - List comprehensions are often faster and more Pythonic
    - Map is useful when reusing a function across multiple calls
    - Both have O(n) time complexity
    """
    import time

    # Performance comparison
    n = 100000

    # Method 1: List comprehension
    start = time.time()
    result1 = [x ** 2 for x in range(n)]
    time1 = time.time() - start

    # Method 2: Map
    start = time.time()
    result2 = list(map(lambda x: x ** 2, range(n)))
    time2 = time.time() - start

    print(f"List comprehension: {time1:.4f}s")
    print(f"Map: {time2:.4f}s")
    print(f"Comprehension is {'faster' if time1 < time2 else 'slower'}")

    # Readability: List comprehension is often preferred
    # These are equivalent:
    squares_comprehension = [x ** 2 for x in range(10)]
    squares_map = list(map(lambda x: x ** 2, range(10)))
    print(f"Equal: {squares_comprehension == squares_map}")

    return time1, time2


def map_practice_problems():
    """
    Common interview problems using map.
    """
    # Problem 1: Convert list of strings to integers
    str_nums = ['1', '2', '3', '4', '5']
    int_nums = list(map(int, str_nums))
    print(f"String to int: {int_nums}")

    # Problem 2: Parse list of strings to floats
    str_floats = ['1.5', '2.3', '3.7']
    floats = list(map(float, str_floats))
    print(f"String to float: {floats}")

    # Problem 3: Extract attribute from objects
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def __repr__(self):
            return f"Person({self.name}, {self.age})"

    people = [Person('Alice', 30), Person('Bob', 25), Person('Charlie', 35)]
    names = list(map(lambda p: p.name, people))
    ages = list(map(lambda p: p.age, people))
    print(f"Names: {names}, Ages: {ages}")

    # Problem 4: Apply multiple transformations
    # Double then square
    numbers = [1, 2, 3, 4, 5]
    result = list(map(lambda x: (x * 2) ** 2, numbers))
    print(f"Double then square: {result}")

    return int_nums, floats, names, ages, result


# =============================================================================
# SECTION 2: FILTER FUNCTION
# =============================================================================

def filter_basic():
    """
    Filter function examples.
    filter(function, iterable) - keeps elements where function returns True

    Time Complexity: O(n) where n is the length of iterable
    Space Complexity: O(n) for the result

    Note: function can be None to keep truthy values
    """
    # Example 1: Filter even numbers
    numbers = list(range(10))
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Even numbers: {evens}")

    # Example 2: Filter odd numbers
    odds = list(filter(lambda x: x % 2 != 0, numbers))
    print(f"Odd numbers: {odds}")

    # Example 3: Filter strings longer than 3 characters
    words = ['hi', 'hello', 'hey', 'world', 'python']
    long_words = list(filter(lambda w: len(w) > 3, words))
    print(f"Words > 3 chars: {long_words}")

    # Example 4: Filter with None (keep truthy values)
    values = [0, 1, '', 'hello', None, False, True, 5]
    truthy = list(filter(None, values))
    print(f"Truthy values: {truthy}")

    # Example 5: Filter prime numbers
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    numbers = range(1, 20)
    primes = list(filter(is_prime, numbers))
    print(f"Primes 1-19: {primes}")

    # Example 6: Filter objects by attribute
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def __repr__(self):
            return f"Person({self.name}, {self.age})"

    people = [Person('Alice', 30), Person('Bob', 17), Person('Charlie', 25)]
    adults = list(filter(lambda p: p.age >= 18, people))
    print(f"Adults: {adults}")

    return evens, odds, long_words, truthy, primes, adults


def filter_vs_list_comprehension():
    """
    Compare filter vs list comprehension with if clause.
    """
    numbers = range(10)

    # Using filter
    evens_filter = list(filter(lambda x: x % 2 == 0, numbers))

    # Using list comprehension
    evens_comp = [x for x in numbers if x % 2 == 0]

    print(f"Filter: {evens_filter}")
    print(f"Comprehension: {evens_comp}")
    print(f"Equal: {evens_filter == evens_comp}")

    # Preference: List comprehension is generally more Pythonic
    # but filter is useful when reusing filter functions

    return evens_filter, evens_comp


def filter_practice_problems():
    """
    Common interview problems using filter.
    """
    # Problem 1: Remove None values from list
    values = [1, None, 2, None, 3, 4, None, 5]
    cleaned = list(filter(lambda x: x is not None, values))
    print(f"Remove None: {cleaned}")

    # Problem 2: Filter palindromes
    words = ['radar', 'hello', 'level', 'world', 'madam']
    palindromes = list(filter(lambda w: w == w[::-1], words))
    print(f"Palindromes: {palindromes}")

    # Problem 3: Filter numbers within range
    numbers = [1, 5, 10, 15, 20, 25, 30]
    in_range = list(filter(lambda x: 10 <= x <= 25, numbers))
    print(f"In range [10,25]: {in_range}")

    # Problem 4: Filter strings starting with vowel
    words = ['apple', 'banana', 'cherry', 'elephant', 'igloo']
    vowels = list(filter(lambda w: w[0].lower() in 'aeiou', words))
    print(f"Start with vowel: {vowels}")

    # Problem 5: Filter dictionary by value
    d = {'a': 1, 'b': 5, 'c': 3, 'd': 8, 'e': 2}
    filtered = dict(filter(lambda item: item[1] > 3, d.items()))
    print(f"Dict value > 3: {filtered}")

    return cleaned, palindromes, in_range, vowels, filtered


# =============================================================================
# SECTION 3: REDUCE FUNCTION
# =============================================================================

def reduce_basic():
    """
    Reduce function examples (from functools).
    reduce(function, iterable, initial) - accumulates values

    Time Complexity: O(n) where n is the length of iterable
    Space Complexity: O(1) for accumulator (not counting output)

    Note: function should take two arguments (accumulator, current)
    """
    # Example 1: Sum all numbers
    numbers = [1, 2, 3, 4, 5]
    total = reduce(lambda acc, x: acc + x, numbers)
    print(f"Sum: {total}")

    # Example 2: Product of all numbers
    product = reduce(lambda acc, x: acc * x, numbers)
    print(f"Product: {product}")

    # Example 3: Find maximum
    numbers = [5, 2, 8, 1, 9]
    max_val = reduce(lambda acc, x: x if x > acc else acc, numbers)
    print(f"Max: {max_val}")

    # Example 4: Find minimum
    min_val = reduce(lambda acc, x: x if x < acc else acc, numbers)
    print(f"Min: {min_val}")

    # Example 5: Concatenate strings
    words = ['Hello', ' ', 'World', '!']
    sentence = reduce(lambda acc, x: acc + x, words)
    print(f"Sentence: '{sentence}'")

    # Example 6: With initial value
    numbers = [1, 2, 3, 4, 5]
    sum_with_initial = reduce(lambda acc, x: acc + x, numbers, 100)
    print(f"Sum with initial 100: {sum_with_initial}")  # 115

    return total, product, max_val, min_val, sentence, sum_with_initial


def reduce_advanced():
    """
    Advanced reduce patterns.
    """
    # Pattern 1: Flatten nested list
    nested = [[1, 2], [3, 4], [5, 6]]
    flat = reduce(lambda acc, x: acc + x, nested, [])
    print(f"Flatten: {flat}")

    # Pattern 2: Count occurrences
    text = "hello world"
    char_count = reduce(
        lambda acc, c: {**acc, c: acc.get(c, 0) + 1},
        text,
        {}
    )
    print(f"Char count: {char_count}")

    # Pattern 3: Group by
    data = [
        {'name': 'Alice', 'dept': 'IT'},
        {'name': 'Bob', 'dept': 'HR'},
        {'name': 'Charlie', 'dept': 'IT'},
    ]
    grouped = reduce(
        lambda acc, item: {**acc, item['dept']: acc.get(item['dept'], []) + [item['name']]},
        data,
        {}
    )
    print(f"Grouped by dept: {grouped}")

    # Pattern 4: Build dictionary from lists
    keys = ['a', 'b', 'c']
    values = [1, 2, 3]
    d = reduce(
        lambda acc, kv: {**acc, kv[0]: kv[1]},
        zip(keys, values),
        {}
    )
    print(f"Built dict: {d}")

    # Pattern 5: Find longest word
    words = ['cat', 'elephant', 'dog', 'hippopotamus']
    longest = reduce(
        lambda acc, w: w if len(w) > len(acc) else acc,
        words,
        ''
    )
    print(f"Longest: {longest}")

    return flat, char_count, grouped, d, longest


def reduce_vs_loop():
    """
    Compare reduce with explicit loops.
    Most of the time, built-in functions (sum, max, etc.) are better!
    """
    numbers = [1, 2, 3, 4, 5]

    # Sum - just use sum()!
    total = sum(numbers)

    # Product - use math.prod (Python 3.8+)
    import math
    product = math.prod(numbers)

    # Max - just use max()!
    max_val = max(numbers)

    # When to use reduce:
    # - Complex custom aggregation
    # - Building complex data structures

    print(f"Sum: {total}, Product: {product}, Max: {max_val}")

    return total, product, max_val


# =============================================================================
# SECTION 4: ENUMERATE FUNCTION
# =============================================================================

def enumerate_basic():
    """
    Enumerate function examples.
    enumerate(iterable, start=0) - adds index to iterable

    Time Complexity: O(n) where n is the length of iterable
    Space Complexity: O(1) for the iterator

    Returns tuples of (index, value)
    """
    # Example 1: Basic enumerate
    fruits = ['apple', 'banana', 'cherry']
    for i, fruit in enumerate(fruits):
        print(f"{i}: {fruit}")

    # Example 2: Start from 1
    for i, fruit in enumerate(fruits, start=1):
        print(f"{i}: {fruit}")

    # Example 3: Create dictionary with indices
    indexed = {i: fruit for i, fruit in enumerate(fruits)}
    print(f"Indexed dict: {indexed}")

    # Example 4: Get index and value together
    result = list(enumerate(fruits))
    print(f"As list of tuples: {result}")

    # Example 5: Using with conditional
    # Find index of first even number
    numbers = [1, 3, 5, 6, 7, 8]
    for i, n in enumerate(numbers):
        if n % 2 == 0:
            print(f"First even at index {i}: {n}")
            break

    # Example 6: Enumerate over string
    for i, char in enumerate("abc"):
        print(f"{i}: {char}")

    return indexed, result


def enumerate_practice():
    """
    Practice problems with enumerate.
    """
    # Problem 1: Find duplicates using enumerate
    arr = [1, 2, 3, 2, 4, 3, 5]
    seen = set()
    duplicates = []
    for i, val in enumerate(arr):
        if val in seen:
            duplicates.append((i, val))
        seen.add(val)
    print(f"Duplicates (index, value): {duplicates}")

    # Problem 2: Get pairs (index, element)
    items = ['a', 'b', 'c']
    pairs = [(i, item) for i, item in enumerate(items)]
    print(f"Pairs: {pairs}")

    # Problem 3: Index of first occurrence
    items = [1, 2, 3, 2, 1]
    target = 2
    index = next((i for i, x in enumerate(items) if x == target), -1)
    print(f"First index of {target}: {index}")

    return duplicates, pairs, index


# =============================================================================
# SECTION 5: ZIP FUNCTION
# =============================================================================

def zip_basic():
    """
    Zip function examples.
    zip(*iterables) - combines iterables element-wise

    Time Complexity: O(n) where n is min length of iterables
    Space Complexity: O(n) for the result

    Returns iterator of tuples
    """
    # Example 1: Basic zip
    names = ['Alice', 'Bob', 'Charlie']
    ages = [25, 30, 35]
    combined = list(zip(names, ages))
    print(f"Combined: {combined}")

    # Example 2: Unzip using *
    names, ages = zip(*combined)
    print(f"Unzipped names: {names}, ages: {ages}")

    # Example 3: Create dictionary
    keys = ['a', 'b', 'c']
    values = [1, 2, 3]
    d = dict(zip(keys, values))
    print(f"Dict: {d}")

    # Example 4: Zip with more iterables
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [7, 8, 9]
    result = list(zip(a, b, c))
    print(f"Three-way: {result}")

    # Example 5: Unequal length (stops at shortest)
    a = [1, 2, 3]
    b = [4, 5]
    result = list(zip(a, b))
    print(f"Unequal: {result}")

    # Example 6: strict=True (Python 3.10+) - raises if unequal
    # result = list(zip(a, b, strict=True))  # Would raise

    return combined, d, result


def zip_advanced():
    """
    Advanced zip patterns.
    """
    # Pattern 1: Iterate over multiple lists
    names = ['Alice', 'Bob', 'Charlie']
    ages = [25, 30, 35]
    cities = ['NYC', 'LA', 'SF']

    for name, age, city in zip(names, ages, cities):
        print(f"{name}, {age}, {city}")

    # Pattern 2: Transpose matrix
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    transposed = list(zip(*matrix))
    print(f"Transposed: {transposed}")

    # Pattern 3: Create tuple of running pairs
    items = [1, 2, 3, 4, 5]
    pairs = list(zip(items, items[1:]))
    print(f"Consecutive pairs: {pairs}")

    # Pattern 4: Chunk list into pairs
    def chunk(lst, n):
        return list(zip(*[iter(lst)] * n))

    nums = [1, 2, 3, 4, 5, 6]
    chunks = chunk(nums, 2)
    print(f"Chunks of 2: {chunks}")

    # Pattern 5: Create sliding window
    def sliding_window(lst, size):
        return list(zip(*[lst[i:] for i in range(size)]))

    nums = [1, 2, 3, 4, 5]
    windows = sliding_window(nums, 3)
    print(f"Sliding window size 3: {windows}")

    return transposed, pairs, chunks, windows


# =============================================================================
# SECTION 6: ALL AND ANY
# =============================================================================

def all_any_basic():
    """
    All and Any function examples.
    all(iterable) - True if ALL elements are truthy
    any(iterable) - True if ANY element is truthy

    Time Complexity: O(n) - stops early if condition determined
    Space Complexity: O(1)
    """
    # Example 1: all() - check all even
    numbers = [2, 4, 6, 8, 10]
    all_even = all(x % 2 == 0 for x in numbers)
    print(f"All even: {all_even}")

    # Example 2: all() with one False
    numbers = [2, 4, 5, 6, 8]
    all_even = all(x % 2 == 0 for x in numbers)
    print(f"All even (with odd): {all_even}")

    # Example 3: any() - check any even
    numbers = [1, 3, 5, 6, 7]
    any_even = any(x % 2 == 0 for x in numbers)
    print(f"Any even: {any_even}")

    # Example 4: any() - check any divisible by 3
    numbers = [1, 4, 5, 7, 8]
    any_div3 = any(x % 3 == 0 for x in numbers)
    print(f"Any divisible by 3: {any_div3}")

    # Example 5: Empty iterable behavior
    print(f"all([]): {all([])}")  # True (vacuous truth)
    print(f"any([]): {any([])}")  # False

    # Example 6: With strings
    words = ['apple', 'banana', 'cherry']
    all_long = all(len(w) > 3 for w in words)
    any_long = any(len(w) > 10 for w in words)
    print(f"All > 3: {all_long}, Any > 10: {any_long}")

    return all_even, any_even, any_div3


def all_any_practice():
    """
    Practice problems with all/any.
    """
    # Problem 1: Check if string has all unique characters
    def is_unique(s):
        return len(s) == len(set(s))

    print(f"'abc': {is_unique('abc')}")  # True
    print(f"'aba': {is_unique('aba')}")  # False

    # Problem 2: Check if list is sorted
    def is_sorted(lst):
        return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

    print(f"[1,2,3]: {is_sorted([1,2,3])}")  # True
    print(f"[1,3,2]: {is_sorted([1,3,2])}")  # False

    # Problem 3: Check if all numbers positive
    nums = [1, 2, 3, 4, 5]
    print(f"All positive: {all(x > 0 for x in nums)}")

    # Problem 4: Check if any string is empty
    strings = ['hello', '', 'world']
    print(f"Has empty: {any(s == '' for s in strings)}")

    # Problem 5: Validate form submission
    form_data = {'name': 'John', 'email': 'john@example.com', 'phone': '123'}
    required = ['name', 'email', 'age']
    has_all = all(field in form_data for field in required)
    print(f"Has all required: {has_all}")

    return


# =============================================================================
# SECTION 7: MIN AND MAX WITH KEY
# =============================================================================

def min_max_key_basic():
    """
    Min and Max with key parameter.
    min(iterable, key=function)
    max(iterable, key=function)

    Time Complexity: O(n) where n is length of iterable
    Space Complexity: O(1) for key function
    """
    # Example 1: Find longest string
    words = ['apple', 'banana', 'cherry', 'date']
    longest = max(words, key=len)
    shortest = min(words, key=len)
    print(f"Longest: {longest}, Shortest: {shortest}")

    # Example 2: Find maximum absolute value
    numbers = [-10, 2, -5, 8, 3]
    max_abs = max(numbers, key=abs)
    min_abs = min(numbers, key=abs)
    print(f"Max abs: {max_abs}, Min abs: {min_abs}")

    # Example 3: Find oldest person
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def __repr__(self):
            return f"{self.name}({self.age})"

    people = [Person('Alice', 30), Person('Bob', 25), Person('Charlie', 35)]
    oldest = max(people, key=lambda p: p.age)
    youngest = min(people, key=lambda p: p.age)
    print(f"Oldest: {oldest}, Youngest: {youngest}")

    # Example 4: Find most common character
    text = "hello world"
    most_common = max(text, key=text.count)
    print(f"Most common: '{most_common}'")

    # Example 5: Find dictionary with max value
    d = {'a': 10, 'b': 5, 'c': 20, 'd': 15}
    max_key = max(d, key=d.get)
    print(f"Max value key: {max_key}")

    # Example 6: Get both key and value
    max_item = max(d.items(), key=lambda kv: kv[1])
    print(f"Max item: {max_item}")

    return longest, shortest, oldest, youngest, most_common


def min_max_key_advanced():
    """
    Advanced min/max patterns.
    """
    # Pattern 1: Get index of min/max
    numbers = [5, 2, 8, 1, 9]
    min_index = numbers.index(min(numbers))
    max_index = numbers.index(max(numbers))
    print(f"Min at: {min_index}, Max at: {max_index}")

    # Pattern 2: Multiple criteria
    # Sort by age, then by name
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def __repr__(self):
            return f"{self.name}({self.age})"

    people = [
        Person('Bob', 30),
        Person('Alice', 30),
        Person('Charlie', 25)
    ]
    # Oldest, or alphabetically first if same age
    result = max(people, key=lambda p: (p.age, -ord(p.name[0])))
    print(f"Max: {result}")

    # Pattern 3: Find key with max value in list of dicts
    data = [
        {'name': 'A', 'score': 85},
        {'name': 'B', 'score': 92},
        {'name': 'C', 'score': 78}
    ]
    best = max(data, key=lambda x: x['score'])
    print(f"Best scorer: {best}")

    # Pattern 4: Find minimum based on computed value
    points = [(1, 2), (3, 1), (2, 3)]
    closest = min(points, key=lambda p: p[0]**2 + p[1]**2)
    print(f"Closest to origin: {closest}")

    # Pattern 5: Find longest word starting with letter
    words = ['hello', 'hi', 'hey', 'world', 'welcome']
    letter = 'w'
    longest_with_w = max(
        [w for w in words if w.startswith(letter)],
        key=len,
        default=''
    )
    print(f"Longest starting with '{letter}': {longest_with_w}")

    return min_index, max_index, best, closest, longest_with_w


# =============================================================================
# SECTION 8: COMBINED PATTERNS
# =============================================================================

def combined_patterns():
    """
    Combining multiple built-in functions.
    """
    # Pattern 1: Map + Filter + Reduce
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Sum of squares of even numbers
    result = reduce(
        lambda acc, x: acc + x,
        map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers))
    )
    print(f"Sum of squares of evens: {result}")

    # Pattern 2: Enumerate + Zip
    names = ['Alice', 'Bob', 'Charlie']
    ages = [25, 30, 35]

    # Create list of dicts
    people = [dict(name=n, age=a, index=i)
              for i, (n, a) in enumerate(zip(names, ages))]
    print(f"People: {people}")

    # Pattern 3: All + Any + Filter
    numbers = [1, 2, 3, 4, 5]
    all_positive = all(x > 0 for x in numbers)
    any_large = any(x > 3 for x in numbers)
    filtered = list(filter(lambda x: x > 2, numbers))
    print(f"All > 0: {all_positive}, Any > 3: {any_large}, Filtered: {filtered}")

    # Pattern 4: Min/Max with key + dict
    d = {'apple': 5, 'banana': 2, 'cherry': 8}
    min_key = min(d, key=d.get)
    max_key = max(d, key=d.get)
    print(f"Min value key: {min_key}, Max: {max_key}")

    # Pattern 5: Complex transformation chain
    words = ['hello', 'world', 'python']

    # Uppercase, then get lengths
    lengths = list(map(len, map(str.upper, words)))
    print(f"Lengths: {lengths}")

    return result, people, min_key, max_key, lengths


# =============================================================================
# SECTION 9: TESTING AND DEMO
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("BUILT-IN FUNCTIONS - TEST DEMO")
    print("=" * 60)

    # Section 1: Map
    print("\n--- Map Function ---")
    map_basic()
    map_vs_list_comprehension()
    map_practice_problems()

    # Section 2: Filter
    print("\n--- Filter Function ---")
    filter_basic()
    filter_vs_list_comprehension()
    filter_practice_problems()

    # Section 3: Reduce
    print("\n--- Reduce Function ---")
    reduce_basic()
    reduce_advanced()
    reduce_vs_loop()

    # Section 4: Enumerate
    print("\n--- Enumerate Function ---")
    enumerate_basic()
    enumerate_practice()

    # Section 5: Zip
    print("\n--- Zip Function ---")
    zip_basic()
    zip_advanced()

    # Section 6: All and Any
    print("\n--- All and Any ---")
    all_any_basic()
    all_any_practice()

    # Section 7: Min and Max with Key
    print("\n--- Min and Max with Key ---")
    min_max_key_basic()
    min_max_key_advanced()

    # Section 8: Combined Patterns
    print("\n--- Combined Patterns ---")
    combined_patterns()

    print("\n" + "=" * 60)
    print("All tests completed!")
    print("=" * 60)

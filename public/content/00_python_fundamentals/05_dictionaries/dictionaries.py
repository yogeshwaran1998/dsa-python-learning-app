"""
Dictionaries - Implementation Guide
===================================
Comprehensive Python implementations covering dictionary creation, access,
.get() method, iteration, defaultdict, and Counter for interviews.
"""

from typing import List, Dict, Any
from collections import defaultdict, Counter


# =============================================================================
# SECTION 1: DICTIONARY CREATION
# =============================================================================

# Empty dictionary
empty_dict = {}
empty_dict2 = dict()

# Basic creation with key-value pairs
person = {
    "name": "Alice",
    "age": 30,
    "city": "NYC"
}

# Using dict() constructor with keyword arguments
person2 = dict(name="Bob", age=25, city="LA")

# From list of tuples
pairs = [("a", 1), ("b", 2), ("c", 3)]
dict_from_pairs = dict(pairs)

# Dictionary comprehension - create dict from expressions
squares = {x: x**2 for x in range(5)}     # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}

# Dictionary with same value for all keys
default_value = {key: 0 for key in "abc"}

# Keys must be immutable (strings, numbers, tuples)
valid_keys = {
    "string_key": 1,
    42: "number key",
    (1, 2): "tuple key",
}

# invalid_keys = {["list"]: "value"}  # TypeError - lists not hashable


# =============================================================================
# SECTION 2: ACCESSING VALUES
# =============================================================================

person = {"name": "Alice", "age": 30, "city": "NYC"}

# Direct access - raises KeyError if key doesn't exist
name = person["name"]          # "Alice"
# person["unknown"]            # KeyError: 'unknown'

# Check if key exists before access
if "name" in person:
    print(f"Name: {person['name']}")

# Using .get() method (safer)
age = person.get("age")        # 30
unknown = person.get("unknown")  # None (no error)

# get() with default value
unknown = person.get("unknown", "N/A")  # "N/A"


# =============================================================================
# SECTION 3: ADDING, UPDATING, AND REMOVING
# =============================================================================

d = {}

# Adding single key-value pair
d["name"] = "Alice"
d["age"] = 30

# Updating existing key
d["age"] = 31

# Adding multiple key-value pairs with update()
d.update({"city": "NYC", "country": "USA"})
d.update([("a", 1), ("b", 2)])

# Removing with pop() - returns the value
value = d.pop("age")           # value = 31, d no longer has "age"

# Removing with del
del d["country"]

# popitem() - remove and return arbitrary key-value pair (Python 3.7+)
key, value = d.popitem()

# clear() - remove all items
d.clear()


# =============================================================================
# SECTION 4: DICTIONARY ITERATION
# =============================================================================

person = {"name": "Alice", "age": 30, "city": "NYC"}

# Iterate over keys (default)
print("Keys:")
for key in person:
    print(f"  {key}")

# Iterate over values
print("Values:")
for value in person.values():
    print(f"  {value}")

# Iterate over key-value pairs (items)
print("Items:")
for key, value in person.items():
    print(f"  {key}: {value}")

# Enumerate over items
print("With index:")
for i, (key, value) in enumerate(person.items()):
    print(f"  {i}: {key} = {value}")

# Dictionary view objects - dynamic views of the dictionary
keys = person.keys()     # dict_keys(['name', 'age', 'city'])
values = person.values() # dict_values(['Alice', 30, 'NYC'])
items = person.items()   # dict_items([('name', 'Alice'), ...])


# =============================================================================
# SECTION 5: THE .get() METHOD IN PRACTICE
# =============================================================================

# Pattern: Counting with .get()
def count_characters(s: str) -> Dict[str, int]:
    """Count character frequencies using .get()"""
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    return counts


# Pattern: Safe nested access
def get_nested(data: dict, *keys, default=None):
    """Safely access nested dictionary values"""
    result = data
    for key in keys:
        if isinstance(result, dict):
            result = result.get(key)
            if result is None:
                return default
        else:
            return default
    return result if result is not None else default


# Pattern: Default value for missing keys
inventory = {"apples": 10, "bananas": 5}
quantity = inventory.get("oranges", 0)  # 0 if not present


# =============================================================================
# SECTION 6: defaultdict
# =============================================================================

# Create defaultdict with default factory
# Options: int, float, list, set, dict, lambda

# Default value of 0 (useful for counting)
word_lengths = defaultdict(int)
for word in ["hello", "world", "hello"]:
    word_lengths[word] += 1
# Result: {'hello': 2, 'world': 1}

# Default value of empty list (useful for grouping)
groups = defaultdict(list)
for word in ["apple", "banana", "apricot", "blueberry"]:
    groups[word[0]].append(word)
# Result: {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry']}

# Default value of empty dict
nested = defaultdict(dict)
nested["person"]["name"] = "Alice"
nested["person"]["age"] = 30
# Result: {'person': {'name': 'Alice', 'age': 30}}

# Custom default with lambda
custom_default = defaultdict(lambda: "N/A")
value = custom_default["missing"]  # "N/A"

# Default value of empty set (useful for unique groupings)
sets_by_first = defaultdict(set)
for word in ["cat", "car", "bar", "bat"]:
    sets_by_first[word[0]].add(word)
# Result: {'c': {'cat', 'car'}, 'b': {'bar', 'bat'}}


# =============================================================================
# SECTION 7: COUNTER
# =============================================================================

# Create Counter from iterable
char_counts = Counter("hello world")
# Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# Create Counter from mapping
c = Counter({"red": 4, "blue": 2})

# Create Counter from keywords
c = Counter(red=4, blue=2)

# Access counts
count = char_counts["l"]        # 3
missing = char_counts["z"]      # 0 (doesn't raise error)

# Update counts
c = Counter(["a", "b", "c"])
c.update(["a", "b", "d"])      # Counter({'a': 2, 'b': 2, 'c': 1, 'd': 1})

# most_common(n) - return n most common elements
text = "the quick brown fox jumps over the lazy dog"
word_counts = Counter(text.split())
top_words = word_counts.most_common(3)  # [('the', 2), ('fox', 1), ...]

# elements() - return all elements (repeats according to count)
c = Counter(a=3, b=1)
list(c.elements())  # ['a', 'a', 'a', 'b']

# Arithmetic operations
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)

added = c1 + c2           # Counter({'a': 4, 'b': 3}) - addition
subtracted = c1 - c2      # Counter({'a': 2}) - subtraction (only positives)
min_counts = c1 & c2       # Counter({'a': 1, 'b': 1}) - intersection (min)
max_counts = c1 | c2       # Counter({'a': 3, 'b': 2}) - union (max)


# =============================================================================
# SECTION 8: PRACTICAL INTERVIEW PATTERNS
# =============================================================================

def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Find indices of two numbers that add up to target.
    Time: O(n), Space: O(n)
    """
    seen = {}  # value -> index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Group anagrams together using dictionary.
    Time: O(n * k), Space: O(n * k)
    """
    groups = defaultdict(list)

    for word in strs:
        # Sort characters to create key
        key = "".join(sorted(word))
        groups[key].append(word)

    return list(groups.values())


def word_frequency(text: str) -> Counter:
    """Count word frequencies in text."""
    words = text.lower().split()
    return Counter(words)


def is_anagram(s: str, t: str) -> bool:
    """Check if two strings are anagrams using Counter."""
    return Counter(s) == Counter(t)


def subarray_sum(nums: List[int], target: int) -> List[int]:
    """
    Find subarray that sums to target (LeetCode 560).
    Time: O(n), Space: O(n)
    """
    prefix_sum = 0
    seen = {0: -1}  # sum -> earliest index

    for i, num in enumerate(nums):
        prefix_sum += num
        if target in seen:
            return [seen[target] + 1, i]
        seen[prefix_sum] = i

    return []


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    Find top k most frequent elements.
    Time: O(n), Space: O(n)
    """
    # Count frequencies
    counts = Counter(nums)

    # Get top k
    return [item for item, count in counts.most_common(k)]


def longest_consecutive_sequence(nums: List[int]) -> int:
    """
    Find longest consecutive sequence length.
    Time: O(n), Space: O(n)
    """
    num_set = set(nums)
    longest = 0

    for num in num_set:
        if num - 1 not in num_set:
            length = 1
            while num + length in num_set:
                length += 1
            longest = max(longest, length)

    return longest


def invert_dictionary(d: Dict[str, int]) -> Dict[int, List[str]]:
    """Invert a dictionary (values become keys)."""
    inverted = defaultdict(list)
    for key, value in d.items():
        inverted[value].append(key)
    return dict(inverted)


def merge_dictionaries(d1: Dict, d2: Dict) -> Dict:
    """Merge two dictionaries (sum values for duplicate keys)."""
    result = Counter(d1) + Counter(d2)
    return dict(result)


# =============================================================================
# SECTION 9: DICTIONARY COMPREHENSION PATTERNS
# =============================================================================

# Basic dictionary comprehension
squares = {x: x**2 for x in range(5)}

# Filter dictionary by value
d = {"a": 1, "b": 2, "c": 3, "d": 4}
filtered = {k: v for k, v in d.items() if v > 2}  # {'c': 3, 'd': 4}

# Swap keys and values
swapped = {v: k for k, v in d.items()}

# Multiple conditions
data = {"apple": 10, "banana": 5, "cherry": 15, "date": 20}
fruits = {k: v for k, v in data.items()
          if len(k) > 5 and v >= 10}  # {'banana': 5 is filtered out... actually}
# Result: {'cherry': 15, 'date': 20}


# =============================================================================
# SECTION 10: DEMONSTRATION
# =============================================================================

if __name__ == "__main__":
    # Basic dictionary operations
    print("=== Dictionary Creation ===")
    person = {"name": "Alice", "age": 30}
    print(f"Created: {person}")

    print("\n=== Accessing Values ===")
    print(f"person['name']: {person['name']}")
    print(f"person.get('age'): {person.get('age')}")
    print(f"person.get('city', 'Unknown'): {person.get('city', 'Unknown')}")

    print("\n=== Iteration ===")
    for key, value in person.items():
        print(f"  {key}: {value}")

    print("\")
    groups = defaultdict(list)
    forn=== defaultdict === word in ["cat", "car", "bar", "bat"]:
        groups[word[0]].append(word)
    print(f"Grouped by first letter: {dict(groups)}")

    print("\n=== Counter ===")
    text = "hello world"
    counts = Counter(text)
    print(f"Counter: {counts}")
    print(f"Most common: {counts.most_common(3)}")

    print("\n=== Interview Patterns ===")
    print(f"Two sum [2,7,11,15], target 9: {two_sum([2, 7, 11, 15], 9)}")
    print(f"Top 2 frequent [1,1,1,2,2,3]: {top_k_frequent([1,1,1,2,2,3], 2)}")

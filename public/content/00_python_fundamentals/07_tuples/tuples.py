"""
Tuples - Implementation Guide
============================
Comprehensive Python implementations covering tuple creation, immutability,
packing/unpacking, namedtuples, and multiple return values.
"""

from typing import List, Tuple, Optional
from collections import namedtuple


# =============================================================================
# SECTION 1: TUPLE CREATION
# =============================================================================

# Empty tuple
empty = ()
empty2 = tuple()

# Single element - comma is REQUIRED!
single = (1,)           # (1,) - this is a tuple
not_tuple = (1)         # 1 - just an integer, not tuple!

# Multiple elements
point = (10, 20, 30)
person = ("Alice", 30, "NYC")

# Packing without parentheses (tuple works without parens)
packed = 1, 2, 3        # (1, 2, 3)

# From iterable - useful for converting
from_list = tuple([1, 2, 3])     # (1, 2, 3)
from_string = tuple("hello")     # ('h', 'e', 'l', 'l', 'o')
from_range = tuple(range(5))     # (0, 1, 2, 3, 4)

# Nested tuples
nested = ((1, 2), (3, 4), (5, 6))

# Tuple with different types
mixed = (1, "hello", 3.14, True, [1, 2], (3, 4))


# =============================================================================
# SECTION 2: IMMUTABILITY
# =============================================================================

t = (1, 2, 3, 4, 5)

# Valid operations - these create NEW tuples
print("Valid operations:")
print(f"t[0] = {t[0]}")              # Access by index - OK
print(f"t[1:3] = {t[1:3]}")          # Slice - OK
print(f"t + (6, 7) = {t + (6, 7)}")  # Concatenation - returns new tuple
print(f"t * 2 = {t * 2}")            # Repetition - returns new tuple

# Check immutability
print("\nImmutability checks:")
print(f"hash(t) = {hash(t)}")         # Hashable if elements are hashable

# These would raise errors (uncomment to test):
# t[0] = 10              # TypeError: 'tuple' object does not support item assignment
# t.append(6)            # AttributeError: 'tuple' object has no attribute 'append'
# t.remove(1)            # AttributeError
# t[1:2] = [20, 30]     # TypeError


# =============================================================================
# SECTION 3: TUPLE UNPACKING
# =============================================================================

# Basic unpacking
point = (10, 20, 30)
x, y, z = point        # x=10, y=20, z=30

# Without parentheses
a, b, c = 1, 2, 3     # Also works

# Extended unpacking with * (Python 3)
first, *middle, last = (1, 2, 3, 4, 5)
# first = 1
# middle = [2, 3, 4]
# last = 5

# Swap using tuple unpacking
a, b = 1, 2
a, b = b, a          # Now a=2, b=1

# Unpack in loop
pairs = [(1, 2), (3, 4), (5, 6)]
for a, b in pairs:
    print(f"Sum: {a + b}")  # 3, 7, 11

# Unpack in function arguments
def print_point(x, y, z):
    print(f"Point: ({x}, {y}, {z})")

point = (10, 20, 30)
print_point(*point)   # Unpacks to print_point(10, 20, 30)


# =============================================================================
# SECTION 4: NAMEDTUPLE
# =============================================================================

# Define namedtuple
Point = namedtuple("Point", ["x", "y"])
# Alternative: Point = namedtuple("Point", "x y")

# Create instance
p = Point(10, 20)

# Access by name
print(f"p.x = {p.x}")              # 10
print(f"p.y = {p.y}")              # 20

# Access by index (still works)
print(f"p[0] = {p[0]}")            # 10
print(f"p[1] = {p[1]}")            # 20

# Tuple-like behavior
print(f"len(p) = {len(p)}")        # 2
x, y = p                           # Unpacking works

# Namedtuple methods
print(f"\nPoint._fields = {Point._fields}")       # ('x', 'y')
print(f"p._asdict() = {p._asdict()}")            # OrderedDict([('x', 10), ('y', 20)])

# _replace() - create new instance with modifications
p2 = p._replace(x=30)              # Point(x=30, y=20)
print(f"p._replace(x=30) = {p2}")

# _make() - create from iterable
p3 = Point._make([40, 50])         # Point(x=40, y=50)
print(f"Point._make([40, 50]) = {p3}")


# =============================================================================
# SECTION 5: NAMEDTUPLE FOR RECORDS
# =============================================================================

# Employee example
Employee = namedtuple("Employee", ["name", "department", "salary"])

emp1 = Employee("Alice", "Engineering", 100000)
emp2 = Employee("Bob", "Sales", 80000)
emp3 = Employee("Charlie", "Engineering", 120000)

# Access fields
print(f"Employee: {emp1.name}, {emp1.department}, ${emp1.salary}")

# Use in collections
employees = [emp1, emp2, emp3]

# Find engineers
engineers = [e for e in employees if e.department == "Engineering"]
print(f"Engineers: {[e.name for e in engineers]}")

# Sort by salary
sorted_employees = sorted(employees, key=lambda e: e.salary)
print(f"Sorted: {[e.name for e in sorted_employees]}")


# =============================================================================
# SECTION 6: MULTIPLE RETURN VALUES
# =============================================================================

def divide(a: int, b: int) -> Tuple[int, int]:
    """Return quotient and remainder."""
    quotient = a // b
    remainder = a % b
    return quotient, remainder


def find_min_max(arr: List[int]) -> Tuple[Optional[int], Optional[int]]:
    """Return min and max of list."""
    if not arr:
        return None, None
    return min(arr), max(arr)


def search_element(arr: List[int], target: int) -> Tuple[bool, int]:
    """Return (found, index) tuple."""
    for i, val in enumerate(arr):
        if val == target:
            return True, i
    return False, -1


def get_stats(arr: List[int]) -> Tuple[int, int, int, float]:
    """Return count, min, max, average."""
    if not arr:
        return 0, 0, 0, 0.0
    return len(arr), min(arr), max(arr), sum(arr) / len(arr)


# Use multiple return values
result = divide(10, 3)
quotient, remainder = result
print(f"10 / 3 = {quotient} remainder {remainder}")

min_val, max_val = find_min_max([1, 2, 3, 4, 5])
print(f"Min: {min_val}, Max: {max_val}")

found, index = search_element([1, 2, 3, 4], 3)
print(f"Found: {found}, Index: {index}")


# =============================================================================
# SECTION 7: TUPLES AS DICTIONARY KEYS
# =============================================================================

# Perfect for coordinates
locations = {
    (40.7128, -74.0060): "New York City",
    (51.5074, -0.1278): "London",
    (35.6762, 139.6503): "Tokyo"
}

print(f"Location: {locations[(40.7128, -74.0060)]}")

# For sparse matrices
matrix_key = (0, 0)
matrix_key2 = (1, 2)

# For ranges
date_ranges = {
    ("2024-01-01", "2024-01-31"): "January",
    ("2024-02-01", "2024-02-29"): "February"
}


# =============================================================================
# SECTION 8: PRACTICAL INTERVIEW PATTERNS
# =============================================================================

def two_sum_indices(nums: List[int], target: int) -> Tuple[int, int]:
    """Find indices of two numbers that add to target."""
    seen = {}  # value -> index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return seen[complement], i
        seen[num] = i

    return -1, -1


def find_element(arr: List[int], target: int) -> Tuple[bool, int]:
    """Find element and return (found, index)."""
    for i, val in enumerate(arr):
        if val == target:
            return True, i
    return False, -1


def partition(arr: List[int], pivot: int) -> Tuple[List[int], List[int]]:
    """Partition array around pivot value."""
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x >= pivot]
    return left, right


def grouping_demo(words: List[str]) -> dict:
    """Group words by first letter using tuples."""
    groups = {}
    for word in words:
        key = word[0]
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return groups


def gcd_extended(a: int, b: int) -> Tuple[int, int, int]:
    """
    Extended Euclidean Algorithm.
    Returns (gcd, x, y) where ax + by = gcd
    """
    if b == 0:
        return a, 1, 0

    gcd, x1, y1 = gcd_extended(b, a % b)
    x = y1
    y = x1 - (a // b) * y1

    return gcd, x, y


# =============================================================================
# SECTION 9: TUPLE COMPARISON AND HASHING
# =============================================================================

# Tuple comparison (element by element)
print(f"(1, 2) < (1, 3): {(1, 2) < (1, 3)}")       # True
print(f"(1, 2) < (2, 1): {(1, 2) < (2, 1)}")       # True
print(f"(1, 2, 3) < (1, 2): {(1, 2, 3) < (1, 2)}")  # False (longer)

# Use tuples for sorting
points = [(1, 2), (0, 1), (2, 0)]
sorted_points = sorted(points)
print(f"Sorted points: {sorted_points}")  # [(0, 1), (1, 2), (2, 0)]

# Sorting by different criteria
points = [(1, 2), (0, 1), (2, 0)]
# Sort by y coordinate
sorted_by_y = sorted(points, key=lambda p: p[1])
print(f"Sorted by y: {sorted_by_y}")  # [(2, 0), (0, 1), (1, 2)]

# Hashable if all elements are hashable
t1 = (1, 2, 3)
t2 = (1, 2, [3, 4])  # Not hashable - contains list!

# Use as dict key
d = {t1: "value"}
print(f"Dict with tuple key: {d}")


# =============================================================================
# SECTION 10: DEMONSTRATION
# =============================================================================

if __name__ == "__main__":
    # Creation
    print("=== Tuple Creation ===")
    t = (1, 2, 3)
    print(f"Created tuple: {t}")

    # Unpacking
    print("\n=== Unpacking ===")
    a, b, c = (1, 2, 3)
    print(f"Unpacked: a={a}, b={b}, c={c}")

    # Swap
    x, y = 1, 2
    x, y = y, x
    print(f"Swapped: x={x}, y={y}")

    # Namedtuple
    print("\n=== Namedtuple ===")
    Point = namedtuple("Point", "x y")
    p = Point(10, 20)
    print(f"Point: {p}, x={p.x}, y={p.y}")

    # Multiple return values
    print("\n=== Multiple Return Values ===")
    q, r = divide(17, 5)
    print(f"17 / 5 = {q} remainder {r}")

    # Tuple as dict key
    print("\n=== Tuple as Dict Key ===")
    d = {(0, 0): "origin"}
    print(f"Dict: {d}")

"""
Sets - Implementation Guide
==========================
Comprehensive Python implementations covering set creation, operations,
membership testing, and frozenset for interviews.
"""

from typing import List, Set, FrozenSet


# =============================================================================
# SECTION 1: SET CREATION
# =============================================================================

# Empty set (note: {} creates dict, not set!)
empty_set = set()

# Set with elements - order is NOT guaranteed
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}

# From iterable - automatically removes duplicates
from_list = set([1, 2, 3, 2, 1])       # {1, 2, 3}
from_string = set("hello")              # {'h', 'e', 'l', 'o'}
from_range = set(range(10))              # {0, 1, 2, ..., 9}

# Mixed types (must be hashable/immutable)
mixed = {1, "hello", (1, 2), 3.14}      # Valid

# INVALID: unhashable types (lists, dicts, other sets)
# invalid = {1, [2, 3]}                 # TypeError: unhashable type

# Set comprehension
squares = {x**2 for x in range(5)}       # {0, 1, 4, 9, 16}
evens = {x for x in range(10) if x % 2 == 0}  # {0, 2, 4, 6, 8}


# =============================================================================
# SECTION 2: SET OPERATIONS - UNION
# =============================================================================

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union using | operator
union_result = set_a | set_b             # {1, 2, 3, 4, 5, 6}

# Union using method
union_method = set_a.union(set_b)        # {1, 2, 3, 4, 5, 6}

# Union with multiple sets
set_c = {6, 7, 8}
multiple_union = set_a | set_b | set_c   # {1, 2, 3, 4, 5, 6, 7, 8}

# Union with list
list_union = set_a | {7, 8, 9}           # {1, 2, 3, 4, 7, 8, 9}


# =============================================================================
# SECTION 3: SET OPERATIONS - INTERSECTION
# =============================================================================

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Intersection using & operator
intersection_result = set_a & set_b      # {3, 4}

# Intersection using method
intersection_method = set_a.intersection(set_b)  # {3, 4}

# Multiple intersections
set_c = {3, 6, 9}
multiple_intersection = set_a & set_b & set_c  # {3}


# =============================================================================
# SECTION 4: SET OPERATIONS - DIFFERENCE
# =============================================================================

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Difference using - operator (elements in a but not in b)
difference_result = set_a - set_b         # {1, 2}

# Difference using method
difference_method = set_a.difference(set_b)  # {1, 2}

# Multiple differences
set_c = {2, 8}
multiple_diff = set_a - set_b - set_c    # {1}


# =============================================================================
# SECTION 5: SET OPERATIONS - SYMMETRIC DIFFERENCE
# =============================================================================

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Symmetric difference using ^ operator (elements in either but not both)
sym_diff_result = set_a ^ set_b           # {1, 2, 5, 6}

# Symmetric difference using method
sym_diff_method = set_a.symmetric_difference(set_b)  # {1, 2, 5, 6}


# =============================================================================
# SECTION 6: MODIFYING SETS
# =============================================================================

s = {1, 2, 3}

# add() - add single element
s.add(4)                  # {1, 2, 3, 4}
s.add(2)                  # No change (already exists)

# update() - add multiple elements
s.update([4, 5, 6])       # {1, 2, 3, 4, 5, 6}
s.update({7, 8}, [9, 10])  # {1, 2, ..., 10}

# remove() - remove element (raises KeyError if not found)
s.remove(10)             # {1, 2, ..., 9}
# s.remove(999)           # KeyError!

# discard() - remove element (no error if not found)
s.discard(999)           # No error, set unchanged
s.discard(9)              # {1, 2, ..., 8}

# pop() - remove and return arbitrary element
arbitrary = s.pop()       # Returns some element, removes it from s

# clear() - remove all elements
s.clear()                 # set()


# =============================================================================
# SECTION 7: MEMBERSHIP TESTING
# =============================================================================

fruits = {"apple", "banana", "cherry", "orange"}

# Check if element is in set - O(1) average time!
print("apple" in fruits)          # True
print("grape" in fruits)         # False

# Check if not in
print("grape" not in fruits)     # True

# Practical use: remove duplicates while preserving order
def unique_ordered(items: List) -> List:
    """Remove duplicates while preserving order using set."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result


# Practical use: check for duplicates
def has_duplicates(items: List) -> bool:
    """Check if list has any duplicates."""
    return len(items) != len(set(items))


# =============================================================================
# SECTION 8: FROZENSET
# =============================================================================

# Create frozenset from iterable
fs1 = frozenset([1, 2, 3, 4])
fs2 = frozenset("hello")         # frozenset({'h', 'e', 'l', 'o'})

# From regular set
regular_set = {1, 2, 3}
fs = frozenset(regular_set)

# Frozenset operations (return new frozensets)
fs_a = frozenset([1, 2, 3])
fs_b = frozenset([3, 4, 5])

union_fs = fs_a | fs_b            # frozenset({1, 2, 3, 4, 5})
intersection_fs = fs_a & fs_b    # frozenset({3})
difference_fs = fs_a - fs_b       # frozenset({1, 2})
sym_diff_fs = fs_a ^ fs_b         # frozenset({1, 2, 4, 5})

# Membership in frozenset
print(2 in fs_a)                 # True
print(5 in fs_a)                  # False

# Frozenset CAN be used as dictionary key (regular set cannot!)
d = {frozenset([1, 2]): "pair1", frozenset([3, 4]): "pair2"}
print(d[frozenset([1, 2])])       # "pair1"

# Frozenset can be element of another set
set_of_frozensets = {frozenset([1, 2]), frozenset([3, 4])}


# =============================================================================
# SECTION 9: PRACTICAL INTERVIEW PATTERNS
# =============================================================================

def has_pair_sum(nums: List[int], target: int) -> bool:
    """
    Check if any two numbers sum to target.
    Time: O(n), Space: O(n)
    Uses set for O(1) membership testing.
    """
    seen = set()

    for num in nums:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)

    return False


def find_common_elements(list1: List, list2: List) -> List:
    """
    Find common elements between two lists.
    Time: O(n + m), Space: O(min(n, m))
    """
    return list(set(list1) & set(list2))


def find_unique_elements(list1: List, list2: List) -> List:
    """
    Find elements that are in exactly one list (not both).
    Time: O(n + m), Space: O(n + m)
    """
    return list(set(list1) ^ set(list2))


def count_unique_elements(*lists: List) -> int:
    """
    Count total unique elements across multiple lists.
    Time: O(n), Space: O(n)
    """
    all_elements = set()
    for lst in lists:
        all_elements.update(lst)
    return len(all_elements)


def find_missing_number(nums: List[int]) -> int:
    """
    Find missing number in range [0, n].
    Time: O(n), Space: O(n)
    """
    n = len(nums)
    full_set = set(range(n + 1))
    return full_set.difference(nums).pop()


def find_intersection_of_arrays(arrays: List[List[int]]) -> List[int]:
    """
    Find common elements across multiple arrays.
    Time: O(n * m), Space: O(min(all))
    """
    if not arrays:
        return []

    result = set(arrays[0])
    for arr in arrays[1:]:
        result &= set(arr)

    return list(result)


def subsets(nums: List[int]) -> List[List[int]]:
    """
    Generate all subsets using bit manipulation and sets.
    Time: O(n * 2^n), Space: O(2^n)
    """
    result = [set()]
    for num in nums:
        result += [subset | {num} for subset in result]
    return [list(s) for s in result]


def longest_unique_substring(s: str) -> int:
    """
    Find length of longest substring with unique characters.
    Time: O(n), Space: O(min(n, alphabet_size))
    """
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length


# =============================================================================
# SECTION 10: SET METHODS REFERENCE
# =============================================================================

s = {1, 2, 3}
other = {3, 4, 5}

# Access methods (return new sets)
s.union(other)                 # Union
s.intersection(other)         # Intersection
s.difference(other)          # Difference
s.symmetric_difference(other) # Symmetric difference
s.copy()                      # Shallow copy

# Update methods (modify in place)
s.update(other)               # s = s | other
s.intersection_update(other)  # s = s & other
s.difference_update(other)   # s = s - other
s.symmetric_difference_update(other)  # s = s ^ other

# Membership and subset checks
s.isdisjoint(other)           # True if no common elements
s.issubset(other)             # True if all s in other
s.issuperset(other)           # True if all other in s


# =============================================================================
# SECTION 11: DEMONSTRATION
# =============================================================================

if __name__ == "__main__":
    # Basic operations
    print("=== Set Creation ===")
    print(f"set([1,2,2,3]): {set([1, 2, 2, 3])}")

    print("\n=== Set Operations ===")
    a, b = {1, 2, 3}, {2, 3, 4}
    print(f"a | b (union): {a | b}")
    print(f"a & b (intersection): {a & b}")
    print(f"a - b (difference): {a - b}")
    print(f"a ^ b (symmetric diff): {a ^ b}")

    print("\n=== Membership Testing ===")
    print(f"'apple' in {{'apple', 'banana'}}: {'apple' in {'apple', 'banana'}}")

    print("\n=== Frozenset ===")
    fs = frozenset([1, 2, 3])
    print(f"frozenset: {fs}")
    print(f"Can use as dict key: {{fs: 'value'}} = { {fs: 'value'} }")

    print("\n=== Interview Patterns ===")
    print(f"has_pair_sum([1,2,3,4], 7): {has_pair_sum([1, 2, 3, 4], 7)}")
    print(f"has_duplicates([1,2,3,3]): {has_duplicates([1, 2, 3, 3])}")
    print(f"find_common([1,2,3], [2,3,4]): {find_common_elements([1, 2, 3], [2, 3, 4])}")

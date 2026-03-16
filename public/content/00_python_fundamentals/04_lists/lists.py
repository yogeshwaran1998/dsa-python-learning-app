"""
Lists - Implementation Guide
============================
Comprehensive Python implementations covering list creation, indexing,
slicing, mutability, sorting, and stack/queue operations.
"""

from typing import List, Optional
from collections import deque


# =============================================================================
# SECTION 1: LIST CREATION
# =============================================================================

# Empty list
empty_list = []
empty_list2 = list()

# List with initial elements
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, None]

# Using list() constructor
from_iterable = list(range(5))           # [0, 1, 2, 3, 4]
from_string = list("hello")               # ['h', 'e', 'l', 'l', 'o']

# List comprehension - Pythonic way to create lists
squares = [x**2 for x in range(10)]       # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
evens = [x for x in range(20) if x % 2 == 0]  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
cubes = [x**3 for x in range(5)]          # [0, 1, 8, 27, 64]

# Nested list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Repeated elements
zeros = [0] * 10                           # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
pattern = [1, 2, 3] * 3                   # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 2D array creation
rows, cols = 3, 4
grid = [[0 for _ in range(cols)] for _ in range(rows)]


# =============================================================================
# SECTION 2: INDEXING AND ACCESS
# =============================================================================

arr = [10, 20, 30, 40, 50]

# Positive indexing - starts from 0
first = arr[0]        # 10 - first element
second = arr[1]      # 20 - second element
last = arr[4]        # 50 - fifth element (last in this case)

# Negative indexing - starts from -1
last_neg = arr[-1]       # 50 - last element
second_last = arr[-2]    # 40 - second to last
first_neg = arr[-5]      # 10 - first element

# Index out of bounds raises error
# arr[10]  # IndexError: list index out of range
# arr[-10]  # IndexError: list index out of range

# Safe access with try-except
def safe_get(lst: List, index: int) -> Optional[int]:
    """Safely get element at index, return None if out of bounds."""
    try:
        return lst[index]
    except IndexError:
        return None


# =============================================================================
# SECTION 3: LIST SLICING
# =============================================================================

arr = [0, 1, 2, 3, 4, 5]

# Basic slicing [start:stop] - stop is EXCLUSIVE
slice1 = arr[1:4]     # [1, 2, 3]
slice2 = arr[:3]      # [0, 1, 2] - from beginning
slice3 = arr[3:]       # [3, 4, 5] - to end
slice4 = arr[:]        # [0, 1, 2, 3, 4, 5] - copy of entire list

# With step [start:stop:step]
every_second = arr[::2]    # [0, 2, 4] - even indices
every_second_alt = arr[1::2]  # [1, 3, 5] - odd indices

# Reverse using negative step
reversed_arr = arr[::-1]   # [5, 4, 3, 2, 1, 0]
reverse_every_other = arr[::-2]  # [5, 3, 1]

# Negative indices in slicing
slice5 = arr[-3:]     # [3, 4, 5] - last 3 elements
slice6 = arr[:-2]     # [0, 1, 2, 3] - all except last 2

# Modify list using slice assignment
arr[1:3] = [10, 20]  # [0, 10, 20, 3, 4, 5]
arr[:2] = []          # Remove first two: [20, 3, 4, 5]


# =============================================================================
# SECTION 4: MUTABILITY AND METHODS
# =============================================================================

# Lists are MUTABLE - can be modified in place
arr = [1, 2, 3]
arr[0] = 10           # [10, 2, 3]
arr.append(4)          # [10, 2, 3, 4]

# append(x) - add element to end (amortized O(1))
stack = []
stack.append(1)
stack.append(2)
stack.append(3)        # stack = [1, 2, 3]

# insert(i, x) - insert at specific index (O(n))
arr = [1, 2, 3]
arr.insert(1, 10)       # [1, 10, 2, 3]

# extend(iterable) - add multiple elements (O(k))
arr = [1, 2]
arr.extend([3, 4, 5])   # [1, 2, 3, 4, 5]

# remove(x) - remove first occurrence (O(n))
arr = [1, 2, 3, 2]
arr.remove(2)           # [1, 3, 2] - removes first 2

# pop(i) - remove and return element at index (O(1) for end, O(n) for front)
arr = [1, 2, 3]
last = arr.pop()        # last = 3, arr = [1, 2]
first = arr.pop(0)      # first = 1, arr = [2]

# index(x) - find first index of element (O(n))
arr = [1, 2, 3, 2]
idx = arr.index(2)      # idx = 1

# count(x) - count occurrences (O(n))
arr = [1, 2, 2, 3, 2]
cnt = arr.count(2)      # cnt = 3

# clear() - remove all elements (O(n))
arr = [1, 2, 3]
arr.clear()             # arr = []

# reverse() - reverse in place (O(n))
arr = [1, 2, 3]
arr.reverse()           # arr = [3, 2, 1]


# =============================================================================
# SECTION 5: SORTING
# =============================================================================

# sort() - sorts in place, modifies original list
arr = [3, 1, 4, 1, 5, 9, 2, 6]
arr.sort()              # arr = [1, 1, 2, 3, 4, 5, 6, 9]

# sorted() - returns new sorted list, original unchanged
arr = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_arr = sorted(arr)  # sorted_arr = [1, 1, 2, 3, 4, 5, 6, 9]
# arr still = [3, 1, 4, 1, 5, 9, 2, 6]

# reverse sort
arr = [3, 1, 4, 1, 5]
arr.sort(reverse=True)  # [5, 4, 3, 1, 1]

# sort with custom key
words = ["banana", "apple", "cherry", "date"]
arr.sort(key=len)       # Sort by length: ['apple', 'date', 'banana', 'cherry']

# case-insensitive sort
words = ["Banana", "apple", "Cherry"]
words.sort(key=str.lower)  # ['apple', 'Banana', 'Cherry']

# sort by multiple criteria
pairs = [(1, "c"), (2, "a"), (1, "b")]
pairs.sort(key=lambda x: (x[0], x[1]))  # [(1, 'b'), (1, 'c'), (2, 'a')]

# Using operator.itemgetter for faster sorting
from operator import itemgetter
pairs.sort(key=itemgetter(0, 1))  # Same as above but faster


# =============================================================================
# SECTION 6: LIST AS STACK (LIFO)
# =============================================================================

# Stack operations using list - O(1) for append/pop from end
stack = []

# Push - add to top of stack
stack.append(1)      # stack = [1]
stack.append(2)      # stack = [1, 2]
stack.append(3)      # stack = [1, 2, 3]

# Pop - remove from top
top = stack.pop()   # top = 3, stack = [1, 2]

# Peek - view top without removing
top = stack[-1]     # top = 2

# Check if empty
is_empty = len(stack) == 0


# =============================================================================
# SECTION 7: LIST AS QUEUE (FIFO) - Use deque!
# =============================================================================

# WRONG: Using list for queue is O(n) for pop(0)
# queue = [1, 2, 3]
# queue.pop(0)  # O(n) - must shift all elements!

# CORRECT: Use collections.deque for O(1) operations
queue = deque()

# Enqueue - add to rear
queue.append(1)      # queue = deque([1])
queue.append(2)      # queue = deque([1, 2])
queue.append(3)      # queue = deque([1, 2, 3])

# Dequeue - remove from front (O(1))
front = queue.popleft()  # front = 1, queue = deque([2, 3])

# Peek - view front without removing
front = queue[0]     # front = 2

# Check if empty
is_empty = len(queue) == 0


# =============================================================================
# SECTION 8: PRACTICAL INTERVIEW PATTERNS
# =============================================================================

def find_element(arr: List[int], target: int) -> int:
    """
    Find index of target in list. Returns -1 if not found.
    Time: O(n)
    """
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1


def find_max(arr: List[int]) -> int:
    """Find maximum element in list. O(n)"""
    if not arr:
        raise ValueError("Empty list")
    max_val = arr[0]
    for val in arr[1:]:
        if val > max_val:
            max_val = val
    return max_val


def remove_duplicates(arr: List[int]) -> List[int]:
    """
    Remove duplicates while preserving order. O(n)
    Uses set to track seen elements.
    """
    seen = set()
    result = []
    for val in arr:
        if val not in seen:
            result.append(val)
            seen.add(val)
    return result


def rotate_list(arr: List[int], k: int) -> List[int]:
    """
    Rotate list to the right by k positions. O(n)
    """
    k = k % len(arr)  # Handle k > len(arr)
    return arr[-k:] + arr[:-k]


def find_missing_number(nums: List[int]) -> int:
    """
    Find missing number in range [0, n]. O(n)
    Uses sum formula: n*(n+1)/2
    """
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


def two_sum_indices(nums: List[int], target: int) -> List[int]:
    """
    Find indices of two numbers that add up to target. O(n)
    Uses hash map for O(1) lookups.
    """
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


def move_zeros(arr: List[int]) -> List[int]:
    """
    Move all zeros to end while maintaining relative order of non-zeros. O(n)
    """
    result = []
    zero_count = 0

    for val in arr:
        if val == 0:
            zero_count += 1
        else:
            result.append(val)

    # Add zeros at the end
    result.extend([0] * zero_count)
    return result


def merge_sorted_lists(list1: List[int], list2: List[int]) -> List[int]:
    """
    Merge two sorted lists into one sorted list. O(n + m)
    Two-pointer technique.
    """
    result = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    # Add remaining elements
    result.extend(list1[i:])
    result.extend(list2[j:])
    return result


def find_palindromes(words: List[str]) -> List[str]:
    """Find all palindromes in a list. O(n * k)"""
    return [word for word in words if word == word[::-1]]


def flatten_nested_list(nested: List) -> List:
    """
    Flatten a nested list. O(n) where n is total elements.
    """
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten_nested_list(item))
        else:
            result.append(item)
    return result


# =============================================================================
# SECTION 9: LIST COMPREHENSION PATTERNS
# =============================================================================

# Basic list comprehension
squares = [x**2 for x in range(10)]

# With condition
evens = [x for x in range(20) if x % 2 == 0]

# Nested comprehension
matrix = [[i * j for j in range(3)] for i in range(3)]

# Dictionary from list
word_lengths = {word: len(word) for word in ["hello", "world"]}

# Set from list
unique_chars = {char for char in "hello world"}


# =============================================================================
# SECTION 10: DEMONSTRATION
# =============================================================================

if __name__ == "__main__":
    # Demonstrate creation
    print("=== List Creation ===")
    print(f"[x**2 for x in range(5)]: {[x**2 for x in range(5)]}")

    # Demonstrate indexing
    print("\n=== Indexing ===")
    arr = [10, 20, 30, 40, 50]
    print(f"arr[0] = {arr[0]}, arr[-1] = {arr[-1]}")

    # Demonstrate slicing
    print("\n=== Slicing ===")
    print(f"arr[1:4] = {arr[1:4]}, arr[::-1] = {arr[::-1]}")

    # Demonstrate methods
    print("\n=== Methods ===")
    arr = [3, 1, 2]
    arr.sort()
    print(f"After sort: {arr}")

    # Demonstrate stack
    print("\n=== Stack ===")
    stack = []
    stack.append(1)
    stack.append(2)
    print(f"Stack: {stack}, Popped: {stack.pop()}")

    # Demonstrate queue
    print("\n=== Queue ===")
    queue = deque([1, 2, 3])
    print(f"Queue: {queue}, Dequeued: {queue.popleft()}")

    # Run interview patterns
    print("\n=== Interview Patterns ===")
    print(f"Two sum: {two_sum_indices([2, 7, 11, 15], 9)}")
    print(f"Remove duplicates: {remove_duplicates([1, 2, 2, 3, 1, 4])}")
    print(f"Rotate [1,2,3,4] by 2: {rotate_list([1, 2, 3, 4], 2)}")

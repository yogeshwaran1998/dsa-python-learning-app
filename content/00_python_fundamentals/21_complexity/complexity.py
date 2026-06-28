"""
Time and Space Complexity of Python Operations
================================================
Comprehensive examples demonstrating complexity of Python's
built-in data structures for interviews and optimization.
"""

import time
import sys
from collections import defaultdict, deque
from typing import List, Dict, Set, Tuple, Any


# =============================================================================
# SECTION 1: LIST COMPLEXITY
# =============================================================================

def list_complexity_demo():
    """
    Demonstrate list operation complexities.

    Key insight: Python list is a dynamic array, not linked list.
    - Index access: O(1) - direct memory offset calculation
    - Append: O(1) amortized - occasional resize
    - Insert at beginning: O(n) - all elements shift
    - Pop from beginning: O(n) - all elements shift
    """

    # Creating lists
    my_list = []  # Empty list
    my_list = [1, 2, 3]  # List with elements

    # O(1) - Direct index access
    # List stores elements in contiguous memory
    # Address = base_address + index * element_size
    element = my_list[0]  # Constant time

    # O(n) - Search
    # Must iterate through elements
    if 2 in my_list:  # Linear search
        pass

    # O(1) amortized - Append
    # Occasionally triggers resize (typically 1.125x growth)
    for _ in range(1000):
        my_list.append(_)

    # O(n) - Insert at beginning
    # All existing elements must shift right
    my_list.insert(0, 0)  # Shifts all elements

    # O(n) - Pop from beginning
    # All elements must shift left
    my_list.pop(0)  # Shifts all elements

    # O(n) - Remove by value
    # Searches, then shifts
    my_list.remove(500)  # Finds first occurrence, shifts

    # O(n) - Index of value
    idx = my_list.index(500)  # Linear search

    # O(n) - Sort (Timsort)
    # O(n log n) time complexity
    my_list.sort()  # In-place, O(1) space extra

    # O(n log n) - Sorted (returns new list)
    sorted_list = sorted(my_list)


def list_vs_deque():
    """
    Compare list and deque for queue operations.

    Deque (double-ended queue):
    - O(1) for append/pop at both ends
    - Implemented as linked list of blocks
    """
    # List - slow for queue operations
    queue_list = []
    queue_list.append(1)  # O(1)
    queue_list.pop(0)      # O(n) - shifts all elements!

    # Deque - fast for queue operations
    from collections import deque
    queue_deque = deque()
    queue_deque.append(1)   # O(1)
    queue_deque.popleft()   # O(1)


# =============================================================================
# SECTION 2: DICTIONARY (DICT) COMPLEXITY
# =============================================================================

def dict_complexity_demo():
    """
    Demonstrate dictionary operation complexities.

    Key insight: Dict uses hash table with open addressing.
    - O(1) average for get, set, contains
    - O(n) worst case (hash collisions)

    Requirements for keys:
    - Must be hashable (immutable)
    - Must implement __hash__ and __eq__
    """

    my_dict = {}

    # O(1) - Insert/Update
    my_dict["key"] = "value"

    # O(1) - Access
    value = my_dict["key"]  # Raises KeyError if missing
    value = my_dict.get("key")  # Returns None if missing
    value = my_dict.get("key", "default")  # With default

    # O(1) - Membership test
    if "key" in my_dict:  # Hash lookup, not iteration
        pass

    # O(1) - Delete
    del my_dict["key"]  # Raises if not found
    value = my_dict.pop("key")  # Returns value, raises if not found
    value = my_dict.pop("key", None)  # With default

    # O(n) - Get all keys/values/items (iteration is O(n))
    for key in my_dict:
        pass
    for value in my_dict.values():
        pass
    for key, value in my_dict.items():
        pass


def dict_use_cases():
    """Demonstrate practical dict use cases with complexity in mind."""

    # Counting - O(n) to build, O(1) lookups
    items = [1, 2, 2, 3, 3, 3]
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1

    # Using defaultdict - cleaner
    counts = defaultdict(int)
    for item in items:
        counts[item] += 1

    # Grouping - O(n) build, O(1) per lookup
    people = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 30},
    ]
    by_age = defaultdict(list)
    for person in people:
        by_age[person["age"]].append(person["name"])

    # Caching/Memoization - O(1) lookup
    cache = {}
    def fib(n):
        if n in cache:
            return cache[n]
        if n <= 1:
            return n
        result = fib(n-1) + fib(n-2)
        cache[n] = result
        return result


# =============================================================================
# SECTION 3: SET COMPLEXITY
# =============================================================================

def set_complexity_demo():
    """
    Demonstrate set operation complexities.

    Key insight: Set is dict without values.
    - O(1) average for add, remove, contains
    - No indexing or ordering
    """

    my_set = {1, 2, 3}

    # O(1) - Add
    my_set.add(4)

    # O(1) - Membership test
    if 2 in my_set:  # Hash lookup
        pass

    # O(1) - Remove
    my_set.remove(3)  # Raises KeyError if not found
    my_set.discard(3)  # No error if not found

    # O(n) - Convert to list (if needed)
    my_list = list(my_set)

    # Set operations
    set1 = {1, 2, 3}
    set2 = {2, 3, 4}

    # O(n+m) - Union
    union = set1 | set2
    union = set1.union(set2)

    # O(min(n,m)) - Intersection
    intersection = set1 & set2

    # O(n) - Difference
    difference = set1 - set2


def set_use_cases():
    """Practical uses of sets."""

    # Deduplication - O(n)
    items = [1, 2, 2, 3, 3, 3]
    unique = list(set(items))  # Order not preserved!

    # Preserve order - O(n)
    unique_ordered = list(dict.fromkeys(items))

    # Finding common elements - O(n)
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    common = set(list1) & set(list2)

    # Fast membership test - O(1) vs O(n)
    allowed = {"a", "b", "c"}
    # Instead of: if char in ["a", "b", "c"]
    if char in allowed:
        pass


# =============================================================================
# SECTION 4: STRING COMPLEXITY
# =============================================================================

def string_complexity_demo():
    """
    Demonstrate string operation complexities.

    Key insight: Strings are IMMUTABLE.
    - Every modification creates a new string
    - Use list + join for efficient building
    """

    s = "hello"

    # O(1) - Index access
    char = s[0]

    # O(k) - Slice (k = length of slice)
    substring = s[1:4]  # "ell"

    # O(n+m) - Concatenation
    # Creates new string each time!
    result = ""
    for _ in range(100):
        result += "a"  # O(n^2) total!

    # O(n) - Efficient building
    parts = ["a"] * 100
    result = "".join(parts)  # O(n)

    # O(n*m) - Find substring
    idx = "hello world".find("world")  # Returns 6
    idx = "hello world".index("world")  # Same but raises if not found

    # O(n) - Split
    words = "hello world python".split()  # ['hello', 'world', 'python']

    # O(n) - Replace (creates new string)
    new_s = s.replace("l", "r")


def string_building():
    """Compare string building methods."""

    # Method 1: Concatenation in loop - SLOW
    start = time.time()
    result = ""
    for i in range(1000):
        result += str(i)
    t1 = time.time() - start

    # Method 2: List + join - FAST
    start = time.time()
    parts = []
    for i in range(1000):
        parts.append(str(i))
    result = "".join(parts)
    t2 = time.time() - start

    # Method 3: List comprehension - FASTEST
    start = time.time()
    result = "".join([str(i) for i in range(1000)])
    t3 = time.time() - start


# =============================================================================
# SECTION 5: TUPLE COMPLEXITY
# =============================================================================

def tuple_complexity_demo():
    """
    Demonstrate tuple operation complexities.

    Key insight: Tuples are IMMUTABLE lists.
    - Can be used as dict keys
    - Slightly smaller memory footprint
    - Cannot be modified after creation
    """

    my_tuple = (1, 2, 3)

    # O(1) - Index access
    element = my_tuple[0]

    # O(k) - Slice
    subset = my_tuple[1:3]

    # O(n) - Search
    if 2 in my_tuple:  # Linear search
        pass

    # O(n) - Index of element
    idx = my_tuple.index(2)

    # O(n) - Count occurrences
    count = my_tuple.count(2)

    # Can be used as dict keys (unlike lists)
    my_dict = {my_tuple: "value"}

    # Tuple unpacking - efficient
    a, b, c = my_tuple


# =============================================================================
# SECTION 6: HEAP OPERATIONS
# =============================================================================

import heapq


def heap_complexity_demo():
    """
    Demonstrate heap operation complexities.

    Key insight: Heap is binary tree stored in array.
    - Parent at i, children at 2i+1, 2i+2
    - Always maintains heap property (parent <= children)
    - Useful for: k smallest/largest, priority queue
    """

    # Create heap from list - O(n)
    heap = [3, 1, 4, 1, 5, 9, 2, 6]
    heapq.heapify(heap)  # In-place, O(n)

    # O(log n) - Push
    heapq.heappush(heap, 0)

    # O(log n) - Pop (smallest)
    smallest = heapq.heappop(heap)

    # O(log n) - Push and pop in one
    result = heapq.heappushpop(heap, 7)

    # Get k smallest - O(n + k log n)
    k_smallest = heapq.nsmallest(3, heap)

    # Get k largest - O(n + k log n)
    k_largest = heapq.nlargest(3, heap)


def heap_applications():
    """Practical applications of heaps."""

    # Kth largest element
    def kth_largest(nums, k):
        heap = nums[:k]
        heapq.heapify(heap)
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heapreplace(heap, num)
        return heap[0]

    # Merge k sorted lists
    def merge_sorted(*lists):
        heap = []
        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(heap, (lst[0], i, 0))
        result = []
        while heap:
            val, list_idx, elem_idx = heapq.heappop(heap)
            result.append(val)
            if elem_idx + 1 < len(lists[list_idx]):
                next_val = lists[list_idx][elem_idx + 1]
                heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
        return result


# =============================================================================
# SECTION 7: PERFORMANCE COMPARISON
# =============================================================================

def compare_membership():
    """Compare membership testing performance: list vs set."""

    n = 100000

    # Create test data
    large_list = list(range(n))
    large_set = set(range(n))
    target = n - 1  # Last element (worst case for list)

    # Test list - O(n)
    start = time.time()
    for _ in range(1000):
        result = target in large_list
    list_time = time.time() - start

    # Test set - O(1)
    start = time.time()
    for _ in range(1000):
        result = target in large_set
    set_time = time.time() - start

    print(f"List membership: {list_time:.4f}s")
    print(f"Set membership: {set_time:.4f}s")


def compare_deduplication():
    """Compare deduplication methods."""

    data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5] * 1000

    # Method 1: set() - loses order
    start = time.time()
    result1 = list(set(data))
    t1 = time.time() - start

    # Method 2: dict.fromkeys() - preserves order (Python 3.7+)
    start = time.time()
    result2 = list(dict.fromkeys(data))
    t2 = time.time() - start

    # Method 3: loop - preserves order, slower
    start = time.time()
    result3 = []
    for x in data:
        if x not in result3:
            result3.append(x)
    t3 = time.time() - start


# =============================================================================
# SECTION 8: OPTIMAL DATA STRUCTURE CHOICES
# =============================================================================

def optimal_choices():
    """
    Guide for choosing optimal data structure.
    """

    # Need to store ordered unique items?
    # Option 1: dict (Python 3.7+) - maintains insertion order
    ordered_unique = {}
    ordered_unique["first"] = 1
    ordered_unique["second"] = 2

    # Need a priority queue?
    # Option: heapq
    import heapq
    pq = []
    heapq.heappush(pq, (priority, item))

    # Need LRU cache?
    # Option: collections.OrderedDict (Python 3.7+, use dict)
    # or implement manually

    # Need fast append and pop at both ends?
    # Option: collections.deque
    from collections import deque
    dq = deque()
    dq.append(1)      # O(1)
    dq.appendleft(0)  # O(1)
    dq.pop()          # O(1)
    dq.popleft()      # O(1)

    # Need counter?
    # Option: collections.Counter
    from collections import Counter
    counts = Counter([1, 2, 2, 3, 3, 3])
    print(counts.most_common(2))  # Two most common


# =============================================================================
# SECTION 9: PRACTICAL EXAMPLES
# =============================================================================

def word_frequency():
    """
    Count word frequencies efficiently.
    """
    text = "the quick brown fox jumps over the lazy dog the fox"

    # O(n) method using Counter
    words = text.split()
    freq = Counter(words)

    # Find most common
    most_common = freq.most_common(2)

    # Manual method using defaultdict
    freq_dict = defaultdict(int)
    for word in words:
        freq_dict[word] += 1


def two_sum_efficient():
    """
    Two sum - compare approaches.
    """

    nums = [2, 7, 11, 15]
    target = 9

    # O(n^2) - Brute force
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    # O(n) - Using dict
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i


def kth_smallest():
    """Find kth smallest using different methods."""

    nums = [7, 4, 6, 3, 9, 1]
    k = 3

    # Method 1: Sort - O(n log n)
    sorted_nums = sorted(nums)
    kth = sorted_nums[k-1]

    # Method 2: Heap - O(n + k log n)
    kth = heapq.nsmallest(k, nums)[-1]

    # Method 3: Quickselect - O(n) average, O(n^2) worst
    # Not implemented here for brevity


# =============================================================================
# SECTION 10: TESTING AND DEMO
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("COMPLEXITY DEMO - TEST OUTPUT")
    print("=" * 60)

    # Section 1: List
    print("\n--- List Complexity ---")
    list_demo = [1, 2, 3, 4, 5]
    print(f"Access[0]: {list_demo[0]}")  # O(1)
    print(f"In list: {3 in list_demo}")  # O(n)

    # Section 2: Dict
    print("\n--- Dict Complexity ---")
    dict_demo = {"a": 1, "b": 2}
    print(f"Get 'a': {dict_demo.get('a')}")  # O(1)

    # Section 3: Set
    print("\n--- Set Complexity ---")
    set_demo = {1, 2, 3}
    print(f"Set contains 2: {2 in set_demo}")  # O(1)

    # Section 4: String
    print("\n--- String Complexity ---")
    str_demo = "hello"
    print(f"Slice [1:3]: {str_demo[1:3]}")  # O(k)
    print(f"Replace: {str_demo.replace('l', 'r')}")  # O(n)

    # Section 5: Tuple
    print("\n--- Tuple Complexity ---")
    tuple_demo = (1, 2, 3)
    print(f"Index access: {tuple_demo[0]}")  # O(1)

    # Section 6: Heap
    print("\n--- Heap Complexity ---")
    heap_demo = [3, 1, 4, 1, 5]
    heapq.heapify(heap_demo)
    print(f"Heap after heapify: {heap_demo}")
    heapq.heappush(heap_demo, 2)
    print(f"Heap after push: {heap_demo}")
    popped = heapq.heappop(heap_demo)
    print(f"Popped: {popped}")

    # Section 7: Performance comparison
    print("\n--- Performance Notes ---")
    print("Use set for membership testing (O(1) vs O(n))")
    print("Use list + join for string building")
    print("Use deque for queue operations")
    print("Use heapq for k smallest/largest")

    print("\n" + "=" * 60)
    print("All demos completed!")
    print("=" * 60)

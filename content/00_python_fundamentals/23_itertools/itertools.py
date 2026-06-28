"""
Itertools - Implementation and Examples
=========================================
Comprehensive Python implementations using itertools module
for efficient iteration, combinations, permutations, and more.
"""

from itertools import (
    count, cycle, repeat,
    permutations, combinations, combinations_with_replacement, product,
    islice, chain,
    filterfalse, groupby, accumulate,
    dropwhile, takewhile
)
# pairwise was added in Python 3.10; provide a fallback for older versions.
try:
    from itertools import pairwise
except ImportError:
    def pairwise(iterable):
        a, b = tee(iterable)
        next(b, None)
        return zip(a, b)
from itertools import tee
from typing import List, Tuple, Iterable, Any


# =============================================================================
# SECTION 1: INFINITE ITERATORS
# =============================================================================

"""
Infinite iterators generate sequences forever.
Use with caution - always add exit condition!
"""


def count_demo():
    """
    count(start=0, step=1) - Infinite counter

    Use cases:
    - Enumerating without starting from 0
    - Generating IDs
    - Creating index-based sequences
    """

    print("\n--- count() Demo ---")

    # Basic counter
    print("Counter from 0:")
    for i in count():
        if i >= 5:
            break
        print(i, end=" ")
    print()

    # Counter with start and step
    print("\nCounter from 10, step 3:")
    for i in count(10, 3):
        if i >= 25:
            break
        print(i, end=" ")
    print()

    # Use case: Add index to existing data
    data = ['a', 'b', 'c']
    print("\nIndexed data:")
    for idx, val in zip(count(1), data):
        print(f"{idx}: {val}")


def cycle_demo():
    """
    cycle(iterable) - Repeats iterable infinitely

    Use cases:
    - Round-robin scheduling
    - Cycling through colors/states
    - Repeating patterns
    """

    print("\n--- cycle() Demo ---")

    # Cycle through states
    states = ['idle', 'running', 'waiting']
    state_cycle = cycle(states)

    print("State machine simulation (5 transitions):")
    for _ in range(5):
        print(f"  State: {next(state_cycle)}")

    # Cycle with index
    print("\nCyclic list with index:")
    colors = ['red', 'green', 'blue']
    for i in range(7):
        print(f"  {i}: {colors[i % len(colors)]}")

    # Equivalent using cycle
    color_cycle = cycle(colors)
    for i in range(7):
        print(f"  {i}: {next(color_cycle)}")


def repeat_demo():
    """
    repeat(elem, n=None) - Repeats element n times or infinitely

    Use cases:
    - Multiplying with accumulate
    - Constant value in zip
    - Fill values
    """

    print("\n--- repeat() Demo ---")

    # Repeat 3 times
    print("Repeat 'x' 3 times:")
    for item in repeat('x', 3):
        print(f"  {item}")

    # Infinite repeat (use with takewhile, etc.)
    print("\nTake 5 from infinite repeat:")
    for i in range(5):
        val = next(repeat('inf'))
        print(f"  {val}")

    # Common use: multiply with accumulate
    print("\nUsing repeat with accumulate:")
    # 2 * 1, 2 * 2, 2 * 3, ...
    result = list(accumulate([1, 2, 3, 4], lambda x, y: x * y))
    print(f"  Accumulate multiply: {result}")


# =============================================================================
# SECTION 2: COMBINATORIC ITERATORS
# =============================================================================

"""
Combinatoric iterators generate combinations and permutations.
These are essential for combinatorial problems!
"""


def permutations_demo():
    """
    permutations(iterable, r=None) - All orderings

    Order MATTERS: ('A','B') != ('B','A')

    Time complexity: O(n! / (n-r)!)
    """

    print("\n--- permutations() Demo ---")

    # All permutations of 'ABC' (r defaults to len)
    print("All permutations of 'ABC':")
    for p in permutations('ABC'):
        print(f"  {p}")

    # Permutations of length 2
    print("\nPermutations of 'ABCD', length 2:")
    for p in permutations('ABCD', 2):
        print(f"  {p}")


def combinations_demo():
    """
    combinations(iterable, r) - Selections without order

    Order DOESN'T matter: ('A','B') is same as ('B','A')

    Time complexity: O(n! / (r! * (n-r)!))
    """

    print("\n--- combinations() Demo ---")

    # All combinations of 2 from 'ABC'
    print("Combinations of 'ABC', length 2:")
    for c in combinations('ABC', 2):
        print(f"  {c}")

    # Compare with permutations
    print("\nPermutations of 'ABC', length 2 (for comparison):")
    for p in permutations('ABC', 2):
        print(f"  {p}")
    print("Note: permutations has 6, combinations has 3 (order doesn't matter)")


def combinations_with_replacement_demo():
    """
    combinations_with_replacement(iterable, r) - With replacement

    Allows selecting same element multiple times.
    """

    print("\n--- combinations_with_replacement() Demo ---")

    print("Combinations with replacement of 'AB', length 2:")
    for c in combinations_with_replacement('AB', 2):
        print(f"  {c}")

    print("\nCombinations with replacement of [1,2,3], length 3:")
    for c in combinations_with_replacement([1, 2, 3], 3):
        print(f"  {c}")


def product_demo():
    """
    product(*iterables, repeat=1) - Cartesian product

    Like nested for loops.
    """

    print("\n--- product() Demo ---")

    # Basic product
    print("Product of [1,2] and ['a','b']:")
    for p in product([1, 2], ['a', 'b']):
        print(f"  {p}")

    # Two dice rolls
    print("\nAll two-dice combinations:")
    dice = range(1, 7)
    count = 0
    for roll in product(dice, dice):
        print(f"  {roll}", end=" ")
        count += 1
        if count % 6 == 0:
            print()
    print()

    # Repeat parameter
    print("\nProduct of 'AB' repeated 3 times:")
    for p in product('AB', repeat=3):
        print(f"  {''.join(p)}", end=" ")
    print()


# =============================================================================
# SECTION 3: ITERATOR SLICING
# =============================================================================

def islice_demo():
    """
    islice(iterable, start, stop, step) - Slice iterator

    Unlike list slicing, this is lazy (doesn't create full list).
    """

    print("\n--- islice() Demo ---")

    # First 5 elements
    print("First 5 from range(20):")
    print(list(islice(range(20), 5)))

    # Elements from index 5 to 10
    print("\nElements 5-9 from range(20):")
    print(list(islice(range(20), 5, 10)))

    # Every other element
    print("\nEvery other element from range(10):")
    print(list(islice(range(10), 0, 10, 2)))

    # Infinite iterator with islice
    print("\nFirst 10 even numbers (from infinite count):")
    print(list(islice(count(0, 2), 10)))


# =============================================================================
# SECTION 4: CHAINING
# =============================================================================

def chain_demo():
    """
    chain(*iterables) - Chain multiple iterables
    """

    print("\n--- chain() Demo ---")

    # Chain lists
    result = list(chain([1, 2], [3, 4], [5]))
    print(f"Chain [1,2], [3,4], [5]: {result}")

    # Chain different types
    result = list(chain('abc', [1, 2], (3, 4)))
    print(f"Chain 'abc', [1,2], (3,4): {result}")


def chain_from_iterable_demo():
    """
    chain.from_iterable(iterable) - Flatten nested iterables

    Equivalent to: [x for sublist in nested for x in sublist]
    """

    print("\n--- chain.from_iterable() Demo ---")

    # Flatten nested list
    nested = [[1, 2], [3, 4], [5]]
    flat = list(chain.from_iterable(nested))
    print(f"Flatten {nested}: {flat}")

    # Flatten list of strings
    words = ["hello", "world"]
    chars = list(chain.from_iterable(words))
    print(f"Flatten {words}: {chars}")

    # Compare with list comprehension
    flat_comp = [c for w in words for c in w]
    print(f"List comprehension: {flat_comp}")


# =============================================================================
# SECTION 5: FILTERING AND ACCUMULATING
# =============================================================================

def filter_demo():
    """
    filterfalse - Filter where function is False
    """

    print("\n--- filterfalse() Demo ---")

    # Filter where x > 5 is FALSE (i.e., x <= 5)
    result = list(filterfalse(lambda x: x > 5, range(10)))
    print(f"filterfalse(x > 5, 0-9): {result}")


def accumulate_demo():
    """
    accumulate(iterable, func=operator.add) - Running sum/product

    Useful for:
    - Prefix sums
    - Running products
    - Cumulative calculations
    """

    print("\n--- accumulate() Demo ---")

    # Default: running sum
    print(f"Running sum of [1,2,3,4,5]: {list(accumulate([1, 2, 3, 4, 5]))}")

    # Running product
    import operator
    print(f"Running product: {list(accumulate([1, 2, 3, 4], operator.mul))}")

    # Max (running maximum)
    print(f"Running max: {list(accumulate([3, 1, 4, 1, 5], max))}")


def dropwhile_takewhile_demo():
    """
    dropwhile - Skip while condition is True
    takewhile - Take while condition is True
    """

    print("\n--- dropwhile/takewhile Demo ---")

    # takewhile - take while x < 5
    print(f"takewhile(x < 5, 0-9): {list(takewhile(lambda x: x < 5, range(10)))}")

    # dropwhile - drop while x < 5
    print(f"dropwhile(x < 5, 0-9): {list(dropwhile(lambda x: x < 5, range(10)))}")

    # Practical use: process until error
    data = [1, 2, 3, 0, 5, 6]  # 0 indicates error
    valid = list(takewhile(lambda x: x > 0, data))
    print(f"Valid data before error: {valid}")


# =============================================================================
# SECTION 6: GROUPING
# =============================================================================

def groupby_demo():
    """
    groupby(iterable, key=None) - Group consecutive elements

    Note: Only groups CONSECUTIVE elements!
    """

    print("\n--- groupby() Demo ---")

    # Group by first letter
    data = ['apple', 'apricot', 'banana', 'blueberry', 'cherry']
    for letter, group in groupby(data, key=lambda x: x[0]):
        print(f"{letter}: {list(group)}")

    # Group consecutive numbers
    print("\nGroup consecutive numbers:")
    numbers = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1]
    for value, group in groupby(numbers):
        count = len(list(group))
        print(f"  {value} appears {count} times consecutively")


def pairwise_demo():
    """
    pairwise(iterable) - Consecutive element pairs (Python 3.10+)

    Useful for:
    - Sliding window of 2
    - Comparing adjacent elements
    """

    print("\n--- pairwise() Demo ---")

    # Sliding window of 2
    data = 'ABCDE'
    print(f"Adjacent pairs in '{data}':")
    for a, b in pairwise(data):
        print(f"  {a}-{b}")

    # Check if sorted
    nums = [1, 2, 3, 5, 4]
    is_sorted = all(a <= b for a, b in pairwise(nums))
    print(f"\nIs {nums} sorted? {is_sorted}")


# =============================================================================
# SECTION 7: PRACTICAL PROBLEMS
# =============================================================================

def generate_subsets():
    """
    Generate all subsets of a set using product.

    Each element can be either in (1) or out (0).
    """

    print("\n--- Generate All Subsets ---")

    nums = [1, 2, 3]

    # product([0,1], repeat=len(nums)) generates all combinations of 0/1
    subsets = []
    for choices in product([0, 1], repeat=len(nums)):
        subset = [nums[i] for i in range(len(nums)) if choices[i]]
        subsets.append(subset)

    print(f"Subsets of {nums}:")
    for s in subsets:
        print(f"  {s}")


def generate_all_parentheses():
    """
    Generate all valid parentheses combinations.

    Classic interview problem using product/itertools.
    """

    print("\n--- Generate Valid Parentheses ---")

    def is_valid(s):
        """Check if parentheses are balanced."""
        count = 0
        for c in s:
            if c == '(':
                count += 1
            else:
                count -= 1
            if count < 0:
                return False
        return count == 0

    n = 3  # Number of pairs
    all_paren = product('()', repeat=2*n)
    valid = [''.join(p) for p in all_paren if is_valid(p)]

    print(f"All valid parentheses for n={n}:")
    for p in valid:
        print(f"  {p}")


def coin_combinations():
    """
    Find all ways to make amount using given coins.
    """

    print("\n--- Coin Combinations ---")

    coins = [1, 2, 5]
    amount = 5

    # Generate all combinations (order doesn't matter)
    # This is a simplified version
    result = []
    for combo in combinations_with_replacement(coins, amount):
        if sum(combo) == amount:
            result.append(combo)

    print(f"Combinations of {coins} that sum to {amount}:")
    print(f"  {result}")


def sliding_window_itertools():
    """
    Create sliding window using islice.
    """

    print("\n--- Sliding Window using itertools ---")

    def sliding_window(iterable, size):
        """Generate sliding windows of given size."""
        it = iter(iterable)
        window = tuple(islice(it, size))
        if len(window) == size:
            yield window
        for item in it:
            window = window[1:] + (item,)
            yield window

    data = range(10)
    window_size = 3

    print(f"Sliding window of size {window_size} over {list(data)}:")
    for window in sliding_window(data, window_size):
        print(f"  {window}")


# =============================================================================
# SECTION 8: PERFORMANCE NOTES
# =============================================================================

def performance_demo():
    """
    Demonstrate lazy evaluation benefits.
    """

    print("\n--- Lazy Evaluation Demo ---")

    # DON'T: Create huge list
    # This would use lots of memory
    # squares = [x**2 for x in range(10**8)]

    # DO: Use generator/islice
    # This is lazy - only computes what's needed
    squares_gen = (x**2 for x in range(10**8))
    first_10 = list(islice(squares_gen, 10))
    print(f"First 10 squares (lazy): {first_10}")

    # islice with infinite iterator
    first_20_evens = list(islice(count(0, 2), 20))
    print(f"First 20 even numbers: {first_20_evens}")


# =============================================================================
# SECTION 9: TESTING AND DEMO
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("ITERTOOLS - TEST DEMO")
    print("=" * 60)

    # Section 1: Infinite iterators
    print("\n--- Section 1: Infinite Iterators ---")
    count_demo()
    cycle_demo()
    repeat_demo()

    # Section 2: Combinatoric
    print("\n--- Section 2: Combinatoric Iterators ---")
    permutations_demo()
    combinations_demo()
    combinations_with_replacement_demo()
    product_demo()

    # Section 3: Iterator slicing
    print("\n--- Section 3: Iterator Slicing ---")
    islice_demo()

    # Section 4: Chaining
    print("\n--- Section 4: Chaining ---")
    chain_demo()
    chain_from_iterable_demo()

    # Section 5: Filtering
    print("\n--- Section 5: Filtering and Accumulating ---")
    filter_demo()
    accumulate_demo()
    dropwhile_takewhile_demo()

    # Section 6: Grouping
    print("\n--- Section 6: Grouping ---")
    groupby_demo()
    pairwise_demo()

    # Section 7: Practical problems
    print("\n--- Section 7: Practical Problems ---")
    generate_subsets()
    generate_all_parentheses()
    coin_combinations()
    sliding_window_itertools()

    # Section 8: Performance
    print("\n--- Section 8: Performance ---")
    performance_demo()

    print("\n" + "=" * 60)
    print("All demos completed!")
    print("=" * 60)

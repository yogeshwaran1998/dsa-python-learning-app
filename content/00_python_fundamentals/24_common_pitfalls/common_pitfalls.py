"""
Common Python Pitfalls - Implementation and Examples
====================================================
Comprehensive examples demonstrating common Python pitfalls
and their solutions for interviews.
"""

import copy
from typing import List, Any


# =============================================================================
# SECTION 1: MUTABLE DEFAULT ARGUMENTS
# =============================================================================

"""
The Problem:
Mutable default arguments are evaluated ONCE at function definition,
not each time the function is called. This leads to shared state.

This is one of the most common Python gotchas!
"""


# WRONG - Don't do this!
def append_to(element, to=[]):
    """This function has a bug - mutable default argument."""
    to.append(element)
    return to


def mutable_default_bug():
    """Demonstrate the mutable default argument bug."""

    print("\n--- Mutable Default Argument Bug ---")

    # First call
    result1 = append_to(1)
    print(f"append_to(1): {result1}")

    # Second call - BUG! Returns [1, 2], not [2]
    result2 = append_to(2)
    print(f"append_to(2): {result2}")
    # Same list object!
    print(f"result1 is result2: {result1 is result2}")

    # Third call
    result3 = append_to(3)
    print(f"append_to(3): {result3}")


# CORRECT - Fix with None
def append_to_fixed(element, to=None):
    """Fixed version using None as default."""
    if to is None:
        to = []
    to.append(element)
    return to


def mutable_default_fixed():
    """Demonstrate the fix."""

    print("\n--- Mutable Default Fixed ---")

    result1 = append_to_fixed(1)
    print(f"append_to_fixed(1): {result1}")

    result2 = append_to_fixed(2)
    print(f"append_to_fixed(2): {result2}")

    result3 = append_to_fixed(3)
    print(f"append_to_fixed(3): {result3}")

    print(f"result1 is result2: {result1 is result2}")  # False


# Real-world example with dict
def add_to_history_bad(message, history=[]):
    """Wrong - mutable default."""
    history.append(message)
    return history


def add_to_history_good(message, history=None):
    """Correct - use None."""
    if history is None:
        history = []
    history.append(message)
    return history


# =============================================================================
# SECTION 2: SHALLOW VS DEEP COPY
# =============================================================================

"""
Understanding the difference between shallow and deep copying is crucial.
- Shallow copy: Top-level is new, but nested objects are shared
- Deep copy: Recursively copies all nested objects
"""


def shallow_copy_demo():
    """Demonstrate shallow copy."""

    print("\n--- Shallow Copy Demo ---")

    original = [[1, 2], [3, 4]]
    print(f"Original: {original}")

    # Method 1: copy()
    shallow1 = original.copy()

    # Method 2: slice
    shallow2 = original[:]

    # Method 3: list() constructor
    shallow3 = list(original)

    # Method 4: copy.copy()
    shallow4 = copy.copy(original)

    # Modify top level - doesn't affect original
    shallow1.append([5, 6])
    print(f"After appending to shallow1: {original}")  # Still [[1,2],[3,4]]

    # Modify NESTED element - affects original!
    shallow2[0][0] = 999
    print(f"After modifying nested in shallow2: {original}")
    # Original is now [[999, 2], [3, 4]]!


def deep_copy_demo():
    """Demonstrate deep copy."""

    print("\n--- Deep Copy Demo ---")

    original = [[1, 2], [3, 4]]
    print(f"Original: {original}")

    # Create deep copy
    deep = copy.deepcopy(original)

    # Modify nested element
    deep[0][0] = 999
    print(f"After modifying deep: {original}")
    print(f"Deep copy: {deep}")
    # Original unchanged!


def copy_methods_comparison():
    """Compare different copy methods."""

    print("\n--- Copy Methods Comparison ---")

    nested = [1, [2, 3], [[4, 5]]]

    # Shallow copy
    shallow = nested.copy()
    shallow[2][0] = 999
    print(f"After shallow copy modification:")
    print(f"  Original: {nested}")  # Changed!
    print(f"  Shallow: {shallow}")

    # Reset
    nested = [1, [2, 3], [[4, 5]]]

    # Deep copy
    deep = copy.deepcopy(nested)
    deep[2][0] = 999
    print(f"After deep copy modification:")
    print(f"  Original: {nested}")  # Unchanged!
    print(f"  Deep: {deep}")


# =============================================================================
# SECTION 3: GENERATOR EXHAUSTION
# =============================================================================

"""
Generators can only be iterated ONCE. After exhaustion, they're empty.
"""


def generator_exhaustion_demo():
    """Demonstrate generator exhaustion."""

    print("\n--- Generator Exhaustion Demo ---")

    gen = (x for x in range(3))

    # First iteration - works
    result1 = list(gen)
    print(f"First iteration: {result1}")

    # Second iteration - exhausted!
    result2 = list(gen)
    print(f"Second iteration: {result2}")  # Empty!


def generator_reuse_solutions():
    """Solutions for generator reuse."""

    print("\n--- Generator Reuse Solutions ---")

    # Solution 1: Convert to list
    gen = (x for x in range(3))
    gen_list = list(gen)  # Materialize

    print(f"First use: {gen_list}")
    print(f"Second use: {gen_list}")  # Works!

    # Solution 2: Make function reusable
    def squares_gen(n):
        return (x**2 for x in range(n))

    # Each call creates new generator
    sq1 = squares_gen(3)
    sq2 = squares_gen(3)

    print(f"First generator: {list(sq1)}")
    print(f"Second generator: {list(sq2)}")

    # Solution 3: Use itertools.tee (creates two iterators)
    from itertools import tee

    gen = (x for x in range(3))
    gen1, gen2 = tee(gen)

    print(f"Tee gen1: {list(gen1)}")
    print(f"Tee gen2: {list(gen2)}")


# =============================================================================
# SECTION 4: INTEGER CACHING
# =============================================================================

"""
Python caches small integers (-5 to 256) for performance.
This can cause unexpected behavior with 'is' comparisons.
"""


def integer_caching_demo():
    """Demonstrate integer caching."""

    print("\n--- Integer Caching Demo ---")

    # Small integers are cached
    a = 256
    b = 256
    print(f"256 is 256: {a is b}")  # True - cached!

    # Large integers are not cached
    a = 257
    b = 257
    print(f"257 is 257: {a is b}")  # False - not cached!

    # Integer in expressions
    a = 10 + 20
    b = 30
    print(f"10+20 is 30: {a is b}")  # May vary!

    # This affects comparisons
    a = 256
    b = 256
    print(f"\na == b: {a == b}")  # True (value)
    print(f"a is b: {a is b}")  # True (identity) - cached!


def integer_caching_issues():
    """Show where integer caching can cause issues."""

    print("\n--- Integer Caching Issues ---")

    # Using 'is' for comparison - WRONG
    # This works for small numbers by accident
    x = 256
    if x is 256:
        print("x is 256 - accidentally works!")

    # But fails for larger
    x = 257
    if x is 257:  # Almost never True!
        print("x is 257")
    else:
        print("x is 257 - FAILS! Use == instead")

    # In sets/dicts - VALUES matter, not identity
    s = set()
    s.add(256)
    s.add(256)
    print(f"\nSet with 256, 256: {len(s)} elements")  # 1

    s.add(257)
    s.add(257)
    print(f"Set with 256, 256, 257, 257: {len(s)} elements")  # 2

    # But identity doesn't matter for values
    d = {}
    d[256] = "first"
    d[256] = "second"
    print(f"Dict [256]: {d[256]}")  # Second overwrites


# =============================================================================
# SECTION 5: LATE BINDING IN CLOSURES
# =============================================================================

"""
In closures, variables are captured by reference, not value.
The value is looked up when the function is called.
"""


def late_binding_bug():
    """Demonstrate late binding in closures bug."""

    print("\n--- Late Binding Bug ---")

    # WRONG - all functions refer to same 'i'
    functions = [lambda: i for i in range(3)]

    print("Calling all functions (bug):")
    for f in functions:
        print(f"  {f()}")  # All print 2!


def late_binding_fixed():
    """Demonstrate solutions for late binding."""

    print("\n--- Late Binding Fixed ---")

    # Solution 1: Default argument captures value
    functions = [lambda x=i: x for i in range(3)]

    print("Solution 1 - Default argument:")
    for f in functions:
        print(f"  {f()}")  # 0, 1, 2

    # Solution 2: Helper function
    def make_function(i):
        return lambda: i

    functions = [make_function(i) for i in range(3)]

    print("\nSolution 2 - Helper function:")
    for f in functions:
        print(f"  {f()}")


# =============================================================================
# SECTION 6: OTHER COMMON PITFALLS
# =============================================================================

def modify_while_iterating():
    """Don't modify list while iterating."""

    print("\n--- Modify While Iterating ---")

    # WRONG - modifies while iterating
    numbers = [1, 2, 3, 4, 5]
    print(f"Original: {numbers}")

    # This can skip elements!
    for num in numbers:
        if num % 2 == 0:
            numbers.remove(num)

    print(f"After removing evens (WRONG): {numbers}")

    # CORRECT - iterate over copy
    numbers = [1, 2, 3, 4, 5]
    for num in numbers[:]:  # Slice creates copy
        if num % 2 == 0:
            numbers.remove(num)

    print(f"After removing evens (CORRECT): {numbers}")

    # Alternative - list comprehension
    numbers = [n for n in numbers if n % 2 != 0]
    print(f"Using comprehension: {numbers}")


def floating_point_comparison():
    """Floating point comparison pitfall."""

    print("\n--- Floating Point Comparison ---")

    # WRONG - don't use ==
    result = 0.1 + 0.2
    print(f"0.1 + 0.2 = {result}")
    print(f"0.1 + 0.2 == 0.3: {result == 0.3}")  # False!

    # CORRECT - use math.isclose
    import math
    print(f"math.isclose(0.1+0.2, 0.3): {math.isclose(result, 0.3)}")

    # Also useful for tolerance
    print(f"math.isclose(1.0, 1.001, rel_tol=0.01): {math.isclose(1.0, 1.001, rel_tol=0.01)}")


def forgetting_return():
    """Forgetting to return in recursion."""

    print("\n--- Forgetting Return ---")

    # WRONG - missing return
    def sum_list_wrong(lst):
        if not lst:
            return 0
        # BUG: Missing return!
        sum_list_wrong(lst[:-1])  # Result not used!
        return lst[-1]  # Only returns last element!

    print(f"sum_list_wrong([1,2,3]): {sum_list_wrong([1, 2, 3])}")

    # CORRECT
    def sum_list_correct(lst):
        if not lst:
            return 0
        return lst[0] + sum_list_correct(lst[1:])

    print(f"sum_list_correct([1,2,3]): {sum_list_correct([1, 2, 3])}")


def mutable_as_default_in_class():
    """Mutable default in class methods."""

    print("\n--- Mutable Default in Class ---")

    # WRONG
    class CounterBad:
        def __init__(self, counts=[]):
            self.counts = counts

        def add(self, name):
            self.counts.append(name)

    c1 = CounterBad()
    c1.add("Alice")
    c2 = CounterBad()
    c2.add("Bob")
    print(f"c1.counts: {c1.counts}")  # ['Alice', 'Bob'] - WRONG!
    print(f"c2.counts: {c2.counts}")  # ['Alice', 'Bob'] - WRONG!

    # CORRECT
    class CounterGood:
        def __init__(self, counts=None):
            if counts is None:
                counts = []
            self.counts = counts

        def add(self, name):
            self.counts.append(name)

    c1 = CounterGood()
    c1.add("Alice")
    c2 = CounterGood()
    c2.add("Bob")
    print(f"c1.counts: {c1.counts}")  # ['Alice']
    print(f"c2.counts: {c2.counts}")  # ['Bob']


# =============================================================================
# SECTION 7: PRACTICAL EXAMPLES
# =============================================================================

def fix_mutable_default_example():
    """Example of fixing a real-world bug."""

    print("\n--- Real World Fix Example ---")

    # BEFORE - buggy
    def process_items(items=[]):
        items.append("processed")
        return items

    print("Buggy version:")
    print(f"  First call: {process_items()}")
    print(f"  Second call: {process_items()}")

    # AFTER - fixed
    def process_items_fixed(items=None):
        if items is None:
            items = []
        items.append("processed")
        return items

    print("\nFixed version:")
    print(f"  First call: {process_items_fixed()}")
    print(f"  Second call: {process_items_fixed()}")


def copy_decision_tree():
    """Help decide which copy method to use."""

    print("\n--- Copy Decision Guide ---")

    print("""
    When to use each copy method:

    1. Simple list (no nested objects):
       - Use list() or [:] - fast and shallow is fine

    2. List with nested lists/objects:
       - Use copy.deepcopy() if you modify nested objects
       - Use list() if you only modify top level

    3. Dictionary:
       - Use .copy() for shallow
       - Use copy.deepcopy() for nested

    4. Custom objects:
       - Implement __copy__ and __deepcopy__ methods
       - Or use copy.copy() / copy.deepcopy()
    """)


# =============================================================================
# SECTION 8: TESTING AND DEMO
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("COMMON PYTHON PITFALLS - TEST DEMO")
    print("=" * 60)

    # Section 1: Mutable Default Arguments
    print("\n--- Section 1: Mutable Default Arguments ---")
    mutable_default_bug()
    mutable_default_fixed()

    # Section 2: Shallow vs Deep Copy
    print("\n--- Section 2: Shallow vs Deep Copy ---")
    shallow_copy_demo()
    deep_copy_demo()
    copy_methods_comparison()

    # Section 3: Generator Exhaustion
    print("\n--- Section 3: Generator Exhaustion ---")
    generator_exhaustion_demo()
    generator_reuse_solutions()

    # Section 4: Integer Caching
    print("\n--- Section 4: Integer Caching ---")
    integer_caching_demo()
    integer_caching_issues()

    # Section 5: Late Binding
    print("\n--- Section 5: Late Binding in Closures ---")
    late_binding_bug()
    late_binding_fixed()

    # Section 6: Other Pitfalls
    print("\n--- Section 6: Other Common Pitfalls ---")
    modify_while_iterating()
    floating_point_comparison()
    forgetting_return()
    mutable_as_default_in_class()

    # Section 7: Practical Examples
    print("\n--- Section 7: Practical Examples ---")
    fix_mutable_default_example()
    copy_decision_tree()

    print("\n" + "=" * 60)
    print("All demos completed!")
    print("=" * 60)

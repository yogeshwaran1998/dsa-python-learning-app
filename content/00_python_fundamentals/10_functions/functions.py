"""
Functions - Implementation and Examples
=======================================
Comprehensive Python implementations covering *args, **kwargs, default arguments,
mutable default pitfalls, lambda functions, and decorators. Practical for interviews.
"""

from typing import List, Callable, Any, Dict, Optional
import functools
import time
from functools import lru_cache


# =============================================================================
# SECTION 1: *ARGS - VARIABLE POSITIONAL ARGUMENTS
# =============================================================================

def args_basic():
    """
    *args allows a function to accept any number of positional arguments.
    These arguments are packed into a tuple.

    Time Complexity: O(n) where n is the number of arguments
    Space Complexity: O(n) for storing the tuple
    """
    # Example 1: Function that accepts variable arguments
    def sum_all(*args):
        """
        Sum all provided arguments.

        Args:
            *args: Variable number of arguments to sum

        Returns:
            Sum of all arguments
        """
        total = 0
        for num in args:
            total += num
        return total

    print(f"Sum 1,2,3: {sum_all(1, 2, 3)}")
    print(f"Sum 1-10: {sum_all(*range(1, 11))}")  # Can unpack with *
    print(f"Sum single: {sum_all(42)}")
    print(f"Sum none: {sum_all()}")

    # Example 2: Find maximum of variable arguments
    def find_max(*args):
        """Find maximum among all arguments."""
        if not args:
            return None
        return max(args)

    print(f"Max of 3,7,2,9: {find_max(3, 7, 2, 9)}")

    # Example 3: Accept any type
    def print_all(*args):
        """Print all arguments with their types."""
        for i, arg in enumerate(args):
            print(f"  [{i}] {arg} (type: {type(arg).__name__})")

    print("Mixed types:")
    print_all(1, "hello", 3.14, [1, 2], {"key": "value"})

    # Example 4: Combining regular and *args
    def greet_names(greeting, *names):
        """Greet each name with the given greeting."""
        return [f"{greeting}, {name}!" for name in names]

    greetings = greet_names("Hello", "Alice", "Bob", "Charlie")
    print(greetings)

    # Example 5: *args with type checking
    def sum_only_numbers(*args):
        """Sum only numeric arguments."""
        total = 0
        for arg in args:
            if isinstance(arg, (int, float)):
                total += arg
        return total

    print(f"Sum mixed (1,'a',2,'b',3): {sum_only_numbers(1, 'a', 2, 'b', 3)}")

    return sum_all, find_max, print_all, greet_names, sum_only_numbers


def args_practice():
    """
    Practice problems with *args.
    """
    # Problem 1: Average of numbers
    def average(*args):
        """Calculate average of numbers."""
        if not args:
            return 0
        return sum(args) / len(args)

    print(f"Average of 1,2,3,4,5: {average(1, 2, 3, 4, 5)}")

    # Problem 2: Count specific type
    def count_type(data_type, *args):
        """Count arguments of specific type."""
        return sum(1 for arg in args if isinstance(arg, data_type))

    print(f"Count strings in (1,'a',2,'b',3,'c'): {count_type(str, 1, 'a', 2, 'b', 3, 'c')}")

    # Problem 3: Concatenate with separator
    def join_with(separator, *args):
        """Join arguments with separator."""
        return separator.join(str(arg) for arg in args)

    print(f"Join with '-': {join_with('-', 'a', 'b', 'c')}")

    return average, count_type, join_with


# =============================================================================
# SECTION 2: **KWARGS - VARIABLE KEYWORD ARGUMENTS
# =============================================================================

def kwargs_basic():
    """
    **kwargs allows a function to accept any number of keyword arguments.
    These arguments are packed into a dictionary.

    Time Complexity: O(n) where n is the number of keyword arguments
    Space Complexity: O(n) for storing the dictionary
    """
    # Example 1: Print keyword arguments
    def print_info(**kwargs):
        """Print all keyword arguments."""
        for key, value in kwargs.items():
            print(f"  {key}: {value}")

    print("User info:")
    print_info(name="Alice", age=30, city="NYC")

    # Example 2: Build configuration
    def create_server(**config):
        """Create server config with defaults."""
        defaults = {
            'host': 'localhost',
            'port': 8080,
            'debug': False,
            'max_connections': 100
        }
        # Update defaults with provided config
        defaults.update(config)
        return defaults

    server1 = create_server()
    server2 = create_server(port=9000, debug=True)

    print(f"Default config: {server1}")
    print(f"Custom config: {server2}")

    # Example 3: Combining *args and **kwargs
    def flexible_func(required, *args, **kwargs):
        """Function with required, optional positional, and keyword args."""
        print(f"Required: {required}")
        print(f"Args: {args}")
        print(f"Kwargs: {kwargs}")

    flexible_func("mandatory", 1, 2, 3, name="Bob", age=25)

    # Example 4: Pass kwargs to another function
    def inner(a, b, c):
        return a + b + c

    def outer(a, b, c, **kwargs):
        # Pass keyword arguments to inner
        return inner(a, b=b, c=c)

    print(f"Outer call: {outer(1, b=2, c=3)}")

    # Example 5: Type-safe kwargs
    def create_person(**kwargs):
        """Create person with type validation."""
        name = kwargs.get('name', '')
        age = kwargs.get('age', 0)
        return {"name": name, "age": age}

    person = create_person(name="Alice", age=30)
    print(f"Person: {person}")

    return print_info, create_server, flexible_func, outer, create_person


def kwargs_practice():
    """
    Practice problems with **kwargs.
    """
    # Problem 1: Count occurrences using kwargs
    def count_values(**kwargs):
        """Count total number of keyword arguments."""
        return len(kwargs)

    print(f"Count 4 kwargs: {count_values(a=1, b=2, c=3, d=4)}")

    # Problem 2: Filter numeric kwargs
    def filter_numeric(**kwargs):
        """Return only numeric keyword arguments."""
        return {k: v for k, v in kwargs.items() if isinstance(v, (int, float))}

    result = filter_numeric(name="Alice", age=30, city="NYC", score=95.5)
    print(f"Numeric kwargs: {result}")

    # Problem 3: Create object from kwargs
    class Person:
        def __init__(self, **kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)

        def __repr__(self):
            return f"Person({self.__dict__})"

    p = Person(name="Bob", age=25, city="LA")
    print(f"Person object: {p}")

    return count_values, filter_numeric, Person


# =============================================================================
# SECTION 3: DEFAULT ARGUMENTS
# =============================================================================

def default_args_basic():
    """
    Default arguments allow specifying default values for parameters.
    Default values are evaluated ONCE when function is defined.
    """
    # Example 1: Simple default arguments
    def greet(name, greeting="Hello"):
        """Greet with optional custom greeting."""
        return f"{greeting}, {name}!"

    print(greet("Alice"))         # Uses default "Hello"
    print(greet("Bob", "Hi"))     # Uses custom "Hi"

    # Example 2: Multiple defaults
    def power(base, exponent=2, verbose=True):
        """Calculate base raised to exponent."""
        result = base ** exponent
        if verbose:
            print(f"{base} ^ {exponent} = {result}")
        return result

    power(3)           # 3^2 = 9
    power(3, 3)        # 3^3 = 27
    power(3, 3, False) # 27 (no print)

    # Example 3: Mutable objects as defaults - THE PITFALL!
    # This is a common interview trap!

    # WRONG - Don't do this!
    def append_to_wrong(element, to=[]):
        """Incorrect: mutable default argument."""
        to.append(element)
        return to

    result1 = append_to_wrong(1)
    result2 = append_to_wrong(2)

    print(f"Wrong: First call returns {result1}")
    print(f"Wrong: Second call returns {result2}")  # [1, 2] - BUG!

    # CORRECT - Use None
    def append_to_correct(element, to=None):
        """Correct: None as default, create new list inside."""
        if to is None:
            to = []
        to.append(element)
        return to

    result1 = append_to_correct(1)
    result2 = append_to_correct(2)

    print(f"Correct: First call returns {result1}")
    print(f"Correct: Second call returns {result2}")  # [2] - Correct!

    return greet, power, append_to_wrong, append_to_correct


def mutable_default_pitfall():
    """
    Detailed explanation of the mutable default argument pitfall.
    This is a CRITICAL topic for interviews!
    """
    print("=" * 60)
    print("MUTABLE DEFAULT ARGUMENT PITFALL - CRITICAL!")
    print("=" * 60)

    # The problem in detail
    def bad_function(data=[]):
        """This is dangerous!"""
        data.append(len(data))
        return data

    # Each call shares the SAME list object
    print("\nCalling bad_function() three times:")
    print(f"  1st call: {bad_function()}")
    print(f"  2nd call: {bad_function()}")
    print(f"  3rd call: {bad_function()}")

    # Why? Because default value [] is created ONCE at function definition
    # All calls use the SAME list object

    # The fix
    def good_function(data=None):
        """Correct way - create new list each call."""
        if data is None:
            data = []
        data.append(len(data))
        return data

    print("\nCalling good_function() three times:")
    print(f"  1st call: {good_function()}")
    print(f"  2nd call: {good_function()}")
    print(f"  3rd call: {good_function()}")

    # This applies to ANY mutable default:
    # - list []
    # - dict {}
    # - set set()
    # - class instances

    return bad_function, good_function


# =============================================================================
# SECTION 4: LAMBDA FUNCTIONS
# =============================================================================

def lambda_basic():
    """
    Lambda functions are anonymous functions defined with 'lambda' keyword.
    Syntax: lambda arguments: expression

    Can have multiple arguments but only ONE expression.
    """
    # Example 1: Simple lambda
    square = lambda x: x ** 2
    print(f"square(5): {square(5)}")

    # Example 2: Lambda with multiple arguments
    add = lambda x, y: x + y
    print(f"add(3, 4): {add(3, 4)}")

    # Example 3: Lambda with conditional
    abs_val = lambda x: x if x >= 0 else -x
    print(f"abs_val(-5): {abs_val(-5)}")

    # Example 4: Lambda with multiple expressions - NOT ALLOWED!
    # This would be a syntax error:
    # lambda x: (print(x), x**2)[1]

    # Example 5: Returning tuples
    get_stats = lambda x: (x, x**2, x**3)
    print(f"get_stats(3): {get_stats(3)}")

    # Example 6: Lambda in sorted()
    names = ["Charlie", "Alice", "Bob"]
    sorted_by_length = sorted(names, key=lambda x: len(x))
    print(f"Sorted by length: {sorted_by_length}")

    return square, add, abs_val, get_stats, sorted_by_length


def lambda_with_builtins():
    """
    Using lambda with built-in functions.
    """
    # Example 1: map() with lambda
    numbers = [1, 2, 3, 4, 5]
    squares = list(map(lambda x: x ** 2, numbers))
    print(f"Map squares: {squares}")

    # Example 2: filter() with lambda
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Filter evens: {evens}")

    # Example 3: sorted() with lambda
    people = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35}
    ]
    sorted_by_age = sorted(people, key=lambda x: x["age"])
    print(f"Sorted by age: {sorted_by_age}")

    # Example 4: max() with lambda
    longest = max(people, key=lambda x: len(x["name"]))
    print(f"Longest name: {longest}")

    # Example 5: reduce() with lambda
    from functools import reduce
    product = reduce(lambda acc, x: acc * x, numbers)
    print(f"Product: {product}")

    return squares, evens, sorted_by_age, longest, product


def lambda_vs_def():
    """
    When to use lambda vs regular function.
    """
    # Use lambda for:
    # - Short, simple functions
    # - One-time use
    # - Callbacks

    # Use def for:
    # - Complex logic
    # - Documentation (docstrings)
    # - Reusability
    # - Multiple statements

    # Example: Same functionality
    # Lambda version
    square_lambda = lambda x: x ** 2

    # Regular function version
    def square_def(x):
        """Return the square of x."""
        return x ** 2

    print(f"Lambda: {square_lambda(5)}")
    print(f"Function: {square_def(5)}")

    # When lambda is appropriate:
    # - In sorted(), map(), filter() etc.
    key_func = lambda x: x * -1
    sorted_desc = sorted([3, 1, 4, 1, 5], key=key_func)
    print(f"Sorted desc: {sorted_desc}")

    # When lambda should be avoided:
    # - Complex logic
    # - Long functions
    # - Functions needing docstrings

    return square_lambda, square_def, sorted_desc


# =============================================================================
# SECTION 5: DECORATORS - BASIC
# =============================================================================

def decorators_basic():
    """
    Decorators wrap functions to add functionality without modifying them.

    A decorator is a function that takes a function and returns a new function.
    """
    # Example 1: Basic decorator
    def my_decorator(func):
        """Decorator that adds printing before and after."""
        def wrapper(*args, **kwargs):
            print("Before calling the function")
            result = func(*args, **kwargs)
            print("After calling the function")
            return result
        return wrapper

    @my_decorator
    def say_hello():
        print("Hello!")

    say_hello()

    # Example 2: Decorator that modifies return value
    def add_exclamation(func):
        """Add exclamation to return value."""
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, str):
                return result + "!"
            return result
        return wrapper

    @add_exclamation
    def get_greeting(name):
        return f"Hello, {name}"

    print(get_greeting("Alice"))

    # Example 3: Preserving function metadata
    def timer_decorator(func):
        """Decorator that measures execution time."""
        @functools.wraps(func)  # Preserves original function's metadata
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"{func.__name__} took {end - start:.4f} seconds")
            return result
        return wrapper

    @timer_decorator
    def slow_function():
        time.sleep(0.1)
        return "Done"

    slow_function()
    print(f"Function name: {slow_function.__name__}")  # Preserved!

    return my_decorator, add_exclamation, timer_decorator


def decorator_with_arguments():
    """
    Decorators that accept arguments.
    """
    # To add arguments to a decorator, we need an extra layer
    def repeat(times):
        """Decorator that calls function multiple times."""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                for _ in range(times):
                    result = func(*args, **kwargs)
                return result
            return wrapper
        return decorator

    @repeat(times=3)
    def greet(name):
        print(f"Hello, {name}!")

    print("Calling greet 3 times:")
    greet("Alice")

    # Example: Conditional logging
    def log_level(level):
        """Decorator that logs based on level."""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(f"[{level.upper()}] Calling {func.__name__}")
                return func(*args, **kwargs)
            return wrapper
        return decorator

    @log_level("debug")
    def process():
        return "processed"

    print(process())

    return repeat, log_level


# =============================================================================
# SECTION 6: @LRU_CACHE DECORATOR
# =============================================================================

def lru_cache_examples():
    """
    @lru_cache (Least Recently Used Cache) caches function results.
    Very useful for optimization and recursive functions!

    Time Complexity: O(1) for cached lookups
    Space Complexity: O(n) where n is cache size
    """
    # Example 1: Fibonacci without cache (exponential time!)
    def fib_slow(n):
        """Slow Fibonacci without caching."""
        if n < 2:
            return n
        return fib_slow(n - 1) + fib_slow(n - 2)

    # Example 2: Fibonacci with lru_cache
    @lru_cache(maxsize=None)
    def fib_fast(n):
        """Fast Fibonacci with memoization."""
        if n < 2:
            return n
        return fib_fast(n - 1) + fib_fast(n - 2)

    # Test performance
    import time

    # Slow version - only test small n
    start = time.time()
    # fib_slow(30) would take too long, so we'll skip it

    # Fast version - much better!
    start = time.time()
    result = fib_fast(100)
    print(f"Fib(100): {result}")
    print(f"Time: {time.time() - start:.6f}s")

    # Cache info
    print(f"Cache info: {fib_fast.cache_info()}")

    # Example 3: Custom function with caching
    @lru_cache(maxsize=128)
    def expensive_computation(x, y):
        """Simulate expensive computation."""
        time.sleep(0.1)  # Simulate work
        return x ** y

    print("\nFirst call (slow):")
    start = time.time()
    result = expensive_computation(2, 10)
    print(f"Result: {result}, Time: {time.time() - start:.4f}s")

    print("\nSecond call (fast - cached):")
    start = time.time()
    result = expensive_computation(2, 10)
    print(f"Result: {result}, Time: {time.time() - start:.4f}s")

    print(f"Cache info: {expensive_computation.cache_info()}")

    # Example 4: Clear cache
    fib_fast.cache_clear()
    print(f"Cache after clear: {fib_fast.cache_info()}")

    return fib_slow, fib_fast, expensive_computation


def custom_memoization():
    """
    Custom memoization (caching) implementation.
    """
    # Simple memoization decorator
    def memoize(func):
        """Custom memoization decorator."""
        cache = {}

        @functools.wraps(func)
        def wrapper(*args):
            if args not in cache:
                cache[args] = func(*args)
            return cache[args]
        return wrapper

    # Example: Memoized factorial
    @memoize
    def factorial(n):
        """Memoized factorial."""
        if n <= 1:
            return 1
        return n * factorial(n - 1)

    print(f"Factorial(10): {factorial(10)}")
    print(f"Factorial(20): {factorial(20)}")

    # Example: Memoized recursive function
    @memoize
    def count_ways(n):
        """Count ways to climb n steps (1 or 2 at a time)."""
        if n <= 1:
            return 1
        return count_ways(n - 1) + count_ways(n - 2)

    print(f"Ways to climb 10 steps: {count_ways(10)}")

    return memoize, factorial, count_ways


# =============================================================================
# SECTION 7: PRACTICAL DECORATOR PATTERNS
# =============================================================================

def practical_decorators():
    """
    Practical decorators for interviews.
    """
    # Pattern 1: Timer decorator
    def timer(func):
        """Measure function execution time."""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            elapsed = time.time() - start
            print(f"{func.__name__}: {elapsed:.4f}s")
            return result
        return wrapper

    # Pattern 2: Debug decorator
    def debug(func):
        """Print function arguments and return value."""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            args_str = ", ".join(repr(a) for a in args)
            kwargs_str = ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
            print(f"Calling {func.__name__}({args_str}, {kwargs_str})")
            result = func(*args, **kwargs)
            print(f"{func.__name__} returned {result!r}")
            return result
        return wrapper

    # Pattern 3: Validation decorator
    def validate_positive(*param_names):
        """Validate that specified parameters are positive."""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                # Get parameter names and values
                import inspect
                sig = inspect.signature(func)
                params = sig.parameters

                # Check positional args
                for i, arg in enumerate(args):
                    param_name = list(params.keys())[i]
                    if param_name in param_names and arg <= 0:
                        raise ValueError(f"{param_name} must be positive, got {arg}")

                # Check keyword args
                for name in param_names:
                    if name in kwargs and kwargs[name] <= 0:
                        raise ValueError(f"{name} must be positive, got {kwargs[name]}")

                return func(*args, **kwargs)
            return wrapper
        return decorator

    # Pattern 4: Retry decorator
    def retry(max_attempts=3, delay=1):
        """Retry function on failure."""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                import random
                for attempt in range(max_attempts):
                    try:
                        return func(*args, **kwargs)
                    except Exception as e:
                        if attempt == max_attempts - 1:
                            raise
                        print(f"Attempt {attempt + 1} failed: {e}, retrying...")
                        time.sleep(delay * (attempt + 1))
            return wrapper
        return decorator

    # Example usage
    @timer
    def compute():
        time.sleep(0.05)
        return "computed"

    @debug
    def add(a, b):
        return a + b

    @validate_positive("n")
    def factorial_positive(n):
        if n <= 1:
            return 1
        return n * factorial_positive(n - 1)

    print("Timer example:")
    compute()

    print("\nDebug example:")
    add(3, 5)

    print("\nValidation example:")
    # factorial_positive(-1)  # Would raise ValueError

    return timer, debug, validate_positive, retry


# =============================================================================
# SECTION 8: CLOSURES
# =============================================================================

def closures_examples():
    """
    Closures - functions that capture variables from their outer scope.
    Decorators rely on closures!
    """
    # Example 1: Simple closure
    def outer(x):
        def inner(y):
            return x + y
        return inner

    closure = outer(10)
    print(f"outer(10)(5): {closure(5)}")  # 15
    print(f"outer(10)(20): {closure(20)}")  # 30

    # Example 2: Closure with mutable state
    def counter():
        count = 0

        def increment():
            nonlocal count  # Required to modify outer variable
            count += 1
            return count

        return increment

    c = counter()
    print(f"Count: {c()}")  # 1
    print(f"Count: {c()}")  # 2
    print(f"Count: {c()}")  # 3

    # Example 3: Closure with multiple variables
    def make_multiplier(factor):
        def multiplier(x):
            return x * factor
        return multiplier

    double = make_multiplier(2)
    triple = make_multiplier(3)

    print(f"double(5): {double(5)}")  # 10
    print(f"triple(5): {triple(5)}")  # 15

    # Example 4: Practical closure - function factory
    def make_greeter(greeting):
        def greeter(name):
            return f"{greeting}, {name}!"
        return greeter

    hello = make_greeter("Hello")
    hi = make_greeter("Hi")
    hey = make_greeter("Hey")

    print(hello("Alice"))
    print(hi("Bob"))
    print(hey("Charlie"))

    return outer, counter, make_multiplier, make_greeter


# =============================================================================
# SECTION 9: TESTING AND DEMO
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("FUNCTIONS - TEST DEMO")
    print("=" * 60)

    # Section 1: *args
    print("\n--- *args Examples ---")
    args_basic()
    args_practice()

    # Section 2: **kwargs
    print("\n--- **kwargs Examples ---")
    kwargs_basic()
    kwargs_practice()

    # Section 3: Default Arguments
    print("\n--- Default Arguments ---")
    default_args_basic()
    mutable_default_pitfall()

    # Section 4: Lambda Functions
    print("\n--- Lambda Functions ---")
    lambda_basic()
    lambda_with_builtins()
    lambda_vs_def()

    # Section 5: Basic Decorators
    print("\n--- Decorators ---")
    decorators_basic()
    decorator_with_arguments()

    # Section 6: @lru_cache
    print("\n--- @lru_cache ---")
    lru_cache_examples()
    custom_memoization()

    # Section 7: Practical Decorators
    print("\n--- Practical Decorators ---")
    practical_decorators()

    # Section 8: Closures
    print("\n--- Closures ---")
    closures_examples()

    print("\n" + "=" * 60)
    print("All tests completed!")
    print("=" * 60)

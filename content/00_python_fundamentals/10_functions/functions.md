# Functions - Theory Guide

## Table of Contents
1. [Args and Kwargs](#args-and-kwargs)
2. [Default Arguments](#default-arguments)
3. [Mutable Default Argument Pitfall](#mutable-default-argument-pitfall)
4. [Lambda Functions](#lambda-functions)
5. [Decorators](#decorators)
6. [The @lru_cache Decorator](#the-lru_cache-decorator)
7. [Interview Tips](#interview-tips)

---

## Args and Kwargs

### What are *args and **kwargs?
- `*args`: Variable number of positional arguments (tuple)
- `**kwargs`: Variable number of keyword arguments (dictionary)

### When to Use
- When you don't know how many arguments will be passed
- For wrapper functions that pass arguments to other functions
- For function overloading (simulated in Python)

### Examples

**Using *args:**
```python
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

sum_all(1, 2, 3)       # 6
sum_all(1, 2, 3, 4, 5) # 15
```

**Using **kwargs:**
```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="NYC")
# name: Alice
# age: 30
# city: NYC
```

**Combining both:**
```python
def func(*args, **kwargs):
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

func(1, 2, 3, name="Bob", age=25)
# Args: (1, 2, 3)
# Kwargs: {'name': 'Bob', 'age': 25}
```

---

## Default Arguments

### What are Default Arguments?
Default arguments allow parameters to have default values. They must come after non-default parameters.

### Rules
1. Default arguments must come after non-default arguments
2. Default values are evaluated once at function definition
3. Default values are shared across calls

### Examples

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Alice")         # "Hello, Alice!"
greet("Bob", "Hi")    # "Hi, Bob!"
```

---

## Mutable Default Argument Pitfall

### The Danger
Using mutable default arguments (list, dict) can cause unexpected behavior because the default is evaluated once, not each call.

### The Problem
```python
def append_to(element, to=[]):
    to.append(element)
    return to

append_to(1)  # Returns [1]
append_to(2)  # Returns [1, 2] - NOT [2]!
```

### Why This Happens
- Default value is created once when function is defined
- All calls share the same list object

### The Fix
```python
# Use None as default and create new list inside
def append_to(element, to=None):
    if to is None:
        to = []
    to.append(element)
    return to

append_to(1)  # Returns [1]
append_to(2)  # Returns [2] - Correct!
```

### Interview Critical Point
This is a common interview trap! Always use None for mutable defaults.

---

## Lambda Functions

### What is a Lambda?
A lambda is an anonymous function defined with the `lambda` keyword. It can have any number of arguments but only one expression.

### Syntax
```python
lambda arguments: expression
```

### When to Use
- Short, simple functions
- Callbacks and higher-order functions
- One-time use functions

### Examples

**Basic lambda:**
```python
square = lambda x: x ** 2
square(5)  # 25
```

**Multiple arguments:**
```python
add = lambda x, y: x + y
add(3, 4)  # 7
```

**With built-in functions:**
```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
```

### Lambda vs Regular Function

```python
# Lambda
square = lambda x: x ** 2

# Equivalent regular function
def square(x):
    return x ** 2
```

### Limitations
- Can only contain expressions (no statements)
- Cannot have docstrings
- Not recommended for complex functions

---

## Decorators

### What is a Decorator?
A decorator is a function that wraps another function to extend its behavior without modifying its code.

### Syntax
```python
@decorator_name
def function_to_decorate():
    pass
```

### Creating a Basic Decorator
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function")
        result = func(*args, **kwargs)
        print("After function")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
```

### Why Use Decorators?
- Add logging
- Measure execution time
- Authentication/authorization
- Caching
- Rate limiting

### Preserving Function Metadata
Use `functools.wraps` to preserve the original function's metadata.

```python
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

---

## The @lru_cache Decorator

### What is @lru_cache?
`@lru_cache` (Least Recently Used Cache) from functools caches function results to avoid redundant computations.

### Syntax
```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
```

### Parameters
- `maxsize`: Maximum number of results to cache (default 128)
- `None`: Unlimited cache

### Examples

**Fibonacci with caching:**
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

fib(100)  # Instant with cache!
```

**Common Interview Use Cases**
- Dynamic programming problems
- Expensive computations
- Repeated lookups

### Clear Cache
```python
fib.cache_clear()    # Clear all cached values
fib.cache_info()    # Show cache info (hits, misses, size)
```

### Other Built-in Decorators
- `@staticmethod`: Static method
- `@classmethod`: Class method
- `@property`: Property decorator

---

## Common Interview Patterns

### 1. Flexible Function Parameters
```python
def make_divider(divisor):
    return lambda x: x / divisor

divide_by_2 = make_divider(2)
divide_by_5 = make_divider(5)
```

### 2. Decorator for Timing
```python
import time
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.4f}s")
        return result
    return wrapper
```

### 3. Decorator for Validation
```python
def validate_positive(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError("Negative value not allowed")
        return func(*args, **kwargs)
    return wrapper
```

### 4. Memoization (Custom Cache)
```python
def memoize(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper
```

---

## Interview Tips

### Key Concepts to Know
1. **Mutable default arguments** - CRITICAL!
2. Difference between `*args` and `**kwargs`
3. How decorators work
4. When to use lambda vs regular function
5. How @lru_cache works

### Common Questions
1. "What is the output of this code with mutable default?"
2. "How would you implement a decorator?"
3. "What's the difference between args and kwargs?"
4. "How does memoization help with time complexity?"

### Mistakes to Avoid
1. Using mutable default arguments (use None)
2. Forgetting `@functools.wraps`
3. Using lambda for complex functions
4. Not understanding closure scope

---

## Summary

| Concept | Key Point |
|---------|-----------|
| *args | Variable positional arguments (tuple) |
| **kwargs | Variable keyword arguments (dict) |
| Default args | Evaluated once at definition |
| Mutable default | Use None instead |
| Lambda | Anonymous function, single expression |
| Decorator | Wraps function to extend behavior |
| @lru_cache | Caches function results |

---

## Practice Problems

### Easy
- [x] Write function with *args that sums all arguments
- [x] Write function with **kwargs that prints all key-value pairs
- [x] Create lambda for addition
- [x] Use @lru_cache for factorial

### Medium
- [x] Implement decorator that logs function calls
- [x] Fix mutable default argument bug
- [x] Create decorator with parameters
- [x] Implement custom memoization

### Hard
- [x] Create decorator that retries on failure
- [x] Implement class-based decorator
- [x] Create decorator for rate limiting
- [x] Chain multiple decorators

# Dictionaries - Theory Guide

## Table of Contents
1. [Dictionary Creation](#dictionary-creation)
2. [Accessing Values](#accessing-values)
3. [The .get() Method](#the-get-method)
4. [Dictionary Iteration](#dictionary-iteration)
5. [defaultdict](#defaultdict)
6. [Counter](#counter)
7. [Interview Tips](#interview-tips)

---

## Dictionary Creation

### Basic Creation
```python
# Empty dictionary
empty = {}
empty2 = dict()

# With key-value pairs
person = {"name": "Alice", "age": 30, "city": "NYC"}

# Using dict() constructor
from_tuples = dict([("a", 1), ("b", 2)])
from_kwargs = dict(name="Alice", age=30)

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### Keys and Values
- Keys must be immutable (str, int, tuple, etc.)
- Values can be any type
- Keys must be unique

---

## Accessing Values

### Direct Access
```python
person = {"name": "Alice", "age": 30}

# Using key (raises KeyError if not found)
name = person["name"]       # "Alice"
# person["unknown"]         # KeyError!

# Check before access
if "name" in person:
    name = person["name"]
```

### Adding and Updating
```python
d = {}
d["key"] = "value"          # Add new key-value
d["key"] = "new_value"      # Update existing
d.update({"a": 1, "b": 2})  # Add multiple
```

### Removing
```python
d = {"a": 1, "b": 2}

value = d.pop("a")          # Remove and return: returns 1
del d["b"]                   # Remove without returning
d.clear()                   # Remove all
```

---

## The .get() Method

### Syntax
```python
d.get(key)              # Returns None if key not found
d.get(key, default)    # Returns default if key not found
```

### Examples
```python
person = {"name": "Alice"}

name = person.get("name")           # "Alice"
age = person.get("age")             # None
age = person.get("age", 0)          # 0 (default)

# Practical use: counting with get
counts = {}
for char in "hello":
    counts[char] = counts.get(char, 0) + 1
# Result: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

---

## Dictionary Iteration

### Iterate Over Keys
```python
d = {"a": 1, "b": 2, "c": 3}

for key in d:
    print(key)       # a, b, c (default)
```

### Iterate Over Values
```python
for value in d.values():
    print(value)     # 1, 2, 3
```

### Iterate Over Items
```python
for key, value in d.items():
    print(f"{key}: {value}")  # a: 1, b: 2, c: 3
```

### Enumerate with Dictionary
```python
for i, (key, value) in enumerate(d.items()):
    print(i, key, value)
```

---

## defaultdict

### What is defaultdict?
A dictionary that provides default values for missing keys.

### Import
```python
from collections import defaultdict
```

### Usage
```python
from collections import defaultdict

# Default value of 0 for missing keys
counts = defaultdict(int)
counts["a"] += 1           # No error, initializes to 0 first
# Result: {'a': 1}

# Default value of empty list
groups = defaultdict(list)
groups["vowels"].append("a")
groups["vowels"].append("e")
# Result: {'vowels': ['a', 'e']}

# Default value with lambda
custom = defaultdict(lambda: "N/A")
print(custom["missing"])   # "N/A"
```

### Common Use Cases
```python
# Grouping by key
from collections import defaultdict

words = ["apple", "banana", "apricot", "blueberry"]
by_first = defaultdict(list)

for word in words:
    by_first[word[0]].append(word)
# {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry']}

# Counting
text = "hello world"
char_count = defaultdict(int)
for char in text:
    if char != " ":
        char_count[char] += 1
```

---

## Counter

### What is Counter?
A specialized dictionary for counting hashable objects.

### Import
```python
from collections import Counter
```

### Basic Usage
```python
# From iterable
counts = Counter("hello world")
# Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# From dictionary
c = Counter({"a": 4, "b": 2})
# Counter({'a': 4, 'b': 2})

# From keyword arguments
c = Counter(a=4, b=2)
```

### Counter Methods
```python
c = Counter("abracadabra")

c.most_common(3)       # Top 3: [('a', 5), ('b', 2), ('r', 2)]
c.elements()           # Iterator: 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'r', 'r', 'c', 'd'
list(c.elements())     # ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'r', 'r', 'c', 'd']

# Arithmetic operations
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)
c1 + c2                 # Counter({'a': 4, 'b': 3})
c1 - c2                 # Counter({'a': 2}) - only positives kept
c1 & c2                 # Counter({'a': 1, 'b': 1}) - min
c1 | c2                 # Counter({'a': 3, 'b': 2}) - max
```

### Practical Examples
```python
# Word frequency
text = "the quick brown fox jumps over the lazy dog"
words = text.split()
word_counts = Counter(words)
# Counter({'the': 2, 'quick': 1, 'brown': 1, ...})

# Find most common word
most_common_word = word_counts.most_common(1)[0][0]

# Intersection of two Counters
list1 = [1, 2, 2, 2, 3]
list2 = [2, 2, 3, 4]
common = Counter(list1) & Counter(list2)
# Counter({2: 2, 3: 1})
```

---

## Interview Tips

### Time Complexity

| Operation | Average | Worst |
|-----------|---------|-------|
| Access by key | O(1) | O(n) |
| Insert/Update | O(1) | O(n) |
| Delete | O(1) | O(n) |
| Search | O(1) | O(n) |

*Worst case is rare with Python's hash table

### Common Patterns

1. **Two Sum using dict**
```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
```

2. **Grouping**
```python
from collections import defaultdict
groups = defaultdict(list)
for item in items:
    groups[key_func(item)].append(item)
```

3. **Frequency counting**
```python
from collections import Counter
counts = Counter(array)
```

### Key Takeaways
- Use .get() to avoid KeyError
- defaultdict simplifies counting and grouping
- Counter provides powerful counting utilities
- Dictionaries maintain insertion order (Python 3.7+)
- Keys must be hashable/immutable

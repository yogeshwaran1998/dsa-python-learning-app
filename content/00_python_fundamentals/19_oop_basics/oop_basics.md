# Object-Oriented Programming (OOP) Basics - Theory Guide

## Table of Contents
1. [Introduction to OOP](#introduction-to-oop)
2. [Classes and Objects](#classes-and-objects)
3. [The __init__ Method](#the-__init__-method)
4. [Inheritance](#inheritance)
5. [Dunder Methods (Magic Methods)](#dunder-methods-magic-methods)
6. [Common Dunder Methods](#common-dunder-methods)
7. [Best Practices](#best-practices)

---

## Introduction to OOP

Object-Oriented Programming is a paradigm that organizes code into "objects" which contain data (attributes) and behavior (methods). Python is a multi-paradigm language that fully supports OOP.

### Key OOP Principles
- **Encapsulation**: Bundling data and methods that operate on that data
- **Inheritance**: Creating new classes from existing ones
- **Polymorphism**: Same interface, different implementations
- **Abstraction**: Hiding complex implementation details

---

## Classes and Objects

### What is a Class?
A class is a blueprint for creating objects. It defines:
- Attributes (variables)
- Methods (functions)

### What is an Object?
An object is an instance of a class. It has:
- State (attribute values)
- Behavior (methods)

### Class Definition Syntax

```python
class ClassName:
    # Class attribute (shared by all instances)
    class_attribute = "value"

    # Constructor - initializes the object
    def __init__(self, param1, param2):
        # Instance attributes (unique to each instance)
        self.param1 = param1
        self.param2 = param2

    # Instance method
    def method_name(self):
        return self.param1 + self.param2
```

---

## The __init__ Method

The `__init__` method is a special method (constructor) called when an object is created. It initializes the object's attributes.

### Key Points
- Called automatically when object is created
- `self` refers to the instance being created
- Can have default parameter values
- Not a true constructor (actual creation done by `__new__`)

### Examples

```python
class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

# Creating objects
person1 = Person("Alice", 30)
person2 = Person("Bob")  # age defaults to 0
```

---

## Inheritance

Inheritance allows a class (child/subclass) to inherit attributes and methods from another class (parent/superclass).

### Syntax

```python
class ParentClass:
    def __init__(self, param):
        self.param = param

    def parent_method(self):
        return "Parent method"

class ChildClass(ParentClass):  # Inherits from ParentClass
    def __init__(self, param, child_param):
        super().__init__(param)  # Call parent's __init__
        self.child_param = child_param

    def child_method(self):
        return "Child method"
```

### Types of Inheritance
1. **Single Inheritance**: One parent, one child
2. **Multiple Inheritance**: Multiple parents (use MRO - Method Resolution Order)
3. **Multilevel Inheritance**: Grandparent -> Parent -> Child
4. **Hierarchical Inheritance**: One parent, multiple children

### The super() Function
Used to call methods from parent class:
- `super().__init__()` - Call parent's constructor
- `super().parent_method()` - Call any parent method

---

## Dunder Methods (Magic Methods)

Dunder (double underscore) methods are special methods with double underscores at the beginning and end (e.g., `__init__`). They enable custom behavior with built-in Python operations.

### Why Use Dunder Methods?
- Define how objects behave with operators (+, -, ==, etc.)
- Enable use of built-in functions (len(), str(), etc.)
- Make classes work seamlessly with Python's syntax

### Common Dunder Methods

| Method | Purpose | Example Use |
|--------|---------|-------------|
| `__init__` | Initialize object | Called on creation |
| `__str__` | Human-readable string | print(obj) |
| `__repr__` | Developer string | repr(obj) |
| `__eq__` | Equality comparison (==) | obj1 == obj2 |
| `__hash__` | Hash value for dict/set | hash(obj) |
| `__lt__`, `__gt__` | Ordering (<, >) | sorted(list) |
| `__add__` | Addition (+) | obj1 + obj2 |
| `__len__` | Length | len(obj) |
| `__contains__` | Membership test | x in obj |

---

## Common Dunder Methods

### 1. Comparison Methods

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        """Equality: obj1 == obj2"""
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        """Hash for use in dict/set - must be consistent with __eq__"""
        return hash((self.x, self.y))

    def __lt__(self, other):
        """Less than: obj1 < obj2"""
        if not isinstance(other, Point):
            return NotImplemented
        return (self.x, self.y) < (other.x, other.y)

    def __le__(self, other):
        """Less than or equal: obj1 <= obj2"""
        return self == other or self < other

    def __gt__(self, other):
        """Greater than: obj1 > obj2"""
        if not isinstance(other, Point):
            return NotImplemented
        return not self <= other

    def __ge__(self, other):
        """Greater than or equal: obj1 >= obj2"""
        return not self < other
```

### Important: hash and eq

**Rule**: If two objects are equal (`__eq__` returns True), they MUST have the same hash value.

```python
# WRONG - breaks dict/set behavior
class Broken:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
        return hash(self.value * 2)  # BAD: same value can have different hashes!

# CORRECT
class Fixed:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)  # Consistent with __eq__
```

### 2. String Methods

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        """Human-readable string for end users"""
        return f"Person: {self.name}, Age: {self.age}"

    def __repr__(self):
        """Developer string - should be unambiguous"""
        return f"Person(name='{self.name}', age={self.age})"
```

### 3. Arithmetic Methods

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Addition: v1 + v2"""
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        """Multiplication: v * scalar"""
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        """Reverse multiplication: scalar * v"""
        return self.__mul__(scalar)
```

### 4. Container Methods

```python
class Stack:
    def __init__(self):
        self.items = []

    def __len__(self):
        """len(stack)"""
        return len(self.items)

    def __contains__(self, item):
        """item in stack"""
        return item in self.items

    def __getitem__(self, index):
        """stack[index]"""
        return self.items[index]
```

---

## Best Practices

### 1. Use dataclasses (Python 3.7+)

```python
from dataclasses import dataclass, field

@dataclass
class Person:
    name: str
    age: int = 0  # default value
    # Auto-generates __init__, __repr__, __eq__

    def __post_init__(self):
        """Custom initialization after auto-generated __init__"""
        if self.age < 0:
            raise ValueError("Age cannot be negative")
```

### 2. Use slots for Memory Optimization

```python
class Optimized:
    __slots__ = ['attr1', 'attr2']

    def __init__(self, a1, a2):
        self.attr1 = a1
        self.attr2 = a2
```

### 3. Return NotImplemented for Unsupported Comparisons

```python
def __eq__(self, other):
    if not isinstance(other, MyClass):
        return NotImplemented  # Let Python try reverse comparison
    return self.value == other.value
```

### 4. Consider frozen (Immutable) Classes for Sets/Dicts

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class ImmutablePoint:
    x: int
    y: int
    # Now can be used as dict key or in set
```

---

## Interview Tips

### Common OOP Interview Questions

1. **What is the difference between __str__ and __repr__?**
   - `__str__`: Informal, human-readable string
   - `__repr__`: Formal, unambiguous, can recreate object

2. **Why implement __hash__ with __eq__?**
   - Objects that compare equal must have the same hash
   - Required for correct behavior in dicts and sets

3. **What is method resolution order (MRO)?**
   - Order in which base classes are searched for methods
   - Use `ClassName.__mro__` or `ClassName.mro()` to view

4. **What is the difference between shallow and deep copy?**
   - Shallow: Copies references (nested objects share memory)
   - Deep: Recursively copies nested objects

5. **When to use __slots__?**
   - Memory optimization for many objects
   - Prevents adding arbitrary attributes

---

## Summary

| Concept | Purpose |
|---------|---------|
| Class | Blueprint for creating objects |
| `__init__` | Constructor - initialize object state |
| Inheritance | Reuse code from parent class |
| `super()` | Call parent class methods |
| `__eq__` | Define equality behavior |
| `__hash__` | Make object hashable for dict/set |
| `__lt__` | Enable sorting and ordering |
| `__str__` / `__repr__` | String representations |
| `__slots__` | Memory optimization |

---

## Practice Problems

- [x] Create a Rectangle class with area and perimeter methods
- [x] Create a Student class that can be compared by GPA
- [x] Create an Immutable class for use in a set
- [x] Implement a custom list that tracks access count
- [x] Create a decorator that adds caching to methods

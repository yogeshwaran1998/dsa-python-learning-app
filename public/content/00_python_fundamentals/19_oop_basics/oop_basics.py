"""
OOP Basics - Implementation and Examples
========================================
Comprehensive Python implementations covering classes, inheritance,
dunder methods, and OOP best practices for interviews.
"""

from typing import List, Optional, Any
from collections import defaultdict


# =============================================================================
# SECTION 1: CLASSES AND OBJECTS
# =============================================================================

class Person:
    """
    A simple class demonstrating basic class structure.

    Class vs Instance Attributes:
    - Class attributes: Shared across all instances
    - Instance attributes: Unique to each instance
    """

    # Class attribute - shared by all Person instances
    species = "Homo sapiens"

    # The __init__ method is called when creating a new instance
    # It's the constructor that initializes the object's state
    def __init__(self, name: str, age: int = 0):
        """
        Initialize a new Person object.

        Args:
            name: The person's name
            age: The person's age (defaults to 0)
        """
        # Instance attributes - unique to each object
        self.name = name
        self.age = age

    # Instance method - takes 'self' as first parameter
    def greet(self) -> str:
        """Return a greeting message."""
        return f"Hello, my name is {self.name}"

    def birthday(self) -> None:
        """Increase age by 1."""
        self.age += 1

    # Special method for string representation (for users)
    def __str__(self) -> str:
        """Return human-readable string when print() or str() is called."""
        return f"Person({self.name}, age={self.age})"

    # Special method for string representation (for developers)
    def __repr__(self) -> str:
        """Return unambiguous string for debugging."""
        return f"Person(name='{self.name}', age={self.age})"


# =============================================================================
# SECTION 2: INHERITANCE
# =============================================================================

class Animal:
    """Base class for all animals."""

    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        """Base implementation - subclasses should override."""
        return f"{self.name} makes a sound"

    def __str__(self) -> str:
        return f"Animal: {self.name}"


class Dog(Animal):
    """Dog inherits from Animal."""

    def __init__(self, name: str, breed: str = "Unknown"):
        # Call parent class constructor
        super().__init__(name)
        # Add Dog-specific attribute
        self.breed = breed

    # Override the speak method
    def speak(self) -> str:
        return f"{self.name} says woof!"

    def fetch(self) -> str:
        """Dog-specific method."""
        return f"{self.name} fetches the ball"


class Cat(Animal):
    """Cat inherits from Animal."""

    def speak(self) -> str:
        return f"{self.name} says meow!"

    def purr(self) -> str:
        return f"{self.name} purrs contentedly"


# Multiple inheritance example
class FlyingDog(Dog, Animal):
    """Inherits from both Dog and Animal (multiple inheritance)."""

    def __init__(self, name: str, breed: str):
        super().__init__(name, breed)

    def fly(self) -> str:
        return f"{self.name} soars through the air!"


# =============================================================================
# SECTION 3: DUNDER METHODS - COMPARISON
# =============================================================================

class Point:
    """
    2D Point class demonstrating comparison dunder methods.

    Key concept: If two objects are equal, they MUST have the same hash.
    """

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    # Equality comparison - defines when two Points are equal
    def __eq__(self, other: object) -> bool:
        """
        Check equality: point1 == point2

        Returns NotImplemented if comparing with non-Point object.
        This allows Python to try the reverse comparison.
        """
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    # Hash function - required if object will be used in dict/set
    # CRITICAL: Must be consistent with __eq__
    # If a == b, then hash(a) MUST == hash(b)
    def __hash__(self) -> int:
        """Return hash value for use in sets/dicts."""
        return hash((self.x, self.y))

    # Less than - enables sorting and < operator
    def __lt__(self, other: 'Point') -> bool:
        """Compare points for sorting (by x, then by y)."""
        if not isinstance(other, Point):
            return NotImplemented
        return (self.x, self.y) < (other.x, other.y)

    # Less than or equal
    def __le__(self, other: 'Point') -> bool:
        return self == other or self < other

    # Greater than
    def __gt__(self, other: 'Point') -> bool:
        return not self <= other

    # Greater than or equal
    def __ge__(self, other: 'Point') -> bool:
        return not self < other

    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Point(x={self.x}, y={self.y})"


# =============================================================================
# SECTION 4: DUNDER METHODS - ARITHMETIC
# =============================================================================

class Vector:
    """
    2D Vector demonstrating arithmetic dunder methods.
    """

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    # Addition: v1 + v2
    def __add__(self, other: 'Vector') -> 'Vector':
        """Vector addition: self + other"""
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    # Subtraction: v1 - v2
    def __sub__(self, other: 'Vector') -> 'Vector':
        """Vector subtraction: self - other"""
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)

    # Multiplication: v * scalar or scalar * v
    def __mul__(self, scalar: float) -> 'Vector':
        """Scalar multiplication: vector * scalar"""
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: float) -> 'Vector':
        """Reverse multiplication: scalar * vector"""
        return self.__mul__(scalar)

    # Unary negation: -v
    def __neg__(self) -> 'Vector':
        """Unary negation: -vector"""
        return Vector(-self.x, -self.y)

    # Absolute value: abs(v)
    def __abs__(self) -> float:
        """Magnitude of vector"""
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y})"


# =============================================================================
# SECTION 5: DUNDER METHODS - CONTAINERS
# =============================================================================

class Stack:
    """
    Stack data structure demonstrating container dunder methods.
    """

    def __init__(self):
        self._items = []

    def push(self, item: Any) -> None:
        """Add item to top of stack."""
        self._items.append(item)

    def pop(self) -> Any:
        """Remove and return top item."""
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> Any:
        """Return top item without removing."""
        if not self._items:
            raise IndexError("peek from empty stack")
        return self._items[-1]

    # Container dunder methods
    def __len__(self) -> int:
        """len(stack) returns number of items."""
        return len(self._items)

    def __getitem__(self, index: int) -> Any:
        """stack[index] - access item by index."""
        return self._items[index]

    def __contains__(self, item: Any) -> bool:
        """item in stack - membership test."""
        return item in self._items

    def __str__(self) -> str:
        return f"Stack({self._items})"

    def __repr__(self) -> str:
        return f"Stack(items={self._items!r})"


class Bag:
    """
    A multiset (bag) demonstrating more container methods.
    """

    def __init__(self):
        self._counts = defaultdict(int)

    def add(self, item: Any) -> None:
        """Add an item to the bag."""
        self._counts[item] += 1

    def remove(self, item: Any) -> None:
        """Remove one occurrence of item."""
        if self._counts[item] > 1:
            self._counts[item] -= 1
        else:
            del self._counts[item]

    def count(self, item: Any) -> int:
        """Get count of specific item."""
        return self._counts[item]

    def __len__(self) -> int:
        """Total number of items in bag."""
        return sum(self._counts.values())

    def __contains__(self, item: Any) -> bool:
        """Check if item is in bag."""
        return item in self._counts

    def __iter__(self):
        """Iterate over items (with duplicates)."""
        for item, count in self._counts.items():
            for _ in range(count):
                yield item

    def __str__(self) -> str:
        items = [f"{k}:{v}" for k, v in self._counts.items()]
        return f"Bag({', '.join(items)})"


# =============================================================================
# SECTION 6: DATA CLASSES (Python 3.7+)
# =============================================================================

from dataclasses import dataclass, field


@dataclass
class PersonDC:
    """
    Using @dataclass decorator - automatically generates:
    - __init__
    - __repr__
    - __eq__
    """
    name: str
    age: int = 0  # Default value

    def __post_init__(self):
        """Custom initialization after auto-generated __init__."""
        if self.age < 0:
            raise ValueError("Age cannot be negative")


@dataclass(frozen=True)
class ImmutablePoint:
    """
    Frozen dataclass - immutable, can be used in sets/dicts.
    """
    x: int
    y: int


@dataclass
class Student:
    """Student with custom ordering by GPA."""
    name: str
    gpa: float
    id: int

    def __lt__(self, other: 'Student') -> bool:
        """Sort by GPA (descending), then by name."""
        return (-self.gpa, self.name) < (-other.gpa, other.name)


# =============================================================================
# SECTION 7: __SLOTS__ FOR MEMORY OPTIMIZATION
# =============================================================================

class RegularClass:
    """Regular class with __dict__ - allows dynamic attributes."""
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


class SlottedClass:
    """Class with __slots__ - no __dict__, less memory."""
    __slots__ = ['a', 'b', 'c']

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


# =============================================================================
# SECTION 8: PRACTICAL EXAMPLES
# =============================================================================

class LRUCache:
    """
    LRU (Least Recently Used) Cache implementation.

    Demonstrates practical use of dunder methods with collections.
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self._cache = {}  # key -> value
        self._order = []  # Track access order

    def get(self, key: Any) -> Optional[Any]:
        """Get value and mark as recently used."""
        if key not in self._cache:
            return None
        # Move to end (most recently used)
        self._order.remove(key)
        self._order.append(key)
        return self._cache[key]

    def put(self, key: Any, value: Any) -> None:
        """Put key-value pair in cache."""
        if key in self._cache:
            # Update existing - move to end
            self._order.remove(key)
        elif len(self._cache) >= self.capacity:
            # Remove least recently used (first item)
            lru_key = self._order.pop(0)
            del self._cache[lru_key]

        self._cache[key] = value
        self._order.append(key)

    def __len__(self) -> int:
        """Number of items in cache."""
        return len(self._cache)

    def __contains__(self, key: Any) -> bool:
        """Check if key is in cache."""
        return key in self._cache

    def __str__(self) -> str:
        return f"LRUCache({self._cache})"


# =============================================================================
# SECTION 9: COMPLETE EXAMPLE - SORTABLE PRODUCT
# =============================================================================

@dataclass
class Product:
    """Product that can be sorted by price or name."""
    name: str
    price: float
    quantity: int

    @property
    def total_value(self) -> float:
        """Total value = price * quantity."""
        return self.price * self.quantity

    def __lt__(self, other: 'Product') -> bool:
        """Compare by price for sorting."""
        return self.price < other.price

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Product):
            return NotImplemented
        return (self.name, self.price, self.quantity) == \
               (other.name, other.price, other.quantity)

    def __hash__(self) -> int:
        """Hash based on immutable fields."""
        return hash((self.name, self.price, self.quantity))


# =============================================================================
# SECTION 10: TESTING AND DEMO
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("OOP BASICS - TEST DEMO")
    print("=" * 60)

    # Section 1: Classes and Objects
    print("\n--- Section 1: Classes and Objects ---")
    person = Person("Alice", 30)
    print(f"Person: {person}")
    print(f"repr: {repr(person)}")
    print(f"Greeting: {person.greet()}")
    print(f"Species (class attr): {Person.species}")

    # Section 2: Inheritance
    print("\n--- Section 2: Inheritance ---")
    dog = Dog("Buddy", "Golden Retriever")
    print(f"Dog speaks: {dog.speak()}")
    print(f"Dog fetches: {dog.fetch()}")

    cat = Cat("Whiskers")
    print(f"Cat speaks: {cat.speak()}")

    # Method Resolution Order
    print(f"\nFlyingDog MRO: {[c.__name__ for c in FlyingDog.__mro__]}")

    # Section 3: Dunder Methods - Comparison
    print("\n--- Section 3: Comparison Dunder Methods ---")
    p1 = Point(1, 2)
    p2 = Point(1, 2)
    p3 = Point(3, 4)

    print(f"p1 == p2: {p1 == p2}")  # True
    print(f"p1 == p3: {p1 == p3}")  # False
    print(f"p1 < p3: {p1 < p3}")   # True

    # Hash consistency check
    print(f"hash(p1) == hash(p2): {hash(p1) == hash(p2)}")

    # Use in set
    point_set = {p1, p2, p3}
    print(f"Set of points (should have 2): {len(point_set)}")

    # Use in dict
    point_dict = {p1: "origin vicinity", p3: "far"}
    print(f"Dict with points: {point_dict}")

    # Section 4: Dunder Methods - Arithmetic
    print("\n--- Section 4: Arithmetic Dunder Methods ---")
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    print(f"v1 + v2 = {v1 + v2}")
    print(f"v1 * 3 = {v1 * 3}")
    print(f"3 * v1 = {3 * v1}")
    print(f"abs(v1) = {abs(v1)}")

    # Section 5: Container Dunder Methods
    print("\n--- Section 5: Container Dunder Methods ---")
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Stack: {stack}")
    print(f"len(stack): {len(stack)}")
    print(f"2 in stack: {2 in stack}")
    print(f"stack[0]: {stack[0]}")

    # Section 6: Data Classes
    print("\n--- Section 6: Data Classes ---")
    person_dc = PersonDC("Bob", 25)
    print(f"DataClass: {person_dc}")

    # Frozen (immutable) dataclass
    point = ImmutablePoint(1, 2)
    # point.x = 3  # Would raise FrozenInstanceError

    point_set = {ImmutablePoint(1, 2), ImmutablePoint(1, 2)}
    print(f"Frozen set (should have 1): {len(point_set)}")

    # Section 7: __slots__
    print("\n--- Section 7: __slots__ Memory Optimization ---")
    import sys

    regular = RegularClass(1, 2, 3)
    slotted = SlottedClass(1, 2, 3)

    print(f"Regular class size: ~{sys.getsizeof(regular.__dict__)} bytes for __dict__")
    print(f"Slotted class: no __dict__, uses fixed memory")

    # Section 8: LRU Cache
    print("\n--- Section 8: LRU Cache ---")
    cache = LRUCache(3)
    cache.put("a", 1)
    cache.put("b", 2)
    cache.put("c", 3)
    print(f"Cache: {cache}")
    print(f"Get 'a': {cache.get('a')}")  # 1
    cache.put("d", 4)  # Evicts 'b' (least recently used)
    print(f"After adding 'd': {cache}")
    print(f"'b' in cache: {'b' in cache}")  # False

    # Section 9: Sortable Products
    print("\n--- Section 9: Sortable Products ---")
    products = [
        Product("Apple", 1.50, 100),
        Product("Banana", 0.50, 200),
        Product("Cherry", 5.00, 50),
    ]

    print("Sorted by price:")
    for p in sorted(products):
        print(f"  {p.name}: ${p.price}")

    # Using in set
    p1 = Product("Apple", 1.50, 100)
    p2 = Product("Apple", 1.50, 100)
    print(f"\np1 == p2: {p1 == p2}")
    print(f"Set of products: {len({p1, p2})} unique")

    print("\n" + "=" * 60)
    print("All tests completed!")
    print("=" * 60)

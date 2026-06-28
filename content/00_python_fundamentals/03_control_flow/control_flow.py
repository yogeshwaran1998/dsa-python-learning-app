"""
Control Flow - Implementation Guide
===================================
Comprehensive Python implementations covering if-elif-else, for/while loops,
range, break/continue/else, and match-case patterns for interviews.
"""

from typing import List, Optional


# =============================================================================
# SECTION 1: IF-ELIF-ELSE STATEMENTS
# =============================================================================

def check_grade(score: int) -> str:
    """
    Convert numerical score to letter grade using if-elif-else.
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def check_age_category(age: int) -> str:
    """
    Categorize age into groups using if statements.
    """
    if age < 0:
        return "Invalid age"
    if age < 13:
        return "Child"
    elif age < 20:
        return "Teenager"
    elif age < 65:
        return "Adult"
    else:
        return "Senior"


def check_falsy_values():
    """
    Demonstrate falsy values in Python.
    Falsy values evaluate to False in conditions.
    """
    # All these are falsy
    falsy_values = [None, False, 0, 0.0, 0j, "", [], {}, set()]

    for val in falsy_values:
        if val:
            print(f"{val} is truthy")
        else:
            print(f"{val} is falsy")

    # Checking with bool()
    print(f"\nbool(None): {bool(None)}")
    print(f"bool(0): {bool(0)}")
    print(f"bool(1): {bool(1)}")
    print(f"bool('hello'): {bool('hello')}")


# =============================================================================
# SECTION 2: FOR LOOPS
# =============================================================================

def iterate_over_list(arr: List[int]) -> None:
    """
    Basic iteration over list elements.
    """
    print("Iterating over list:")
    for item in arr:
        print(f"  {item}")


def iterate_with_index(arr: List[str]) -> None:
    """
    Iterate using range and len to get indices.
    """
    print("Iterating with index:")
    for i in range(len(arr)):
        print(f"  Index {i}: {arr[i]}")


def iterate_with_enumerate(arr: List[int]) -> None:
    """
    Iterate using enumerate to get index and value.
    Preferred over range(len()) in modern Python.
    """
    print("Using enumerate:")
    for index, value in enumerate(arr):
        print(f"  Index {index}: {value}")

    # Start enumeration from different index
    print("\nUsing enumerate(start=1):")
    for index, value in enumerate(arr, start=1):
        print(f"  Position {index}: {value}")


def iterate_multiple_sequences() -> None:
    """
    Iterate over multiple sequences using zip.
    """
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    cities = ["NYC", "LA", "SF"]

    print("Using zip:")
    for name, age, city in zip(names, ages, cities):
        print(f"  {name}, {age}, {city}")


def iterate_over_string() -> None:
    """
    Iterate over string characters.
    """
    word = "hello"
    print("Characters in 'hello':")
    for char in word:
        print(f"  {char}")


def iterate_over_dict() -> None:
    """
    Iterate over dictionary.
    """
    d = {"a": 1, "b": 2, "c": 3}

    print("Keys:")
    for key in d:
        print(f"  {key}")

    print("\nValues:")
    for value in d.values():
        print(f"  {value}")

    print("\nItems (key-value pairs):")
    for key, value in d.items():
        print(f"  {key}: {value}")


def iterate_with_condition() -> None:
    """
    Using continue to skip iterations.
    """
    print("Skip even numbers:")
    for i in range(10):
        if i % 2 == 0:
            continue  # Skip even numbers
        print(f"  {i}")


# =============================================================================
# SECTION 3: WHILE LOPS
# =============================================================================

def countdown() -> None:
    """
    Basic countdown using while loop.
    """
    count = 5
    while count > 0:
        print(count)
        count -= 1
    print("Blast off!")


def find_first_match(items: List[int], target: int) -> Optional[int]:
    """
    Find index of first occurrence of target using while loop.
    """
    index = 0
    while index < len(items):
        if items[index] == target:
            return index
        index += 1
    return None


def calculate_factorial(n: int) -> int:
    """
    Calculate factorial using while loop.
    """
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result


def find_gcd(a: int, b: int) -> int:
    """
    Find GCD using Euclidean algorithm (while loop).
    """
    while b != 0:
        a, b = b, a % b
    return abs(a)


def reverse_number(n: int) -> int:
    """
    Reverse digits of a number using while loop.
    """
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return reversed_num


# =============================================================================
# SECTION 4: RANGE FUNCTION
# =============================================================================

def demonstrate_range() -> None:
    """
    Demonstrate various range() usages.
    """
    # range(stop) - from 0 to stop-1
    print("range(5):", list(range(5)))

    # range(start, stop) - from start to stop-1
    print("range(2, 5):", list(range(2, 5)))

    # range(start, stop, step) - with step
    print("range(0, 10, 2):", list(range(0, 10, 2)))

    # Negative range
    print("range(5, 0, -1):", list(range(5, 0, -1)))

    # Common patterns
    print("\nIterating with range:")
    for i in range(5):
        print(f"  {i}", end=" ")
    print()


def range_for_indexing(arr: List[int]) -> None:
    """
    Use range for index-based iteration.
    """
    print("Array elements with indices:")
    for i in range(len(arr)):
        print(f"  arr[{i}] = {arr[i]}")


# =============================================================================
# SECTION 5: BREAK, CONTINUE, AND ELSE
# =============================================================================

def find_element(arr: List[int], target: int) -> Optional[int]:
    """
    Find element using break - returns index or None.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return None


def find_element_with_break(arr: List[int], target: int) -> Optional[int]:
    """
    Find element and break early using break statement.
    """
    for i, val in enumerate(arr):
        if val == target:
            print(f"Found {target} at index {i}")
            break  # Exit the loop
    else:
        # This runs only if loop completes without break
        print(f"{target} not found in array")
        return None

    return i


def skip_negative_values(arr: List[int]) -> List[int]:
    """
    Skip negative values using continue.
    """
    result = []
    for val in arr:
        if val < 0:
            continue  # Skip this iteration
        result.append(val)
    return result


def use_else_with_for():
    """
    Demonstrate else clause with for loop.
    Executes after loop completes normally (no break).
    """
    # This will print "Not found" because 100 is not in range(10)
    print("Searching for 100 in range(10):")
    for i in range(10):
        if i == 100:
            print(f"Found {i}")
            break
    else:
        print("Not found - else clause executed")

    # This will print "Found 5" and NOT execute else
    print("\nSearching for 5 in range(10):")
    for i in range(10):
        if i == 5:
            print(f"Found {i}")
            break
    else:
        print("Not found - else clause executed")


def use_else_with_while():
    """
    Demonstrate else clause with while loop.
    """
    counter = 0
    target = 5

    while counter < target:
        counter += 1
        if counter == 3:
            print("Found 3, breaking")
            break
    else:
        # Executes if while condition becomes false without break
        print("Loop completed without finding target")

    # Another example: wait for condition
    print("\nWait for condition example:")
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        attempts += 1
        print(f"  Attempt {attempts}")
    else:
        print("Max attempts reached - else executed")


# =============================================================================
# SECTION 6: MATCH-CASE (Python 3.10+)
# Implemented portably below so these demos run on Python 3.9 too; each
# docstring shows the equivalent Python 3.10+ match-case form.
# =============================================================================

def http_status_code(status: int) -> str:
    """
    Map HTTP status codes to messages.

    Python 3.10+ match-case form:
        match status:
            case 200: return "OK"
            case 404: return "Not Found"
            case _:   return "Unknown Status"
    """
    codes = {
        200: "OK", 201: "Created", 204: "No Content",
        400: "Bad Request", 401: "Unauthorized", 403: "Forbidden",
        404: "Not Found", 500: "Internal Server Error",
    }
    return codes.get(status, "Unknown Status")


def describe_shape(shape: dict) -> str:
    """
    Describe a shape dict (capture-pattern example).

    Python 3.10+ match-case form:
        match shape:
            case {"type": "circle", "radius": r}: ...
            case {"type": "rectangle", "width": w, "height": h}: ...
    """
    t = shape.get("type")
    if t == "circle" and "radius" in shape:
        return f"Circle with radius {shape['radius']}"
    if t == "rectangle" and "width" in shape and "height" in shape:
        return f"Rectangle {shape['width']}x{shape['height']}"
    if t == "square" and "side" in shape:
        return f"Square with side {shape['side']}"
    return "Unknown shape"


def categorize_number(n: int) -> str:
    """
    Categorize a number (guard example).

    Python 3.10+ match-case form:
        match n:
            case n if n < 0: return "Negative"
            case 0:          return "Zero"
            case n if n % 2 == 0: return "Even positive"
            case _:          return "Odd positive"
    """
    if n < 0:
        return "Negative"
    if n == 0:
        return "Zero"
    if n % 2 == 0:
        return "Even positive"
    return "Odd positive"


def process_command(command: str) -> str:
    """
    Parse a command (sequence + OR pattern example).

    Python 3.10+ match-case form:
        match command.split():
            case ["echo", *args]:        ...
            case ["quit" | "exit" | "q"]: ...
            case ["help"]:               ...
            case _:                      ...
    """
    parts = command.split()
    if parts and parts[0] == "echo":
        return f"Echo: {' '.join(parts[1:])}"
    if parts == ["quit"] or parts == ["exit"] or parts == ["q"]:
        return "Goodbye!"
    if parts == ["help"]:
        return "Available commands: echo, quit, help"
    return "Unknown command"


# =============================================================================
# SECTION 7: PRACTICAL INTERVIEW PATTERNS
# =============================================================================

def two_sum_brute_force(nums: List[int], target: int) -> List[int]:
    """
    Find two numbers that add up to target - O(n^2).
    Basic approach using nested loops.
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def find_max_subarray_length(arr: List[int], max_sum: int) -> int:
    """
    Find longest subarray with sum <= max_sum using sliding window.
    """
    max_length = 0
    current_sum = 0
    left = 0

    for right in range(len(arr)):
        current_sum += arr[right]

        while current_sum > max_sum:
            current_sum -= arr[left]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length


def find_duplicates(arr: List[int]) -> List[int]:
    """
    Find all duplicate elements in array.
    Uses set to track seen elements.
    """
    seen = set()
    duplicates = []

    for num in arr:
        if num in seen:
            duplicates.append(num)
        else:
            seen.add(num)

    return duplicates


def is_sorted(arr: List[int]) -> bool:
    """
    Check if array is sorted in ascending order.
    Uses adjacent comparison in loop.
    """
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


def find_missing_number(nums: List[int]) -> int:
    """
    Find missing number in range [0, n].
    Uses sum formula: n*(n+1)/2
    """
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


def fizzbuzz(n: int) -> List[str]:
    """
    Classic FizzBuzz problem.
    """
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


# =============================================================================
# SECTION 8: DEMONSTRATION
# =============================================================================

if __name__ == "__main__":
    # Test if-elif-else
    print("=== If-Elif-Else ===")
    print(f"Score 85: {check_grade(85)}")
    print(f"Age 25: {check_age_category(25)}")

    # Test for loops
    print("\n=== For Loops ===")
    iterate_with_enumerate([10, 20, 30])

    # Test while loops
    print("\n=== While Loops ===")
    print(f"Factorial of 5: {calculate_factorial(5)}")
    print(f"GCD of 48 and 18: {find_gcd(48, 18)}")

    # Test range
    print("\n=== Range ===")
    demonstrate_range()

    # Test break, continue, else
    print("\n=== Break, Continue, Else ===")
    find_element_with_break([1, 2, 3, 4, 5], 3)
    use_else_with_for()

    # Test match-case (Python 3.10+)
    print("\n=== Match-Case ===")
    print(f"Status 404: {http_status_code(404)}")
    print(f"Command 'quit': {process_command('quit')}")

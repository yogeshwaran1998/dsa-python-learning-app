"""
Stacks - Implementation and Examples
====================================
Comprehensive Python implementations for stack problems
commonly asked in FAANG interviews.
"""

from typing import List, Optional


# =============================================================================
# SECTION 1: STACK IMPLEMENTATION
# =============================================================================

class Stack:
    """
    Basic stack implementation using Python list.

    Time: All operations O(1), Space: O(n)
    """

    def __init__(self):
        self.items = []

    def push(self, item) -> None:
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def size(self) -> int:
        return len(self.items)

    def __repr__(self):
        return f"Stack({self.items})"


# =============================================================================
# SECTION 2: VALID PARENTHESES
# =============================================================================

def is_valid_parentheses(s: str) -> bool:
    """
    Check if string has valid parentheses.

    Time: O(n), Space: O(n)
    """
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()

    return len(stack) == 0


def longest_valid_parentheses(s: str) -> int:
    """
    Find length of longest valid parentheses substring.

    Time: O(n), Space: O(1)
    """
    max_length = 0
    stack = [-1]  # Base for first valid substring

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_length = max(max_length, i - stack[-1])

    return max_length


# =============================================================================
# SECTION 3: MIN STACK
# =============================================================================

class MinStack:
    """
    Stack that supports retrieving minimum in O(1).

    Time: All operations O(1), Space: O(2n) = O(n)
    """

    def __init__(self):
        self.stack = []  # (value, min_so_far)
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def get_min(self) -> int:
        return self.min_stack[-1] if self.min_stack else None


class MinStackOptimal:
    """
    Space-optimized Min Stack using single stack.

    Time: O(1) amortized for all operations, Space: O(n)
    """

    def __init__(self):
        self.stack = []
        self.min_val = float('inf')

    def push(self, val: int) -> None:
        if val <= self.min_val:
            self.stack.append(self.min_val)
            self.min_val = val
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            popped = self.stack.pop()
            if popped == self.min_val and self.stack:
                self.min_val = self.stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def get_min(self) -> int:
        return self.min_val


# =============================================================================
# SECTION 4: MONOTONIC STACK
# =============================================================================

def next_greater_element(nums: List[int]) -> List[int]:
    """
    Find next greater element for each element.

    For each element, find the first element to the right that's greater.

    Time: O(n), Space: O(n)

    Example:
    Input: [1, 2, 1, 3, 4]
    Output: [2, 3, 3, -1, -1]
    """
    n = len(nums)
    result = [-1] * n
    stack = []  # Store indices

    for i in range(n):
        # Current element is greater than stack top
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)

    return result


def next_smaller_element(nums: List[int]) -> List[int]:
    """
    Find next smaller element for each element.

    Time: O(n), Space: O(n)
    """
    n = len(nums)
    result = [-1] * n
    stack = []

    for i in range(n):
        while stack and nums[i] < nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)

    return result


def next_greater_element_circular(nums: List[int]) -> List[int]:
    """
    Find next greater element in circular array.

    Time: O(n), Space: O(n)
    """
    n = len(nums)
    result = [-1] * n
    stack = []

    # Iterate twice to simulate circular behavior
    for i in range(2 * n):
        current = nums[i % n]

        while stack and current > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = current

        # Only add to stack on first pass
        if i < n:
            stack.append(i % n)

        # Clear stack if we've processed first pass
        if i >= n and not stack:
            break

    return result


def daily_temperatures(temps: List[int]) -> List[int]:
    """
    For each day, find how many days until warmer temperature.

    Time: O(n), Space: O(n)
    """
    n = len(temps)
    result = [0] * n
    stack = []  # Store indices

    for i in range(n):
        while stack and temps[i] > temps[stack[-1]]:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)

    return result


# =============================================================================
# SECTION 5: REMOVE ADJACENT DUPLICATES
# =============================================================================

def remove_adjacent_duplicates(s: str) -> str:
    """
    Remove all adjacent duplicate pairs.

    Time: O(n), Space: O(n)

    Example:
    "azxxzy" → "ay"

    Algorithm: Use stack, if current char equals top, pop; else push.
    """
    stack = []

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    return ''.join(stack)


def remove_all_adjacent_duplicates_ii(s: str, k: int) -> str:
    """
    Remove all adjacent duplicates when k consecutive same chars exist.

    Time: O(n), Space: O(n)
    """
    stack = []  # [(char, count)]

    for char in s:
        if stack and stack[-1][0] == char:
            stack[-1] = (char, stack[-1][1] + 1)
            if stack[-1][1] == k:
                stack.pop()
        else:
            stack.append((char, 1))

    result = []
    for char, count in stack:
        result.append(char * count)

    return ''.join(result)


# =============================================================================
# SECTION 6: EXPRESSION EVALUATION
# =============================================================================

def evaluate_postfix(tokens: List[str]) -> int:
    """
    Evaluate postfix expression.

    Time: O(n), Space: O(n)

    Example tokens: ["3", "4", "+", "2", "*"]
    Result: (3 + 4) * 2 = 14
    """
    stack = []
    operators = {'+', '-', '*', '/'}

    for token in tokens:
        if token in operators:
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            else:  # division
                result = int(a / b)  # truncate towards zero

            stack.append(result)
        else:
            stack.append(int(token))

    return stack[-1]


def infix_to_postfix(tokens: List[str]) -> List[str]:
    """
    Convert infix expression to postfix.

    Time: O(n), Space: O(n)
    """
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    stack = []

    for token in tokens:
        if token.isalnum():
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Remove '('
        else:  # operator
            while (stack and stack[-1] != '(' and
                   precedence[stack[-1]] >= precedence[token]):
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return output


def basic_calculator(s: str) -> int:
    """
    Evaluate basic arithmetic expression with + and -.

    Time: O(n), Space: O(n)
    """
    stack = []
    sign = 1
    num = 0
    result = 0

    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char == '+':
            result += sign * num
            sign = 1
            num = 0
        elif char == '-':
            result += sign * num
            sign = -1
            num = 0
        elif char == '(':
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif char == ')':
            result += sign * num
            result = stack.pop() + stack.pop() * result
            num = 0
            sign = 1

    result += sign * num
    return result


# =============================================================================
# SECTION 7: LARGEST RECTANGLE
# =============================================================================

def largest_rectangle_histogram(heights: List[int]) -> int:
    """
    Find largest rectangle in histogram.

    Time: O(n), Space: O(n)

    For each bar, calculate area with it as shortest bar.
    """
    stack = []
    max_area = 0

    for i, h in enumerate(heights + [0]):  # Add sentinel
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    return max_area


def largest_rectangle_matrix(matrix: List[List[int]]) -> int:
    """
    Find largest rectangle of 1s in binary matrix.

    Time: O(m*n), Space: O(n)
    """
    if not matrix:
        return 0

    max_area = 0
    heights = [0] * len(matrix[0])

    for row in matrix:
        for i, val in enumerate(row):
            heights[i] = heights[i] + 1 if val else 0
        max_area = max(max_area, largest_rectangle_histogram(heights))

    return max_area


# =============================================================================
# SECTION 8: TRAPPING RAIN WATER (STACK APPROACH)
# =============================================================================

def trap_rain_water(heights: List[int]) -> int:
    """
    Calculate trapped water using stack.

    Time: O(n), Space: O(n)
    """
    stack = []
    water = 0

    for i, h in enumerate(heights):
        while stack and h > heights[stack[-1]]:
            prev = stack.pop()
            if not stack:
                break
            distance = i - stack[-1] - 1
            bounded_height = min(h, heights[stack[-1]]) - heights[prev]
            water += distance * bounded_height
        stack.append(i)

    return water


# =============================================================================
# SECTION 9: DECODE STRING
# =============================================================================

def decode_string(s: str) -> str:
    """
    Decode string with repeat counts.

    Time: O(n), Space: O(n)

    Example:
    "3[a2[c]]" → "accaccacc"
    """
    stack = []
    current_num = 0
    current_str = ""

    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            stack.append((current_str, current_num))
            current_str = ""
            current_num = 0
        elif char == ']':
            prev_str, num = stack.pop()
            current_str = prev_str + current_str * num
        else:
            current_str += char

    return current_str


# =============================================================================
# SECTION 10: TESTING AND DEMO
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("STACK ALGORITHMS - TEST DEMO")
    print("=" * 60)

    # Test valid parentheses
    print("\n--- Valid Parentheses ---")
    tests = ["()", "()[]{}", "(]", "([)]", "{[]}"]
    for test in tests:
        print(f"'{test}': {is_valid_parentheses(test)}")

    # Test longest valid parentheses
    print("\n--- Longest Valid Parentheses ---")
    test = ")()())"
    result = longest_valid_parentheses(test)
    print(f"'{test}': {result}")

    # Test MinStack
    print("\n--- Min Stack ---")
    min_stack = MinStack()
    min_stack.push(5)
    min_stack.push(2)
    min_stack.push(8)
    print(f"After push 5,2,8: min={min_stack.get_min()}")
    min_stack.pop()
    print(f"After pop: min={min_stack.get_min()}")

    # Test Next Greater Element
    print("\n--- Next Greater Element ---")
    nums = [1, 2, 1, 3, 4]
    result = next_greater_element(nums)
    print(f"Next greater for {nums}: {result}")

    # Test Daily Temperatures
    temps = [73, 74, 75, 71, 69, 72, 76, 73]
    result = daily_temperatures(temps)
    print(f"Daily temps {temps}: {result}")

    # Test Remove Adjacent Duplicates
    print("\n--- Remove Adjacent Duplicates ---")
    s = "azxxzy"
    result = remove_adjacent_duplicates(s)
    print(f"Remove adjacent duplicates from '{s}': '{result}'")

    # Test Postfix Evaluation
    print("\n--- Postfix Evaluation ---")
    tokens = ["3", "4", "+", "2", "*"]
    result = evaluate_postfix(tokens)
    print(f"Evaluate {tokens}: {result}")

    # Test Calculator
    print("\n--- Basic Calculator ---")
    expr = "(1+(4+5+2)-3)+(6+8)"
    result = basic_calculator(expr)
    print(f"Calculate '{expr}': {result}")

    # Test Decode String
    print("\n--- Decode String ---")
    s = "3[a2[c]]"
    result = decode_string(s)
    print(f"Decode '{s}': '{result}'")

    # Test Largest Rectangle
    print("\n--- Largest Rectangle ---")
    heights = [2, 1, 5, 6, 2, 3]
    result = largest_rectangle_histogram(heights)
    print(f"Largest rectangle in {heights}: {result}")

    # Test Trapping Rain Water
    print("\n--- Trapping Rain Water ---")
    heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    result = trap_rain_water(heights)
    print(f"Trapped water in {heights}: {result}")

    print("\n" + "=" * 60)
    print("All tests completed!")
    print("=" * 60)

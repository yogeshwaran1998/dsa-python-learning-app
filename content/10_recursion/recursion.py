"""
Recursion - Implementation and Examples
=====================================
Comprehensive Python implementations for recursion
commonly asked in FAANG interviews.
"""

from typing import List, Tuple


# =============================================================================
# SECTION 1: BASIC RECURSION
# =============================================================================

def factorial(n: int) -> int:
    """Calculate factorial recursively."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n: int) -> int:
    """Calculate nth Fibonacci number."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def power(base: int, exp: int) -> int:
    """Calculate base raised to exp."""
    if exp == 0:
        return 1
    if exp % 2 == 0:
        half = power(base, exp // 2)
        return half * half
    return base * power(base, exp - 1)


# =============================================================================
# SECTION 2: BACKTRACKING
# =============================================================================

def subsets(nums: List[int]) -> List[List[int]]:
    """Generate all subsets."""
    result = []

    def backtrack(start: int, path: List[int]):
        result.append(path[:])

        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result


def permutations(nums: List[int]) -> List[List[int]]:
    """Generate all permutations."""
    result = []

    def backtrack(path: List[int], used: List[bool]):
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(path, used)
            path.pop()
            used[i] = False

    backtrack([], [False] * len(nums))
    return result


def combinations(n: int, k: int) -> List[List[int]]:
    """Generate all combinations of k numbers from 1-n."""
    result = []

    def backtrack(start: int, path: List[int]):
        if len(path) == k:
            result.append(path[:])
            return

        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()

    backtrack(1, [])
    return result


def solve_n_queens(n: int) -> List[List[str]]:
    """Solve N-Queens problem."""
    result = []
    cols = set()
    pos_diag = set()  # row + col
    neg_diag = set()  # row - col

    board = [['.' for _ in range(n)] for _ in range(n)]

    def backtrack(row: int):
        if row == n:
            result.append([''.join(row) for row in board])
            return

        for col in range(n):
            if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
                continue

            cols.add(col)
            pos_diag.add(row + col)
            neg_diag.add(row - col)
            board[row][col] = 'Q'

            backtrack(row + 1)

            cols.remove(col)
            pos_diag.remove(row + col)
            neg_diag.remove(row - col)
            board[row][col] = '.'

    backtrack(0)
    return result


# =============================================================================
# SECTION 3: DIVIDE AND CONQUER
# =============================================================================

def merge_sort(arr: List[int]) -> List[int]:
    """Merge sort implementation."""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
    """Merge two sorted arrays."""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr: List[int]) -> List[int]:
    """Quick sort implementation."""
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# =============================================================================
# SECTION 4: TREE RECURSION
# =============================================================================

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: TreeNode) -> int:
    """Maximum depth of binary tree."""
    if not root:
        return 0

    return 1 + max(max_depth(root.left), max_depth(root.right))


def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    """Check if two trees are identical."""
    if not p and not q:
        return True
    if not p or not q:
        return False

    return (p.val == q.val and
            is_same_tree(p.left, q.left) and
            is_same_tree(p.right, q.right))


# =============================================================================
# SECTION 5: TESTING
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("RECURSION - TEST DEMO")
    print("=" * 60)

    print(f"\nFactorial of 5: {factorial(5)}")
    print(f"Fibonacci of 10: {fibonacci(10)}")
    print(f"2^10: {power(2, 10)}")

    print("\n--- Subsets ---")
    nums = [1, 2, 3]
    print(f"Subsets of {nums}:")
    for s in subsets(nums):
        print(f"  {s}")

    print("\n--- Permutations ---")
    nums = [1, 2, 3]
    print(f"Permutations of {nums}:")
    for p in permutations(nums):
        print(f"  {p}")

    print("\n--- Combinations ---")
    print(f"Combinations of 4 choose 2:")
    for c in combinations(4, 2):
        print(f"  {c}")

    print("\n" + "=" * 60)
    print("All tests completed!")
    print("=" * 60)

"""
Problem Solving - Implementation and Examples
============================================
Comprehensive examples demonstrating problem-solving approaches
from brute force to optimized solutions.
"""

from typing import List, Optional, Tuple


# =============================================================================
# SECTION 1: EDGE CASES
# =============================================================================

"""
Understanding and handling edge cases is crucial.
Always test: empty, single, negative, duplicates, extremes.
"""


def find_max_edge_cases():
    """
    Find maximum with proper edge case handling.
    """
    def find_max(nums: List[int]) -> Optional[int]:
        # Edge case: empty list
        if not nums:
            return None

        # Standard case
        max_val = nums[0]
        for num in nums[1:]:
            if num > max_val:
                max_val = num
        return max_val

    # Test edge cases
    print("\n--- Edge Case Testing ---")
    print(f"Empty: {find_max([])}")  # None
    print(f"Single: {find_max([5])}")  # 5
    print(f"Negatives: {find_max([-5, -3, -1])}")  # -1
    print(f"Duplicates: {find_max([1, 1, 1])}")  # 1
    print(f"Mixed: {find_max([-1, 0, 1])}")  # 1


def two_sum_edge_cases():
    """
    Two sum with edge case handling.
    """
    def two_sum(nums: List[int], target: int) -> List[int]:
        # Edge cases: empty, single element
        if not nums or len(nums) < 2:
            return []

        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

        return []

    # Test
    print("\n--- Two Sum Edge Cases ---")
    print(f"Empty: {two_sum([], 9)}")  # []
    print(f"Single: {two_sum([1], 9)}")  # []
    print(f"Two: {two_sum([1, 2], 3)}")  # [0, 1]
    print(f"Negative: {two_sum([-1, 2], 1)}")  # [0, 1]
    print(f"Duplicates: {two_sum([3, 3], 6)}")  # [0, 1]


# =============================================================================
# SECTION 2: BRUTE FORCE APPROACH
# =============================================================================

"""
Start with brute force to understand the problem.
Then optimize if needed.
"""


def two_sum_brute(nums: List[int], target: int) -> List[int]:
    """
    Brute force: Check all pairs.
    Time: O(n^2), Space: O(1)
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def contains_duplicate_brute(nums: List[int]) -> bool:
    """
    Brute force: Compare each pair.
    Time: O(n^2), Space: O(1)
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False


def max_subarray_brute(nums: List[int]) -> int:
    """
    Brute force: Try all subarrays.
    Time: O(n^3), Space: O(1)

    Note: This is O(n^2) actually if optimized,
    but conceptually checks all combinations.
    """
    if not nums:
        return 0

    max_sum = float('-inf')
    n = len(nums)

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            max_sum = max(max_sum, current_sum)

    return max_sum


# =============================================================================
# SECTION 3: HASH-BASED OPTIMIZATION
# =============================================================================

"""
Use hash table for O(1) lookups.
"""


def two_sum_hash(nums: List[int], target: int) -> List[int]:
    """
    Hash-based: Use dict for O(1) lookups.
    Time: O(n), Space: O(n)
    """
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


def contains_duplicate_hash(nums: List[int]) -> bool:
    """
    Hash-based: Use set for O(1) lookups.
    Time: O(n), Space: O(n)
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


def longest_consecutive(nums: List[int]) -> int:
    """
    Find longest consecutive sequence.
    Time: O(n), Space: O(n)

    Uses hash for O(1) lookups.
    """
    if not nums:
        return 0

    num_set = set(nums)
    max_length = 0

    for num in num_set:
        # Only start counting from beginning of sequence
        if num - 1 not in num_set:
            current = num
            length = 1

            while current + 1 in num_set:
                current += 1
                length += 1

            max_length = max(max_length, length)

    return max_length


# =============================================================================
# SECTION 4: TWO POINTERS
# =============================================================================

"""
Two pointers pattern for sorted arrays.
"""


def two_sum_sorted(arr: List[int], target: int) -> List[int]:
    """
    Two pointers on sorted array.
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(arr) - 1

    while left < right:
        current = arr[left] + arr[right]
        if current == target:
            return [left, right]
        elif current < target:
            left += 1
        else:
            right -= 1

    return []


def remove_duplicates_sorted(arr: List[int]) -> int:
    """
    Remove duplicates in-place from sorted array.
    Time: O(n), Space: O(1)
    """
    if not arr:
        return 0

    slow = 0
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]

    return slow + 1


def container_with_most_water(heights: List[int]) -> int:
    """
    Find container that holds most water.
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(heights) - 1
    max_area = 0

    while left < right:
        width = right - left
        height = min(heights[left], heights[right])
        max_area = max(max_area, width * height)

        # Move the shorter line
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_area


# =============================================================================
# SECTION 5: SLIDING WINDOW
# =============================================================================

"""
Sliding window for subarray problems.
"""


def min_subarray_len(target: int, nums: List[int]) -> int:
    """
    Find minimum length of subarray with sum >= target.
    Time: O(n), Space: O(1)
    """
    if not nums:
        return 0

    left = 0
    current_sum = 0
    min_len = float('inf')

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return min_len if min_len != float('inf') else 0


def longest_substring_k_distinct(s: str, k: int) -> int:
    """
    Find longest substring with at most k distinct chars.
    Time: O(n), Space: O(k)
    """
    if k == 0 or not s:
        return 0

    from collections import defaultdict

    char_count = defaultdict(int)
    left = 0
    max_length = 0

    for right in range(len(s)):
        char_count[s[right]] += 1

        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length


def max_sum_subarray_k(nums: List[int], k: int) -> int:
    """
    Maximum sum of k consecutive elements.
    Time: O(n), Space: O(1)
    """
    if len(nums) < k:
        return 0

    # Initial window
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # Slide window
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum


# =============================================================================
# SECTION 6: DYNAMIC PROGRAMMING
# =============================================================================

"""
DP for problems with overlapping subproblems.
"""


def climb_stairs(n: int) -> int:
    """
    Climbing stairs: 1 or 2 steps at a time.
    Time: O(n), Space: O(1)
    """
    if n <= 2:
        return n

    prev, curr = 1, 2
    for _ in range(3, n + 1):
        prev, curr = curr, prev + curr

    return curr


def fibonacci(n: int) -> int:
    """
    Fibonacci - optimized DP.
    Time: O(n), Space: O(1)
    """
    if n <= 1:
        return n

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr

    return curr


def house_robber(nums: List[int]) -> int:
    """
    Maximum money without robbing adjacent houses.
    Time: O(n), Space: O(1)
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    prev, curr = nums[0], max(nums[0], nums[1])

    for i in range(2, len(nums)):
        prev, curr = curr, max(curr, prev + nums[i])

    return curr


def coin_change(coins: List[int], amount: int) -> int:
    """
    Minimum coins to make amount.
    Time: O(n * amount), Space: O(amount)
    """
    if amount == 0:
        return 0
    if not coins:
        return -1

    # dp[i] = minimum coins to make amount i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1

    return dp[amount] if dp[amount] != float('inf') else -1


def longest_increasing_subsequence(nums: List[int]) -> int:
    """
    LIS length.
    Time: O(n^2), Space: O(n)
    """
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n  # dp[i] = LIS ending at i

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


# =============================================================================
# SECTION 7: PROBLEM CLASSIFICATION
# =============================================================================

def classify_problem(problem_type: str) -> str:
    """
    Classification guide for common problem types.
    """
    guides = {
        "find_pair_sum": "Use hash (unsorted) or two pointers (sorted)",
        "subarray_sum": "Use prefix sum + hash, or sliding window",
        "duplicates": "Use set for O(n), sort for O(n log n)",
        "sorting": "Use built-in sorted() or sort in place",
        "search": "Binary search for sorted, hash for unsorted",
        "sliding_window": "Two pointers moving same direction",
        "two_pointers": "Sorted array, opposite directions",
        "graph": "BFS for shortest path, DFS for existence",
        "tree": "DFS (recursion) or BFS (level order)",
        "dp": "Identify state and transition",
    }

    return guides.get(problem_type, "Unknown problem type")


# =============================================================================
# SECTION 8: OPTIMIZATION PATTERN EXAMPLES
# =============================================================================

"""
Show optimization progression for a single problem.
"""


def max_subarray_sum_optimization():
    """
    Show progression from brute force to optimized.
    """

    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    # O(n^3) - Truly brute force (not shown, too slow)

    # O(n^2) - Single loop
    def max_subarray_n2(arr):
        max_sum = float('-inf')
        n = len(arr)
        for i in range(n):
            current = 0
            for j in range(i, n):
                current += arr[j]
                max_sum = max(max_sum, current)
        return max_sum

    # O(n) - Kadane's algorithm
    def max_subarray_kadane(arr):
        max_sum = arr[0]
        current = arr[0]

        for num in arr[1:]:
            current = max(num, current + num)
            max_sum = max(max_sum, current)

        return max_sum

    print("\n--- Max Subarray Optimization ---")
    print(f"O(n^2): {max_subarray_n2(nums)}")
    print(f"Kadane: {max_subarray_kadane(nums)}")


# =============================================================================
# SECTION 9: TESTING AND DEMO
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("PROBLEM SOLVING - TEST DEMO")
    print("=" * 60)

    # Section 1: Edge Cases
    print("\n--- Section 1: Edge Cases ---")
    find_max_edge_cases()
    two_sum_edge_cases()

    # Section 2: Brute Force
    print("\n--- Section 2: Brute Force ---")
    print(f"Two sum brute [2,7,11,15], 9: {two_sum_brute([2, 7, 11, 15], 9)}")
    print(f"Contains duplicate [1,2,3,1]: {contains_duplicate_brute([1, 2, 3, 1])}")

    # Section 3: Hash
    print("\n--- Section 3: Hash Optimization ---")
    print(f"Two sum hash [2,7,11,15], 9: {two_sum_hash([2, 7, 11, 15], 9)}")
    print(f"Contains duplicate hash [1,2,3,1]: {contains_duplicate_hash([1, 2, 3, 1])}")
    print(f"Longest consecutive [100,4,200,1,3,2]: {longest_consecutive([100, 4, 200, 1, 3, 2])}")

    # Section 4: Two Pointers
    print("\n--- Section 4: Two Pointers ---")
    print(f"Two sum sorted [1,2,4,6], 8: {two_sum_sorted([1, 2, 4, 6], 8)}")
    arr = [1, 1, 2, 2, 3]
    new_len = remove_duplicates_sorted(arr)
    print(f"Remove duplicates: {arr[:new_len]}")

    # Section 5: Sliding Window
    print("\n--- Section 5: Sliding Window ---")
    print(f"Min subarray len >= 7, [2,3,1,2,4,3]: {min_subarray_len(7, [2, 3, 1, 2, 4, 3])}")
    print(f"Longest k=2 'eceba': {longest_substring_k_distinct('eceba', 2)}")

    # Section 6: DP
    print("\n--- Section 6: Dynamic Programming ---")
    print(f"Climb stairs 5: {climb_stairs(5)}")
    print(f"Fibonacci 10: {fibonacci(10)}")
    print(f"House robber [1,2,3,1]: {house_robber([1, 2, 3, 1])}")
    print(f"Coin change [1,2,5], 11: {coin_change([1, 2, 5], 11)}")

    # Section 7: Problem Classification
    print("\n--- Section 7: Problem Classification ---")
    print(f"find_pair_sum: {classify_problem('find_pair_sum')}")
    print(f"sliding_window: {classify_problem('sliding_window')}")

    # Section 8: Optimization
    print("\n--- Section 8: Optimization Progression ---")
    max_subarray_sum_optimization()

    print("\n" + "=" * 60)
    print("All demos completed!")
    print("=" * 60)

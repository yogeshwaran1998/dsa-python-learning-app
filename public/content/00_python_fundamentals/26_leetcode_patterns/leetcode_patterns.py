"""
LeetCode Patterns - Implementation and Examples
================================================
Comprehensive implementations of common LeetCode patterns
for algorithm problem-solving.
"""

from typing import List, Optional
from collections import deque


# =============================================================================
# SECTION 1: TWO POINTERS
# =============================================================================

"""
Two Pointers Pattern:
- Use two pointers moving in same or opposite direction
- Time: O(n), Space: O(1) typically
- Works well with sorted arrays
"""


def two_sum_sorted(arr: List[int], target: int) -> List[int]:
    """
    Find two numbers that add to target in sorted array.
    Time: O(n), Space: O(1)

    Two pointers start at opposite ends and move toward center.
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
    Returns new length.

    Uses slow pointer for result, fast for scanning.
    """
    if not arr:
        return 0

    slow = 0
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]

    return slow + 1


def is_palindrome(s: str) -> bool:
    """
    Check if string is palindrome.
    Uses two pointers from start and end.
    """
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


def container_with_most_water(heights: List[int]) -> int:
    """
    Container with most water - classic two pointers.
    Move the shorter line to try to increase height.
    """
    left, right = 0, len(heights) - 1
    max_area = 0

    while left < right:
        width = right - left
        height = min(heights[left], heights[right])
        max_area = max(max_area, width * height)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_area


# =============================================================================
# SECTION 2: SLIDING WINDOW
# =============================================================================

"""
Sliding Window Pattern:
- Maintain a window that slides through data
- Useful for subarray/substring problems
- Can be fixed or variable size
"""


def max_sum_subarray_k(arr: List[int], k: int) -> int:
    """
    Maximum sum of k consecutive elements.
    Fixed window size.
    """
    if len(arr) < k:
        return 0

    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum


def min_subarray_len(target: int, arr: List[int]) -> int:
    """
    Minimum length of subarray with sum >= target.
    Variable window size - expands right, shrinks left.
    """
    left = 0
    current_sum = 0
    min_len = float('inf')

    for right in range(len(arr)):
        current_sum += arr[right]

        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= arr[left]
            left += 1

    return min_len if min_len != float('inf') else 0


def longest_substring_k_distinct(s: str, k: int) -> int:
    """
    Longest substring with at most k distinct characters.
    Variable window with dict for character counts.
    """
    if k == 0 or not s:
        return 0

    char_count = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1

        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length


def longest_substring_no_repeats(s: str) -> int:
    """
    Longest substring without repeating characters.
    Uses dict to track last seen position.
    """
    char_index = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1

        char_index[s[right]] = right
        max_length = max(max_length, right - left + 1)

    return max_length


# =============================================================================
# SECTION 3: FAST AND SLOW POINTERS
# =============================================================================

"""
Fast and Slow Pointers:
- Two pointers moving at different speeds
- Used for cycle detection in linked lists
- Can find middle element
"""


class ListNode:
    """Definition for singly-linked list node."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head: Optional[ListNode]) -> bool:
    """
    Detect cycle in linked list.
    Floyd's Tortoise and Hare algorithm.

    If there's a cycle, fast and slow will meet.
    """
    if not head or not head.next:
        return False

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Find middle of linked list.
    When fast reaches end, slow is at middle.
    """
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def find_cycle_start(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Find start of cycle in linked list.
    """
    if not head or not head.next:
        return None

    # Phase 1: Find intersection
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if not fast or not fast.next:
        return None

    # Phase 2: Find cycle start
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


# =============================================================================
# SECTION 4: BINARY SEARCH
# =============================================================================

"""
Binary Search Pattern:
- For sorted arrays or monotonic functions
- Time: O(log n), Space: O(1)
"""


def binary_search(arr: List[int], target: int) -> int:
    """
    Standard binary search.
    Returns index if found, -1 otherwise.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def search_insert_position(arr: List[int], target: int) -> int:
    """
    Find where to insert target.
    """
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left


def find_first_last(arr: List[int], target: int) -> List[int]:
    """
    Find first and last position of target.
    """
    def find_position(find_first):
        left, right = 0, len(arr) - 1
        result = -1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                result = mid
                if find_first:
                    right = mid - 1
                else:
                    left = mid + 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return result

    return [find_position(True), find_position(False)]


def search_rotated(arr: List[int], target: int) -> int:
    """
    Search in rotated sorted array.

    One half is always sorted.
    Determine which half is sorted and check target.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        # Left half is sorted
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


# =============================================================================
# SECTION 5: PREFIX SUM
# =============================================================================

"""
Prefix Sum Pattern:
- Pre-compute cumulative sums
- Enables O(1) range sum queries
- Useful for subarray sum problems
"""


class PrefixSum:
    """Prefix sum data structure for range queries."""
    def __init__(self, arr: List[int]):
        self.prefix = [0] * (len(arr) + 1)
        for i, val in enumerate(arr):
            self.prefix[i + 1] = self.prefix[i] + val

    def range_sum(self, left: int, right: int) -> int:
        """Sum from left to right (inclusive)."""
        return self.prefix[right + 1] - self.prefix[left]


def subarray_sum_k(nums: List[int], k: int) -> int:
    """
    Count subarrays with sum equals k.
    Uses hashmap to store prefix sum frequencies.
    """
    count = 0
    prefix_sum = 0
    sum_freq = {0: 1}

    for num in nums:
        prefix_sum += num
        if prefix_sum - k in sum_freq:
            count += sum_freq[prefix_sum - k]
        sum_freq[prefix_sum] = sum_freq.get(prefix_sum, 0) + 1

    return count


# =============================================================================
# SECTION 6: DEPTH-FIRST SEARCH (DFS)
# =============================================================================

"""
DFS Pattern:
- Explore as deep as possible before backtracking
- Uses recursion or stack
- Good for tree/graph traversal
"""


class TreeNode:
    """Definition for binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """Root -> Left -> Right"""
    if not root:
        return []
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)


def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """Left -> Root -> Right"""
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)


def postorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """Left -> Right -> Root"""
    if not root:
        return []
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.val]


def max_depth(root: Optional[TreeNode]) -> int:
    """Maximum depth of binary tree."""
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def has_path_sum(root: Optional[TreeNode], target: int) -> bool:
    """Check if there's root-to-leaf path with given sum."""
    if not root:
        return False
    if not root.left and not root.right:
        return root.val == target
    return has_path_sum(root.left, target - root.val) or \
           has_path_sum(root.right, target - root.val)


# =============================================================================
# SECTION 7: BREADTH-FIRST SEARCH (BFS)
# =============================================================================

"""
BFS Pattern:
- Level-by-level exploration
- Uses queue
- Good for shortest path in unweighted graphs
"""


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """Level order traversal of binary tree."""
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)

    return result


def min_depth(root: Optional[TreeNode]) -> int:
    """Minimum depth of binary tree."""
    if not root:
        return 0

    queue = deque([(root, 1)])

    while queue:
        node, depth = queue.popleft()
        if not node.left and not node.right:
            return depth
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))

    return 0


# =============================================================================
# SECTION 8: BACKTRACKING
# =============================================================================

"""
Backtracking Pattern:
- Try all possibilities
- Backtrack when dead end
- Used for combinations/permutations
"""


def subsets(nums: List[List[int]]) -> List[List[int]]:
    """
    Generate all subsets.
    For each element, either include or exclude it.
    """
    result = []

    def backtrack(index, path):
        result.append(path[:])

        for i in range(index, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result


def permutations(nums: List[List[int]]) -> List[List[int]]:
    """
    Generate all permutations.
    Swap each element with subsequent elements.
    """
    result = []

    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
            return

        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    backtrack(0)
    return result


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """Find all combinations that sum to target."""
    result = []

    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path[:])
            return
        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, remaining - candidates[i])
            path.pop()

    backtrack(0, [], target)
    return result


# =============================================================================
# SECTION 9: DYNAMIC PROGRAMMING
# =============================================================================

"""
DP Patterns:
- Fibonacci: Build from previous states
- Knapsack: Choose or don't choose
- LIS: DP with binary search optimization
"""


def climb_stairs(n: int) -> int:
    """Climbing stairs - Fibonacci pattern."""
    if n <= 2:
        return n
    prev, curr = 1, 2
    for _ in range(3, n + 1):
        prev, curr = curr, prev + curr
    return curr


def house_robber(nums: List[int]) -> int:
    """House robber - don't rob adjacent houses."""
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    prev, curr = nums[0], max(nums[0], nums[1])
    for i in range(2, len(nums)):
        prev, curr = curr, max(curr, prev + nums[i])
    return curr


def coin_change(coins: List[int], amount: int) -> int:
    """Minimum coins to make amount."""
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1


def longest_increasing_subsequence(nums: List[int]) -> int:
    """LIS length - O(n^2) DP."""
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


def knapsack(values: List[int], weights: List[int], capacity: int) -> int:
    """0/1 Knapsack problem."""
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]


# =============================================================================
# SECTION 10: TESTING AND DEMO
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("LEETCODE PATTERNS - TEST DEMO")
    print("=" * 60)

    # Section 1: Two Pointers
    print("\n--- Section 1: Two Pointers ---")
    print(f"Two sum [1,2,4,6], target 8: {two_sum_sorted([1, 2, 4, 6], 8)}")
    arr = [1, 1, 2, 2, 3]
    new_len = remove_duplicates_sorted(arr)
    print(f"Remove duplicates: {arr[:new_len]}")
    print(f"Is 'racecar' palindrome: {is_palindrome('racecar')}")
    print(f"Container most water [1,8,6,2,5,4,8,3,7]: {container_with_most_water([1,8,6,2,5,4,8,3,7])}")

    # Section 2: Sliding Window
    print("\n--- Section 2: Sliding Window ---")
    print(f"Max sum 3 elements [2,1,5,2,3,2]: {max_sum_subarray_k([2,1,5,2,3,2], 3)}")
    print(f"Min subarray len >= 7 [2,3,1,2,4,3]: {min_subarray_len(7, [2,3,1,2,4,3])}")
    print(f"Longest k=2 'eceba': {longest_substring_k_distinct('eceba', 2)}")
    print(f"Longest no repeats 'abcabcbb': {longest_substring_no_repeats('abcabcbb')}")

    # Section 4: Binary Search
    print("\n--- Section 4: Binary Search ---")
    print(f"Binary search [1,2,3,4,5], 3: {binary_search([1,2,3,4,5], 3)}")
    print(f"Search insert [1,3,5,6], 5: {search_insert_position([1,3,5,6], 5)}")
    print(f"Search rotated [4,5,6,7,0,1,2], 0: {search_rotated([4,5,6,7,0,1,2], 0)}")

    # Section 5: Prefix Sum
    print("\n--- Section 5: Prefix Sum ---")
    print(f"Subarray sum equals k [1,1,1], k=2: {subarray_sum_k([1,1,1], 2)}")

    # Section 9: DP
    print("\n--- Section 9: Dynamic Programming ---")
    print(f"Climb stairs 5: {climb_stairs(5)}")
    print(f"House robber [1,2,3,1]: {house_robber([1,2,3,1])}")
    print(f"Coin change [1,2,5], 11: {coin_change([1,2,5], 11)}")
    print(f"LIS [10,9,2,5,3,7,101,18]: {longest_increasing_subsequence([10,9,2,5,3,7,101,18])}")

    print("\n" + "=" * 60)
    print("All patterns demo completed!")
    print("=" * 60)

"""
Comprehensive Algorithms - DP, Greedy, Sliding Window, Two Pointers, Bit Manipulation
================================================================================
Comprehensive Python implementations for advanced algorithm topics
commonly asked in FAANG interviews.
"""

from typing import List, Tuple


# =============================================================================
# SECTION 1: DYNAMIC PROGRAMMING - 1D
# =============================================================================

def fibonacci_dp(n: int) -> int:
    """Fibonacci with DP (bottom-up)."""
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def fibonacci_optimized(n: int) -> int:
    """Fibonacci with O(1) space."""
    if n <= 1:
        return n

    prev, curr = 0, 1

    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr

    return curr


def climb_stairs(n: int) -> int:
    """Climbing stairs problem."""
    if n <= 2:
        return n

    prev, curr = 1, 2

    for i in range(3, n + 1):
        prev, curr = curr, prev + curr

    return curr


def house_robber(nums: List[int]) -> int:
    """Maximum amount you can rob without robbing adjacent houses."""
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
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1

    return dp[amount] if dp[amount] != float('inf') else -1


def longest_increasing_subsequence(nums: List[int]) -> int:
    """LIS length."""
    if not nums:
        return 0

    dp = [1] * len(nums)

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


# =============================================================================
# SECTION 2: DYNAMIC PROGRAMMING - 2D
# =============================================================================

def unique_paths(m: int, n: int) -> int:
    """Unique paths in grid (robot movement)."""
    dp = [[1] * n for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]


def min_path_sum(grid: List[List[int]]) -> int:
    """Minimum path sum in grid."""
    m, n = len(grid), len(grid[0])

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                grid[i][j] += grid[i][j - 1]
            elif j == 0:
                grid[i][j] += grid[i - 1][j]
            else:
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

    return grid[m - 1][n - 1]


def longest_common_subsequence(s1: str, s2: str) -> int:
    """LCS length."""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


def edit_distance(s1: str, s2: str) -> int:
    """Minimum edits to convert s1 to s2."""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[m][n]


def longest_palindromic_subsequence(s: str) -> int:
    """LPS length."""
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2 if length > 2 else 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]


def word_break(s: str, word_dict: List[str]) -> bool:
    """Check if string can be segmented into dictionary words."""
    word_set = set(word_dict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[n]


# =============================================================================
# SECTION 3: GREEDY ALGORITHMS
# =============================================================================

def activity_selection(activities: List[Tuple[int, int]]) -> int:
    """Maximum number of non-overlapping activities."""
    activities.sort(key=lambda x: x[1])
    count = 1
    end = activities[0][1]

    for start, finish in activities[1:]:
        if start >= end:
            count += 1
            end = finish

    return count


def jump_game(nums: List[int]) -> bool:
    """Can we reach end of array."""
    max_reach = 0

    for i, jump in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + jump)

    return True


def jump_game_ii(nums: List[int]) -> int:
    """Minimum jumps to reach end."""
    if len(nums) <= 1:
        return 0

    jumps = 0
    current_end = 0
    max_reach = 0

    for i in range(len(nums) - 1):
        max_reach = max(max_reach, i + nums[i])

        if i == current_end:
            jumps += 1
            current_end = max_reach

    return jumps


def maximum_subarray_kadane(nums: List[int]) -> int:
    """Maximum sum subarray (Kadane's algorithm)."""
    max_sum = nums[0]
    current = nums[0]

    for num in nums[1:]:
        current = max(num, current + num)
        max_sum = max(max_sum, current)

    return max_sum


def partition_labels(s: str) -> List[int]:
    """Partition labels so each character appears once."""
    last = {c: i for i, c in enumerate(s)}

    result = []
    start = end = 0

    for i, c in enumerate(s):
        end = max(end, last[c])

        if i == end:
            result.append(end - start + 1)
            start = i + 1

    return result


# =============================================================================
# SECTION 4: SLIDING WINDOW
# =============================================================================

def max_sum_subarray_k(nums: List[int], k: int) -> int:
    """Maximum sum of k consecutive elements."""
    window = sum(nums[:k])
    max_sum = window

    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]
        max_sum = max(max_sum, window)

    return max_sum


def min_subarray_length(nums: List[int], target: int) -> int:
    """Minimum length with sum >= target."""
    left = 0
    current = 0
    min_len = float('inf')

    for right in range(len(nums)):
        current += nums[right]

        while current >= target:
            min_len = min(min_len, right - left + 1)
            current -= nums[left]
            left += 1

    return min_len if min_len != float('inf') else 0


def length_of_longest_substring_k_distinct(s: str, k: int) -> int:
    """Longest substring with at most k distinct characters."""
    char_count = {}
    left = 0
    max_len = 0

    for right, c in enumerate(s):
        char_count[c] = char_count.get(c, 0) + 1

        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


def fruit_into_baskets(fruits: List[int]) -> int:
    """Max fruits in two baskets."""
    left = 0
    fruit_count = {}
    max_fruits = 0

    for right, fruit in enumerate(fruits):
        fruit_count[fruit] = fruit_count.get(fruit, 0) + 1

        while len(fruit_count) > 2:
            fruit_count[fruits[left]] -= 1
            if fruit_count[fruits[left]] == 0:
                del fruit_count[fruits[left]]
            left += 1

        max_fruits = max(max_fruits, right - left + 1)

    return max_fruits


# =============================================================================
# SECTION 5: TWO POINTERS
# =============================================================================

def pair_sum_sorted(arr: List[int], target: int) -> List[int]:
    """Find pair with target sum in sorted array."""
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


def pair_sum_unsorted(arr: List[int], target: int) -> List[int]:
    """Find pair in unsorted array."""
    seen = {}

    for i, num in enumerate(arr):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i

    return []


def remove_duplicates(arr: List[int]) -> int:
    """Remove duplicates in-place."""
    if not arr:
        return 0

    slow = 0

    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]

    return slow + 1


def three_sum(nums: List[int]) -> List[List[int]]:
    """Find all unique triplets summing to zero."""
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return result


# =============================================================================
# SECTION 6: BIT MANIPULATION
# =============================================================================

def count_bits(n: int) -> int:
    """Count number of 1 bits."""
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count


def is_power_of_two(n: int) -> bool:
    """Check if n is power of 2."""
    return n > 0 and (n & (n - 1)) == 0


def swap_bits(x: int, i: int, j: int) -> int:
    """Swap bits at positions i and j."""
    if ((x >> i) & 1) != ((x >> j) & 1):
        x ^= (1 << i) | (1 << j)
    return x


def reverse_bits(n: int) -> int:
    """Reverse bits of integer."""
    result = 0

    for i in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1

    return result


def single_number(nums: List[int]) -> int:
    """Find number appearing once (all others twice)."""
    result = 0
    for num in nums:
        result ^= num
    return result


def missing_number(nums: List[int]) -> int:
    """Find missing number in 0..n."""
    result = len(nums)
    for i, num in enumerate(nums):
        result ^= i ^ num
    return result


def sum_two_integers(a: int, b: int) -> int:
    """Add two integers without + or -."""
    while b:
        carry = a & b
        a = a ^ b
        b = carry << 1

    return a


def reverse_integer(x: int) -> int:
    """Reverse digits of integer."""
    sign = -1 if x < 0 else 1
    x = abs(x)

    result = 0
    while x:
        result = result * 10 + x % 10
        x //= 10

    result *= sign

    if result < -2**31 or result > 2**31 - 1:
        return 0

    return result


# =============================================================================
# SECTION 7: TESTING
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("COMPREHENSIVE ALGORITHMS - TEST DEMO")
    print("=" * 60)

    # DP Tests
    print("\n--- Dynamic Programming ---")
    print(f"Fibonacci(10): {fibonacci_dp(10)}")
    print(f"Climb stairs(5): {climb_stairs(5)}")
    print(f"House robber([1,2,3,1]): {house_robber([1,2,3,1])}")
    print(f"Coin change([1,2,5], 11): {coin_change([1,2,5], 11)}")
    print(f"LIS([10,9,2,5,3,7]): {longest_increasing_subsequence([10,9,2,5,3,7])}")

    print("\n--- 2D DP ---")
    print(f"Unique paths(3,7): {unique_paths(3, 7)}")
    print(f"Edit distance('horse', 'ros'): {edit_distance('horse', 'ros')}")

    # Greedy Tests
    print("\n--- Greedy ---")
    activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10)]
    print(f"Activity selection: {activity_selection(activities)}")
    print(f"Jump game([2,3,1,1,4]): {jump_game([2,3,1,1,4])}")
    print(f"Jump game II([2,3,1,1,4]): {jump_game_ii([2,3,1,1,4])}")

    # Sliding Window Tests
    print("\n--- Sliding Window ---")
    print(f"Max sum of 3 in [2,1,5,2,3,4]: {max_sum_subarray_k([2,1,5,2,3,4], 3)}")
    print(f"Min subarray >= 7: {min_subarray_length([2,3,1,2,4,3], 7)}")

    # Two Pointers Tests
    print("\n--- Two Pointers ---")
    print(f"Pair sum [1,2,3,4,6] target 6: {pair_sum_sorted([1,2,3,4,6], 6)}")
    print(f"Remove duplicates [1,1,2,2,3]: {remove_duplicates([1,1,2,2,3])}")

    # Bit Manipulation Tests
    print("\n--- Bit Manipulation ---")
    print(f"Count bits(11): {count_bits(11)}")
    print(f"Is power of 2(8): {is_power_of_two(8)}")
    print(f"Single number [2,2,1]: {single_number([2,2,1])}")
    print(f"Missing number [3,0,1]: {missing_number([3,0,1])}")
    print(f"Sum of 1+2: {sum_two_integers(1, 2)}")

    print("\n" + "=" * 60)
    print("All tests completed!")
    print("=" * 60)

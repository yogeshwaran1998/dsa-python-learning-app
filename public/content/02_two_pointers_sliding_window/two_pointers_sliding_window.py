"""
Two Pointers & Sliding Window - Implementation and Examples
=========================================================
Comprehensive Python implementations commonly asked in FAANG interviews.
"""

from typing import List
from collections import Counter, defaultdict


# =============================================================================
# SECTION 1: TWO POINTERS - OPPOSITE DIRECTION (FIND PAIRS)
# =============================================================================

def pair_sum_sorted(arr: List[int], target: int) -> List[int]:
    """
    Find two numbers that add up to target in sorted array.

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


def three_sum(nums: List[int]) -> List[List[int]]:
    """
    Find all unique triplets that sum to zero.

    Time: O(n²), Space: O(1) excluding output
    """
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


def four_sum(nums: List[int], target: int) -> List[List[int]]:
    """Find all unique quadruplets that sum to target. Time: O(n³)"""
    nums.sort()
    result = []

    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, len(nums) - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            left, right = j + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]

                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1

    return result


# =============================================================================
# SECTION 2: TWO POINTERS - PARTITIONING
# =============================================================================

def partition_array(arr: List[int], pivot: int) -> int:
    """
    Dutch National Flag - partition around pivot.
    Elements < pivot left, == pivot middle, > pivot right.

    Time: O(n), Space: O(1)
    """
    left, mid, right = 0, 0, len(arr) - 1

    while mid <= right:
        if arr[mid] < pivot:
            arr[left], arr[mid] = arr[mid], arr[left]
            left += 1
            mid += 1
        elif arr[mid] == pivot:
            mid += 1
        else:
            arr[mid], arr[right] = arr[right], arr[mid]
            right -= 1

    return left


def sort_colors(nums: List[int]) -> None:
    """Sort colors (0=red, 1=white, 2=blue) in-place. Time: O(n)"""
    left = mid = 0
    right = len(nums) - 1

    while mid <= right:
        if nums[mid] == 0:
            nums[left], nums[mid] = nums[mid], nums[left]
            left += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[right] = nums[right], nums[mid]
            right -= 1


# =============================================================================
# SECTION 3: TWO POINTERS - SAME DIRECTION (REMOVE DUPLICATES)
# =============================================================================

def remove_duplicates_inplace(nums: List[int]) -> int:
    """
    Remove duplicates from sorted array in-place.

    Time: O(n), Space: O(1)
    """
    if not nums:
        return 0

    slow = 0

    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1


def remove_duplicates_allow_k(nums: List[int], k: int) -> int:
    """
    Remove duplicates allowing at most k occurrences.

    Time: O(n), Space: O(1)
    """
    if not nums or k < 1:
        return 0

    slow = 0
    count = 1

    for fast in range(1, len(nums)):
        if nums[fast] == nums[slow]:
            count += 1
        else:
            count = 1

        if count <= k:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1


# =============================================================================
# SECTION 4: CONTAINER PROBLEMS
# =============================================================================

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

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_area


def trap_rain_water(heights: List[int]) -> int:
    """Calculate trapped water between bars. Time: O(n), Space: O(1)"""
    if not heights:
        return 0

    left, right = 0, len(heights) - 1
    left_max, right_max = 0, 0
    water = 0

    while left < right:
        if heights[left] < heights[right]:
            if heights[left] >= left_max:
                left_max = heights[left]
            else:
                water += left_max - heights[left]
            left += 1
        else:
            if heights[right] >= right_max:
                right_max = heights[right]
            else:
                water += right_max - heights[right]
            right -= 1

    return water


# =============================================================================
# SECTION 5: LINKED LIST TWO POINTERS
# =============================================================================

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head: ListNode) -> bool:
    """Detect if linked list has cycle using Floyd's. Time: O(n)"""
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


def find_middle(head: ListNode) -> ListNode:
    """Find middle node of linked list. Time: O(n)"""
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def find_nth_from_end(head: ListNode, n: int) -> ListNode:
    """Find nth node from end in one pass. Time: O(n)"""
    fast = head
    slow = head

    for _ in range(n):
        if not fast:
            return None
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    return slow


# =============================================================================
# SECTION 6: SLIDING WINDOW - FIXED SIZE
# =============================================================================

def max_sum_subarray_k(arr: List[int], k: int) -> int:
    """
    Find maximum sum of k consecutive elements.

    Time: O(n), Space: O(1)
    """
    if len(arr) < k:
        return 0

    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum


def average_of_subarray_k(arr: List[float], k: int) -> List[float]:
    """Find average of all contiguous subarrays of size k."""
    if len(arr) < k:
        return []

    window_sum = sum(arr[:k])
    result = [window_sum / k]

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        result.append(window_sum / k)

    return result


def find_all_anagrams(s: str, p: str) -> List[int]:
    """Find all start indices of p's anagrams in s. Time: O(n + m)"""
    if len(p) > len(s):
        return []

    p_count = Counter(p)
    s_count = Counter()
    result = []

    for i in range(len(s)):
        s_count[s[i]] += 1

        if i >= len(p):
            s_count[s[i - len(p)]] -= 1
            if s_count[s[i - len(p)]] == 0:
                del s_count[s[i - len(p)]]

        if s_count == p_count:
            result.append(i - len(p) + 1)

    return result


# =============================================================================
# SECTION 7: SLIDING WINDOW - VARIABLE SIZE
# =============================================================================

def min_subarray_length(arr: List[int], target: int) -> int:
    """
    Find minimum length of contiguous subarray with sum >= target.

    Time: O(n), Space: O(1)
    """
    if not arr:
        return 0

    left = 0
    current_sum = 0
    min_length = float('inf')

    for right in range(len(arr)):
        current_sum += arr[right]

        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= arr[left]
            left += 1

    return min_length if min_length != float('inf') else 0


def longest_substring_k_distinct(s: str, k: int) -> int:
    """
    Find length of longest substring with at most k distinct characters.

    Time: O(n), Space: O(k)
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
    Find length of longest substring without repeating characters.

    Time: O(n), Space: O(min(n, alphabet_size))
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


def fruit_into_baskets(fruits: List[int]) -> int:
    """Maximum fruits with at most 2 types. Time: O(n), Space: O(1)"""
    fruit_count = {}
    left = 0
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
# SECTION 8: SLIDING WINDOW - ADVANCED
# =============================================================================

def count_subarrays_with_k_distinct(nums: List[int], k: int) -> int:
    """
    Count subarrays with exactly k distinct integers.

    Time: O(n), Space: O(k)
    Formula: atMostK(k) - atMostK(k-1)
    """
    def at_most_k(k):
        if k == 0:
            return 0

        count = 0
        freq = defaultdict(int)
        distinct = 0
        left = 0

        for right in range(len(nums)):
            if freq[nums[right]] == 0:
                distinct += 1
            freq[nums[right]] += 1

            while distinct > k:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    distinct -= 1
                left += 1

            count += right - left + 1

        return count

    return at_most_k(k) - at_most_k(k - 1)


def max_consecutive_ones_ii(nums: List[int]) -> int:
    """Longest sequence of 1s after flipping at most one 0."""
    left = 0
    zero_count = 0
    max_ones = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1

        while zero_count > 1:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        max_ones = max(max_ones, right - left + 1)

    return max_ones


def max_vowels(s: str, k: int) -> int:
    """Maximum vowels in any substring of length k."""
    vowels = set('aeiou')
    count = sum(1 for c in s[:k] if c in vowels)
    max_count = count

    for i in range(k, len(s)):
        if s[i - k] in vowels:
            count -= 1
        if s[i] in vowels:
            count += 1
        max_count = max(max_count, count)

    return max_count


# =============================================================================
# SECTION 9: TESTING
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("TWO POINTERS & SLIDING WINDOW - TEST DEMO")
    print("=" * 60)

    # Two Pointers - Pair Sum
    print("\n--- Two Pointers: Pair Sum ---")
    arr = [1, 2, 3, 4, 6]
    print(f"Pair summing to 5 in {arr}: {pair_sum_sorted(arr, 5)}")

    # Two Pointers - Three Sum
    print("\n--- Two Pointers: Three Sum ---")
    nums = [-1, 0, 1, 2, -1, -4]
    print(f"Three sum for {nums}:")
    for triplet in three_sum(nums):
        print(f"  {triplet}")

    # Two Pointers - Remove Duplicates
    print("\n--- Two Pointers: Remove Duplicates ---")
    nums = [1, 1, 1, 2, 2, 3]
    length = remove_duplicates_allow_k(nums, 2)
    print(f"Allow 2 duplicates: {nums[:length]}")

    # Two Pointers - Container
    print("\n--- Two Pointers: Container ---")
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(f"Max water in {heights}: {container_with_most_water(heights)}")

    # Sliding Window - Fixed
    print("\n--- Sliding Window: Fixed ---")
    arr = [2, 1, 5, 1, 3, 2]
    print(f"Max sum of 3 in {arr}: {max_sum_subarray_k(arr, 3)}")

    # Sliding Window - Variable
    print("\n--- Sliding Window: Variable ---")
    arr = [2, 3, 4, 2, 1, 5, 7]
    print(f"Min subarray >= 7 in {arr}: {min_subarray_length(arr, 7)}")

    s = "abcabcbb"
    print(f"Longest no repeats in '{s}': {longest_substring_no_repeats(s)}")

    # Anagrams
    print("\n--- Sliding Window: Anagrams ---")
    s = "cbaebabacb"
    p = "abc"
    print(f"Anagram indices in '{s}' for '{p}': {find_all_anagrams(s, p)}")

    # K Distinct
    print("\n--- Sliding Window: K Distinct ---")
    nums = [1, 2, 1, 2, 3]
    print(f"Exactly 2 distinct in {nums}: {count_subarrays_with_k_distinct(nums, 2)}")

    # Fruit baskets
    print("\n--- Sliding Window: Fruit Baskets ---")
    fruits = [1, 2, 1, 2, 3, 2, 2]
    print(f"Max fruits in 2 baskets: {fruit_into_baskets(fruits)}")

    # Sort colors
    print("\n--- Two Pointers: Sort Colors ---")
    nums = [2, 0, 2, 1, 1, 0]
    sort_colors(nums)
    print(f"Sorted: {nums}")

    print("\n" + "=" * 60)
    print("All tests completed!")
    print("=" * 60)

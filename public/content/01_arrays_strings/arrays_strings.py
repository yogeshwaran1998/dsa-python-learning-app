"""
Arrays and Strings - Implementation and Examples
================================================
Comprehensive Python implementations for arrays and strings patterns
commonly asked in FAANG interviews.
"""

from typing import List, Dict, Tuple, Optional
from collections import defaultdict, Counter


# =============================================================================
# SECTION 1: TWO POINTERS PATTERN
# =============================================================================

def two_sum_sorted(arr: List[int], target: int) -> List[int]:
    """
    Find two numbers that add up to target in a sorted array.
    Uses two pointers from both ends.

    Time: O(n), Space: O(1)
    """
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []  # No solution found


def two_sum_unsorted(arr: List[int], target: int) -> List[int]:
    """
    Find two numbers that add up to target in unsorted array.
    Uses hash map for O(n) time.

    Time: O(n), Space: O(n)
    """
    seen = {}  # value -> index

    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []


def remove_duplicates_inplace(nums: List[int]) -> int:
    """
    Remove duplicates in-place from sorted array.
    Returns the count of unique elements.

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


def remove_element_inplace(nums: List[int], val: int) -> int:
    """
    Remove all occurrences of val in-place.
    Returns the count of remaining elements.

    Time: O(n), Space: O(1)
    """
    slow = 0

    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1

    return slow


def partition_array(arr: List[int], pivot: int) -> int:
    """
    Partition array around pivot (Dutch National Flag problem).
    Elements < pivot on left, == pivot in middle, > pivot on right.

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
        else:  # arr[mid] > pivot
            arr[mid], arr[right] = arr[right], arr[mid]
            right -= 1

    return left  # Returns index after left partition


# =============================================================================
# SECTION 2: SLIDING WINDOW PATTERN
# =============================================================================

def max_sum_subarray_k(arr: List[int], k: int) -> int:
    """
    Find maximum sum of k consecutive elements.

    Time: O(n), Space: O(1)
    """
    if len(arr) < k:
        return 0

    # Calculate initial window
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Slide the window
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum


def min_subarray_length(arr: List[int], target: int) -> int:
    """
    Find minimum length of contiguous subarray with sum >= target.
    Returns 0 if no such subarray exists.

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
    Find longest substring with at most k distinct characters.

    Time: O(n), Space: O(k)
    """
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


def longest_substring_no_repeats(s: str) -> int:
    """
    Find length of longest substring without repeating characters.

    Time: O(n), Space: O(min(n, alphabet_size))
    """
    char_index = {}  # Last seen index of each character
    left = 0
    max_length = 0

    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1

        char_index[s[right]] = right
        max_length = max(max_length, right - left + 1)

    return max_length


def count_anagrams(s: str, pattern: str) -> int:
    """
    Count number of anagram occurrences of pattern in string s.

    Time: O(n + m), Space: O(1) - assuming fixed alphabet
    """
    if len(pattern) > len(s):
        return 0

    # Character frequency maps
    pattern_count = Counter(pattern)
    window_count = Counter()
    result = 0
    matched = 0

    # Initialize first window
    for i in range(len(pattern)):
        char = s[i]
        window_count[char] += 1
        if window_count[char] == pattern_count.get(char, 0):
            matched += 1

    if matched == len(pattern_count):
        result += 1

    # Slide window
    for i in range(len(pattern), len(s)):
        # Add new character
        new_char = s[i]
        window_count[new_char] += 1
        if window_count[new_char] == pattern_count.get(new_char, 0):
            matched += 1

        # Remove old character
        old_char = s[i - len(pattern)]
        if window_count[old_char] == pattern_count.get(old_char, 0):
            matched -= 1
        window_count[old_char] -= 1

        if matched == len(pattern_count):
            result += 1

    return result


# =============================================================================
# SECTION 3: PREFIX SUM PATTERN
# =============================================================================

class PrefixSum:
    """
    Prefix Sum data structure for efficient range queries.
    """

    def __init__(self, arr: List[int]):
        self.prefix = [0] * (len(arr) + 1)
        for i, num in enumerate(arr):
            self.prefix[i + 1] = self.prefix[i] + num

    def range_sum(self, left: int, right: int) -> int:
        """
        Calculate sum from index left to right (inclusive).

        Time: O(1), Space: O(n)
        """
        return self.prefix[right + 1] - self.prefix[left]


def subarray_sum_k(nums: List[int], k: int) -> int:
    """
    Find number of continuous subarrays that sum to k.

    Time: O(n), Space: O(n)
    """
    count = 0
    prefix_sum = 0
    sum_freq = {0: 1}  # prefix_sum -> frequency

    for num in nums:
        prefix_sum += num

        # If (prefix_sum - k) exists, we found a subarray summing to k
        if prefix_sum - k in sum_freq:
            count += sum_freq[prefix_sum - k]

        sum_freq[prefix_sum] = sum_freq.get(prefix_sum, 0) + 1

    return count


def subarray_divisible_k(nums: List[int], k: int) -> int:
    """
    Find number of continuous subarrays where sum is divisible by k.

    Time: O(n), Space: O(k)
    """
    count = 0
    prefix_sum = 0
    remainder_freq = [0] * k
    remainder_freq[0] = 1  # Empty prefix has remainder 0

    for num in nums:
        prefix_sum += num
        remainder = prefix_sum % k
        if remainder < 0:
            remainder += k  # Handle negative numbers

        count += remainder_freq[remainder]
        remainder_freq[remainder] += 1

    return count


# =============================================================================
# SECTION 4: KADANE'S ALGORITHM
# =============================================================================

def max_subarray_sum(nums: List[int]) -> int:
    """
    Find maximum sum of contiguous subarray (Kadane's algorithm).

    Time: O(n), Space: O(1)
    Returns empty array sum as 0 for empty input.
    """
    if not nums:
        return 0

    max_sum = nums[0]
    current_sum = nums[0]

    for num in nums[1:]:
        # Either extend previous subarray or start new one
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


def max_subarray_sum_with_indices(nums: List[int]) -> Tuple[int, int, int]:
    """
    Find maximum sum with start and end indices.

    Time: O(n), Space: O(1)
    Returns: (max_sum, start_index, end_index)
    """
    if not nums:
        return (0, -1, -1)

    max_sum = nums[0]
    current_sum = nums[0]
    start = 0
    end = 0
    temp_start = 0

    for i in range(1, len(nums)):
        current_sum += nums[i]

        if nums[i] > current_sum:
            current_sum = nums[i]
            temp_start = i

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    return (max_sum, start, end)


def max_subarray_product(nums: List[int]) -> int:
    """
    Find maximum product of contiguous subarray.

    Time: O(n), Space: O(1)
    """
    if not nums:
        return 0

    max_prod = nums[0]
    min_prod = nums[0]
    result = nums[0]

    for i in range(1, len(nums)):
        # When nums[i] is negative, max and min swap
        if nums[i] < 0:
            max_prod, min_prod = min_prod, max_prod

        max_prod = max(nums[i], max_prod * nums[i])
        min_prod = min(nums[i], min_prod * nums[i])
        result = max(result, max_prod)

    return result


# =============================================================================
# SECTION 5: CYCLIC SORT PATTERN
# =============================================================================

def find_missing_positive(nums: List[int]) -> int:
    """
    Find the smallest missing positive integer.

    Time: O(n), Space: O(1)

    Key insight: Place each number at its correct index (num-1)
    """
    n = len(nums)

    # Place each number in its correct position
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            correct_idx = nums[i] - 1
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]

    # Find first index where position doesn't match
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1


def find_all_duplicates(nums: List[int]) -> List[int]:
    """
    Find all numbers that appear twice in O(n) time and O(1) space.

    Time: O(n), Space: O(1) - excluding output
    """
    result = []

    for num in nums:
        idx = abs(num) - 1
        if nums[idx] < 0:
            result.append(abs(num))
        else:
            nums[idx] = -nums[idx]

    return result


def find_disappeared_numbers(nums: List[int]) -> List[int]:
    """
    Find all numbers from 1 to n that are missing.

    Time: O(n), Space: O(1) - excluding output
    """
    result = []

    for num in nums:
        idx = abs(num) - 1
        if nums[idx] > 0:
            nums[idx] = -nums[idx]

    for i in range(len(nums)):
        if nums[i] > 0:
            result.append(i + 1)

    return result


# =============================================================================
# SECTION 6: STRING ALGORITHMS
# =============================================================================

def reverse_string(s: List[str]) -> None:
    """
    Reverse string in-place.

    Time: O(n), Space: O(1)
    """
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


def reverse_words(s: str) -> str:
    """
    Reverse words in a string without extra space.

    Time: O(n), Space: O(1) - modifies in place conceptually
    """
    # Split, reverse, join - O(n) space for split
    words = s.split()
    return ' '.join(reversed(words))


def reverse_words_inplace(s: List[str]) -> None:
    """
    Reverse words in-place in character array.

    Time: O(n), Space: O(1)
    """
    # Step 1: Reverse entire array
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    # Step 2: Reverse each word
    start = 0
    while start < len(s):
        end = start
        while end < len(s) and s[end] != ' ':
            end += 1

        # Reverse word from start to end-1
        left, right = start, end - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        start = end + 1


def is_palindrome(s: str) -> bool:
    """
    Check if string is palindrome (alphanumeric only, case-insensitive).

    Time: O(n), Space: O(1)
    """
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


def longest_palindromic_substring(s: str) -> str:
    """
    Find longest palindromic substring using expand around center.

    Time: O(n²), Space: O(1)
    """
    if not s:
        return ""

    start, end = 0, 0

    for i in range(len(s)):
        # Odd length palindrome
        len1 = expand_around_center(s, i, i)
        # Even length palindrome
        len2 = expand_around_center(s, i, i + 1)

        max_len = max(len1, len2)

        if max_len > end - start + 1:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    return s[start:end + 1]


def expand_around_center(s: str, left: int, right: int) -> int:
    """
    Expand around center to find palindrome length.
    """
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    return right - left - 1


def minimum_window_substring(s: str, t: str) -> str:
    """
    Find minimum window substring of t in s.

    Time: O(n + m), Space: O(m) where m = len(t)
    """
    if not t or not s:
        return ""

    # Character frequency of pattern
    target_count = Counter(t)
    required = len(target_count)

    # Sliding window
    window_count = defaultdict(int)
    formed = 0
    left, right = 0, 0

    # Result tracking
    ans = float('inf'), 0, 0

    while right < len(s):
        char = s[right]
        window_count[char] += 1

        if char in target_count and window_count[char] == target_count[char]:
            formed += 1

        # Try to shrink window
        while formed == required:
            # Update answer
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)

            # Remove from left
            char = s[left]
            if char in target_count and window_count[char] == target_count[char]:
                formed -= 1
            window_count[char] -= 1
            left += 1

        right += 1

    return s[ans[1]:ans[2] + 1] if ans[0] != float('inf') else ""


# =============================================================================
# SECTION 7: COMMON UTILITY FUNCTIONS
# =============================================================================

def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """
    Merge overlapping intervals.

    Time: O(n log n), Space: O(n)
    """
    if not intervals:
        return []

    # Sort by start time
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = merged[-1][1]

        if start <= last_end:
            # Overlapping - extend the last interval
            merged[-1][1] = max(last_end, end)
        else:
            # Non-overlapping
            merged.append([start, end])

    return merged


def insert_interval(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    """
    Insert new interval into sorted, non-overlapping intervals.

    Time: O(n), Space: O(n)
    """
    merged = []
    i = 0
    n = len(intervals)
    start, end = new_interval

    # Add intervals before new_interval
    while i < n and intervals[i][1] < start:
        merged.append(intervals[i])
        i += 1

    # Merge overlapping intervals
    while i < n and intervals[i][0] <= end:
        start = min(start, intervals[i][0])
        end = max(end, intervals[i][1])
        i += 1

    merged.append([start, end])

    # Add remaining intervals
    while i < n:
        merged.append(intervals[i])
        i += 1

    return merged


def container_with_most_water(heights: List[int]) -> int:
    """
    Find container that holds most water.

    Time: O(n), Space: O(1) - Two pointers from both ends
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


def trapping_rain_water(heights: List[int]) -> int:
    """
    Calculate total water trapped between bars.

    Time: O(n), Space: O(1)
    """
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
# SECTION 8: TESTING AND DEMO
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("ARRAY AND STRING ALGORITHMS - TEST DEMO")
    print("=" * 60)

    # Test Two Pointers
    print("\n--- Two Pointers ---")
    arr = [1, 2, 3, 4, 6, 8, 9]
    target = 10
    result = two_sum_sorted(arr, target)
    print(f"Two sum for {arr} with target {target}: {result}")
    print(f"  -> Elements: {arr[result[0]]}, {arr[result[1]]}")

    # Test Remove Duplicates
    nums = [1, 1, 2, 2, 3, 4, 4, 5]
    new_len = remove_duplicates_inplace(nums)
    print(f"Remove duplicates: {nums[:new_len]} (length: {new_len})")

    # Test Sliding Window
    print("\n--- Sliding Window ---")
    arr = [2, 1, 5, 1, 3, 2]
    k = 3
    result = max_sum_subarray_k(arr, k)
    print(f"Max sum of {k} consecutive elements in {arr}: {result}")

    s = "cbbebi"
    result = longest_substring_k_distinct(s, 3)
    print(f"Longest substring with ≤3 distinct chars in '{s}': {result}")

    # Test Kadane
    print("\n--- Kadane's Algorithm ---")
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_sum, start, end = max_subarray_sum_with_indices(arr)
    print(f"Max subarray sum in {arr}: {max_sum}")
    print(f"  -> Subarray: {arr[start:end+1]}")

    # Test Cyclic Sort
    print("\n--- Cyclic Sort ---")
    nums = [3, 4, -1, 1]
    result = find_missing_positive(nums)
    print(f"First missing positive in {nums}: {result}")

    # Test String Algorithms
    print("\n--- String Algorithms ---")
    palindrome = "A man, a plan, a canal: Panama"
    print(f"Is '{palindrome[:20]}...' palindrome? {is_palindrome(palindrome)}")

    s = "babad"
    result = longest_palindromic_substring(s)
    print(f"Longest palindrome in '{s}': {result}")

    s = "ADOBECODEBANC"
    t = "ABC"
    result = minimum_window_substring(s, t)
    print(f"Minimum window for '{t}' in '{s}': '{result}'")

    # Test Intervals
    print("\n--- Interval Problems ---")
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    result = merge_intervals(intervals)
    print(f"Merged intervals {intervals}: {result}")

    heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    result = trapping_rain_water(heights)
    print(f"Trapped water in {heights}: {result} units")

    print("\n" + "=" * 60)
    print("All tests completed!")
    print("=" * 60)

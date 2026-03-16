"""
Sliding Window Pattern - Implementation and Examples
======================================================
Comprehensive Python implementations of sliding window technique
commonly asked in FAANG interviews.

Topics covered:
1. Fixed size sliding window
2. Variable size sliding window
3. Deque-based sliding window
4. Classic interview problems
"""

from typing import List, Optional, Dict
from collections import deque, Counter


# =============================================================================
# SECTION 1: FIXED SIZE SLIDING WINDOW
# =============================================================================

def max_sum_subarray_k(arr: List[int], k: int) -> int:
    """
    Find maximum sum of k consecutive elements.

    How it works:
    1. Calculate sum of first k elements (initial window)
    2. Slide window: subtract leftmost, add next element
    3. Track maximum sum

    Time: O(n), Space: O(1)

    Args:
        arr: List of integers
        k: Size of window

    Returns:
        Maximum sum of k consecutive elements

    Example:
        Input: [2, 1, 5, 1, 3, 2], k = 3
        Output: 9 (5+1+3 at indices 2,3,4)
    """
    # Edge case: array too small
    if len(arr) < k:
        return 0

    # Step 1: Calculate sum of first window of size k
    # This establishes our initial window from index 0 to k-1
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Step 2: Slide the window through the array
    # For each new position, we:
    # - Subtract the element leaving the window (arr[i - k])
    # - Add the new element entering the window (arr[i])
    for i in range(k, len(arr)):
        # Slide by removing leftmost element and adding new element
        # This is O(1) instead of recalculating entire sum (which would be O(k))
        window_sum += arr[i] - arr[i - k]

        # Update maximum if current window is larger
        max_sum = max(max_sum, window_sum)

    return max_sum


def average_of_subarray_k(arr: List[float], k: int) -> List[float]:
    """
    Calculate average of all contiguous subarrays of size k.

    How it works:
    - Same as max sum but divide by k for average
    - Slide window and compute average

    Time: O(n), Space: O(1) excluding output

    Args:
        arr: List of numbers
        k: Size of window

    Returns:
        List of averages for each window position
    """
    if len(arr) < k:
        return []

    # Calculate initial window sum
    window_sum = sum(arr[:k])
    result = [window_sum / k]

    # Slide window
    for i in range(k, len(arr)):
        # Add new element, remove old element
        window_sum += arr[i] - arr[i - k]
        result.append(window_sum / k)

    return result


def max_consecutive_ones(arr: List[int]) -> int:
    """
    Find maximum number of consecutive 1's in binary array.
    Uses fixed window where we count zeros.

    Time: O(n), Space: O(1)

    Args:
        arr: Binary array (0s and 1s)

    Returns:
        Maximum consecutive 1's after flipping at most one 0
    """
    # This is actually a variable window problem
    # But demonstrates sliding window thinking

    max_ones = 0  # Track max consecutive 1s
    zero_count = 0  # Count zeros in current window
    left = 0  # Left pointer of window

    # Expand window with right pointer
    for right in range(len(arr)):
        # If we see a zero, increment zero count
        if arr[right] == 0:
            zero_count += 1

        # If we have more than one zero, shrink from left
        while zero_count > 1:
            if arr[left] == 0:
                zero_count -= 1
            left += 1

        # Now window has at most 1 zero
        # Update max length
        max_ones = max(max_ones, right - left + 1)

    return max_ones


def contains_pattern(arr: List[int], pattern_len: int, repetitions: int) -> bool:
    """
    Check if array contains k repeated subarrays.

    Time: O(n), Space: O(1)

    Args:
        arr: List of integers
        pattern_len: Length of each pattern
        repetitions: Number of repetitions required

    Returns:
        True if pattern repeats, False otherwise

    Example:
        Input: [1,2,1,2,1,2], pattern_len=2, repetitions=3
        Output: True (pattern [1,2] repeats 3 times)
    """
    # Not a sliding window problem but uses similar iteration
    # Just for demonstration of window-based thinking

    n = len(arr)
    expected_len = pattern_len * repetitions

    if n < expected_len:
        return False

    # Get the first pattern to compare against
    = arr[:pattern_len]

    # Check each window of correct size
    for pattern i in range(1, n - expected_len + 1):
        window = arr[i:i + pattern_len]

        # Compare with original pattern
        if window == pattern:
            # Found matching start, check full repetition
            all_match = True
            for j in range(repetitions):
                start = i + j * pattern_len
                if arr[start:start + pattern_len] != pattern:
                    all_match = False
                    break

            if all_match:
                return True

    # Also check from start
    for i in range(1, n - expected_len + 1):
        all_match = True
        for j in range(repetitions):
            start = i + j * pattern_len
            if arr[start:start + pattern_len] != pattern:
                all_match = False
                break

        if all_match:
            return True

    return False


# =============================================================================
# SECTION 2: VARIABLE SIZE SLIDING WINDOW
# =============================================================================

def longest_substring_without_repeating(s: str) -> int:
    """
    Find length of longest substring without repeating characters.

    How it works:
    - Use two pointers: left (start of window), right (end)
    - Use set to track characters in current window
    - Expand right to include new character
    - Shrink left when duplicate found
    - Track maximum window size

    Time: O(n), Space: O(min(n, m)) where m is character set size

    Args:
        s: Input string

    Returns:
        Length of longest substring without repeating characters

    Example:
        Input: "abcabcbb"
        Output: 3 (substring "abc" or "bca" or "cab")
    """
    # Edge case: empty string
    if not s:
        return 0

    # Use set to track characters in current window
    # Set allows O(1) lookup for duplicates
    char_set = set()

    # Left pointer marks start of current window
    left = 0

    # Track maximum length found
    max_length = 0

    # Right pointer expands the window
    for right in range(len(s)):
        # Get current character
        current_char = s[right]

        # If character already in window, we have a duplicate
        # Need to shrink window from left until duplicate is removed
        while current_char in char_set:
            # Remove leftmost character from set
            char_set.remove(s[left])
            # Move left pointer forward (shrinking window)
            left += 1

        # Add current character to set (expanding window)
        char_set.add(current_char)

        # Update maximum length
        # Window is from left to right (inclusive), so +1
        max_length = max(max_length, right - left + 1)

    return max_length


def min_subarray_length(target: int, arr: List[int]) -> int:
    """
    Find minimum length of contiguous subarray with sum >= target.
    Returns 0 if no such subarray exists.

    How it works:
    - Expand window by moving right
    - Add elements to current sum
    - Shrink window from left while sum >= target
    - Track minimum length

    Time: O(n), Space: O(1)

    Args:
        target: Target sum
        arr: List of positive integers

    Returns:
        Minimum length of subarray with sum >= target

    Example:
        Input: target = 7, arr = [2,3,1,2,4,3]
        Output: 2 (subarray [4,3] has sum 7)
    """
    # Edge case: empty array
    if not arr:
        return 0

    # Initialize pointers and sum
    left = 0
    current_sum = 0
    min_length = float('inf')  # Start with infinity

    # Expand window with right pointer
    for right in range(len(arr)):
        # Add current element to sum
        current_sum += arr[right]

        # Shrink window while we have valid sum
        # Try to find minimum length
        while current_sum >= target:
            # Update minimum length
            current_length = right - left + 1
            min_length = min(min_length, current_length)

            # Remove leftmost element to try smaller window
            current_sum -= arr[left]
            left += 1

    # Return 0 if no valid subarray found
    return 0 if min_length == float('inf') else min_length


def fruit_into_baskets(fruits: List[int]) -> int:
    """
    Find maximum number of fruits we can collect with at most two types.
    Equivalent to finding longest substring with at most 2 unique characters.

    How it works:
    - Use sliding window with at most 2 unique types
    - Track count of each fruit type
    - Shrink window when third type added

    Time: O(n), Space: O(1) (at most 3 fruit types tracked)

    Args:
        fruits: List of integers representing fruit types

    Returns:
        Maximum number of fruits we can collect
    """
    # Use dictionary to track fruit counts in window
    fruit_count = {}

    # Pointers
    left = 0
    max_fruits = 0

    # Expand window
    for right in range(len(fruits)):
        # Add fruit to count
        fruit = fruits[right]
        fruit_count[fruit] = fruit_count.get(fruit, 0) + 1

        # Shrink window if we have more than 2 types
        while len(fruit_count) > 2:
            # Remove fruit at left pointer
            left_fruit = fruits[left]
            fruit_count[left_fruit] -= 1

            # Remove from dict if count becomes 0
            if fruit_count[left_fruit] == 0:
                del fruit_count[left_fruit]

            left += 1

        # Update maximum
        max_fruits = max(max_fruits, right - left + 1)

    return max_fruits


def longest_repeating_character_replacement(s: str, k: int) -> int:
    """
    Find length of longest substring that can be made by replacing
    at most k characters.

    How it works:
    - Track count of each character in window
    - Window is valid if (window_size - max_count) <= k
    - max_count is count of most frequent character
    - Expand window, shrink when invalid

    Time: O(n), Space: O(1) (26 letters)

    Args:
        s: Input string
        k: Maximum number of replacements allowed

    Returns:
        Length of longest substring after at most k replacements
    """
    # Edge cases
    if not s or k >= len(s):
        return len(s)

    # Track character counts in window
    char_count = [0] * 26  # 26 lowercase letters

    # Pointers
    left = 0
    max_count = 0  # Count of most frequent char in window
    max_length = 0

    for right in range(len(s)):
        # Add current character to count
        idx = ord(s[right]) - ord('a')
        char_count[idx] += 1

        # Update max count in current window
        max_count = max(max_count, char_count[idx])

        # Check if window is valid
        # Characters to replace = window_size - max_count
        # If > k, need to shrink window
        while (right - left + 1) - max_count > k:
            # Remove leftmost character
            left_idx = ord(s[left]) - ord('a')
            char_count[left_idx] -= 1
            left += 1

            # Note: we don't update max_count here
            # Because it may still be the max from another character

        # Update maximum length
        max_length = max(max_length, right - left + 1)

    return max_length


# =============================================================================
# SECTION 3: DEQUE-BASED SLIDING WINDOW
# =============================================================================

def max_sliding_window_deque(nums: List[int], k: int) -> List[int]:
    """
    Find maximum element in each sliding window of size k.
    Uses monotonic decreasing deque.

    How it works:
    - Maintain deque in decreasing order
    - Deque stores indices, not values
    - Front of deque is always index of maximum
    - Remove indices outside current window

    Time: O(n), Space: O(k)

    Args:
        nums: List of integers
        k: Window size

    Returns:
        List of maximum values for each window position

    Example:
        Input: [1,3,-1,-3,5,3,6,7], k=3
        Output: [3,3,5,5,6,7]
    """
    # Edge case
    if not nums or k == 0:
        return []

    # Monotonic decreasing deque
    # Stores indices of elements in decreasing order of their values
    # Front (left) always has the maximum
    dq = deque()

    result = []

    for i in range(len(nums)):
        # Step 1: Remove indices outside the window [i-k+1, i]
        # If front of deque is older than k positions, remove it
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # Step 2: Maintain monotonic decreasing order
        # Remove all indices with smaller value than current
        # (they can never be maximum while current element is in window)
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        # Step 3: Add current index to deque
        dq.append(i)

        # Step 4: Start recording results once we have full first window
        if i >= k - 1:
            # Front of deque is index of maximum for current window
            result.append(nums[dq[0]])

    return result


def min_sliding_window_deque(nums: List[int], k: int) -> List[int]:
    """
    Find minimum element in each sliding window of size k.
    Uses monotonic increasing deque.

    How it works:
    - Similar to max but maintain increasing order
    - Front always has minimum

    Time: O(n), Space: O(k)

    Args:
        nums: List of integers
        k: Window size

    Returns:
        List of minimum values for each window position
    """
    if not nums or k == 0:
        return []

    # Monotonic increasing deque
    dq = deque()

    result = []

    for i in range(len(nums)):
        # Remove indices outside window
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # Maintain increasing order (remove larger elements)
        while dq and nums[dq[-1]] > nums[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


# =============================================================================
# SECTION 4: MINIMUM WINDOW SUBSTRING (ADVANCED)
# =============================================================================

def min_window_substring(s: str, t: str) -> str:
    """
    Find minimum window in s that contains all characters of t.
    Maintains counts of required characters.

    How it works:
    1. Create frequency count of characters needed in t
    2. Expand window to include all needed characters
    3. Shrink window while still valid
    4. Track minimum valid window

    Time: O(n + m), Space: O(m) where m is charset size

    Args:
        s: Source string
        t: Target string (pattern)

    Returns:
        Minimum window substring containing all of t, or empty string

    Example:
        Input: s = "ADOBECODEBANC", t = "ABC"
        Output: "BANC"
    """
    # Edge cases
    if not s or not t:
        return ""

    # Create dictionary of character counts needed
    # This is our "requirement" to satisfy the pattern
    need = Counter(t)

    # Track how many required characters we have in current window
    # When all values in window_counts match or exceed need, window is valid
    window_counts = Counter()

    # Track number of unique characters satisfied
    # When equals len(need), we have a valid window
    have = 0
    need_len = len(need)

    # Pointers
    left = 0
    min_len = float('inf')
    min_start = 0

    # Expand window with right pointer
    for right in range(len(s)):
        # Add current character to window
        char = s[right]
        window_counts[char] += 1

        # Check if this character satisfies a requirement
        # (only if we still need it)
        if char in need and window_counts[char] == need[char]:
            have += 1

        # While we have a valid window, try to shrink it
        while have == need_len:
            # Update minimum if this is smaller
            current_len = right - left + 1
            if current_len < min_len:
                min_len = current_len
                min_start = left

            # Try to shrink from left
            left_char = s[left]
            window_counts[left_char] -= 1

            # If removing this breaks validity, stop shrinking
            if left_char in need and window_counts[left_char] < need[left_char]:
                have -= 1

            left += 1

    # Return empty string if no valid window found
    return "" if min_len == float('inf') else s[min_start:min_start + min_len]


# =============================================================================
# SECTION 5: SLIDING WINDOW WITH HASHTABLE
# =============================================================================

def find_anagrams(s: str, p: str) -> List[int]:
    """
    Find all starting indices of anagrams of p in s.
    An anagram is a permutation of p.

    How it works:
    - Use sliding window of size len(p)
    - Compare character frequencies in window
    - Use hash-based comparison

    Time: O(n), Space: O(1)

    Args:
        s: Source string
        p: Pattern string

    Returns:
        List of starting indices of anagrams
    """
    if not s or not p or len(p) > len(s):
        return []

    # Character counts
    p_count = Counter(p)
    window_count = Counter()

    # Window size is length of p
    p_len = len(p)
    result = []

    # Build initial window
    for i in range(p_len):
        window_count[s[i]] += 1

    # Check if first window is anagram
    if window_count == p_count:
        result.append(0)

    # Slide window through rest of string
    for i in range(p_len, len(s)):
        # Add new character (right side of window)
        window_count[s[i]] += 1

        # Remove old character (left side of window)
        left_char = s[i - p_len]
        window_count[left_char] -= 1

        # Clean up zero counts
        if window_count[left_char] == 0:
            del window_count[left_char]

        # Check if current window is anagram
        if window_count == p_count:
            result.append(i - p_len + 1)

    return result


def count_vowels_substrings(s: str) -> int:
    """
    Count number of substrings where all characters are vowels.

    Time: O(n), Space: O(1)

    Args:
        s: Input string

    Returns:
        Count of substrings with only vowels
    """
    vowels = set('aeiou')
    count = 0
    window_size = 0

    for char in s:
        if char in vowels:
            # Each vowel extends all previous vowel-only substrings
            # Plus starts a new substring of length 1
            window_size += 1
            count += window_size
        else:
            # Reset window when consonant encountered
            window_size = 0

    return count


# =============================================================================
# TEST FUNCTIONS
# =============================================================================

def run_tests():
    """Run test cases for all implementations."""

    # Test max_sum_subarray_k
    arr = [2, 1, 5, 1, 3, 2]
    result = max_sum_subarray_k(arr, 3)
    print(f"Max Sum Subarray (k=3): {result}")  # Expected: 9

    # Test longest_substring_without_repeating
    s = "abcabcbb"
    result = longest_substring_without_repeating(s)
    print(f"Longest Substring Without Repeating: {result}")  # Expected: 3

    # Test min_subarray_length
    result = min_subarray_length(7, [2, 3, 1, 2, 4, 3])
    print(f"Min Subarray Length >= 7: {result}")  # Expected: 2

    # Test max_sliding_window_deque
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    result = max_sliding_window_deque(nums, 3)
    print(f"Max Sliding Window: {result}")  # Expected: [3,3,5,5,6,7]

    # Test min_window_substring
    s = "ADOBECODEBANC"
    t = "ABC"
    result = min_window_substring(s, t)
    print(f"Min Window Substring: '{result}'")  # Expected: "BANC"

    # Test fruit_into_baskets
    fruits = [1, 2, 1, 2, 3, 2, 2]
    result = fruit_into_baskets(fruits)
    print(f"Fruit Into Baskets: {result}")  # Expected: 5

    # Test find_anagrams
    s = "cbaebabacb"
    p = "abc"
    result = find_anagrams(s, p)
    print(f"Find Anagrams: {result}")  # Expected: [0, 6]


if __name__ == "__main__":
    run_tests()

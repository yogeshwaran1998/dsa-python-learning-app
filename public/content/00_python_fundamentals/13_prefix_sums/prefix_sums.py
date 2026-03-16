"""
Prefix Sums Pattern - Implementation and Examples
==================================================
Comprehensive Python implementations of prefix sums technique
commonly asked in FAANG interviews.

Topics covered:
1. 1D Prefix Sums
2. 2D Prefix Sums
3. Range sum queries
4. Subarray sum problems
"""

from typing import List, Tuple


# =============================================================================
# SECTION 1: 1D PREFIX SUMS
# =============================================================================

class PrefixSum1D:
    """
    Immutable array with prefix sum preprocessing.
    Allows O(1) range sum queries after O(n) preprocessing.
    """

    def __init__(self, nums: List[int]):
        """
        Precompute prefix sums for efficient range queries.

        How it works:
        - prefix[i] = sum of nums[0] to nums[i] inclusive
        - We prepend 0 to handle edge cases easily
        - prefix[0] = 0 means "sum of nothing"

        Time: O(n), Space: O(n)

        Args:
            nums: Input array
        """
        # Edge case: empty array
        if not nums:
            self.prefix = [0]
            return

        # Create prefix sum array
        # Length is n+1 to handle queries from index 0
        n = len(nums)
        self.prefix = [0] * (n + 1)

        # Build prefix sums iteratively
        # prefix[i+1] = prefix[i] + nums[i]
        # This means prefix[i] = sum of first i elements (0 to i-1)
        for i in range(n):
            # At index i, we add nums[i] to previous sum
            self.prefix[i + 1] = self.prefix[i] + nums[i]

    def range_sum(self, left: int, right: int) -> int:
        """
        Calculate sum of elements from index left to right (inclusive).

        How it works:
        - Sum from 0 to right = prefix[right + 1]
        - Sum from 0 to left-1 = prefix[left]
        - Desired sum = prefix[right + 1] - prefix[left]

        Time: O(1), Space: O(1)

        Args:
            left: Starting index (inclusive)
            right: Ending index (inclusive)

        Returns:
            Sum of elements in range [left, right]

        Example:
            nums = [1, 2, 3, 4, 5]
            prefix = [0, 1, 3, 6, 10, 15]
            range_sum(1, 3) = prefix[4] - prefix[1] = 6 - 1 = 5
        """
        # Validate indices
        if left < 0 or right >= len(self.prefix) - 1:
            raise IndexError("Indices out of bounds")

        # Key insight: prefix[right+1] includes elements up to right
        # prefix[left] includes elements before left
        # Subtracting gives us elements from left to right
        return self.prefix[right + 1] - self.prefix[left]


def running_sum(nums: List[int]) -> List[int]:
    """
    Calculate running sum of array elements in-place.
    Transform array where each element becomes sum of all previous elements.

    How it works:
    - Modify array in-place
    - Each element = previous element + current original value

    Time: O(n), Space: O(1)

    Args:
        nums: Input array (modified in-place)

    Returns:
        Array with running sums

    Example:
        Input: [1, 2, 3, 4]
        Output: [1, 3, 6, 10]
    """
    # Iterate from index 1
    # Each element adds the previous cumulative sum
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]

    return nums


def pivot_index(nums: List[int]) -> int:
    """
    Find the pivot index where left sum equals right sum.

    How it works:
    - Calculate total sum first
    - Iterate and maintain left sum
    - At pivot: left_sum == total - left_sum - nums[i]

    Time: O(n), Space: O(1)

    Args:
        nums: List of integers

    Returns:
        Index of pivot, or -1 if none exists
    """
    # Calculate total sum of all elements
    total = sum(nums)

    # Track sum of elements to the left of current index
    left_sum = 0

    # Iterate through array
    for i, num in enumerate(nums):
        # Right sum = total - left_sum - current element
        # Check if left equals right
        if left_sum == total - left_sum - num:
            return i

        # Add current element to left sum for next iteration
        left_sum += num

    # No pivot found
    return -1


def subarray_sum_equals_k_bruteforce(nums: List[int], k: int) -> int:
    """
    Count number of continuous subarrays that sum to k.
    Uses prefix sums for O(n^2) solution.

    How it works:
    - Build prefix sums
    - For each possible range, check if sum equals k

    Time: O(n^2), Space: O(n)
    """
    n = len(nums)
    # Build prefix sums
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    count = 0

    # Check all possible ranges
    for i in range(n):
        for j in range(i + 1, n + 1):
            # Sum from i to j-1 = prefix[j] - prefix[i]
            if prefix[j] - prefix[i] == k:
                count += 1

    return count


# =============================================================================
# SECTION 2: SUBARRAY SUM EQUALS K (OPTIMIZED)
# =============================================================================

def subarray_sum_equals_k(nums: List[int], k: int) -> int:
    """
    Count number of continuous subarrays that sum to k.
    Uses hashmap to achieve O(n) time.

    How it works:
    - Key insight: if prefix[j] - prefix[i] = k, then prefix[i] = prefix[j] - k
    - For each prefix sum, count how many previous prefix sums equal (current - k)
    - Use hashmap to store counts of prefix sums seen so far

    Time: O(n), Space: O(n)

    Args:
        nums: List of integers (can include negative numbers)
        k: Target sum

    Returns:
        Number of continuous subarrays with sum equal to k

    Example:
        Input: nums = [1, 1, 1], k = 2
        Output: 2 (subarrays: [1,1] at index 0-1 and 1-2)
    """
    # Hashmap to store count of prefix sums
    # prefix_sum -> count of occurrences
    prefix_count = {0: 1}  # Initialize with 0 to handle subarrays starting at 0

    # Current prefix sum
    prefix = 0

    # Count of valid subarrays
    count = 0

    # Iterate through array
    for num in nums:
        # Update current prefix sum
        prefix += num

        # Check if (prefix - k) exists in hashmap
        # This means there was a prefix sum earlier that when subtracted
        # from current prefix gives us k
        if prefix - k in prefix_count:
            # Add count of such prefix sums
            count += prefix_count[prefix - k]

        # Add/update current prefix sum in hashmap
        prefix_count[prefix] = prefix_count.get(prefix, 0) + 1

    return count


def subarray_sum_equals_k_with_indices(nums: List[int], k: int) -> List[List[int]]:
    """
    Find all continuous subarrays that sum to k.
    Returns list of [start, end] indices.

    Time: O(n), Space: O(n)

    Args:
        nums: List of integers
        k: Target sum

    Returns:
        List of [start, end] pairs for each valid subarray
    """
    # Store prefix sum and the indices where it occurs
    prefix_map = {0: [-1]}  # prefix sum 0 occurs at index -1 (before array)
    prefix = 0
    result = []

    for i, num in enumerate(nums):
        prefix += num

        # Check if prefix - k exists
        target = prefix - k
        if target in prefix_map:
            # Each occurrence gives us a valid subarray
            for start in prefix_map[target]:
                result.append([start + 1, i])

        # Add current index to map
        if prefix not in prefix_map:
            prefix_map[prefix] = []
        prefix_map[prefix].append(i)

    return result


# =============================================================================
# SECTION 3: 2D PREFIX SUMS
# =============================================================================

class PrefixSum2D:
    """
    2D matrix with prefix sum preprocessing.
    Allows O(1) rectangle sum queries after O(m*n) preprocessing.
    """

    def __init__(self, matrix: List[List[int]]):
        """
        Precompute 2D prefix sums for efficient rectangle queries.

        How it works:
        - prefix[i][j] = sum of all elements in rectangle (0,0) to (i-1, j-1)
        - Uses inclusion-exclusion principle

        Time: O(m*n), Space: O(m*n)

        Args:
            matrix: 2D matrix of integers
        """
        # Edge case: empty matrix
        if not matrix or not matrix[0]:
            self.prefix = [[]]
            return

        m = len(matrix)
        n = len(matrix[0])

        # Create prefix sum matrix with extra row and column
        # This makes it easier to handle boundary conditions
        # prefix has dimensions (m+1) x (n+1)
        self.prefix = [[0] * (n + 1) for _ in range(m + 1)]

        # Build prefix sums
        # For each cell, sum = current + top + left - top-left
        for i in range(m):
            for j in range(n):
                # Inclusion-exclusion principle:
                # Sum of rectangle (0,0) to (i,j) =
                #   matrix[i][j] +
                #   prefix[i][j+1] (rectangle above) +
                #   prefix[i+1][j] (rectangle to left) -
                #   prefix[i][j] (overlapping rectangle counted twice)
                self.prefix[i + 1][j + 1] = (
                    matrix[i][j] +
                    self.prefix[i][j + 1] +
                    self.prefix[i + 1][j] -
                    self.prefix[i][j]
                )

    def rectangle_sum(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
        Calculate sum of elements in rectangle from (row1, col1) to (row2, col2).

        How it works:
        - Use inclusion-exclusion principle
        - Sum of rectangle = bottom-right - top - left + top-left

        Time: O(1), Space: O(1)

        Args:
            row1: Top row index
            col1: Left column index
            row2: Bottom row index
            col2: Right column index

        Returns:
            Sum of all elements in the rectangle

        Example:
            matrix = [[1,2,3],[4,5,6],[7,8,9]]
            rectangle_sum(1,1,2,2) = 5+6+8+9 = 28
        """
        # Validate indices
        if not self.prefix or not self.prefix[0]:
            return 0

        # Key: Use prefix array which has extra row/column
        # prefix indices are shifted by 1 compared to matrix indices
        #
        # Visual explanation:
        # prefix[row2+1][col2+1] contains sum of (0,0) to (row2, col2)
        # prefix[row1][col2+1] contains sum of (0,0) to (row1-1, col2)
        # prefix[row2+1][col1] contains sum of (0,0) to (row2, col1-1)
        # prefix[row1][col1] contains sum of (0,0) to (row1-1, col1-1)
        #
        # Using inclusion-exclusion:
        # desired = prefix[row2+1][col2+1] - prefix[row1][col2+1]
        #            - prefix[row2+1][col1] + prefix[row1][col1]

        return (
            self.prefix[row2 + 1][col2 + 1] -
            self.prefix[row1][col2 + 1] -
            self.prefix[row2 + 1][col1] +
            self.prefix[row1][col1]
        )


def matrix_block_sum(mat: List[List[int]], k: int) -> List[List[int]]:
    """
    Calculate sum of elements in k x k blocks around each cell.
    For each cell (i, j), sum elements from (i-k, j-k) to (i+k, j+k).

    How it works:
    - Build 2D prefix sum first
    - For each cell, query rectangle sum in O(1)

    Time: O(m*n), Space: O(m*n)

    Args:
        mat: 2D matrix
        k: Block size (radius)

    Returns:
        Matrix where each cell contains sum of k-neighborhood
    """
    if not mat or not mat[0]:
        return []

    m = len(mat)
    n = len(mat[0])

    # Build prefix sum
    prefix = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            prefix[i + 1][j + 1] = (
                mat[i][j] +
                prefix[i][j + 1] +
                prefix[i + 1][j] -
                prefix[i][j]
            )

    # Build result matrix
    result = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            # Calculate bounds of k-neighborhood
            # Clamp to matrix boundaries
            row1 = max(0, i - k)
            col1 = max(0, j - k)
            row2 = min(m - 1, i + k)
            col2 = min(n - 1, j + k)

            # Query rectangle sum using prefix
            result[i][j] = (
                prefix[row2 + 1][col2 + 1] -
                prefix[row1][col2 + 1] -
                prefix[row2 + 1][col1] +
                prefix[row1][col1]
            )

    return result


# =============================================================================
# SECTION 4: PREFIX SUM VARIATIONS
# =============================================================================

def subarray_divisible_by_k(nums: List[int], k: int) -> int:
    """
    Count number of continuous subarrays where sum is divisible by k.

    How it works:
    - Use prefix sums and modulo
    - If prefix[i] % k == prefix[j] % k, then (i,j) subarray is divisible
    - Use hashmap to count occurrences of each remainder

    Time: O(n), Space: O(k)

    Args:
        nums: List of integers
        k: Divisor

    Returns:
        Count of subarrays where sum is divisible by k
    """
    # Hashmap to count remainder occurrences
    remainder_count = {0: 1}  # Initialize for subarrays starting at 0
    prefix = 0
    count = 0

    for num in nums:
        prefix += num

        # Python handles negative modulo differently
        # We need to normalize to positive remainder
        remainder = prefix % k
        if remainder < 0:
            remainder += k

        # Add to count if we've seen this remainder before
        count += remainder_count.get(remainder, 0)

        # Record this remainder
        remainder_count[remainder] = remainder_count.get(remainder, 0) + 1

    return count


def maximum_subarray_sum_with_k(nums: List[int], k: int) -> int:
    """
    Find maximum sum subarray of length exactly k using prefix sums.

    Time: O(n), Space: O(n)

    Args:
        nums: List of integers
        k: Required subarray length

    Returns:
        Maximum sum of any subarray with length exactly k
    """
    if not nums or k > len(nums):
        return 0

    # Build prefix sums
    prefix = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        prefix[i + 1] = prefix[i] + nums[i]

    # Find maximum difference with exactly k distance
    max_sum = float('-inf')

    for i in range(len(nums) - k + 1):
        # Sum of subarray from i to i+k-1
        current_sum = prefix[i + k] - prefix[i]
        max_sum = max(max_sum, current_sum)

    return max_sum


def prefix_sum_with_range_queries():
    """
    Demonstrate prefix sum with multiple range queries.
    Useful for interview pattern.
    """
    # Example: Multiple queries on same array
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Build prefix sum
    prefix = PrefixSum1D(nums)

    # Answer multiple queries in O(1) each
    queries = [(0, 4), (3, 7), (0, 9), (2, 5)]

    for left, right in queries:
        result = prefix.range_sum(left, right)
        print(f"Sum from {left} to {right}: {result}")


# =============================================================================
# SECTION 5: DIFFERENCE ARRAY (RELATED TO PREFIX SUMS)
# =============================================================================

def range_update_array(nums: List[int], operations: List[List[int]]) -> List[int]:
    """
    Apply multiple range increment operations efficiently.
    Uses difference array technique.

    How it works:
    - Instead of updating each element in range (O(n) per operation)
    - Use difference array for O(1) range update
    - Convert back to actual array at the end

    Time: O(n + m) where m = number of operations, Space: O(n)

    Args:
        nums: Initial array
        operations: List of [start, end, val] to add val to range [start, end]

    Returns:
        Array after all operations
    """
    n = len(nums)

    # Create difference array
    # diff[i] = nums[i] - nums[i-1] (with nums[-1] = 0)
    diff = [0] * (n + 1)  # Extra element for easier handling

    # Apply each operation to difference array
    for start, end, val in operations:
        # Adding val to range [start, end]
        diff[start] += val
        diff[end + 1] -= val  # Next element after range

    # Convert difference array back to actual array
    # prefix sum of diff gives us the final array
    result = [0] * n
    current = 0

    for i in range(n):
        current += diff[i]
        result[i] = nums[i] + current

    return result


# =============================================================================
# TEST FUNCTIONS
# =============================================================================

def run_tests():
    """Run test cases for all implementations."""

    # Test 1D prefix sum
    nums = [1, 2, 3, 4, 5]
    prefix = PrefixSum1D(nums)
    print(f"Prefix Sum 1D - Range [1,3]: {prefix.range_sum(1, 3)}")  # 9

    # Test running sum
    nums = [1, 2, 3, 4]
    result = running_sum(nums.copy())
    print(f"Running Sum: {result}")  # [1,3,6,10]

    # Test pivot index
    nums = [1, 7, 3, 6, 5, 6]
    result = pivot_index(nums)
    print(f"Pivot Index: {result}")  # 3

    # Test subarray sum equals k
    nums = [1, 1, 1]
    result = subarray_sum_equals_k(nums, 2)
    print(f"Subarray Sum Equals K: {result}")  # 2

    # Test 2D prefix sum
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    prefix2d = PrefixSum2D(matrix)
    result = prefix2d.rectangle_sum(1, 1, 2, 2)
    print(f"Prefix Sum 2D - Rectangle: {result}")  # 28

    # Test matrix block sum
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = matrix_block_sum(mat, 1)
    print(f"Matrix Block Sum: {result}")

    # Test subarray divisible by k
    nums = [4, 5, 0, -2, -3, 1]
    result = subarray_divisible_by_k(nums, 5)
    print(f"Subarray Divisible by K: {result}")  # 7


if __name__ == "__main__":
    run_tests()

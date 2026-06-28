"""
Bit Manipulation - Implementation and Examples
=============================================
Comprehensive Python implementations for bit manipulation problems
commonly asked in FAANG interviews.
"""

from typing import List


# =============================================================================
# SECTION 1: BASIC BIT OPERATIONS
# =============================================================================

def get_bit(num: int, i: int) -> int:
    """Get bit at position i (0-indexed from right)."""
    return (num >> i) & 1


def set_bit(num: int, i: int) -> int:
    """Set bit at position i to 1."""
    return num | (1 << i)


def clear_bit(num: int, i: int) -> int:
    """Clear bit at position i to 0."""
    return num & ~(1 << i)


def update_bit(num: int, i: int, bit: int) -> int:
    """Set bit at position i to given bit value."""
    mask = ~(1 << i)
    return (num & mask) | (bit << i)


def count_set_bits(num: int) -> int:
    """Count number of 1 bits (population count)."""
    count = 0
    while num:
        num &= num - 1  # Remove rightmost set bit
        count += 1
    return count


def count_set_bits_builtin(num: int) -> int:
    """Count using built-in function."""
    return bin(num).count('1')


# =============================================================================
# SECTION 2: COMMON TRICKS
# =============================================================================

def is_power_of_two(num: int) -> bool:
    """
    Check if n is power of 2.

    Time: O(1), Space: O(1)

    Key: n & (n-1) clears the only set bit
    """
    return num > 0 and (num & (num - 1)) == 0


def is_power_of_four(num: int) -> bool:
    """Check if n is power of 4."""
    if num <= 0:
        return False

    # Check power of 2 and only one bit set
    if num & (num - 1) != 0:
        return False

    # Check bit is at odd position
    return num & 0x55555555 != 0


def reverse_bits(num: int, bits: int = 32) -> int:
    """
    Reverse bits of integer.

    Time: O(bits), Space: O(1)
    """
    result = 0

    for i in range(bits):
        if num & (1 << i):
            result |= 1 << (bits - 1 - i)

    return result


def reverse_bits_optimized(num: int) -> int:
    """
    Reverse bits using magic.

    Time: O(1), Space: O(1)
    """
    # 32-bit magic numbers
    num = (num >> 16) | (num << 16)  # swap halfs
    num = ((num & 0xFF00FF00) >> 8) | ((num & 0x00FF00FF) << 8)
    num = ((num & 0xF0F0F0F0) >> 4) | ((num & 0x0F0F0F0F) << 4)
    num = ((num & 0xCCCCCCCC) >> 2) | ((num & 0x33333333) << 2)
    num = ((num & 0xAAAAAAAA) >> 1) | ((num & 0x55555555) << 1)
    return num


def swap_bits(num: int, i: int, j: int) -> int:
    """
    Swap bits at positions i and j.

    Time: O(1), Space: O(1)
    """
    if ((num >> i) & 1) != ((num >> j) & 1):
        num ^= (1 << i) | (1 << j)
    return num


def single_number(nums: List[int]) -> int:
    """
    Find number appearing once (others appear twice).

    Time: O(n), Space: O(1)

    Key: a ^ a = 0, a ^ 0 = a
    """
    result = 0
    for num in nums:
        result ^= num
    return result


def single_number_ii(nums: List[int]) -> int:
    """
    Find number appearing once (others appear 3 times).

    Time: O(n), Space: O(1)

    Using bitmask approach
    """
    ones = 0
    twos = 0

    for num in nums:
        ones = (ones ^ num) & ~twos
        twos = (twos ^ num) & ~ones

    return ones


def missing_number(nums: List[int]) -> int:
    """
    Find missing number in 0..n.

    Time: O(n), Space: O(1)

    XOR all indices and values
    """
    result = len(nums)
    for i, num in enumerate(nums):
        result ^= i ^ num
    return result


def find_duplicate(nums: List[int]) -> int:
    """
    Find duplicate number (without modifying array).

    Time: O(n), Space: O(1)
    """
    slow = nums[0]
    fast = nums[0]

    # Find intersection
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Find entrance to cycle
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow


# =============================================================================
# SECTION 3: ARITHMETIC OPERATIONS
# =============================================================================

def add_without_plus(a: int, b: int) -> int:
    """
    Add two integers without + or -.

    Mask to 32 bits each step so the carry terminates: Python ints are
    arbitrary precision, so an unmasked carry on a negative operand would
    shift forever. Reinterpret the final 32-bit value as signed.

    Time: O(1), Space: O(1)
    """
    mask = 0xFFFFFFFF
    while b & mask:
        carry = (a & b) & mask
        a = (a ^ b) & mask
        b = carry << 1

    a &= mask
    # If the sign bit (bit 31) is set, the result is negative in two's complement.
    return a if a <= 0x7FFFFFFF else ~(a ^ mask)


def subtract_without_minus(a: int, b: int) -> int:
    """
    Subtract without - using two's complement.
    a - b = a + (~b + 1)
    """
    return add_without_plus(a, add_without_plus(~b, 1))


def multiply_without_star(a: int, b: int) -> int:
    """
    Multiply without * using shift and add.
    """
    result = 0
    is_negative = (a < 0) ^ (b < 0)

    a = abs(a)
    b = abs(b)

    while b:
        if b & 1:
            result = add_without_plus(result, a)
        a <<= 1
        b >>= 1

    return -result if is_negative else result


def divide_without_slash(a: int, b: int) -> int:
    """
    Divide without / using shift and subtract.
    """
    if b == 0:
        raise ZeroDivisionError

    is_negative = (a < 0) ^ (b < 0)

    a = abs(a)
    b = abs(b)

    result = 0

    for i in range(31, -1, -1):
        if (a >> i) >= b:
            result |= (1 << i)
            a -= (b << i)

    return -result if is_negative else result


def reverse_integer(x: int) -> int:
    """
    Reverse digits of integer.

    Time: O(d), Space: O(1)
    """
    sign = -1 if x < 0 else 1
    x = abs(x)

    result = 0
    while x:
        result = result * 10 + x % 10
        x //= 10

    result *= sign

    # Handle overflow
    if result < -2**31 or result > 2**31 - 1:
        return 0

    return result


# =============================================================================
# SECTION 4: BITmask PROBLEMS
# =============================================================================

def subsets(elements: List[int]) -> List[List[int]]:
    """
    Generate all subsets using bitmask.

    Time: O(n * 2^n), Space: O(2^n)
    """
    n = len(elements)
    result = []

    for mask in range(1 << n):
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(elements[i])
        result.append(subset)

    return result


def gray_code(n: int) -> List[int]:
    """
    Generate Gray code sequence.

    Time: O(2^n), Space: O(2^n)

    Gray code: i ^ (i >> 1)
    """
    return [i ^ (i >> 1) for i in range(1 << n)]


def count_bits(num: int) -> List[int]:
    """
    Count bits for all numbers from 0 to n.

    Time: O(n), Space: O(n)

    dp[i] = dp[i >> 1] + (i & 1)
    """
    result = [0] * (num + 1)

    for i in range(1, num + 1):
        result[i] = result[i >> 1] + (i & 1)

    return result


# =============================================================================
# SECTION 5: TESTING
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("BIT MANIPULATION - TEST DEMO")
    print("=" * 60)

    # Basic operations
    num = 10  # 1010 in binary
    print(f"\nNumber: {num} (binary: {bin(num)})")
    print(f"Get bit at pos 1: {get_bit(num, 1)}")
    print(f"Set bit at pos 0: {set_bit(num, 0)}")
    print(f"Clear bit at pos 1: {clear_bit(num, 1)}")

    # Common tricks
    print("\n--- Common Tricks ---")
    print(f"Is 8 power of 2: {is_power_of_two(8)}")
    print(f"Is 7 power of 2: {is_power_of_two(7)}")
    print(f"Count bits in 15: {count_set_bits(15)}")
    print(f"Reverse bits of 1 (32-bit): {reverse_bits(1, 32)}")

    # Arithmetic
    print("\n--- Arithmetic ---")
    print(f"5 + 3 = {add_without_plus(5, 3)}")
    print(f"10 - 3 = {subtract_without_minus(10, 3)}")
    print(f"3 * 4 = {multiply_without_star(3, 4)}")
    print(f"10 / 3 = {divide_without_slash(10, 3)}")

    # Array problems
    print("\n--- Array Problems ---")
    print(f"Single number [2,2,1]: {single_number([2, 2, 1])}")
    print(f"Missing number [3,0,1]: {missing_number([3, 0, 1])}")
    print(f"Duplicate [1,3,4,2,2]: {find_duplicate([1, 3, 4, 2, 2])}")

    # Subsets
    print("\n--- Subsets ---")
    elements = [1, 2, 3]
    print(f"Subsets of {elements}:")
    for s in subsets(elements):
        print(f"  {s}")

    # Gray code
    print(f"\nGray code (n=3): {gray_code(3)}")

    print("\n" + "=" * 60)
    print("All tests completed!")
    print("=" * 60)

"""
Linked Lists - Implementation and Examples
==========================================
Comprehensive Python implementations for linked list problems
commonly asked in FAANG interviews.
"""

from typing import Optional, List
from collections import defaultdict


# =============================================================================
# SECTION 1: NODE DEFINITIONS
# =============================================================================

class ListNode:
    """
    Definition for singly linked list node.
    """

    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"


class DoublyListNode:
    """
    Definition for doubly linked list node.
    """

    def __init__(self, val: int = 0, next: 'DoublyListNode' = None,
                 prev: 'DoublyListNode' = None):
        self.val = val
        self.next = next
        self.prev = prev


class RandomListNode:
    """
    Definition for linked list with random pointer.
    """

    def __init__(self, val: int = 0, next: 'RandomListNode' = None,
                 random: 'RandomListNode' = None):
        self.val = val
        self.next = next
        self.random = random


# =============================================================================
# SECTION 2: HELPER FUNCTIONS
# =============================================================================

def create_linked_list(values: List[int]) -> Optional[ListNode]:
    """
    Create a linked list from a list of values.

    Time: O(n), Space: O(n)
    """
    if not values:
        return None

    dummy = ListNode(0)
    current = dummy

    for val in values:
        current.next = ListNode(val)
        current = current.next

    return dummy.next


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    """
    Convert linked list to Python list for easy visualization.

    Time: O(n), Space: O(n)
    """
    result = []
    current = head

    while current:
        result.append(current.val)
        current = current.next

    return result


def get_length(head: Optional[ListNode]) -> int:
    """
    Get length of linked list.

    Time: O(n), Space: O(1)
    """
    length = 0
    current = head

    while current:
        length += 1
        current = current.next

    return length


# =============================================================================
# SECTION 3: REVERSAL OPERATIONS
# =============================================================================

def reverse_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverse a singly linked list in-place.

    Time: O(n), Space: O(1)

    Algorithm:
    - Iterate through list
    - Reverse each pointer
    - Move prev forward

    Example:
    1 -> 2 -> 3 -> None
    becomes
    None <- 1 <- 2 <- 3
    """
    prev = None
    current = head

    while current:
        next_temp = current.next  # Save next
        current.next = prev       # Reverse pointer
        prev = current           # Move prev forward
        current = next_temp      # Move current forward

    return prev


def reverse_linked_list_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverse linked list using recursion.

    Time: O(n), Space: O(n) - recursion stack
    """
    if not head or not head.next:
        return head

    # Reverse the rest
    new_head = reverse_linked_list_recursive(head.next)

    # Reverse current pointer
    head.next.next = head
    head.next = None

    return new_head


def reverse_between(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    """
    Reverse nodes from position left to right (1-indexed).

    Time: O(n), Space: O(1)

    Steps:
    1. Find node before left (dummy -> ... -> prev)
    2. Reverse from left to right
    3. Reconnect
    """
    dummy = ListNode(0, head)
    prev = dummy

    # Move to node before left
    for _ in range(left - 1):
        prev = prev.next

    # Reverse the sublist
    current = prev.next
    for _ in range(right - left):
        temp = current.next
        current.next = temp.next
        temp.next = prev.next
        prev.next = temp

    return dummy.next


def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """
    Reverse nodes in groups of k.

    Time: O(n), Space: O(1)

    If less than k nodes remain, keep them unchanged.
    """
    dummy = ListNode(0, head)
    prev_group_end = dummy

    while True:
        # Check if we have k nodes remaining
        kth = get_kth_node(prev_group_end, k)
        if not kth:
            break

        next_group_start = kth.next

        # Reverse current group
        prev, current = kth.next, prev_group_end.next

        for _ in range(k):
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        # Connect with previous group
        first_node_of_group = prev_group_end.next
        prev_group_end.next = kth
        prev_group_end = first_node_of_group

    return dummy.next


def get_kth_node(start: ListNode, k: int) -> Optional[ListNode]:
    """
    Get kth node from start (not including start).

    Time: O(k), Space: O(1)
    """
    current = start
    for _ in range(k):
        if not current:
            return None
        current = current.next
    return current


# =============================================================================
# SECTION 4: FAST AND SLOW POINTERS
# =============================================================================

def has_cycle(head: Optional[ListNode]) -> bool:
    """
    Detect if linked list has a cycle using Floyd's algorithm.

    Time: O(n), Space: O(1)

    If there's a cycle, fast and slow pointers will eventually meet.
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


def find_cycle_start(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Find the start node of the cycle.

    Time: O(n), Space: O(1)

    Mathematical proof:
    - Let distance from head to cycle start = F
    - Let distance from cycle start to meeting point = a
    - Let cycle length = C

    - Slow travels: F + a
    - Fast travels: F + a + n*C (n >= 1)

    Since fast = 2 * slow:
    2(F + a) = F + a + n*C
    F + a = n*C
    F = n*C - a

    Therefore, if we start another pointer from head and move both
    one step at a time, they'll meet at cycle start.
    """
    if not head or not head.next:
        return None

    slow = head
    fast = head

    # Find meeting point
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if not fast or not fast.next:
        return None

    # Find cycle start
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


def find_middle(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Find middle node of linked list.

    Time: O(n), Space: O(1)

    For even-length lists, returns second middle.
    """
    if not head:
        return None

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def find_middle_previous(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Find node just before middle (useful for deletions).

    Time: O(n), Space: O(1)
    """
    if not head or not head.next:
        return None

    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def find_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Find nth node from end in one pass.

    Time: O(n), Space: O(1)

    Maintain gap of n between fast and slow.
    """
    if not head or n <= 0:
        return None

    fast = head
    slow = head

    # Move fast n steps ahead
    for _ in range(n):
        if not fast:
            return None
        fast = fast.next

    # Move both until fast reaches end
    while fast:
        slow = slow.next
        fast = fast.next

    return slow


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Remove nth node from end in one pass.

    Time: O(n), Space: O(1)
    """
    dummy = ListNode(0, head)
    fast = dummy
    slow = dummy

    # Move fast n+1 steps ahead
    for _ in range(n + 1):
        fast = fast.next

    # Move both
    while fast:
        fast = fast.next
        slow = slow.next

    # Delete node
    slow.next = slow.next.next

    return dummy.next


# =============================================================================
# SECTION 5: MERGING AND COMBINING
# =============================================================================

def merge_two_sorted_lists(l1: Optional[ListNode],
                          l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Merge two sorted linked lists into one sorted list.

    Time: O(n + m), Space: O(1)
    """
    dummy = ListNode(0)
    current = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    # Attach remaining
    current.next = l1 or l2

    return dummy.next


def merge_k_sorted_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Merge k sorted linked lists using divide and conquer.

    Time: O(N log k), Space: O(1) - ignoring recursion stack
    where N = total number of elements
    """
    if not lists:
        return None

    if len(lists) == 1:
        return lists[0]

    mid = len(lists) // 2
    left = merge_k_sorted_lists(lists[:mid])
    right = merge_k_sorted_lists(lists[mid:])

    return merge_two_sorted_lists(left, right)


def merge_k_sorted_lists_heap(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Merge k sorted lists using min heap.

    Time: O(N log k), Space: O(k)
    """
    import heapq

    dummy = ListNode(0)
    current = dummy

    # Initialize heap with first node of each list
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst.val, i, lst))

    while heap:
        val, i, node = heapq.heappop(heap)
        current.next = node
        current = current.next

        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next


# =============================================================================
# SECTION 6: DELETION OPERATIONS
# =============================================================================

def delete_node(head: Optional[ListNode], node: ListNode) -> None:
    """
    Delete a node from linked list (given only the node).

    Time: O(1), Space: O(1)

    Note: Cannot delete last node this way.
    """
    if not node or not node.next:
        return

    # Copy next node's value
    node.val = node.next.val
    # Skip next node
    node.next = node.next.next


def delete_duplicates_sorted(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Remove duplicates from sorted linked list.

    Time: O(n), Space: O(1)
    """
    if not head:
        return head

    current = head

    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next

    return head


def delete_duplicates_unsorted(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Remove duplicates from unsorted linked list.

    Time: O(n), Space: O(n) - using hash set

    For O(1) space, see delete_duplicates_unsorted_inplace
    """
    if not head:
        return head

    seen = {head.val}
    current = head

    while current and current.next:
        if current.next.val in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.val)
            current = current.next

    return head


def delete_duplicates_unsorted_inplace(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Remove duplicates without extra space.

    Time: O(n²), Space: O(1)
    """
    if not head:
        return head

    current = head

    while current:
        runner = current
        while runner.next:
            if runner.next.val == current.val:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next

    return head


# =============================================================================
# SECTION 7: PALINDROME AND CYCLIC PROBLEMS
# =============================================================================

def is_palindrome(head: Optional[ListNode]) -> bool:
    """
    Check if linked list is palindrome.

    Time: O(n), Space: O(1)

    Steps:
    1. Find middle
    2. Reverse second half
    3. Compare both halves
    4. (Optional) Reverse back
    """
    if not head or not head.next:
        return True

    # Find middle
    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    second_half = reverse_linked_list(slow.next)

    # Compare
    first = head
    second = second_half

    result = True
    while second:
        if first.val != second.val:
            result = False
            break
        first = first.next
        second = second.next

    # Restore (optional)
    slow.next = reverse_linked_list(second_half)

    return result


def rotate_right(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """
    Rotate list right by k places.

    Time: O(n), Space: O(1)

    Edge case: k can be larger than list length
    """
    if not head or k == 0:
        return head

    # Get length
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    # Normalize k
    k = k % length
    if k == 0:
        return head

    # Find new tail (length - k - 1)
    new_tail = head
    for _ in range(length - k - 1):
        new_tail = new_tail.next

    # Rotate
    new_head = new_tail.next
    new_tail.next = None
    tail.next = head

    return new_head


def odd_even_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Rearrange list so all odd nodes come before even nodes.

    Time: O(n), Space: O(1)
    """
    if not head or not head.next:
        return head

    odd = head
    even = head.next
    even_head = even

    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next

    odd.next = even_head

    return head


def swap_pairs(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Swap every two adjacent nodes.

    Time: O(n), Space: O(1)
    """
    dummy = ListNode(0, head)
    prev = dummy

    while prev.next and prev.next.next:
        first = prev.next
        second = first.next

        # Swap
        prev.next = second
        first.next = second.next
        second.next = first

        prev = first

    return dummy.next


# =============================================================================
# SECTION 8: DEEP COPY WITH RANDOM POINTER
# =============================================================================

def deep_copy_random_list(head: Optional[RandomListNode]) -> Optional[RandomListNode]:
    """
    Clone linked list with random pointer.

    Time: O(n), Space: O(1) - using interweaving approach
    """
    if not head:
        return None

    # Step 1: Create copy nodes and interweave
    # Original: A -> B -> C
    # After:    A -> A' -> B -> B' -> C -> C'
    current = head
    while current:
        new_node = RandomListNode(current.val)
        new_node.next = current.next
        current.next = new_node
        current = new_node.next

    # Step 2: Copy random pointers
    current = head
    while current:
        if current.random:
            current.next.random = current.random.next
        current = current.next.next

    # Step 3: Separate original and copy lists
    dummy = ListNode(0)
    copy_current = dummy
    current = head

    while current:
        copy_current.next = current.next
        copy_current = copy_current.next
        current.next = current.next.next
        current = current.next

    return dummy.next


# =============================================================================
# SECTION 9: DOUBLY LINKED LIST OPERATIONS
# =============================================================================

class DoublyLinkedList:
    """
    Doubly linked list implementation with head and tail.
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, val: int) -> None:
        """Add node to end. Time: O(1)"""
        node = DoublyListNode(val)

        if not self.tail:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

        self.size += 1

    def prepend(self, val: int) -> None:
        """Add node to beginning. Time: O(1)"""
        node = DoublyListNode(val)

        if not self.head:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

        self.size += 1

    def remove(self, node: DoublyListNode) -> None:
        """Remove node. Time: O(1)"""
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        self.size -= 1


# =============================================================================
# SECTION 10: TESTING AND DEMO
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("LINKED LIST ALGORITHMS - TEST DEMO")
    print("=" * 60)

    # Test basic operations
    print("\n--- Basic Operations ---")
    head = create_linked_list([1, 2, 3, 4, 5])
    print(f"Created list: {linked_list_to_list(head)}")

    # Test reversal
    print("\n--- Reversal ---")
    head = create_linked_list([1, 2, 3, 4, 5])
    reversed_head = reverse_linked_list(head)
    print(f"Reversed: {linked_list_to_list(reversed_head)}")

    # Test middle finding
    print("\n--- Middle Finding ---")
    head = create_linked_list([1, 2, 3, 4, 5])
    middle = find_middle(head)
    print(f"Middle of [1,2,3,4,5]: {middle.val if middle else None}")

    head = create_linked_list([1, 2, 3, 4, 5, 6])
    middle = find_middle(head)
    print(f"Middle of [1-6]: {middle.val if middle else None}")

    # Test nth from end
    print("\n--- Nth From End ---")
    head = create_linked_list([1, 2, 3, 4, 5])
    nth = find_nth_from_end(head, 2)
    print(f"2nd from end: {nth.val if nth else None}")

    # Test merging sorted lists
    print("\n--- Merge Sorted Lists ---")
    l1 = create_linked_list([1, 2, 4])
    l2 = create_linked_list([1, 3, 4])
    merged = merge_two_sorted_lists(l1, l2)
    print(f"Merged [1,2,4] and [1,3,4]: {linked_list_to_list(merged)}")

    # Test palindrome
    print("\n--- Palindrome ---")
    head = create_linked_list([1, 2, 3, 2, 1])
    print(f"Is [1,2,3,2,1] palindrome? {is_palindrome(head)}")

    # Test rotation
    print("\n--- Rotation ---")
    head = create_linked_list([1, 2, 3, 4, 5])
    rotated = rotate_right(head, 2)
    print(f"Rotate [1-5] by 2: {linked_list_to_list(rotated)}")

    # Test odd-even
    print("\n--- Odd-Even ---")
    head = create_linked_list([1, 2, 3, 4, 5, 6])
    result = odd_even_list(head)
    print(f"Odd-even arrangement: {linked_list_to_list(result)}")

    # Test swap pairs
    print("\n--- Swap Pairs ---")
    head = create_linked_list([1, 2, 3, 4])
    result = swap_pairs(head)
    print(f"Swap pairs of [1-4]: {linked_list_to_list(result)}")

    # Test k-group reversal
    print("\n--- Reverse K-Group ---")
    head = create_linked_list([1, 2, 3, 4, 5])
    result = reverse_k_group(head, 2)
    print(f"Reverse in groups of 2: {linked_list_to_list(result)}")

    print("\n" + "=" * 60)
    print("All tests completed!")
    print("=" * 60)

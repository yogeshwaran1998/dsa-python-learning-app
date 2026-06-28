"""
Binary Search Trees - Implementation and Examples
================================================
Comprehensive Python implementations for BST problems
commonly asked in FAANG interviews.
"""

from typing import List, Optional, Tuple


# =============================================================================
# SECTION 1: BST NODE AND HELPER
# =============================================================================

class TreeNode:
    """Definition for BST node."""

    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


def create_bst(values: List[int]) -> Optional[TreeNode]:
    """Create BST from sorted array."""
    if not values:
        return None

    mid = len(values) // 2
    root = TreeNode(values[mid])
    root.left = create_bst(values[:mid])
    root.right = create_bst(values[mid + 1:])

    return root


# =============================================================================
# SECTION 2: SEARCH
# =============================================================================

def search_bst(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """
    Search for node with given value in BST.

    Time: O(h), Space: O(h) recursive, O(1) iterative
    """
    while root and root.val != val:
        if val < root.val:
            root = root.left
        else:
            root = root.right

    return root


def search_bst_recursive(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """Recursive search in BST."""
    if not root or root.val == val:
        return root

    if val < root.val:
        return search_bst_recursive(root.left, val)
    return search_bst_recursive(root.right, val)


# =============================================================================
# SECTION 3: INSERTION
# =============================================================================

def insert_into_bst(root: Optional[TreeNode], val: int) -> TreeNode:
    """
    Insert value into BST.

    Time: O(h), Space: O(h)
    """
    if not root:
        return TreeNode(val)

    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)

    return root


def insert_iterative(root: Optional[TreeNode], val: int) -> TreeNode:
    """Iterative insertion."""
    if not root:
        return TreeNode(val)

    current = root
    while True:
        if val < current.val:
            if not current.left:
                current.left = TreeNode(val)
                break
            current = current.left
        else:
            if not current.right:
                current.right = TreeNode(val)
                break
            current = current.right

    return root


# =============================================================================
# SECTION 4: DELETION
# =============================================================================

def delete_node(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    """
    Delete node with given key from BST.

    Time: O(h), Space: O(h)

    Cases:
    1. Leaf node - simply remove
    2. One child - replace with child
    3. Two children - replace with inorder successor, delete successor
    """
    if not root:
        return None

    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        # Found the node to delete
        if not root.left:
            return root.right
        if not root.right:
            return root.left

        # Two children - find inorder successor
        successor = find_min(root.right)
        root.val = successor.val
        root.right = delete_node(root.right, successor.val)

    return root


def find_min(node: TreeNode) -> TreeNode:
    """Find node with minimum value."""
    while node.left:
        node = node.left
    return node


def find_max(node: TreeNode) -> TreeNode:
    """Find node with maximum value."""
    while node.right:
        node = node.right
    return node


# =============================================================================
# SECTION 5: VALIDATION
# =============================================================================

def is_valid_bst(root: Optional[TreeNode]) -> bool:
    """
    Validate if tree is a valid BST.

    Time: O(n), Space: O(h)
    """
    def validate(node, low, high):
        if not node:
            return True

        if node.val <= low or node.val >= high:
            return False

        return (validate(node.left, low, node.val) and
                validate(node.right, node.val, high))

    return validate(root, float('-inf'), float('inf'))


def is_valid_bst_inorder(root: Optional[TreeNode]) -> bool:
    """
    Validate BST using inorder traversal.
    Inorder of BST should be strictly increasing.

    Time: O(n), Space: O(h)
    """
    prev = [float('-inf')]

    def inorder(node):
        if not node:
            return True

        if not inorder(node.left):
            return False

        if node.val <= prev[0]:
            return False
        prev[0] = node.val

        return inorder(node.right)

    return inorder(root)


# =============================================================================
# SECTION 6: KTH SMALLEST/LARGEST
# =============================================================================

def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    """
    Find kth smallest element in BST.

    Time: O(h + k), Space: O(h)
    """
    stack = []
    current = root

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        k -= 1

        if k == 0:
            return current.val

        current = current.right

    return -1


def kth_smallest_recursive(root: Optional[TreeNode], k: int) -> int:
    """Recursive approach with counter."""
    result = [None]
    count = [k]

    def inorder(node):
        if not node or count[0] <= 0:
            return

        inorder(node.left)
        count[0] -= 1

        if count[0] == 0:
            result[0] = node.val
            return

        inorder(node.right)

    inorder(root)
    return result[0]


def kth_largest(root: Optional[TreeNode], k: int) -> int:
    """Find kth largest (reverse inorder)."""
    stack = []
    current = root

    while stack or current:
        while current:
            stack.append(current)
            current = current.right

        current = stack.pop()
        k -= 1

        if k == 0:
            return current.val

        current = current.left

    return -1


# =============================================================================
# SECTION 7: RANGE QUERIES
# =============================================================================

def range_sum_bst(root: Optional[TreeNode], low: int, high: int) -> int:
    """
    Sum of values in range [low, high].

    Time: O(n), Space: O(h)
    """
    if not root:
        return 0

    if root.val < low:
        return range_sum_bst(root.right, low, high)
    if root.val > high:
        return range_sum_bst(root.left, low, high)

    return (root.val +
            range_sum_bst(root.left, low, high) +
            range_sum_bst(root.right, low, high))


def range_sum_bst_iterative(root: Optional[TreeNode], low: int, high: int) -> int:
    """Iterative range sum."""
    stack = [root]
    total = 0

    while stack:
        node = stack.pop()
        if not node:
            continue

        if low <= node.val <= high:
            total += node.val
            stack.append(node.left)
            stack.append(node.right)
        elif node.val < low:
            stack.append(node.right)
        else:
            stack.append(node.left)

    return total


def find_nodes_in_range(root: Optional[TreeNode], low: int, high: int) -> List[int]:
    """Find all nodes in range."""
    result = []

    def traverse(node):
        if not node:
            return

        if low <= node.val <= high:
            result.append(node.val)

        if node.val > low:
            traverse(node.left)
        if node.val < high:
            traverse(node.right)

    traverse(root)
    return result


# =============================================================================
# SECTION 8: BST ITERATOR
# =============================================================================

class BSTIterator:
    """
    Iterator for BST - next() returns next smallest.

    Time: O(1) amortized, Space: O(h)
    """

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._push_left(root)

    def _push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()
        self._push_left(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# =============================================================================
# SECTION 9: BST TO LINKED LIST
# =============================================================================

def flatten_bst_to_sorted_list(root: Optional[TreeNode]) -> List[int]:
    """Convert BST to sorted list using inorder."""
    result = []

    def inorder(node):
        if not node:
            return
        inorder(node.left)
        result.append(node.val)
        inorder(node.right)

    inorder(root)
    return result


def bst_to_linked_list(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """Convert BST to sorted circular doubly linked list."""
    if not root:
        return None

    # In-place conversion using threading
    prev = [None]

    def inorder(node):
        if not node:
            return

        inorder(node.left)

        if prev[0]:
            prev[0].right = node
            node.left = prev[0]
        else:
            # First node (smallest)
            head = node

        prev[0] = node
        inorder(node.right)

    head = [None]
    inorder(root)

    # Connect head and tail
    if prev[0]:
        prev[0].right = head[0]
        head[0].left = prev[0]

    return head[0] if head[0] else None


# =============================================================================
# SECTION 10: CONVERT BETWEEN REPRESENTATIONS
# =============================================================================

def sorted_array_to_bst(nums: List[int]) -> Optional[TreeNode]:
    """
    Convert sorted array to balanced BST.

    Time: O(n), Space: O(n)
    """
    def build(low, high):
        if low > high:
            return None

        mid = (low + high) // 2
        node = TreeNode(nums[mid])
        node.left = build(low, mid - 1)
        node.right = build(mid + 1, high)
        return node

    return build(0, len(nums) - 1)


def bst_to_sorted_array(root: Optional[TreeNode]) -> List[int]:
    """Convert BST to sorted array."""
    result = []

    def inorder(node):
        if not node:
            return
        inorder(node.left)
        result.append(node.val)
        inorder(node.right)

    inorder(root)
    return result


# =============================================================================
# SECTION 11: RECOVER BST
# =============================================================================

def recover_tree(root: Optional[TreeNode]) -> None:
    """
    Recover BST where two nodes were swapped.

    Time: O(n), Space: O(h)
    """
    first = [None]
    second = [None]
    prev = [TreeNode(float('-inf'))]

    def inorder(node):
        if not node:
            return

        inorder(node.left)

        if prev[0].val > node.val:
            if not first[0]:
                first[0] = prev[0]
            second[0] = node

        prev[0] = node
        inorder(node.right)

    inorder(root)
    first[0].val, second[0].val = second[0].val, first[0].val


# =============================================================================
# SECTION 12: LOWEST COMMON ANCESTOR IN BST
# =============================================================================

def lca_bst(root: Optional[TreeNode], p: int, q: int) -> Optional[TreeNode]:
    """
    Find lowest common ancestor in BST.

    Time: O(h), Space: O(h)
    """
    while root:
        if root.val > p and root.val > q:
            root = root.left
        elif root.val < p and root.val < q:
            root = root.right
        else:
            return root

    return None


# =============================================================================
# SECTION 13: TESTING AND DEMO
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("BST ALGORITHMS - TEST DEMO")
    print("=" * 60)

    # Create sample BST
    #        8
    #       / \
    #      3   10
    #     / \    \
    #    1   6    14
    #      / \   /
    #     4   7 13

    values = [1, 3, 4, 6, 7, 8, 10, 13, 14]
    root = create_bst(values)

    # Helper for inorder (defined before first use below)
    def inorder_traversal(root):
        result = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)
        return result

    # Test search
    print("\n--- Search ---")
    print(f"Search 6: {search_bst(root, 6).val if search_bst(root, 6) else 'Not found'}")
    print(f"Search 5: {search_bst(root, 5) if search_bst(root, 5) else 'Not found'}")

    # Test insertion
    print("\n--- Insertion ---")
    root = insert_into_bst(root, 5)
    print(f"Insert 5, inorder: {inorder_traversal(root)}")

    # Test validation
    print("\n--- Validation ---")
    # Create invalid tree
    invalid = TreeNode(5, TreeNode(1), TreeNode(6, TreeNode(4)))
    print(f"Is valid: {is_valid_bst(invalid)}")

    # Test Kth smallest
    print("\n--- Kth Smallest ---")
    print(f"3rd smallest: {kth_smallest(root, 3)}")
    print(f"2nd largest: {kth_largest(root, 2)}")

    # Test range sum
    print("\n--- Range Sum ---")
    print(f"Sum [5, 12]: {range_sum_bst(root, 5, 12)}")

    # Test BST Iterator
    print("\n--- BST Iterator ---")
    iterator = BSTIterator(root)
    result = []
    while iterator.hasNext():
        result.append(iterator.next())
    print(f"Iterator output: {result[:5]}...")

    # Test sorted array to BST
    print("\n--- Array to BST ---")
    arr = [1, 2, 3, 4, 5, 6, 7]
    bst = sorted_array_to_bst(arr)
    print(f"Array to BST inorder: {bst_to_sorted_array(bst)}")

    # Test LCA
    print("\n--- LCA ---")
    print(f"LCA of 4 and 7: {lca_bst(root, 4, 7).val if lca_bst(root, 4, 7) else 'Not found'}")

    # Test deletion
    print("\n--- Deletion ---")
    # Create fresh tree
    root = create_bst([1, 3, 4, 6, 7, 8, 10, 13, 14])
    root = delete_node(root, 6)
    print(f"Delete 6, inorder: {inorder_traversal(root)}")

    print("\n" + "=" * 60)
    print("All tests completed!")
    print("=" * 60)

"""
Binary Trees - Implementation and Examples
==========================================
Comprehensive Python implementations for binary tree problems
commonly asked in FAANG interviews.
"""

from typing import List, Optional, Tuple
from collections import deque


# =============================================================================
# SECTION 1: TREE NODE DEFINITION
# =============================================================================

class TreeNode:
    """
    Definition for binary tree node.
    """

    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"


# =============================================================================
# SECTION 2: HELPER FUNCTIONS
# =============================================================================

def create_tree_from_list(values: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Create binary tree from level-order list representation.

    Time: O(n), Space: O(n)
    """
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        # Left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        # Right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """
    Convert binary tree to level-order list representation.

    Time: O(n), Space: O(n)
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()

    return result


def get_height(root: Optional[TreeNode]) -> int:
    """Get height of tree."""
    if not root:
        return 0
    return 1 + max(get_height(root.left), get_height(root.right))


# =============================================================================
# SECTION 3: DEPTH-FIRST TRAVERSALS
# =============================================================================

def preorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """
    Pre-order: Root -> Left -> Right.

    Time: O(n), Space: O(h) where h = height
    """
    result = []

    def traverse(node):
        if not node:
            return
        result.append(node.val)      # Visit root
        traverse(node.left)          # Left subtree
        traverse(node.right)         # Right subtree

    traverse(root)
    return result


def preorder_iterative(root: Optional[TreeNode]) -> List[int]:
    """Iterative pre-order using stack."""
    if not root:
        return []

    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result


def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """
    In-order: Left -> Root -> Right.
    For BST, gives sorted output.

    Time: O(n), Space: O(h)
    """
    result = []

    def traverse(node):
        if not node:
            return
        traverse(node.left)          # Left subtree
        result.append(node.val)      # Visit root
        traverse(node.right)         # Right subtree

    traverse(root)
    return result


def inorder_iterative(root: Optional[TreeNode]) -> List[int]:
    """Iterative in-order using stack."""
    result = []
    stack = []
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        result.append(current.val)
        current = current.right

    return result


def postorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """
    Post-order: Left -> Right -> Root.

    Time: O(n), Space: O(h)
    """
    result = []

    def traverse(node):
        if not node:
            return
        traverse(node.left)          # Left subtree
        traverse(node.right)         # Right subtree
        result.append(node.val)      # Visit root

    traverse(root)
    return result


def postorder_iterative(root: Optional[TreeNode]) -> List[int]:
    """
    Iterative post-order using two stacks.
    """
    if not root:
        return []

    result = []
    stack1 = [root]
    stack2 = []

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

    while stack2:
        result.append(stack2.pop().val)

    return result


# =============================================================================
# SECTION 4: BREADTH-FIRST TRAVERSAL
# =============================================================================

def level_order_traversal(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Level-order traversal (BFS).

    Time: O(n), Space: O(w) where w = max width
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result


def level_order_traversal_single_list(root: Optional[TreeNode]) -> List[int]:
    """Level-order as single list."""
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result


def zigzag_level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Zigzag level-order: alternate direction each level.

    Time: O(n), Space: O(w)
    """
    if not root:
        return []

    result = []
    queue = deque([root])
    left_to_right = True

    while queue:
        level_size = len(queue)
        level = deque()

        for _ in range(level_size):
            node = queue.popleft()

            if left_to_right:
                level.append(node.val)
            else:
                level.appendleft(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(list(level))
        left_to_right = not left_to_right

    return result


# =============================================================================
# SECTION 5: TREE PROPERTIES
# =============================================================================

def maximum_depth(root: Optional[TreeNode]) -> int:
    """
    Find maximum depth of binary tree.

    Time: O(n), Space: O(h)
    """
    if not root:
        return 0

    return 1 + max(maximum_depth(root.left), maximum_depth(root.right))


def minimum_depth(root: Optional[TreeNode]) -> int:
    """
    Find minimum depth (first leaf).

    Time: O(n), Space: O(h)
    """
    if not root:
        return 0

    if not root.left:
        return 1 + minimum_depth(root.right)
    if not root.right:
        return 1 + minimum_depth(root.left)

    return 1 + min(minimum_depth(root.left), minimum_depth(root.right))


def is_balanced(root: Optional[TreeNode]) -> bool:
    """
    Check if tree is balanced (heights differ by at most 1).

    Time: O(n), Space: O(h)
    """
    def get_height(node):
        if not node:
            return 0

        left = get_height(node.left)
        if left == -1:
            return -1

        right = get_height(node.right)
        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1

        return 1 + max(left, right)

    return get_height(root) != -1


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """Check if two trees are identical."""
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False

    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


def is_symmetric(root: Optional[TreeNode]) -> bool:
    """
    Check if tree is symmetric.

    Time: O(n), Space: O(h)
    """
    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False

        return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

    return is_mirror(root.left, root.right)


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Invert binary tree (swap left and right children).

    Time: O(n), Space: O(h)
    """
    if not root:
        return root

    root.left, root.right = root.right, root.left

    invert_tree(root.left)
    invert_tree(root.right)

    return root


# =============================================================================
# SECTION 6: PATH PROBLEMS
# =============================================================================

def has_path_sum(root: Optional[TreeNode], target: int) -> bool:
    """
    Check if there's root-to-leaf path with sum = target.

    Time: O(n), Space: O(h)
    """
    if not root:
        return False

    if not root.left and not root.right:
        return root.val == target

    return (has_path_sum(root.left, target - root.val) or
            has_path_sum(root.right, target - root.val))


def path_sum(root: Optional[TreeNode], target: int) -> List[List[int]]:
    """
    Find all root-to-leaf paths that sum to target.

    Time: O(n), Space: O(h)
    """
    result = []

    def find_paths(node, remaining, path):
        if not node:
            return

        path.append(node.val)

        if not node.left and not node.right:
            if remaining == node.val:
                result.append(path.copy())
        else:
            find_paths(node.left, remaining - node.val, path)
            find_paths(node.right, remaining - node.val, path)

        path.pop()

    find_paths(root, target, [])
    return result


def binary_tree_maximum_path_sum(root: Optional[TreeNode]) -> int:
    """
    Find maximum path sum (any node to any node).

    Time: O(n), Space: O(h)
    """
    max_sum = float('-inf')

    def max_gain(node):
        nonlocal max_sum

        if not node:
            return 0

        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)

        path_sum = node.val + left_gain + right_gain
        max_sum = max(max_sum, path_sum)

        return node.val + max(left_gain, right_gain)

    max_gain(root)
    return max_sum


# =============================================================================
# SECTION 7: LOWEST COMMON ANCESTOR
# =============================================================================

def lowest_common_ancestor(root: Optional[TreeNode],
                           p: Optional[TreeNode],
                           q: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Find lowest common ancestor of two nodes.

    Time: O(n), Space: O(h)
    """
    if not root or root == p or root == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root

    return left or right


def lowest_common_ancestor_bst(root: Optional[TreeNode],
                               p: Optional[TreeNode],
                               q: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Find LCA in BST (optimized using BST properties).

    Time: O(h), Space: O(h)
    """
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root

    return None


# =============================================================================
# SECTION 8: SERIALIZATION
# =============================================================================

def serialize(root: Optional[TreeNode]) -> str:
    """
    Serialize tree to string using pre-order.

    Time: O(n), Space: O(n)
    """
    def encode(node):
        if not node:
            return "null,"
        return str(node.val) + "," + encode(node.left) + encode(node.right)

    return encode(root)


def deserialize(data: str) -> Optional[TreeNode]:
    """
    Deserialize string back to tree.

    Time: O(n), Space: O(n)
    """
    values = data.split(',')

    def decode():
        if not values or values[i[0]] == 'null':
            return None

        node = TreeNode(int(values[i[0]]))
        i[0] += 1
        node.left = decode()
        node.right = decode()
        return node

    i = [0]
    return decode()


# =============================================================================
# SECTION 9: BOUNDARY TRAVERSAL
# =============================================================================

def boundary_traversal(root: Optional[TreeNode]) -> List[int]:
    """
    Boundary traversal: left boundary + leaves + right boundary.

    Time: O(n), Space: O(h)
    """
    if not root:
        return []

    result = [root.val]

    def add_left_boundary(node):
        if not node:
            return
        if node.left:
            result.append(node.val)
            add_left_boundary(node.left)
        elif node.right:
            result.append(node.val)
            add_left_boundary(node.right)

    def add_leaves(node):
        if not node:
            return
        if not node.left and not node.right:
            result.append(node.val)
            return
        add_leaves(node.left)
        add_leaves(node.right)

    def add_right_boundary(node):
        if not node:
            return
        if node.right:
            add_right_boundary(node.right)
            result.append(node.val)
        elif node.left:
            add_right_boundary(node.left)
            result.append(node.val)

    add_left_boundary(root.left)
    add_leaves(root)
    add_right_boundary(root.right)

    return result


# =============================================================================
# SECTION 10: VERTICAL ORDER
# =============================================================================

def vertical_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Vertical order traversal (top to bottom, left to right).

    Time: O(n log n), Space: O(n)
    """
    if not root:
        return []

    from collections import defaultdict

    columns = defaultdict(list)
    queue = deque([(root, 0)])

    while queue:
        node, col = queue.popleft()
        columns[col].append(node.val)

        if node.left:
            queue.append((node.left, col - 1))
        if node.right:
            queue.append((node.right, col + 1))

    return [columns[col] for col in sorted(columns.keys())]


# =============================================================================
# SECTION 11: TESTING AND DEMO
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("BINARY TREE ALGORITHMS - TEST DEMO")
    print("=" * 60)

    # Create sample tree
    #        1
    #       / \
    #      2   3
    #     / \   \
    #    4   5   6

    values = [1, 2, 3, 4, 5, None, 6]
    root = create_tree_from_list(values)

    # Test traversals
    print("\n--- Traversals ---")
    print(f"Pre-order:   {preorder_traversal(root)}")
    print(f"In-order:    {inorder_traversal(root)}")
    print(f"Post-order:  {postorder_traversal(root)}")
    print(f"Level-order: {level_order_traversal(root)}")

    # Test tree properties
    print("\n--- Tree Properties ---")
    print(f"Max depth: {maximum_depth(root)}")
    print(f"Min depth: {minimum_depth(root)}")
    print(f"Is balanced: {is_balanced(root)}")

    # Test path sum
    print("\n--- Path Sum ---")
    target = 7
    print(f"Path sum to {target}: {path_sum(root, target)}")
    print(f"Has path sum {target}: {has_path_sum(root, target)}")

    # Test symmetric
    # Create symmetric tree
    #     1
    #    / \
    #   2   2
    #  / \ / \
    # 3  4 4  3
    sym_values = [1, 2, 2, 3, 4, 4, 3]
    sym_root = create_tree_from_list(sym_values)
    print(f"\nIs symmetric: {is_symmetric(sym_root)}")

    # Test invert
    print("\n--- Invert Tree ---")
    print(f"Original level-order: {level_order_traversal_single_list(root)}")
    inverted = invert_tree(root)
    print(f"Inverted level-order: {level_order_traversal_single_list(inverted)}")

    # Test zigzag
    print("\n--- Zigzag Order ---")
    root2 = create_tree_from_list([1, 2, 3, 4, 5, 6, 7])
    print(f"Zigzag: {zigzag_level_order(root2)}")

    # Test vertical order
    print("\n--- Vertical Order ---")
    #      1
    #    /   \
    #   2     3
    #  / \   /
    # 4   5 6
    vert_values = [1, 2, 3, 4, None, 5, 6]
    vert_root = create_tree_from_list(vert_values)
    print(f"Vertical order: {vertical_order(vert_root)}")

    # Test serialization
    print("\n--- Serialization ---")
    serialized = serialize(root)
    print(f"Serialized: {serialized[:50]}...")
    deserialized = deserialize(serialized)
    print(f"Deserialized level-order: {level_order_traversal_single_list(deserialized)}")

    print("\n" + "=" * 60)
    print("All tests completed!")
    print("=" * 60)

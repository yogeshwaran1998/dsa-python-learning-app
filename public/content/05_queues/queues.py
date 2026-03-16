"""
Queues - Implementation and Examples
====================================
Comprehensive Python implementations for queue problems
commonly asked in FAANG interviews.
"""

from typing import List, Optional
from collections import deque


# =============================================================================
# SECTION 1: QUEUE IMPLEMENTATIONS
# =============================================================================

class Queue:
    """
    Basic queue implementation using list.

    Time: O(1) amortized for enqueue/dequeue, O(n) worst case for pop(0)
    Space: O(n)
    """

    def __init__(self):
        self.items = []

    def enqueue(self, item) -> None:
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.items[0]

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def size(self) -> int:
        return len(self.items)


class QueueUsingTwoStacks:
    """
    Queue implemented using two stacks.

    Time:
    - Amortized O(1) for push and pop
    - Worst case O(n) when transferring
    Space: O(n)
    """

    def __init__(self):
        self.stack_in = []  # For enqueue
        self.stack_out = []  # For dequeue

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if not self.stack_out:
            raise IndexError("Queue is empty")
        return self.stack_out.pop()

    def peek(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if not self.stack_out:
            raise IndexError("Queue is empty")
        return self.stack_out[-1]

    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out


class CircularQueue:
    """
    Circular queue implementation using fixed-size array.

    Time: O(1) for all operations
    Space: O(k) where k is capacity
    """

    def __init__(self, k: int):
        self.k = k
        self.queue = [None] * k
        self.head = -1
        self.tail = -1

    def enqueue(self, value: int) -> bool:
        if self.is_full():
            return False

        if self.head == -1:
            self.head = 0

        self.tail = (self.tail + 1) % self.k
        self.queue[self.tail] = value
        return True

    def dequeue(self) -> bool:
        if self.is_empty():
            return False

        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:
            self.head = (self.head + 1) % self.k
        return True

    def Front(self) -> int:
        if self.head == -1:
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.tail == -1:
            return -1
        return self.queue[self.tail]

    def is_empty(self) -> bool:
        return self.head == -1

    def is_full(self) -> bool:
        return (self.tail + 1) % self.k == self.head


# =============================================================================
# SECTION 2: SLIDING WINDOW MAXIMUM
# =============================================================================

def sliding_window_maximum(nums: List[int], k: int) -> List[int]:
    """
    Find maximum value in each sliding window.

    Time: O(n), Space: O(k)

    Algorithm: Use deque to store indices
    - Maintain decreasing deque (front = max)
    - Remove indices outside window
    - Remove indices smaller than current
    """
    if not nums or k == 0:
        return []

    result = []
    deque = deque()  # Store indices

    for i in range(len(nums)):
        # Remove indices outside current window
        while deque and deque[0] < i - k + 1:
            deque.popleft()

        # Remove indices of smaller elements
        while deque and nums[deque[-1]] < nums[i]:
            deque.pop()

        deque.append(i)

        # Start adding to result when window is complete
        if i >= k - 1:
            result.append(nums[deque[0]])

    return result


def min_sliding_window(nums: List[int], k: int) -> List[int]:
    """
    Find minimum value in each sliding window.

    Time: O(n), Space: O(k)
    """
    if not nums or k == 0:
        return []

    result = []
    deque = deque()  # Store indices, maintain increasing

    for i in range(len(nums)):
        # Remove indices outside window
        while deque and deque[0] < i - k + 1:
            deque.popleft()

        # Remove indices of larger elements
        while deque and nums[deque[-1]] > nums[i]:
            deque.pop()

        deque.append(i)

        if i >= k - 1:
            result.append(nums[deque[0]])

    return result


# =============================================================================
# SECTION 3: BFS PATTERN
# =============================================================================

def binary_tree_level_order(root) -> List[List[int]]:
    """
    Level order traversal of binary tree using BFS.

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


def shortest_path_binary_matrix(grid: List[List[int]]) -> int:
    """
    Find shortest path from top-left to bottom-right in binary grid.
    0 = empty, 1 = blocked.

    Time: O(n*m), Space: O(n*m)
    """
    if grid[0][0] or grid[-1][-1]:
        return -1

    n = len(grid)
    queue = deque([(0, 0, 1)])  # row, col, distance
    grid[0][0] = 1  # Mark as visited

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0),
                 (1, 1), (1, -1), (-1, 1), (-1, -1)]

    while queue:
        row, col, dist = queue.popleft()

        if row == n - 1 and col == n - 1:
            return dist

        for dr, dc in directions:
            nr, nc = row + dr, col + dc

            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                grid[nr][nc] = 1  # Mark visited
                queue.append((nr, nc, dist + 1))

    return -1


def open_lock(deadends: List[str], target: str) -> int:
    """
    Find minimum turns to open combination lock from "0000".
    Deadends are combinations that can't be used.

    Time: O(10^4), Space: O(10^4)
    """
    if "0000" in deadends:
        return -1

    if target == "0000":
        return 0

    visited = set(deadends)
    queue = deque([("0000", 0)])

    while queue:
        combination, turns = queue.popleft()

        for i in range(4):
            for delta in [-1, 1]:
                new_comb = list(combination)
                new_comb[i] = str((int(new_comb[i]) + delta) % 10)
                new_comb_str = ''.join(new_comb)

                if new_comb_str == target:
                    return turns + 1

                if new_comb_str not in visited:
                    visited.add(new_comb_str)
                    queue.append((new_comb_str, turns + 1))

    return -1


def snakes_and_ladders(board: List[List[int]]) -> int:
    """
    Find minimum moves from square 1 to n*n using snakes and ladders.

    Time: O(n^2), Space: O(n^2)
    """
    n = len(board)
    # Reverse board (bottom to top)
    board.reverse()

    moves = 0
    queue = deque([1])
    visited = set([1])

    while queue:
        for _ in range(len(queue)):
            curr = queue.popleft()

            for next_square in range(curr + 1, min(curr + 6, n * n) + 1):
                # Calculate row and col
                row = (next_square - 1) // n
                col = (next_square - 1) % n

                # Check for snake or ladder
                dest = next_square if board[row][col] == -1 else board[row][col]

                if dest == n * n:
                    return moves + 1

                if dest not in visited:
                    visited.add(dest)
                    queue.append(dest)

        moves += 1

    return -1


# =============================================================================
# SECTION 4: RECENT COUNTER
# =============================================================================

class RecentCounter:
    """
    Track number of recent requests within 3000ms time window.

    Time: O(1) amortized, Space: O(n)
    """

    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)

        # Remove requests older than 3000ms
        while self.requests[0] < t - 3000:
            self.requests.popleft()

        return len(self.requests)


# =============================================================================
# SECTION 5: TASK SCHEDULER
# =============================================================================

def least_interval(tasks: List[str], n: int) -> int:
    """
    Find minimum intervals to finish all tasks with cooling period n.

    Time: O(n * log(26)), Space: O(26)

    Formula: max(len(tasks), (max_freq - 1) * (n + 1) + max_count)
    """
    from collections import Counter

    # Count frequency of each task
    freq = Counter(tasks)
    max_freq = max(freq.values())

    # Count how many tasks have max frequency
    max_count = sum(1 for f in freq.values() if f == max_freq)

    # Calculate using formula
    part_length = (max_freq - 1) * (n + 1) + max_count

    return max(len(tasks), part_length)


def least_interval_detailed(tasks: List[str], n: int) -> int:
    """
    Detailed implementation using priority queue.

    Time: O(T * n), Space: O(26) where T = total tasks
    """
    from collections import Counter
    import heapq

    freq = [-c for c in Counter(tasks).values()]
    heapq.heapify(freq)

    time = 0
    cooling = deque()

    while heap or cooling:
        time += 1

        if heap:
            count = heapq.heappop(heap) + 1
            if count != 0:
                cooling.append((count, time + n))

        if cooling and cooling[0][1] == time:
            heapq.heappush(heap, cooling.popleft()[0])

    return time


# =============================================================================
# SECTION 6: MOVING AVERAGE
# =============================================================================

class MovingAverage:
    """
    Calculate moving average of last k numbers.

    Time: O(1), Space: O(k)
    """

    def __init__(self, size: int):
        self.window = deque(maxlen=size)
        self.sum = 0

    def next(self, val: int) -> float:
        if len(self.window) == self.window.maxlen:
            self.sum -= self.window[0]

        self.window.append(val)
        self.sum += val

        return self.sum / len(self.window)


# =============================================================================
# SECTION 7: DEQUE OPERATIONS
# =============================================================================

class MaxQueue:
    """
    Queue that supports max operation in O(1).

    Time: O(1) amortized, Space: O(n)
    """

    def __init__(self):
        self.queue = deque()
        self.max_deque = deque()  # Maintain decreasing order

    def push(self, x: int) -> None:
        self.queue.append(x)

        # Maintain decreasing deque
        while self.max_deque and self.max_deque[-1] < x:
            self.max_deque.pop()
        self.max_deque.append(x)

    def pop(self) -> int:
        if not self.queue:
            return -1

        val = self.queue.popleft()

        if val == self.max_deque[0]:
            self.max_deque.popleft()

        return val

    def max(self) -> int:
        return self.max_deque[0] if self.max_deque else -1


# =============================================================================
# SECTION 8: FIRST UNIQUE NUMBER
# =============================================================================

class FirstUnique:
    """
    Find first unique number from stream.

    Time: O(1) for add, O(1) for showFirstUnique
    Space: O(n)
    """

    def __init__(self, nums: List[int]):
        self.queue = deque()
        self.count = {}

        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        while self.queue and self.count[self.queue[0]] > 1:
            self.queue.popleft()

        return self.queue[0] if self.queue else -1

    def add(self, value: int) -> None:
        self.count[value] = self.count.get(value, 0) + 1
        self.queue.append(value)


# =============================================================================
# SECTION 9: TESTING AND DEMO
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("QUEUE ALGORITHMS - TEST DEMO")
    print("=" * 60)

    # Test sliding window maximum
    print("\n--- Sliding Window Maximum ---")
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    result = sliding_window_maximum(nums, k)
    print(f"Maximum in sliding window size {k} for {nums}:")
    print(f"  Result: {result}")

    # Test moving average
    print("\n--- Moving Average ---")
    ma = MovingAverage(3)
    values = [1, 10, 3, 5]
    for v in values:
        print(f"  next({v}) = {ma.next(v):.2f}")

    # Test recent counter
    print("\n--- Recent Counter ---")
    rc = RecentCounter()
    times = [1, 100, 3001, 3002]
    for t in times:
        print(f"  ping({t}) = {rc.ping(t)}")

    # Test task scheduler
    print("\n--- Task Scheduler ---")
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    result = least_interval(tasks, n)
    print(f"Tasks {tasks} with n={n}: {result} intervals")

    # Test circular queue
    print("\n--- Circular Queue ---")
    cq = CircularQueue(3)
    print(f"  Enqueue 1: {cq.enqueue(1)}")
    print(f"  Enqueue 2: {cq.enqueue(2)}")
    print(f"  Enqueue 3: {cq.enqueue(3)}")
    print(f"  Enqueue 4 (full): {cq.enqueue(4)}")
    print(f"  Front: {cq.Front()}")
    print(f"  Rear: {cq.Rear()}")

    # Test queue using two stacks
    print("\n--- Queue Using Two Stacks ---")
    q = QueueUsingTwoStacks()
    q.push(1)
    q.push(2)
    print(f"  push 1,2; peek: {q.peek()}")
    print(f"  pop: {q.pop()}")
    print(f"  pop: {q.pop()}")
    print(f"  empty: {q.empty()}")

    print("\n" + "=" * 60)
    print("All tests completed!")
    print("=" * 60)

"""
Tries (Prefix Trees) - Implementation and Examples
=================================================
Comprehensive Python implementations for Trie problems
commonly asked in FAANG interviews.
"""

from typing import List, Optional


# =============================================================================
# SECTION 1: BASIC TRIE IMPLEMENTATION
# =============================================================================

class TrieNode:
    """Node in the Trie."""

    def __init__(self):
        self.children = {}  # char -> TrieNode
        self.is_end = False  # Marks end of word
        self.word_count = 0  # For counting multiple insertions


class Trie:
    """
    Trie (Prefix Tree) implementation.

    Time: Insert O(m), Search O(m), Prefix O(m)
    Space: O(ALPHABET_SIZE * m * n) where m = avg word length
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Insert word into trie."""
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_end = True
        node.word_count += 1

    def search(self, word: str) -> bool:
        """Check if word exists in trie."""
        node = self._find_node(word)
        return node is not None and node.is_end

    def starts_with(self, prefix: str) -> bool:
        """Check if any word starts with prefix."""
        return self._find_node(prefix) is not None

    def _find_node(self, prefix: str) -> Optional[TrieNode]:
        """Find node corresponding to prefix."""
        node = self.root

        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]

        return node

    def delete(self, word: str) -> bool:
        """Delete word from trie."""
        def _delete(node: TrieNode, word: str, depth: int) -> bool:
            if depth == len(word):
                if not node.is_end:
                    return False
                node.is_end = False
                return len(node.children) == 0

            char = word[depth]
            if char not in node.children:
                return False

            should_delete_child = _delete(node.children[char], word, depth + 1)

            if should_delete_child:
                del node.children[char]
                return len(node.children) == 0

            return False

        if not self.search(word):
            return False

        _delete(self.root, word, 0)
        return True


# =============================================================================
# SECTION 2: LONGEST COMMON PREFIX
# =============================================================================

def longest_common_prefix(strs: List[str]) -> str:
    """
    Find longest common prefix string.

    Time: O(n * m), Space: O(1)
    """
    if not strs:
        return ""

    # Start with first string as prefix
    prefix = strs[0]

    for s in strs[1:]:
        # Reduce prefix until it's a prefix of s
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix


def longest_common_prefix_vertical(strs: List[str]) -> str:
    """
    Vertical scanning approach.

    Time: O(n * m), Space: O(1)
    """
    if not strs:
        return ""

    for i, char in enumerate(strs[0]):
        for s in strs[1:]:
            if i >= len(s) or s[i] != char:
                return strs[0][:i]

    return strs[0]


# =============================================================================
# SECTION 3: WORD SEARCH IN TRIE
# =============================================================================

class WordDictionary:
    """
    Search for words with wildcard support.
    Allows dot (.) to match any character.

    Time: O(m) for search, O(m) for insert
    """

    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word: str) -> None:
        """Add word to dictionary."""
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_end = True

    def search(self, word: str) -> bool:
        """Search for word with dot wildcards."""

        def dfs(node: TrieNode, index: int) -> bool:
            if index == len(word):
                return node.is_end

            char = word[index]

            if char == '.':
                # Try all children
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
                return False
            else:
                if char not in node.children:
                    return False
                return dfs(node.children[char], index + 1)

        return dfs(self.root, 0)


# =============================================================================
# SECTION 4: AUTOCOMPLETE SYSTEM
# =============================================================================

class AutocompleteSystem:
    """
    Autocomplete system with sentence ranking.

    Time: O(m) for input, O(n log n) for sorting results
    """

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.search_history = ""

        # Build trie with frequency
        for sentence, count in zip(sentences, times):
            self._insert_sentence(sentence, count)

    def _insert_sentence(self, sentence: str, count: int = 1) -> None:
        """Insert sentence with count."""
        node = self.root

        for char in sentence:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_end = True
        node.word_count += count
        node.sentence = sentence

    def input(self, c: str) -> List[str]:
        """
        Process input character.

        Returns top 3 sentences with highest frequency.
        """
        if c == '#':
            # End of current sentence
            self._insert_sentence(self.search_history, 1)
            self.search_history = ""
            return []

        self.search_history += c
        results = []

        # Find all matching sentences
        node = self.root
        for char in self.search_history:
            if char not in node.children:
                return []
            node = node.children[char]

        # Collect all sentences from this prefix
        self._collect_sentences(node, results)

        # Sort by frequency and return top 3
        results.sort(key=lambda x: (-x[1], x[0]))
        return [s[0] for s in results[:3]]

    def _collect_sentences(self, node: TrieNode, results: List[tuple]) -> None:
        """Collect all sentences starting from node."""
        if node.is_end:
            results.append((node.sentence, node.word_count))

        for child in node.children.values():
            self._collect_sentences(child, results)


# =============================================================================
# SECTION 5: REPLACE WORDS
# =============================================================================

def replace_words(dictionary: List[str], sentence: str) -> str:
    """
    Replace words with shortest root from dictionary.

    Time: O(m * n) where m = sentence length, n = dict size
    """
    trie = Trie()

    # Insert all roots
    for word in dictionary:
        trie.insert(word)

    words = sentence.split()
    result = []

    for word in words:
        # Find shortest root
        prefix = ""
        found = False

        for char in word:
            prefix += char
            if trie.starts_with(prefix):
                if trie.search(prefix):
                    result.append(prefix)
                    found = True
                    break

        if not found:
            result.append(word)

    return ' '.join(result)


# =============================================================================
# SECTION 6: PALINDROME PAIRS
# =============================================================================

def palindrome_pairs(words: List[str]) -> List[List[int]]:
    """
    Find all pairs of indices where concatenation forms palindrome.

    Time: O(n * m²), Space: O(n * m)

    Optimized using trie.
    """
    if not words:
        return []

    result = []
    trie = Trie()

    # Insert reversed words
    for i, word in enumerate(words):
        trie.insert(word[::-1])

    # Find pairs
    for i, word in enumerate(words):
        # Check all possible splits
        for j in range(len(word) + 1):
            prefix = word[:j]
            suffix = word[j:]

            # Check if prefix forms palindrome with reversed suffix
            if is_palindrome(prefix):
                reversed_suffix = suffix[::-1]
                if trie.search(reversed_suffix):
                    idx = trie._find_node(reversed_suffix).word_count - 1
                    if idx != i:
                        result.append([i, idx])

            # Check if suffix forms palindrome with reversed prefix
            if j < len(word) and is_palindrome(suffix):
                reversed_prefix = prefix[::-1]
                if trie.search(reversed_prefix):
                    idx = trie._find_node(reversed_prefix).word_count - 1
                    if idx != i:
                        result.append([idx, i])

    return result


def is_palindrome(s: str) -> bool:
    """Check if string is palindrome."""
    return s == s[::-1]


# =============================================================================
# SECTION 7: MAXIMUM XOR IN ARRAY
# =============================================================================

class TrieXor:
    """
    Trie for finding maximum XOR pair.
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, num: int) -> None:
        """Insert number as binary string."""
        node = self.root

        for i in range(31, -1, -1):
            bit = (num >> i) & 1

            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]

    def find_max_xor(self, num: int) -> int:
        """Find maximum XOR with any number in trie."""
        node = self.root
        max_xor = 0

        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            opposite = 1 - bit

            if opposite in node.children:
                max_xor = (max_xor << 1) | 1
                node = node.children[opposite]
            else:
                max_xor = max_xor << 1
                node = node.children[bit]

        return max_xor


def find_maximum_xor(nums: List[int]) -> int:
    """
    Find maximum XOR of any two numbers.

    Time: O(n * 32), Space: O(n * 32)
    """
    trie = TrieXor()

    # Insert all numbers
    for num in nums:
        trie.insert(num)

    # Find max XOR for each
    max_xor = 0
    for num in nums:
        max_xor = max(max_xor, trie.find_max_xor(num))

    return max_xor


# =============================================================================
# SECTION 8: MAP SUM PAIRS
# =============================================================================

class MapSum:
    """
    MapSum stores key-value pairs where sum is over keys with prefix.

    Time: O(m) for insert and sum
    """

    def __init__(self):
        self.root = TrieNode()
        self.values = {}  # key -> value

    def insert(self, key: str, val: int) -> None:
        """Insert or update key-value pair."""
        delta = val - self.values.get(key, 0)
        self.values[key] = val

        node = self.root

        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.word_count += delta

    def sum(self, prefix: str) -> int:
        """Get sum of all keys with given prefix."""
        node = self.root

        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]

        return node.word_count


# =============================================================================
# SECTION 9: DESIGN ADD AND SEARCH WORDS
# =============================================================================

class WordFilter:
    """
    Design a structure that supports adding words and
    filtering words matching a pattern with wildcards.

    Time: O(m) for add, O(m) for filter
    """

    def __init__(self, words: List[str]):
        self.trie = Trie()

        for i, word in enumerate(words):
            # Create multiple prefixes to support suffix search
            for j in range(len(word)):
                prefix = word[:j + 1]
                key = prefix + '#' + word
                self.trie.insert(key)

        self.word_count = len(words)

    def f(self, prefix: str, suffix: str) -> int:
        """Find index of word matching prefix and suffix."""
        key = prefix + '#' + suffix

        # Find matching words
        node = self.trie._find_node(key)
        if node:
            return node.word_count - 1

        return -1


# =============================================================================
# SECTION 10: TESTING AND DEMO
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("TRIE ALGORITHMS - TEST DEMO")
    print("=" * 60)

    # Test basic Trie
    print("\n--- Basic Trie ---")
    trie = Trie()
    words = ["apple", "app", "apply", "banana", "band"]

    for word in words:
        trie.insert(word)

    print(f"Search 'app': {trie.search('app')}")
    print(f"Search 'appl': {trie.search('appl')}")
    print(f"Starts with 'app': {trie.starts_with('app')}")
    print(f"Starts with 'ban': {trie.starts_with('ban')}")

    # Test longest common prefix
    print("\n--- Longest Common Prefix ---")
    strs = ["flower", "flow", "flight"]
    print(f"LCP of {strs}: '{longest_common_prefix(strs)}'")

    strs2 = ["dog", "racecar", "car"]
    print(f"LCP of {strs2}: '{longest_common_prefix(strs2)}'")

    # Test Word Dictionary
    print("\n--- Word Dictionary ---")
    wd = WordDictionary()
    words = ["bad", "dad", "mad"]
    for word in words:
        wd.add_word(word)

    print(f"Search 'pad': {wd.search('pad')}")
    print(f"Search 'bad': {wd.search('bad')}")
    print(f"Search '.ad': {wd.search('.ad')}")
    print(f"Search 'b..': {wd.search('b..')}")

    # Test Map Sum
    print("\n--- Map Sum ---")
    ms = MapSum()
    ms.insert("apple", 3)
    print(f"Sum 'ap': {ms.sum('ap')}")
    ms.insert("app", 2)
    print(f"Sum 'ap': {ms.sum('ap')}")
    ms.insert("apple", 2)  # Update
    print(f"Sum 'ap': {ms.sum('ap')}")

    # Test Maximum XOR
    print("\n--- Maximum XOR ---")
    nums = [3, 10, 5, 25, 2, 8]
    result = find_maximum_xor(nums)
    print(f"Maximum XOR in {nums}: {result}")
    # Expected: 5 ^ 25 = 28

    # Test Replace Words
    print("\n--- Replace Words ---")
    dictionary = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    result = replace_words(dictionary, sentence)
    print(f"Replace: '{result}'")

    print("\n" + "=" * 60)
    print("All tests completed!")
    print("=" * 60)

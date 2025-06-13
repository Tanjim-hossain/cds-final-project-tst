class TSTNode:
    """
    Node class for Ternary Search Tree.
    Each node stores a character and pointers to left, middle, and right children.
    The is_end flag is True if this node marks the end of a valid string.
    """
    __slots__ = ['char', 'left', 'mid', 'right', 'is_end']

    def __init__(self, char):
        self.char = char
        self.left = None
        self.mid = None
        self.right = None
        self.is_end = False

class TernarySearchTree:
    """
    Ternary Search Tree (TST) for efficient string storage and retrieval.
    Supports insert, search, prefix search, count, all_strings, and ASCII visualization.
    """
    def __init__(self):
        """Initialize an empty TST."""
        self.root = None

    def insert(self, word):
        """
        Insert a string into the TST.
        :param word: String to insert.
        """
        if not word:
            return
        if not self.root:
            self.root = TSTNode(word[0])
        node = self.root
        idx = 0
        while True:
            char = word[idx]
            if char < node.char:
                if not node.left:
                    node.left = TSTNode(char)
                node = node.left
            elif char > node.char:
                if not node.right:
                    node.right = TSTNode(char)
                node = node.right
            else:  # char == node.char
                if idx == len(word) - 1:
                    node.is_end = True
                    return
                if not node.mid:
                    node.mid = TSTNode(word[idx + 1])
                node = node.mid
                idx += 1

    def search(self, word):
        """
        Check if a string exists in the TST.
        :param word: String to search.
        :return: True if found, False otherwise.
        """
        if not word or not self.root:
            return False
        node = self.root
        idx = 0
        while node:
            char = word[idx]
            if char < node.char:
                node = node.left
            elif char > node.char:
                node = node.right
            else:
                if idx == len(word) - 1:
                    return node.is_end
                node = node.mid
                idx += 1
        return False

    def prefix_search(self, prefix):
        """
        Find all strings in the TST that start with the given prefix.
        :param prefix: Prefix string.
        :return: List of strings starting with prefix.
        """
        results = []
        def _collect(node, prefix_so_far):
            if node is None:
                return
            if node.is_end:
                results.append(prefix_so_far + node.char)
            _collect(node.left, prefix_so_far)
            _collect(node.mid, prefix_so_far + node.char)
            _collect(node.right, prefix_so_far)
        def _search_prefix(node, word, idx):
            if node is None:
                return None
            char = word[idx]
            if char < node.char:
                return _search_prefix(node.left, word, idx)
            elif char > node.char:
                return _search_prefix(node.right, word, idx)
            elif idx < len(word) - 1:
                return _search_prefix(node.mid, word, idx + 1)
            else:
                return node
        if not prefix:
            return []
        node = _search_prefix(self.root, prefix, 0)
        if node is None:
            return []
        if node.is_end:
            results.append(prefix)
        _collect(node.mid, prefix)
        return results

    def count(self):
        """
        Count the total number of unique strings stored in the TST.
        :return: Integer count.
        """
        def _count(node):
            if node is None:
                return 0
            cnt = 1 if node.is_end else 0
            return cnt + _count(node.left) + _count(node.mid) + _count(node.right)
        return _count(self.root)

    def all_strings(self):
        """
        Return a list of all strings stored in the TST.
        :return: List of strings.
        """
        results = []
        def _collect(node, path):
            if node is None:
                return
            _collect(node.left, path)
            new_path = path + node.char
            if node.is_end:
                results.append(new_path)
            _collect(node.mid, new_path)
            _collect(node.right, path)
        _collect(self.root, "")
        return results

    def ascii_display(self):
        """
        Print an ASCII visualization of the TST structure.
        Useful for small trees and debugging.
        """
        def _display(node, indent="", last='updown'):
            if node is None:
                return
            # Right subtree first
            if node.right:
                _display(node.right, indent + "     ", 'up')
            # Node itself
            if last == 'up':
                print(indent + ' \\-----', end='')
            elif last == 'down':
                print(indent + ' \\-----', end='')
            else:
                print(indent + ' |-----', end='')
            print(f"[{node.char}]" + ("*" if node.is_end else ""))
            # Middle subtree 
            if node.mid:
                _display(node.mid, indent + " |    ", 'updown')
            # Left subtree 
            if node.left:
                _display(node.left, indent + "     ", 'down')
        print("ASCII representation of TST:")
        _display(self.root)
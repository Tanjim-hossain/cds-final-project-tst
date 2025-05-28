class TSTNode:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.left = None
        self.eq = None
        self.right = None

class TernarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, word):
        if word:
            self.root = self._insert(self.root, word, 0)

    def _insert(self, node, word, index):
        char = word[index]

        if not node:
            node = TSTNode(char)

        if char < node.char:
            node.left = self._insert(node.left, word, index)
        elif char > node.char:
            node.right = self._insert(node.right, word, index)
        else:
            if index + 1 < len(word):
                node.eq = self._insert(node.eq, word, index + 1)
            else:
                if not node.is_end:
                    self.size += 1
                node.is_end = True
        return node

    def search(self, word):
        return self._search(self.root, word, 0)

    def _search(self, node, word, index):
        if not node:
            return False
        char = word[index]

        if char < node.char:
            return self._search(node.left, word, index)
        elif char > node.char:
            return self._search(node.right, word, index)
        else:
            if index == len(word) - 1:
                return node.is_end
            return self._search(node.eq, word, index + 1)

    def prefix_search(self, prefix):
        results = []
        node = self._prefix_node(self.root, prefix, 0)
        if node:
            if node.is_end:
                results.append(prefix)
            self._collect(node.eq, prefix, results)
        return results

    def _prefix_node(self, node, prefix, index):
        if not node:
            return None
        char = prefix[index]

        if char < node.char:
            return self._prefix_node(node.left, prefix, index)
        elif char > node.char:
            return self._prefix_node(node.right, prefix, index)
        else:
            if index == len(prefix) - 1:
                return node
            return self._prefix_node(node.eq, prefix, index + 1)
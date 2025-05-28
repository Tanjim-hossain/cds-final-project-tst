class TSTNode:
    def __init__(self, char):
        self.char = char
        self.left = None
        self.mid = None
        self.right = None
        self.is_end = False

class TernarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, word):
        def _insert(node, word, idx):
            char = word[idx]
            if not node:
                node = TSTNode(char)
            if char < node.char:
                node.left = _insert(node.left, word, idx)
            elif char > node.char:
                node.right = _insert(node.right, word, idx)
            elif idx < len(word) - 1:
                node.mid = _insert(node.mid, word, idx+1)
            else:
                node.is_end = True
            return node
        if word:
            self.root = _insert(self.root, word, 0)

    def search(self, word):
        def _search(node, word, idx):
            if not node:
                return False
            char = word[idx]
            if char < node.char:
                return _search(node.left, word, idx)
            elif char > node.char:
                return _search(node.right, word, idx)
            elif idx < len(word) - 1:
                return _search(node.mid, word, idx+1)
            else:
                return node.is_end
        return _search(self.root, word, 0) if word else False

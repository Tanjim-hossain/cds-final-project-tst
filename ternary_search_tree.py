class TSTNode:
    __slots__ = ['char', 'left', 'mid', 'right', 'is_end']  # Memory optimization

    def __init__(self, char):
        self.char = char
        self.left = None
        self.mid = None
        self.right = None
        self.is_end = False


class TernarySearchTree:
    def __init__(self):
        self.root = None

    #CHANGED: Iterative version of insert
    def insert(self, word):
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
           
    #CHANGED: Iterative version of search
    def search(self, word):
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
   
        def _count(node):
            if node is None:
                return 0
            cnt = 1 if node.is_end else 0
            return cnt + _count(node.left) + _count(node.mid) + _count(node.right)

        return _count(self.root)

    def all_strings(self):
 
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

        def _display(node, indent="", last='updown'):
            if node is None:
                return
            # first, display right subtree
            if node.right:
                _display(node.right, indent + "     ", 'up')
            # then this node
            if last == 'up':
                print(indent + ' \\-----', end='')
            elif last == 'down':
                print(indent + ' \\-----', end='')  
            else:
                print(indent + ' |-----', end='')
            print(f"[{node.char}]" + ("*" if node.is_end else ""))
            # then middle subtree
            if node.mid:
                _display(node.mid, indent + " |    ", 'updown')
            # finally left subtree
            if node.left:
                _display(node.left, indent + "     ", 'down')

        print("ASCII representation of TST:")
        _display(self.root)

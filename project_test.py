import unittest
from ternary_search_tree import TernarySearchTree

DATA_PATH = "/Users/tanjimhossain/Documents/Concepts of Data Science/CDS_final-project/data/search_trees/"

class TestTernarySearchTree(unittest.TestCase):
    def setUp(self):
        self.tst = TernarySearchTree()
        # Load real insert and not-insert words
        with open(DATA_PATH + "insert_words.txt") as f:
            self.insert_words = [line.strip() for line in f if line.strip()]
        with open(DATA_PATH + "not_insert_words.txt") as f:
            self.not_insert_words = [line.strip() for line in f if line.strip()]
        # Insert all words
        for word in self.insert_words:
            self.tst.insert(word)

    def test_inserted_words_found(self):
        for word in self.insert_words:
            self.assertTrue(self.tst.search(word), f"Word '{word}' should be found after insertion.")

    def test_not_inserted_words_not_found(self):
        for word in self.not_insert_words:
            self.assertFalse(self.tst.search(word), f"Word '{word}' should NOT be found (was not inserted).")

if __name__ == "__main__":
    unittest.main()

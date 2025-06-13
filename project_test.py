import unittest
from ternary_search_tree import TernarySearchTree

DATA_PATH = "/Users/tanjimhossain/Documents/Concepts of Data Science/CDS_final-project/data/search_trees/"

class TestTernarySearchTree(unittest.TestCase):
    def setUp(self):
        self.tst = TernarySearchTree()
        # Load words to insert and not insert
        with open(DATA_PATH + "insert_words.txt") as f:
            self.insert_words = [line.strip() for line in f if line.strip()]
        with open(DATA_PATH + "not_insert_words.txt") as f:
            self.not_insert_words = [line.strip() for line in f if line.strip()]
        for word in self.insert_words:
            self.tst.insert(word)

    def test_inserted_words_found(self):
        for word in self.insert_words:
            self.assertTrue(self.tst.search(word), f"Word '{word}' should be found after insertion.")

    def test_not_inserted_words_not_found(self):
        for word in self.not_insert_words:
            self.assertFalse(self.tst.search(word), f"Word '{word}' should NOT be found (was not inserted).")

    def test_prefix_search(self):
        # Try several prefixes including an edge case and a typical case
        test_prefixes = ["a", "ab", "z", self.insert_words[0][:2]]
        for prefix in test_prefixes:
            results = self.tst.prefix_search(prefix)
            for word in results:
                self.assertTrue(word.startswith(prefix), f"Word '{word}' does not start with prefix '{prefix}'")

    def test_count(self):
        self.assertEqual(self.tst.count(), len(set(self.insert_words)), "TST count should match number of unique inserted words.")

    def test_all_strings(self):
        all_words = self.tst.all_strings()
        for word in self.insert_words:
            self.assertIn(word, all_words, f"Inserted word '{word}' missing from all_strings().")

if __name__ == "__main__":
    unittest.main()
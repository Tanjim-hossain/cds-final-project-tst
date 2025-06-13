"""
demo_tst_with_real_data.py

Demonstrates the usage of Ternary Search Tree (TST) with the real project dataset.
Features:
- Insertion of words from file
- Search and negative search checks
- Prefix search example
- Word count
- Retrieve all stored words
- ASCII tree visualization
"""

from ternary_search_tree import TernarySearchTree

# Data path (update if your path changes)
DATA_PATH = "/Users/tanjimhossain/Documents/Concepts of Data Science/CDS_final-project/data/search_trees/"

# Load insert words
with open(DATA_PATH + "insert_words.txt") as f:
    insert_words = [line.strip() for line in f if line.strip()]

# Load not-insert words
with open(DATA_PATH + "not_insert_words.txt") as f:
    not_insert_words = [line.strip() for line in f if line.strip()]

# Build tree
tst = TernarySearchTree()
for word in insert_words:
    tst.insert(word)

print("\n--- TST Demo with Real Dataset ---")
print("Total words inserted:", len(insert_words))

# Check: all inserted words are found
all_inserted_found = all(tst.search(word) for word in insert_words)
print("All inserted words found?", all_inserted_found)

# Check: all not-inserted words are NOT found
all_not_inserted_not_found = all(not tst.search(word) for word in not_insert_words)
print("All not-inserted words not found?", all_not_inserted_not_found)

# Print some example searches
if insert_words:
    print(f"Example: search '{insert_words[0]}':", tst.search(insert_words[0]))
if not_insert_words:
    print(f"Example: search '{not_insert_words[0]}':", tst.search(not_insert_words[0]))

# Prefix search example
if insert_words:
    prefix = insert_words[0][:2]
    prefix_results = tst.prefix_search(prefix)
    print(f"Prefix search for '{prefix}': (showing up to 5 results)", prefix_results[:5])

# Count words
print("TST count (number of unique words):", tst.count())

# List all words (just preview the first 10)
all_words = tst.all_strings()
print("First 10 words in TST:", all_words[:10])

# ASCII tree display (can be large for a big dataset)
print("\nASCII Display (partial tree):")
tst.ascii_display()

print("\nDEMO COMPLETE\n")

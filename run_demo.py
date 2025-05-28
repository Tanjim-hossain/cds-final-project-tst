from ternary_search_tree import TernarySearchTree

# data path
data_path = "/Users/tanjimhossain/Documents/Concepts of Data Science/CDS_final-project/data/search_trees/"

# Load insert words
with open(data_path + "insert_words.txt") as f:
    insert_words = [line.strip() for line in f if line.strip()]

# Load not-insert words
with open(data_path + "not_insert_words.txt") as f:
    not_insert_words = [line.strip() for line in f if line.strip()]

# Build tree
tst = TernarySearchTree()
for word in insert_words:
    tst.insert(word)

# all inserted words should be found
all_inserted_found = all(tst.search(word) for word in insert_words)
print("All inserted words found?", all_inserted_found)

# none of the not-inserted words should be found
all_not_inserted_not_found = all(not tst.search(word) for word in not_insert_words)
print("All not-inserted words not found?", all_not_inserted_not_found)

# Print some results for manual check
if insert_words:
    print(f"Example: search '{insert_words[0]}' =", tst.search(insert_words[0]))
if not_insert_words:
    print(f"Example: search '{not_insert_words[0]}' =", tst.search(not_insert_words[0]))

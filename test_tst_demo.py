from ternary_search_tree import TernarySearchTree

# insertion and search
tst = TernarySearchTree()
words = ["cat", "cab", "dog", "dot", "rat", "rate", "catnip"]
for word in words:
    tst.insert(word)

print("\n--- BASIC SEARCH TESTS ---")
for w in ["cat", "dog", "rat", "dot", "cab", "rate", "catnip"]:
    print(f"Search '{w}':", tst.search(w))  

for w in ["ca", "do", "caterpillar", "rattle"]:
    print(f"Search '{w}':", tst.search(w))  

# Prefix search
print("\n--- PREFIX SEARCH TESTS ---")
for prefix in ["ca", "do", "ra", "cat"]:
    print(f"Prefix '{prefix}':", tst.prefix_search(prefix))

# Count of words
print("\n--- COUNT TEST ---")
print("Number of words in TST:", tst.count())  

# List all words
print("\n--- ALL STRINGS TEST ---")
print("All stored words:", sorted(tst.all_strings()))

# ASCII Display
print("\n--- ASCII TREE VISUALIZATION ---")
tst.ascii_display()

# Insert and test empty string
print("\n--- EMPTY STRING EDGE CASE ---")
tst.insert("")
print("Search '':", tst.search(""))  
print("Prefix search '':", tst.prefix_search(""))  
# Insert and search for single-character word
print("\n--- SINGLE CHARACTER TEST ---")
tst.insert("a")
print("Search 'a':", tst.search("a"))  
print("Prefix search 'a':", tst.prefix_search("a"))  

# Prefix that matches nothing
print("\n--- NO MATCH PREFIX TEST ---")
print("Prefix 'zzz':", tst.prefix_search("zzz"))  

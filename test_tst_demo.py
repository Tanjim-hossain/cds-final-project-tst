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
#  cases of invalid inputs
print("\n--- INVALID AND EDGE INPUT TESTS ---")
invalid_inputs = ["", "!", "123", "@cat", "car#", " "]
for invalid in invalid_inputs:
    tst.insert(invalid)
    print(f"Search '{invalid}':", tst.search(invalid))

# Test for long words
print("\n--- LONG STRING TESTS ---")
long_words = ["supercalifragilisticexpialidocious",
              "pneumonoultramicroscopicsilicovolcanoconiosis"]
for long_word in long_words:
    tst.insert(long_word)
    print(f"Search '{long_word}':", tst.search(long_word))


# Prefix search
print("\n--- PREFIX SEARCH TESTS ---")
for prefix in ["ca", "do", "ra", "cat"]:
    print(f"Prefix '{prefix}':", tst.prefix_search(prefix))

# Count of words
print("\n--- COUNT TEST ---")
print("Number of words in TST:", tst.count())  

# Test for all strings
print("\n--- FINAL COUNT TEST ---")
print("Total words in TST:", tst.count())

# List all words
print("\n--- ALL STRINGS TEST ---")
print("All stored words:", sorted(tst.all_strings()))

# ASCII Display
print("\n--- ASCII TREE VISUALIZATION ---")
tst.ascii_display()

# Test for case sensitivity
print("\n--- CASE SENSITIVITY TEST ---")
tst.insert("Cat")
tst.insert("DOG")
print("Search 'Cat':", tst.search("Cat"))
print("Search 'DOG':", tst.search("DOG"))
print("Prefix 'C':", tst.prefix_search("C"))


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

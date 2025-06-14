"""
benchmark_tst.py

Benchmarks Ternary Search Tree (TST) insert and search performance using a large English word list.
Generates and saves two plots: total operation time and average time per word.
"""

import time
import matplotlib.pyplot as plt
from ternary_search_tree import TernarySearchTree

DATA_PATH = "/Users/tanjimhossain/Documents/Concepts of Data Science/CDS_final-project/data/search_trees/"

# Load a large list of words
with open(DATA_PATH + "corncob_lowercase.txt") as f:
    all_words = [line.strip() for line in f if line.strip()]

# Choose different sizes for benchmarking
sizes = [100, 500, 1000, 5000, 10000, 20000, 40000, 50000]
insert_times = []
search_times = []

for size in sizes:
    print(f"Benchmarking for size {size}...")
    words = all_words[:size]
    tst = TernarySearchTree()
    
    # Time insertion
    t0 = time.time()
    for word in words:
        tst.insert(word)
    insert_times.append(time.time() - t0)
    
    # Time search
    t0 = time.time()
    for word in words:
        tst.search(word)
    search_times.append(time.time() - t0)

# Plot 1: Total Insert & Search Time
plt.figure(num=1, figsize=(8,5))
plt.plot(sizes, insert_times, marker='o', label="Insert Time")
plt.plot(sizes, search_times, marker='o', label="Search Time")
plt.xlabel("Number of Words")
plt.ylabel("Total Time (seconds)")
plt.title("Ternary Search Tree Performance: Insert & Search")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("TST_total_time.png")
plt.show()

# Plot 2: Average Time per Word
per_word_insert = [t/s for t,s in zip(insert_times, sizes)]
per_word_search = [t/s for t,s in zip(search_times, sizes)]
x = range(len(sizes))
width = 0.35

plt.figure(num=2, figsize=(6,4))
plt.bar(x, per_word_insert, width, label="Insert per Word")
plt.bar([i+width for i in x], per_word_search, width, label="Search per Word")
plt.xticks([i+width/2 for i in x], sizes, rotation=45)
plt.xlabel("Number of Words")
plt.ylabel("Time per Word (seconds)")
plt.title("Average Time per Word")
plt.legend()
plt.tight_layout()
plt.savefig("TST_avg_time.png")
plt.show()

print("\nBenchmark complete! Plots saved as 'TST_total_time.png' and 'TST_avg_time.png'.")

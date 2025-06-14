import time
from ternary_search_tree import TernarySearchTree
import os

import matplotlib.pyplot as plt   

DATA_PATH = os.path.join("data", "search_trees")

# Load data
with open(os.path.join(DATA_PATH, "corncob_lowercase.txt")) as f:
    all_words = [line.strip() for line in f if line.strip()]

sizes = [100, 500, 1000, 5000, 10000, 20000, 40000, 50000]
insert_times = []
search_times = []

overall_start = time.time()

for size in sizes:
    print(f"Benchmarking for size {size}...", flush=True)
    words = all_words[:size]
    tst = TernarySearchTree()
    # Insert timing
    t0 = time.time()
    for word in words:
        tst.insert(word)
    t_insert = time.time() - t0
    insert_times.append(t_insert)
    print(f"Insert time for {size}: {t_insert:.4f} sec", flush=True)
    # Search timing
    t0 = time.time()
    for word in words:
        tst.search(word)
    t_search = time.time() - t0
    search_times.append(t_search)
    print(f"Search time for {size}: {t_search:.4f} sec", flush=True)

overall_end = time.time()

print(f"\n==== Benchmark completed ====", flush=True)
print(f"Total runtime: {overall_end - overall_start:.2f} seconds", flush=True)
print(f"Insert times (s): {insert_times}", flush=True)
print(f"Search times (s): {search_times}", flush=True)


# Plot 1: Insert/Search Time vs. Number of Words
plt.figure(figsize=(8,5))
plt.plot(sizes, insert_times, marker='o', label="Insert Time")
plt.plot(sizes, search_times, marker='o', label="Search Time")
plt.xlabel("Number of Words")
plt.ylabel("Time (seconds)")
plt.title("Insert/Search Time vs. Number of Words")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("TST_total_time.png")
plt.close()

# Plot 2: Average Time per Word vs. Number of Words
per_word_insert = [t/s for t,s in zip(insert_times, sizes)]
per_word_search = [t/s for t,s in zip(search_times, sizes)]
x = range(len(sizes))
width = 0.35
plt.figure(figsize=(6,4))
plt.bar(x, per_word_insert, width, label="Insert per Word")
plt.bar([i+width for i in x], per_word_search, width, label="Search per Word")
plt.xticks([i+width/2 for i in x], sizes, rotation=45)
plt.xlabel("Number of Words")
plt.ylabel("Time per Word (s)")
plt.title("Average Time per Word vs. Number of Words")
plt.legend()
plt.tight_layout()
plt.savefig("TST_avg_time.png")
plt.close()
print("PNG plots saved in:", os.getcwd())

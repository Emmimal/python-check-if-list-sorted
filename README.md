# python-check-if-list-sorted
5 efficient O(n) ways to check if a Python list is sorted — without the O(n log n) cost of sort(). Code examples + explanations

This repo shares **5 efficient ways** to check if a Python list is sorted — all O(n) with early exit, no wasteful `sort()`!

For the **full detailed guide** (explanations, edge cases, benchmarks, NumPy/Pandas tips, and more), read my blog post:

🔗 [**How to Check If a List Is Sorted in Python – Complete Guide**](https://emitechlogic.com/check-if-list-is-sorted-python/)

Star this repo if helpful! ⭐

## Why This Matters

Avoid this common trap:

```python
# Wasteful — O(n log n) + copy!
def is_sorted_bad(lst):
    return lst == sorted(lst)

Use these instead!
The 5 Methods

1. all() + zip() — Pythonic Favorite

def is_sorted_zip(lst):
    return all(x <= y for x, y in zip(lst, lst[1:]))

# Strictly increasing (no duplicates)
def is_strictly_sorted_zip(lst):
    return all(x < y for x, y in zip(lst, lst[1:]))

2. Classic For Loop — Clear & Explicit
def is_sorted_loop(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

3. all() + range() — Index Access
def is_sorted_range(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

4. itertools.pairwise() — Modern (Python 3.10+)

from itertools import pairwise

def is_sorted_pairwise(lst):
    return all(x <= y for x, y in pairwise(lst))

5. operator.le — Custom Objects/Keys
import operator

def is_sorted_by(lst, key=lambda x: x):
    return all(key(x) <= key(y) for x, y in zip(lst, lst[1:]))

Descending Order Example
def is_non_increasing(lst):
    return all(x >= y for x, y in zip(lst, lst[1:]))

Quick Tests (Run in Python)
print(is_sorted_zip([1, 2, 3, 4]))      # True
print(is_sorted_zip([1, 3, 2, 4]))      # False
print(is_sorted_zip([5, 5, 5]))         # True (non-decreasing)

Tips

Empty/single-element lists → Always True
For NumPy: np.all(arr[:-1] <= arr[1:])
For Pandas: series.is_monotonic_increasing

Full explanations + more:
🔗 https://emitechlogic.com/check-if-list-is-sorted-python/

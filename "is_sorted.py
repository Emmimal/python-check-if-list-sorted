"""
is_sorted.py

A lightweight Python module with multiple efficient ways to check if a list
is sorted. All methods run in O(n) time with early exit.

Author: Nirmala (EmiTechLogic)
Blog: https://emitechlogic.com/check-if-list-is-sorted-python/
GitHub: https://github.com/yourusername/python-check-if-list-sorted

Usage:
    from is_sorted import is_sorted_ascending, is_sorted_descending

    print(is_sorted_ascending([1, 2, 3, 4]))      # True
    print(is_sorted_ascending([1, 3, 2, 4]))      # False
"""

from __future__ import annotations

from typing import Any, Callable, Iterable, Sequence


# Backport of itertools.pairwise for Python < 3.10
def _pairwise(iterable: Iterable[Any]) -> Iterable[tuple[Any, Any]]:
    """Yield consecutive overlapping pairs from iterable."""
    it = iter(iterable)
    a = next(it, None)
    if a is None:
        return
    for b in it:
        yield a, b
        a = b


# Detect if the built-in pairwise is available (Python 3.10+)
try:
    from itertools import pairwise  # type: ignore
except ImportError:
    pairwise = _pairwise  # Fall back to our implementation


def is_sorted_ascending(
    lst: Sequence[Any],
    *,
    strict: bool = False,
    key: Callable[[Any], Any] | None = None,
) -> bool:
    """
    Check if a sequence is sorted in non-decreasing (ascending) order.

    Parameters
    ----------
    lst : Sequence
        The sequence to check.
    strict : bool, default False
        If True, require strictly increasing order (no duplicates).
    key : callable, optional
        A key function to determine the sort key for each element
        (e.g., key=str.lower or key=lambda x: x.age).

    Returns
    -------
    bool
        True if sorted, False otherwise.

    Examples
    --------
    >>> is_sorted_ascending([1, 2, 3, 4])
    True
    >>> is_sorted_ascending([1, 2, 2, 3])
    True
    >>> is_sorted_ascending([1, 2, 2, 3], strict=True)
    False
    """
    if key is None:
        key = lambda x: x

    compare = lambda x, y: x < y if strict else x <= y

    # Use pairwise (built-in or backport) for cleanest implementation
    return all(compare(key(x), key(y)) for x, y in pairwise(lst))


def is_sorted_descending(
    lst: Sequence[Any],
    *,
    strict: bool = False,
    key: Callable[[Any], Any] | None = None,
) -> bool:
    """
    Check if a sequence is sorted in non-increasing (descending) order.

    Parameters
    ----------
    lst : Sequence
        The sequence to check.
    strict : bool, default False
        If True, require strictly decreasing order (no duplicates).
    key : callable, optional
        A key function for custom sorting criteria.

    Returns
    -------
    bool
        True if sorted descending, False otherwise.
    """
    if key is None:
        key = lambda x: x

    compare = lambda x, y: x > y if strict else x >= y

    return all(compare(key(x), key(y)) for x, y in pairwise(lst))


# Alternative implementations (kept for reference/learning)
def is_sorted_ascending_zip(lst: Sequence[Any], strict: bool = False) -> bool:
    """Using zip() + lst[1:] (classic approach)."""
    compare = lambda x, y: x < y if strict else x <= y
    return all(compare(x, y) for x, y in zip(lst, lst[1:]))


def is_sorted_ascending_loop(lst: Sequence[Any], strict: bool = False) -> bool:
    """Classic for-loop version (great for interviews)."""
    compare = lambda x, y: x < y if strict else x <= y
    for i in range(len(lst) - 1):
        if not compare(lst[i], lst[i + 1]):
            return False
    return True


def is_sorted_ascending_range(lst: Sequence[Any], strict: bool = False) -> bool:
    """Index-based with range()."""
    compare = lambda x, y: x < y if strict else x <= y
    return all(compare(lst[i], lst[i + 1]) for i in range(len(lst) - 1))


# Export public API
__all__ = [
    "is_sorted_ascending",
    "is_sorted_descending",
    "is_sorted_ascending_zip",
    "is_sorted_ascending_loop",
    "is_sorted_ascending_range",
    "pairwise",
]


# Simple demo when run directly
if __name__ == "__main__":
    test_lists = [
        [1, 2, 3, 4],
        [1, 3, 2, 4],
        [5, 5, 5],
        [],
        [42],
        [10, 8, 8, 5, 2],
    ]

    for lst in test_lists:
        asc = is_sorted_ascending(lst)
        asc_strict = is_sorted_ascending(lst, strict=True)
        desc = is_sorted_descending(lst)
        print(f"{lst!r}: ascending={asc} (strict={asc_strict}), descending={desc}")

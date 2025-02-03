#!/usr/bin/python3
"""
This module implements a CountedIterator class that keeps track
of iteration count.
"""


class CountedIterator:
    """Iterator that counts items fetched during iteration."""

    def __init__(self, iterable):
        """Initialize with iterable and counter."""
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """Return self as iterator."""
        return self

    def __next__(self):
        """Return next item and increment counter."""
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """Return number of items iterated."""
        return self.count

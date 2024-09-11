#!/usr/bin/env python3
"""Apply the LIFO Caching."""
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """Last In First Out algorithm."""

    counter = None

    def __init__(self):
        """Call constructor of parent class."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Insert Key and value."""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key = self.cache_data.popitem(True)
                print("Discarded: {}".format(last_key))
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Retrieve an item by key."""
        return self.cache_data.get(key, None)

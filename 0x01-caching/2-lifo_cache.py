#!/usr/bin/env python3
"""Apply the LIFO Caching."""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Last In First Out algorithm."""

    counter = BaseCaching.MAX_ITEMS - 1

    def __init__(self):
        """Call constructor of parent class."""
        super().__init__()

    def put(self, key, item):
        """Insert Key and value."""
        if key is None or item is None:
            return
        self.index = 0
        self.new_dict = {}
        if not self.cache_data or len(self.cache_data) < BaseCaching.MAX_ITEMS:
            self.cache_data[key] = item
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            return
        else:
            for key1, value1 in self.cache_data.items():
                if self.index > BaseCaching.MAX_ITEMS:
                    break
                elif self.index == LIFOCache.counter:
                    discarded = "Discard: " + str(key1)
                    print(discarded)
                    self.new_dict[key] = item
                else:
                    self.new_dict[key1] = value1
                self.index = self.index + 1
            LIFOCache.counter = LIFOCache.counter - 1
            if LIFOCache.counter < 0:
                LIFOCache.counter = BaseCache.MAX_ITEMS - 1
            self.cache_data = self.new_dict

    def get(self, key):
        """Retrieve an item by key."""
        return self.cache_data.get(key, None)

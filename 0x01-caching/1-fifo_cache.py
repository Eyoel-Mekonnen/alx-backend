#!/usr/bin/env python3
"""Implement the FIFO caching policy."""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Class that will implement the FIFO approach."""

    counter = 0

    def __init__(self):
        """Call the parent class which intializes cache_data."""
        super().__init__()

    def put(self, key, item):
        """Put Key and item in the dictonary."""
        if key is None or item is None:
            return
        self.index = 0
        self.new_dict = {}
        if not self.cache_data or len(self.cache_data) < BaseCaching.MAX_ITEMS:
            self.cache_data[key] = item
        if key in self.cache_data:
            self.cache_data[key] = item
            return
        else:
            for key1, value1 in self.cache_data.items():
                if self.index > BaseCaching.MAX_ITEMS:
                    break
                elif FIFOCache.counter == self.index:
                    discarded = "DISCARD: " + str(key1)
                    print(discarded)
                    self.new_dict[key] = item
                else:
                    self.new_dict[key1] = value1
                self.index = self.index + 1
            FIFOCache.counter = FIFOCache.counter + 1
            if FIFOCache.counter >= BaseCaching.MAX_ITEMS:
                FIFOCache.counter = 0
            self.cache_data = self.new_dict

    def get(self, key):
        """Retrieve an item by key."""
        return self.cache_data.get(key, None)

#!/usr/bin/env python3
"""Least recently Used algorithm."""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """Upate Least Recently Used."""

    def __init__(self):
        super().__init__
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Evict the Least Recently Used."""
        if key is None or item is None:
            return
        if key in self.cache_data:
            del self.cache_data[key]
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key, lru_value = self.cache_data.popitem(last=False)
            print("DISCARD: {}".format(lru_key))
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item by key."""
        return self.cache_data.get(key, None)

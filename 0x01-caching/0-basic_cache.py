#!/usr/bin/env python3
"""Basic Dictonary Storing Key and Value."""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Class the inherit from BaseCaching that put and get."""

    def put(self, key, item):
        """Put key and item into dictionary."""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrive the item associated with key."""
        if key in self.cache_data.keys():
            return self.cache_data[key]
        elif key is None or key not in self.cache_data.keys():
            return None

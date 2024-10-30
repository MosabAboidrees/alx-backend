#!/usr/bin/env python3
""" LRUCache module """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class inherits from BaseCaching
        and implements an LRU caching system.
    """

    def __init__(self):
        """ Initialize the LRU Cache """
        super().__init__()
        self.order = []  # To keep track of access order

    def put(self, key, item):
        """ Add an item to the cache data dictionary.
        Args:
            key: the key under which to store the item
            item: the item to be stored
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                # If the key is already in cache, update its position
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the least recently used item
                lru_key = self.order.pop(0)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")

            # Add the item to cache and update its position
            # as most recently used
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Retrieve an item from the cache data dictionary by key.
        Args:
            key: the key to look up in the cache data
        Returns:
            The item associated with the key if it exists; None otherwise.
        """
        if key in self.cache_data:
            # Move the accessed key to the end to mark it as recently used
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None

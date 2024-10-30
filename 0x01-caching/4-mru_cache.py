#!/usr/bin/env python3
""" MRUCache module """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class inherits from BaseCaching
        and implements an MRU caching system.
    """

    def __init__(self):
        """ Initialize the MRU Cache """
        super().__init__()
        self.order = []  # To track the order of access

    def put(self, key, item):
        """ Add an item to the cache data dictionary.
        Args:
            key: the key under which to store the item
            item: the item to be stored
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                # Remove the key from the order to update its position
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the most recently used item
                mru_key = self.order.pop(-1)
                del self.cache_data[mru_key]
                print(f"DISCARD: {mru_key}")

            # Add the item to cache and mark it as the most recently used
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
            # Update the order to mark key as most recently used
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None

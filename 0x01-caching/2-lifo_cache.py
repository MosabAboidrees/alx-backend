#!/usr/bin/env python3
""" LIFOCache module """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class inherits from BaseCaching
        and implements a LIFO caching system.
    """

    def __init__(self):
        """ Initialize the LIFO Cache """
        super().__init__()
        self.last_key = None  # To keep track of the last added key

    def put(self, key, item):
        """ Add an item to the cache data dictionary.
        Args:
            key: the key under which to store the item
            item: the item to be stored
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the most recently added key
                if self.last_key is not None:
                    del self.cache_data[self.last_key]
                    print(f"DISCARD: {self.last_key}")

            # Update the cache and the last added key
            self.cache_data[key] = item
            self.last_key = key

    def get(self, key):
        """ Retrieve an item from the cache data dictionary by key.
        Args:
            key: the key to look up in the cache data
        Returns:
            The item associated with the key if it exists; None otherwise.
        """
        return self.cache_data.get(key)

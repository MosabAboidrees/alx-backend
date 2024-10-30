#!/usr/bin/env python3
""" BasicCache module """


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class inherits from BaseCaching
        and implements a basic caching system without a limit.
    """

    def put(self, key, item):
        """ Add an item to the cache data dictionary.
        Args:
            key: the key under which to store the item
            item: the item to be stored
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from the cache data dictionary by key.
        Args:
            key: the key to look up in the cache data
        Returns:
            The item associated with the key if it exists; None otherwise.
        """
        return self.cache_data.get(key)

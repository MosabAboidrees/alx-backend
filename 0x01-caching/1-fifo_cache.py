#!/usr/bin/env python3
""" FIFOCache module """

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class inherits from BaseCaching
        and implements a FIFO caching system.
    """

    def __init__(self):
        """ Initialize the FIFO Cache """
        super().__init__()
        self.order = []  # To maintain the order of insertion

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
                # Discard the first item in the order list
                oldest_key = self.order.pop(0)
                del self.cache_data[oldest_key]
                print(f"DISCARD: {oldest_key}")

            # Add the new key and update order
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Retrieve an item from the cache data dictionary by key.
        Args:
            key: the key to look up in the cache data
        Returns:
            The item associated with the key if it exists; None otherwise.
        """
        return self.cache_data.get(key)

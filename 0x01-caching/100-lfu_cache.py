#!/usr/bin/env python3
""" LFUCache module """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class inherits from BaseCaching
        and implements an LFU caching system.
    """

    def __init__(self):
        """ Initialize the LFU Cache """
        super().__init__()
        self.frequency = {}  # Tracks the access frequency of each key
        self.order = []      # Tracks the access order of keys

    def put(self, key, item):
        """ Add an item to the cache data dictionary.
        Args:
            key: the key under which to store the item
            item: the item to be stored
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                # Update the item and increment frequency
                self.cache_data[key] = item
                self.frequency[key] += 1
            else:
                # If the cache is full, discard an item
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    self.discard_lfu()
                # Insert the new item
                self.cache_data[key] = item
                self.frequency[key] = 1
            # Update order for LRU when items have the same frequency
            self.update_order(key)

    def get(self, key):
        """ Retrieve an item from the cache data dictionary by key.
        Args:
            key: the key to look up in the cache data
        Returns:
            The item associated with the key if it exists; None otherwise.
        """
        if key in self.cache_data:
            # Increment frequency and update order
            self.frequency[key] += 1
            self.update_order(key)
            return self.cache_data[key]
        return None

    def discard_lfu(self):
        """ Discard the least frequently used item.
            If there is a tie in frequency,
            discard the least recently used item.
        """
        # Find the minimum frequency among current items
        min_freq = min(self.frequency.values())
        # Filter keys with the minimum frequency
        candidates = [k for k in self.order if self.frequency[k] == min_freq]
        # Choose the oldest key among those with minimum frequency
        lfu_key = candidates[0]
        # Remove from cache, frequency, and order
        del self.cache_data[lfu_key]
        del self.frequency[lfu_key]
        self.order.remove(lfu_key)
        print(f"DISCARD: {lfu_key}")

    def update_order(self, key):
        """ Update the order of access to manage
        LRU for items with equal frequency """
        if key in self.order:
            self.order.remove(key)
        self.order.append(key)

#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination.
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Return the dataset, loading it from the CSV file if not already cached.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                self.__dataset = [row for row in reader][1:]  # Skip header
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Create a dictionary where keys are the original
        indices and values are dataset rows.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset =\
                {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieve a deletion-resilient page of the dataset
        based on index and page_size.

        Args:
            index (int): The start index for the page.
            page_size (int): The number of items to include in the page.

        Returns:
            dict: A dictionary with pagination details.
        """
        # Ensure the provided index is within the bounds of the indexed dataset
        assert 0 <= index < len(self.indexed_dataset()), "Index out of range."

        data = []
        next_index = index

        for _ in range(page_size):
            while next_index not in self.__indexed_dataset and\
                    next_index < len(self.__indexed_dataset):
                next_index += 1
            if next_index < len(self.__indexed_dataset):
                data.append(self.__indexed_dataset[next_index])
                next_index += 1

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index,
        }

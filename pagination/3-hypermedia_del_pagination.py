#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return a deletion-resilient page of the dataset
        with hypermedia-style pagination metadata.

        Args:
            index (int): Starting index of the page (0-indexed).
            page_size (int): Number of items to include in the page.

        Returns:
            Dict: A dictionary containing:
            - index (int): The starting index of the returned page.
            - next_index (Optional[int]): The index to use for the next page,
              or None if there is no next page.
            - page_size (int): The number of items actually returned
              in the current page.
            - data (List[List]): The list of dataset rows for the current page.

        Raises:
            AssertionError: If `index` or `page_size` are invalid,
            or if `index` is out of range.
        """
        if index is None:
            index = 0

        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        # Retrieve the indexed dataset
        indexed_dataset = self.indexed_dataset()
        # Find the highest index available in the dataset
        max_index = max(indexed_dataset.keys())

        assert index <= max_index

        # Iterate through the dataset, skipping deleted indices
        current = index
        data = []
        while len(data) < page_size and current <= max_index:
            if current in indexed_dataset:  # Add only if the row exists
                data.append(indexed_dataset[current])
            current += 1  # Move to the next index

        # Determine the starting index for the next page
        if current > max_index:
            next_index = None
        else:
            next_index = current

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(data),
            'data': data,
            }

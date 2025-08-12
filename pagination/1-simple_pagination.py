#!/usr/bin/env python3
"""
Module for calculating pagination indexes.
"""
from typing import Tuple, List
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indexes for pagination.

    Args:
        page (int): Page number (1-indexed, i.e., page 1 = first block).
        page_size (int): Number of items per page.

    Returns:
        Tuple[int, int]: A tuple (start_index, end_index):
            - start_index: position of the first item on the page.
            - end_index: position just after the last item on the page.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return a specific page of the dataset.

        Args:
            page (int): Page number to retrieve (1-indexed).
            page_size (int): Number of items per page.

        Returns:
            List[List]: A sublist of the dataset corresponding
            to the requested page. Returns an empty list if
            the starting index is outside the dataset range.

        Raises:
            AssertionError: If `page` or `page_size` are not positive integers.
            """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data = self.dataset()
        start, end = index_range(page, page_size)

        if start >= len(data):
            return []

        return data[start:end]

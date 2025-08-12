#!/usr/bin/env python3
"""
Module for calculating pagination indexes.
"""
from typing import Tuple, List, Dict
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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Return paginated data along with hypermedia-style pagination metadata.
        Returns:
            Dict: A dictionary with the following keys:
            - page_size (int): Actual number of items in the current page.
            - page (int): Current page number.
            - data (List[List]): The dataset rows for the current page.
            - next_page: The next page number, or None if on the last page.
            - prev_page: The prev page number, or None if on the first page.
            - total_pages (int): Total number of available pages.
        """
        # Retrieve the page with get_page
        page_data = self.get_page(page, page_size)

        # Number total of elements
        total_items = len(self.dataset())

        # Number total of pages (round up to the nearest whole number)
        total_pages = math.ceil(total_items / page_size)

        return {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages,
            }

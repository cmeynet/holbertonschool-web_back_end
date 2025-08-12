#!/usr/bin/env python3
"""
Module for calculating pagination indexes.
"""
from typing import Tuple


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

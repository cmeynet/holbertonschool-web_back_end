#!/usr/bin/env python3
"""
Coroutine called async_comprehension that takes no arguments.
"""
import asyncio
from typing import List


async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers from async_generator using async comprehension.
    Returns:
        List[float]: The list of collected random numbers.
    """
    results = [x async for x in async_generator()]
    return results

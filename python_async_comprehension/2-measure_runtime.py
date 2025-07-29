#!/usr/bin/env python3
"""
Coroutine that will execute async_comprehension four times in parallel.
"""
import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total execution time of running async_comprehension()
    four times in parallel using asyncio.gather.

    Returns:
        float: The total execution time in seconds.
    """
    start = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
        )
    end = time.perf_counter()

    total_time = end - start

    return total_time

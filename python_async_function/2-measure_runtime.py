#!/usr/bin/env python3
"""
Function with integers n and max_delay as arguments that measures
the total execution time for wait_n(n, max_delay), and returns total_time / n
"""
import asyncio
import time

wait_random = __import__("0-basic_async_syntax").wait_random
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average execution time per coroutine for wait_n.

    Args:
        n (int): Number of coroutines to run.
        max_delay (int): Maximum delay (in seconds) for each coroutine.

    Returns:
        float: The average execution time per coroutine, in seconds.
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()

    total_time = end - start
    return total_time / n

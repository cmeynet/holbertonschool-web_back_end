#!/usr/bin/env python3
"""
Async routine called wait_n that takes in 2 int arguments
(in this order): n and max_delay.
"""
from typing import List
import random
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay
    and return the list of delays in ascending order of completion.
    """
    tasks = []

    for i in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    list_delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        list_delays.append(delay)

    return list_delays

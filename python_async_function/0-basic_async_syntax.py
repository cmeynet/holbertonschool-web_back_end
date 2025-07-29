#!/usr/bin/env python3
"""
Asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random
that waits for a random delay between 0 and max_delay
(included and float value) seconds and eventually returns it.
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ Asynchronous coroutine that waits for a random delay.

    Args:
        max_delay (int, optional): Maximum number of seconds to wait.
                                   Defaults to 10.

    Returns:
        float: The actual delay time waited, as a floating-point number. """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

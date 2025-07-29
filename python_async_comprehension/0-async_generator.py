#!/usr/bin/env python3
"""
Coroutine called async_generator that takes no arguments.
"""
import random
from typing import AsyncGenerator
import asyncio


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronous generator that yields 10 random float values between 1 and 10.
    Each value is produced after asynchronously waiting for 1 second.
    Yield a random number between 0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

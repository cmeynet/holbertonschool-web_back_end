#!/usr/bin/env python3
"""
Function task_wait_random that takes an integer max_delay
and returns a asyncio.Task.
"""
from asyncio import Task
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> None:
    """
    Create and return an asyncio.Task for wait_random.

    Args:
        max_delay (int): Maximum number of seconds for the random delay.

    Returns:
        asyncio.Task: A Task object representing the scheduled coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))

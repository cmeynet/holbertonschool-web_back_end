#!/usr/bin/env python3
"""
Function task_wait_n that takes an integer max_delay
and returns a list of delays.
"""
from typing import List
from asyncio import Task
import asyncio

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run task_wait_random n times with the given max_delay
    and return the list of delays in ascending order of completion.

    Args:
        n (int): Number of tasks to spawn.
        max_delay (int): Maximum delay for each task.

    Returns:
        List[float]: List of delays in the order they completed.
    """

    tasks: List[Task[float]] = []
    for i in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    list_delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        list_delays.append(delay)

    return list_delays

#!/usr/bin/env python3
"""Run task_wait_random n times and return delays in order"""


import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run task_wait_random n times with max_delay.
    Return delays in order of completion.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delays.append(await task)
    return delays

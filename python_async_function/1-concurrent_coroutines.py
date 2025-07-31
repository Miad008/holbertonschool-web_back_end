#!/usr/bin/env python3
"""Run multiple coroutines and return sorted list of delays"""


import asyncio
import bisect
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times and return delays in ascending order"""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays: List[float] = []

    for task in tasks:
        delay = await task
        bisect.insort(delays, delay) 

    return delays

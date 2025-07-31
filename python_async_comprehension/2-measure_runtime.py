#!/usr/bin/env python3
"""Measure total runtime of running async_comprehension 4 times in parallel"""


import asyncio
import time
from typing import Callable
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Run async_comprehension 4 times in parallel and measure total time.
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start

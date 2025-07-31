#!/usr/bin/env python3
"""Run async_comprehension 4 times and measure total time"""


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Run async_comprehension 4 times in parallel, return total time.
    """
    start = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    return time.perf_counter() - start

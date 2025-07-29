#!/usr/bin/env python3
"""Module for executing wait_random coroutines concurrently."""


import asyncio
from typing import List
from 0_basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Return sorted delays from multiple wait_random coroutines."""
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)

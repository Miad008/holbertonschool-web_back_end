#!/usr/bin/env python3
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously waits for a random delay between 0 and max_delay (inclusive).
    
    Args:
        max_delay (int): The maximum delay in seconds (default is 10).
    
    Returns:
        float: The random delay time in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

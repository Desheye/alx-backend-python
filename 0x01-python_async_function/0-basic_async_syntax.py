#!/usr/bin/env python3
'''
    Demonstrating the basics of asynchronous programming.
'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay
    (inclusive, as a float value)
    seconds and eventually returns it.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

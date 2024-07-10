#!/usr/bin/env python3

""" Example of Async Comprehensions """

from asyncio import gather
from time import time

# Assume async_comprehension is imported from another module
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Measure the runtime for four parallel comprehensions """
    start = time()
    tasks = [async_comprehension() for i in range(4)]
    await gather(*tasks)
    end = time()
    return (end - start)

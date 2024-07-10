#!/usr/bin/env python3

""" Example of Async Comprehensions """

from asyncio import sleep
from random import uniform
from typing import List

# Assume async_generator is imported from another module
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Generate a list of floats using async comprehensions """
    result = [i async for i in async_generator()]
    return result

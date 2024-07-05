#!/usr/bin/env python3
'''8 module.
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    return lambda x: x * multiplier

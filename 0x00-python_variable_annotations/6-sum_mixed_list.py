#!/usr/bin/env python3
''' 6 module.
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''ist of integers and floating-point numbers.
    '''
    return float(sum(mxd_lst))

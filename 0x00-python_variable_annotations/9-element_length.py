#!/usr/bin/env python3
""" duck type: iterable object"""
from typing import Mapping, MutableMapping, Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Elements length """
    return [(i, len(i)) for i in lst]

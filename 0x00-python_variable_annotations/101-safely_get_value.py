#!/usr/bin/env python3
""" Demonstrating more complex type annotations """

from typing import Mapping, Any, Sequence, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None
                     ) -> Union[Any, T]:
    """ Safely retrieves a value from a dictionary """
    if key in dct:
        return dct[key]
    else:
        return default

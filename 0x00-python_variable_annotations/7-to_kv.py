#!/usr/bin/env python3
'''type annotation using tuples'''

from typing import Callable, Iterator, Union, Optional, List, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''takes k and v as args and returns a tuple'''

    return (k, v**2)

#!/usr/bin/env python3

'''type-annotated functions with list'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''function that returns sum of a list'''
    return sum(input_list)

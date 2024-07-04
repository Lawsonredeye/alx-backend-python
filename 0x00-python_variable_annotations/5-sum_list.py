#!/usr/bin/env python3
"""function sum_list which takes a list input_list of floats
as argument and returns their sum as a float."""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Takes a list of float numbers and sum it up and returns a
    float value"""
    count: float = 0
    for i in input_list:
        count += i
    return count

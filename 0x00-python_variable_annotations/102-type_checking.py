#!/usr/bin/env python3
"""Use mypy to validate the following piece of code
and apply any necessary changes."""
from typing import Tuple, List, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Use mypy to validate the following
    piece of code and apply any necessary changes."""
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)

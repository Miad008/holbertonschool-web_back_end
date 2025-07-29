#!/usr/bin/env python3
"""Module for creating a multiplier function."""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by the multiplier."""
    def multiplier_function(n: float) -> float:
        return n * multiplier
    return multiplier_function

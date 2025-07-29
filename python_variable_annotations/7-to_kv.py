#!/usr/bin/env python3
"""Module for creating a tuple with string and squared number."""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple with string and the square of the number."""
    return (k, float(v ** 2))

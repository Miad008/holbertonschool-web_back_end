#!/usr/bin/env python3
"""Module for creating a tuple of string and the square of an integer or float."""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple where the first element is the string and the second is the square of the number."""
    return (k, float(v ** 2))

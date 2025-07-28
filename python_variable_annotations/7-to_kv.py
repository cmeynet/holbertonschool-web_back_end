#!/usr/bin/env python3
"""
Type-annotated function to_kv that takes a string k
and an int OR float v as arguments and returns a tuple.
"""
from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    """ Return tuple of string and int or float """
    return k, v**2

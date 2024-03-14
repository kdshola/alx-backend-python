#!/usr/bin/env python3
""" Module for annotated function to_kv """
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ returns a tupe of sting and of v to the power of 2 """
    return (k, float(v ** 2))

#!/usr/bin/env python3
""" Module for annotated function safely_get_value """
from typing import Any, Mapping, Union, TypeVar

T = TypeVar('T')
Var = Union[T, None]
Ret = Union[Any, T]


def safely_get_value(dct: Mapping, key: Any, default: Var = None) -> Ret:
    """ Gets the first element in a dictionary """
    if key in dct:
        return dct[key]
    else:
        return default

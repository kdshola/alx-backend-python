#!/usr/bin/env python3
""" Module for annotated function make_multiplier """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ returns a functionn that multiplies two floats """
    def multiply(arg: float) -> float:
        """ Multiplies 2 floats """
        return arg * multiplier
    return multiply

#!/usr/bin/env python3
""" Module for annotated function sum_mixed_list """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ returns the sum a list of ints and floats """
    return sum(mxd_lst)

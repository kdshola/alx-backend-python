#!/usr/bin/env python3
""" Module for annotated element_length """
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Retuns a list tuple of containing an iterable and its length """
    return [(i, len(i)) for i in lst]

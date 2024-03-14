#!/usr/bin/env python3
""" Module for annotated function safe_first_element """
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Retuns first element of a sequence if it exist or none """
    if lst:
        return lst[0]
    else:
        return None

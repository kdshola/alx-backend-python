#!/usr/bin/env python3
""" Module for routine function waint_n """
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_dalay: int) -> List[float]:
    """ spawns wait_random n times with the specified max_delay """
    task_objects = [asyncio.create_task(wait_random(max_dalay))
                    for _ in range(n)]
    tasks = [await task for task in asyncio.as_completed(task_objects)]
    return tasks

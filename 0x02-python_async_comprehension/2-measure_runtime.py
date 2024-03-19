#!/usr/bin/env python3
""" Module for coroutine measure_runtime """

import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measure the total runtime and return it for executing
    async_comprehension four times in parallel """
    start = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    return time.perf_counter() - start

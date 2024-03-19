#!/usr/bin/env python3
""" Module for coroutine function wait_random """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Sleeps for random max_delay seconds and retuns time it slept """
    sleep_time = random.uniform(0.0, max_delay)
    await asyncio.sleep(sleep_time)
    return sleep_time

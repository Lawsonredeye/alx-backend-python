#!/usr/bin/env python3
'''Measure the runtime'''

import asyncio
import typing
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    '''Calculates the total measure_time for the entire process
    to run and it takes the number of times wait_n would be called and
    max_delay is the delay time'''
    start_time: float = time.perf_counter()
    await wait_n(n, max_delay)
    end_time: float = time.perf_counter() - start_time
    elapsed_time: float = end_time / n
    return elapsed_time

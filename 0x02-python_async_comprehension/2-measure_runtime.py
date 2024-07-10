#!/usr/bin/env python3
'''measure_runtime should measure the total runtime and return it.'''
import asyncio
import typing
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Measure the total time it takes for a coroutine to run and execute
    and its returns a float value'''
    start: float = time.perf_counter()
    await asyncio.gather(
            async_comprehension(), async_comprehension(),
            async_comprehension(), async_comprehension()
            )
    runtime: float = time.perf_counter() - start
    return runtime

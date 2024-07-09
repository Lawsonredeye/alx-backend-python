#!/usr/bin/env python3
'''execute multiple coroutines at the same time with async'''

import asyncio
import typing


wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    '''an async routine called wait_n that takes in 2 int
    arguments (in this order): n and max_delay.'''
    new_await: list = []
    for i in range(n):
        new_value = await asyncio.gather(task_wait_random(max_delay))
        new_await.extend(new_value)
    return new_await

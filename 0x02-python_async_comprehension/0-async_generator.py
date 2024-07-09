#!/usr/bin/env python3
'''Module which handles a coroutine generator function which returns an int'''

import asyncio
import typing
import random


async def async_generator() -> typing.AsyncGenerator[float, None]:
    '''Coroutine function that returns a randomize value'''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
